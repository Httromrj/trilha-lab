import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Lê o valor total da compra como inteiro
valor_compra = int(input())

if valor_compra < 50:
    print("Obrigado por comprar conosco!")
elif valor_compra <= 99:
    print("Parabens! Voce ganhou um brinde!")
elif valor_compra <= 199:
    print("Desconto de 10 reais aplicado!")
else:
    print("Desconto de 25 reais aplicado!")
