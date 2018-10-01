from django.shortcuts import render
from tts_watson.TtsWatson import TtsWatson
from django.shortcuts import HttpResponse
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions
import win32com.client as wincl
import os
from nltk.tokenize import word_tokenize
from .forms import MemoryForm
from .models import Memory
from nltk.corpus import words

english_words=words.words()

speak = wincl.Dispatch("SAPI.SpVoice")

def play(request):

    if request.method == "POST":
        tex=request.POST.get("speak")
        ttsWatson = TtsWatson('42657070-d2ed-4d8d-bac3-05d505e42b9a', 'ePrw5TcBlL6N', 'en-US_AllisonVoice') 
        num = word_tokenize(tex)
        numlength=len(num)-1
        tcount=0
        newtex=""
        for n in num:
            word=n.lower()
            sent="".join(word)
            if tcount==0:
                newtex=newtex+sent
            else:
                newtex=newtex+ " " + sent
            tcount+=1
        print(newtex)
        memo=Memory.objects.filter(query=newtex)
        
        
        if len(tex) != 0 and memo:
            for me in memo:
                ttsWatson.play(me.reply)

            return render(request, "page/index.html")
        else:
            ttsWatson.play("Sorry, I didn't understand")
            return render(request, "page/index.html")

    else:
        return render(request, "page/front.html")
 

def talk(request):
    return render(request, "page/index.html")

def back(request):
    return render(request, "page/front.html")

def train(request):
    if request.method == "POST":
        query=request.POST.get("query")
        qu=word_tokenize(query)
        l=len(qu)-1
        newquery=""
        qcount=0
        for q in qu:
            wor=q.lower()
            sent="".join(wor)
            if qcount==0:
                newquery=newquery+sent
            else:
                newquery=newquery+" "+sent
            qcount +=1
    
        reply=request.POST.get("reply")
        re=word_tokenize(reply)
        newreply=""
        rcount=0
        for r in re:
            w=r.lower()
            se="".join(w)
            if rcount==0:
                newreply=newreply+se
            else:
                newreply=newreply+ " " + se
            rcount+=1

        s=Memory.objects.create(query=newquery,reply=newreply)

        return render(request, "page/train.html")

    else:
        return render(request, "page/train.html")
