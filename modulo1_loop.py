import modulo2 # quando o modulo2 chama o modulo1, e aqui o modulo1 chama o
               # modulo2. Veja o resultado quando eu executo a linha de comando
               # Erro "dad-lock" ==> loop           

NOME = "Bruna"

def say_hi(n):
    print(f"Hi {n}")

modulo2.say_hello(NOME)

#*************
#* Resultado *
#*************

#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundie_rewardss % python mo
#dulo2.py
#Traceback (most recent call last):
#  File "/Users/albertosoares/Projetos/dundie_rewardss/modulo2.py", line 1, 
#  in <module> import modulo1
#  File "/Users/albertosoares/Projetos/dundie_rewardss/modulo1.py", line 1, 
#  in <module> import modulo2 
#  File "/Users/albertosoares/Projetos/dundie_rewardss/modulo2.py", line 7, 
#  in <module>
#  modulo1.say_hi(modulo1.NOME)
#  AttributeError: partially initialized module 'modulo1' has no attribute 
# 'say_hi' (most likely due to a circular import)
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundie_rewardss % 