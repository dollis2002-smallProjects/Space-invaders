def signo(value):
    if value > 0:
        print("Es positivo")
    elif value == 0:
        print("Es cero")
    else:
        print("Es negativo")

signo(int(input("Inserte un numero: ")))

#%%
from math import pi

def volumenEsfera(radio):
    return pi*(4/3)*radio**3

print(volumenEsfera(float(input("Radio: "))))
     
# %%
