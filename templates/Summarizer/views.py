from django.http import HttpResponse
from django.shortcuts import render
# Sumy Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
#NLTK PKG
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq  


def index(request):
    #Home
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    nltk = request.POST.get('nltk', 'off')
    sumy = request.POST.get('sumy', 'off')
    

    #If NLTK algorithm is check
    if nltk == "on":
        analyzed = ""
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(djtext)
        freqTable = dict()
        for word in words: 
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable: 
                freqTable[word] += 1
            else:
                freqTable[word] = 1
        sentences = sent_tokenize(djtext) 
        sentenceValue = dict() 
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]
        average = int(sumValues / len(sentenceValue))
        for sentence in sentences: 
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                analyzed += " " + sentence

        params = {'purpose':'NLTK Algorithm', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    # If sumy algorithm is check
    elif sumy == 'on':
        analyzed = ""
        parser = PlaintextParser.from_string(djtext,Tokenizer("english"))
        lex_summarizer = LexRankSummarizer()
        summary = lex_summarizer(parser.document,3)
        summary_list = [str(sentence) for sentence in summary]
        analyzed = ' '.join(summary_list)
        params = {'purpose':'Sumy Algorithm', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    # If no checkbox is on 
    else:
    	return render(request, 'error.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    #get username and password
    user = request.POST.get('uname', 'default')
    pas = request.POST.get('psw', 'default')
    #Checkbox value
    remember = request.POST.get('remember', 'off')
    #Check condition 
    if user == 'admin' and pas == 'password':
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


