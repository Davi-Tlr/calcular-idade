from datetime import datetime

nome = (input ("Digite seu nome? "))
dtnasc = (input ("Qual sua data de nascimento? "))

datual = datetime.now().day
matual = datetime.now().month
aatual = datetime.now().year

dianasc, mesnasc, anonasc = dtnasc.split("/")
dianasc, mesnasc, anonasc = int(dianasc), int(mesnasc), int(anonasc)
idade = aatual - anonasc
#---------------------------------------------------------------------------
#--- Verifica se o aniversário ja passou ou
if (mesnasc > matual): idade -= 1
elif (mesnasc == matual): 
    if (dianasc > datual): idade -= 1
    elif (dianasc == datual): print ("PARABÉNS HOJE É SEU NÍVER!!!")
#----------------------------------------------------------------------------
print (f"Você tem {idade} anos! ")
