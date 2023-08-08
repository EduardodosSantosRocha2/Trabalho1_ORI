import PyPDF2
import nltk
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer as snS

stop_words = stopwords.words('portuguese');
stemmer = snS('portuguese')

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

def Stemizar(lista):
    lista_stemizada = [stemmer.stem(palavra) for palavra in lista]
    return lista_stemizada










