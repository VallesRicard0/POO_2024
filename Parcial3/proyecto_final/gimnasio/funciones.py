def borrarPantalla():
  import os  
  os.system("cls" if os.name == 'nt' else 'clear')

def esperarTecla():
    print("\n \t \tOprima cualquier tecla para continuar ...")
    input()