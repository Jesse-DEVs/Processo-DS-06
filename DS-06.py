class DS06:
    def Apertadeira(self):
        return("Com a apertadeira, aperte o Bolt")
        
    def pegar(self):
        return("Pegar")
        
    def bolt(self, bolt):
        self.bolt = bolt
        return f"{self.bolt}"
        
    def posicionamento(self):
        return("Posicionar")
        
class Passo1_Handle(DS06):
    def handle(self):
        return("Pegar a handle")
    
    def Checar(self):
        return("Varifiar se a handle está com a mesma cor do carro")

    def Bracket(self):
        return("Bracket")

class Passo2_Latch(DS06):
    def Latch(self):
        return("Pegar a Latch")

    def Travar(self):
        return("Travar a vareta na Handle")

class Passo3_Sash(DS06):
    def Sash(self):
        return("Pegar o Sash")
        
    def Channel(self):
        return("Channel no Sash")


def main():
    # Instanciando os passos
    passo1 = Passo1_Handle()
    passo2 = Passo2_Latch()
    passo3 = Passo3_Sash()

    # Chamando os métodos de cada passo
    print("Passo 1:\n")
    print(passo1.handle())
    print(passo1.Checar())
    print(passo1.posicionamento())
    print(passo1.pegar())
    print(passo1.Bracket())
    print(passo1.posicionamento())
    print(passo1.pegar())
    print(passo1.bolt("Bolt wash - 6x12"))
    print(passo1.Apertadeira())
    
    print("\nPasso 2:\n")
    print(passo2.Latch())
    print(passo2.posicionamento())
    print(passo2.Travar())
    print(passo2.pegar())
    print(passo2.bolt("Bolt Latch - M6"))
    print(passo2.Apertadeira())
    
    print("\nPasso 3:\n")
    print(passo3.Sash())
    print(passo3.posicionamento())
    print(passo3.pegar())
    print(passo3.bolt("Bolt wash - 6x16"))
    print(passo3.Apertadeira())
    print(passo3.posicionamento())
    print(passo3.Channel())
   
if __name__ == "__main__":
    main()
