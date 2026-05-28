import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from abc import ABC, abstractmethod #, abstractproperty (Não é mais usado)

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
 #   @abstractproperty   - Não é mais usado
    def marca(self):
        pass

class controleTV(ControleRemoto):
    def ligar(self):
        print("Ligado!")

    def desligar(self):
        print("desligado!")
    
    @property
    def marca(self):
        return "LG"

controle = controleTV()
controle.ligar()
controle.desligar()
