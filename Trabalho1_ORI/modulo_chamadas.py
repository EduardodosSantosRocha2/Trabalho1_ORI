import TrabalhoORI as t

#Ler StopWords
t.lerPDF(t.lista1, 0);
t.lerPDF(t.lista2,1);
t.lerPDF(t.lista3,2);
t.lerPDF(t.lista4,3);
t.lerPDF(t.lista5,4);
t.lerPDF(t.lista6,5);
t.lerPDF(t.lista7, 6);

#Remover StopWords
t.lista1 = t.removerStopWords(t.lista1,1);
t.lista2 = t.removerStopWords(t.lista2,2);
t.lista3 = t.removerStopWords(t.lista3,3);
t.lista4 = t.removerStopWords(t.lista4,4);
t.lista5 = t.removerStopWords(t.lista5,5);
t.lista6 = t.removerStopWords(t.lista6,6);
t.lista7 = t.removerStopWords(t.lista7,7);

#Printar a lista sem StopWords
t.printarStopWords(t.lista1,1)
t.printarStopWords(t.lista2,2)
t.printarStopWords(t.lista3,3)
t.printarStopWords(t.lista4,4)
t.printarStopWords(t.lista5,5)
t.printarStopWords(t.lista6,6)
t.printarStopWords(t.lista7,7)


#Stemizar
t.lista1 = t.Stemizar(t.lista1,1);
t.lista2 = t.Stemizar(t.lista2,2);
t.lista3 = t.Stemizar(t.lista3,3);
t.lista4 = t.Stemizar(t.lista4,4);
t.lista5 = t.Stemizar(t.lista5,5);
t.lista6 = t.Stemizar(t.lista6,6);
t.lista7 = t.Stemizar(t.lista7,7);

#Printar a lista Stemizar

t.printarStermizado(t.lista1,1);
t.printarStermizado(t.lista2,2);
t.printarStermizado(t.lista3,3);
t.printarStermizado(t.lista4,4);
t.printarStermizado(t.lista5,5);
t.printarStermizado(t.lista6,6);
t.printarStermizado(t.lista7,7);



t.listamae = [t.lista1, t.lista2 , t.lista3, t.lista4,t.lista5, t.lista6 , t.lista7 ] ;
for lista in t.listamae:
    lista.sort()
#
#Gera Indice Invertido
t.IndiceIv(t.listamae)








