Frase = input("Ingresa una palabra: ").lower().replace(" ","")

def Palindromo():
    alreves=Frase[::-1]
    if alreves == Frase:
        print(f"{Frase} es un palindromo")
    else:
        print(f"{Frase} no es un palindromo")
Palindromo() 
print(":)")               