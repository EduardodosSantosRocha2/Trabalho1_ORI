import TrabalhoORI as t

t.lerPDF(t.lista1, 0);
t.lerPDF(t.lista2,1);
t.lerPDF(t.lista3,2);
t.lerPDF(t.lista4,3);
t.lerPDF(t.lista5,4);
t.lerPDF(t.lista6,5);
t.lerPDF(t.lista7, 6);
t.lista1 = t.removerStopWords(t.lista1);
t.lista2 = t.removerStopWords(t.lista2);
t.lista3 = t.removerStopWords(t.lista3);
t.lista4 = t.removerStopWords(t.lista4);
t.lista5 = t.removerStopWords(t.lista5);
t.lista6 = t.removerStopWords(t.lista6);
t.lista7 = t.removerStopWords(t.lista7);

print(t.lista2)
t.lista2 = t.Stemizar(t.lista2);
print(t.lista2)