import PyPDF2
import nltk
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words('portuguese');
stop_words.append(",");
stop_words.append(':');
stop_words.append('.');
stop_words.append('-');
stop_words.append('!');
stop_words.append('—');
stop_words.append('oh');
stop_words.append('…');




pdfs = ['A_Canção_dos_tamanquinhos_Cecília_Meireles.pdf','Pontinho_de_Vista_Pedro_Bandeira.pdf',
        'A_porta_Vinicius_de_Moraes.pdf','Ao_pé_de_sua_criança_Pablo_Neruda.pdf','As_borboletas_Vinicius_de_Moraes.pdf',
        'Convite_José_Paulo_Paes.pdf','Pontinho_de_Vista_Pedro_Bandeira.pdf'];
lista1 = []; lista2 = []; lista3 = []; lista4 = []; lista5 = []; lista6 = []; lista7 = [];


def geradordelista(lista_destino, palavras):
    for palavra in palavras:
        lista_destino.append(palavra);

def lerPDF(lista, pos):
    pdf = open(pdfs[pos], 'rb');
    reader = PyPDF2.PdfReader(pdf);
    pagina = reader.pages[0];
    texto = pagina.extract_text();
    texto = texto.replace('…', ' …');
    palavras = word_tokenize(texto);
    geradordelista(lista, palavras);

def removerStopWords(lista):
    lista_aux = [palavra for palavra in lista if palavra.lower() not in stop_words] #List comprehension
    return lista_aux




lerPDF(lista1,0);
lerPDF(lista2,1);
lerPDF(lista3,2);
lerPDF(lista4,3);
lerPDF(lista5,4);
lerPDF(lista6,5);
lerPDF(lista7, 6);
lista1 = removerStopWords(lista1);
lista2 = removerStopWords(lista2);
lista3 = removerStopWords(lista3);
lista4 = removerStopWords(lista4);
lista5 = removerStopWords(lista5);
lista6 = removerStopWords(lista6);
lista7 = removerStopWords(lista7);
print(lista2)







