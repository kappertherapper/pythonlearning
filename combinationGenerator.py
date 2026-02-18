liste = ['a', 'b', 'c']

for i in range(len(liste)):
    for j in range(i, len(liste)):
        for k in range (j, len(liste)):
            print (liste[i], liste[j], liste[k])