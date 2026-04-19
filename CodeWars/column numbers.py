def collum(x: str):
    x = x.upper()
    soma = 0
    contador = 0
    for i in range((len(x)-1), -1, -1):
        calculo = (ord(x[contador])-64)*26**i
        print((ord(x[contador])-64), "* 26 **", i)
        soma+=calculo
        contador+=1
    return soma