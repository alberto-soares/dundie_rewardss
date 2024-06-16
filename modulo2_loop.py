import modulo1 # Como Python é uma linguagem interpretada o que significa 
               # execuçao linha a linha, observar que modulo2 chama o modulo1 

def say_hello(n):
    print(f"Hello {n}")

modulo1.say_hi(modulo1.NOME)

say_hello(modulo1.NOME)

#*************
#* Resultado *
#*************

#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundie_rewardss % python mo
#dulo3.py
#Hi Bruna
#Hello Bruna
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundie_rewardss %