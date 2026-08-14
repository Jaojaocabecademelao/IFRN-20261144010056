# Verifica se um número é ímpar ou par

class Verific_Im_par:
  def __init__(self, número):
    self.numero = None

    if type(número) == int:
      self.numero = int(número)
    else:
      raise ValueError(f"Verific_Im_Par.__init__: {número} não é um número válido, coloque um inteiro de base 10")

  def Par(self):
    if self.numero == 0:
      raise ValueError("0 é um número neutro")
    elif self.numero % 2 == 0:
      return True
    else:
      return False 
    
  def Impar(self):
    if self.numero == 0:
      raise ValueError("0 é um número neutro")
    elif self.numero % 2 == 0:
      return False
    else:
      return True 
    
  def __str__(self):
    if self.Par() == True:
      return f"{self.numero} é par"
    elif not self.Par():
      return f"{self.numero} é ímpar"
    else:
      return self.Par

num = Verific_Im_par(input(""))

print(num)
