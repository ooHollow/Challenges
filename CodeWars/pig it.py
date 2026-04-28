def pig_it(text: str):
    l = text.split(" ")
    lista = []
    for i in l:
        if i.isalpha():
            new = i[1:] + i[0] + "ay"
            lista.append(new)
        else:
            lista.append(i)
    x = " ".join(lista)
    return x