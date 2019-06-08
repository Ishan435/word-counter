from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')


def countpage(request):

    fulltext1= request.GET['fulltext']
    wordlist= fulltext1.replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace('-',' ').replace('(',' ').replace(')',' ').replace('"',' ').split()


    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'counts.html',{'fulltext2':fulltext1,'counter':len(wordlist),'wordlog':sortedwords})

def aboutpage(request):

    return render(request,'about.html')
