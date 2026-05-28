import pandas as pd

url = "http://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"

df = pd.read_csv(url)
print(df.head())


#1 - Análise exploratória dos dados - Problema de Classificação desbalanceada
#df["Class"].value_counts(normalize=True)
print(df["Class"].value_counts(normalize=True))

#2 - Feature Engineering - Criar novas variáveis ou transformar as existentes para melhorar a performance do modelo
import numpy as np
df["Amount_log"] = np.log1p(df["Amount"])

from sklearn.model_selection import train_test_split
X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.3, random_state=42
    )


#3 - Logistic Regression - Modelo de classificação para detecção de fraudes
from sklearn.linear_model import LogisticRegression 
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))    

#3.1 - Avaliação do modelo - Métricas de avaliação para classificação desbalanceada
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

y_probs = model.predict_proba(X_test)[:, 1]  # Probabilidades para a classe positiva
fpr, tpr,_ = roc_curve(y_test, y_probs)

plt.plot(fpr, tpr)
plt.title("Roc Curve")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()

print("AUC:", roc_auc_score(y_test, y_probs))


#3.2 - Técnicas de balanceamento - precision-recall curve.
from sklearn.metrics import precision_recall_curve
precision, recall, _ = precision_recall_curve(y_test, y_probs)
plt.plot(recall, precision)
plt.title("Precision-Recall Curve")
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.show()


#3.3 - Técnicas de balanceamento - Under-sampling e Over-sampling

#under-sampling
fraudes = df[df["Class"] == 1]
normais = df[df["Class"] == 0].sample(len(fraudes), random_state=42)
df_under = pd.concat([fraudes, normais])

#oversampling
from imblearn.over_sampling import SMOTE
smote = SMOTE()
x_res, y_res = smote.fit_resample(X, y)


#3.4 - Random Forest - Modelo de classificação baseado em árvores para detecção de fraudes
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(
    n_estimators=50, 
    max_depth=10,
    class_weight="balanced",
    n_jobs=-1,
    random_state=42
)

rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print(classification_report(y_test, y_pred_rf))


#4 - Usando um Pipeline para encadear as etapas de pré-processamento e modelagem
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

pipeline.fit(X_train, y_train)
y_pred_pipeline = pipeline.predict(X_test)

print(
    classification_report(
        y_test,
        y_pred_pipeline
    )
)

#4.1 - pipeline com ajuste de threshold para melhorar a precisão
threshold = 0.3
y_pred_custom = (y_probs > threshold).astype(int)
print(classification_report(y_test, y_pred_custom))


#5 - Modelo avançado - XGBoost para detecção de fraudes
from xgboost import XGBClassifier
xgb = XGBClassifier(
   scale_pos_weight=10,
   eval_metric="logloss"
)
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)
print(classification_report(y_test, y_pred_xgb))



#6 - Importancia das variáveis - Análise de feature importance para entender quais variáveis mais contribuem para a detecção de fraudes
import matplotlib.pyplot as plt
importances = xgb.feature_importances_

plt.bar(range(len(importances)), importances)
plt.title("Importancia das variáveis")
plt.xlabel("Variáveis")
plt.ylabel("Importancia")
plt.show()


#7 - Ajuste de parametros - GridSearchCV para encontrar os melhores hiperparâmetros do modelo
from sklearn.model_selection import GridSearchCV
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [3, 5]
  }
grid = GridSearchCV(
    estimator=XGBClassifier(eval_metric="logloss"),
    param_grid=param_grid,
    scoring="recall",
    cv=3
)
grid.fit(X_train, y_train)
print("Melhor modelo:", grid.best_params_)


#8 - Explicabilidade do modelo - SHAP values para entender a importância das features na detecção de fraudes
import shap
explainer = shap.TreeExplainer(xgb)
shap_values = explainer(X_test[:100])  # Explicação para as primeiras 100 amostras
shap.plots.bar(shap_values)