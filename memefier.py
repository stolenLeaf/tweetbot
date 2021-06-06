#importamos dependencias
import random

#posibles opciones para saber si una letra se debe escribir en mayuscula
choices=[0,1]

def memefy(text):
    memefied_text=[]
    for letter in text:
        #elegir si la letra se debe pasar a mayuscula
        if random.choices(choices)==1:
            memefied_text.append(letter.upper())
        else:
            memefied_text.append(letter.lower())
    return ''.join(memefied_text)
