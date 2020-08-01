# i have created this file - Deepak

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyzer(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlinermv = request.POST.get('newlinermv', 'off')
    spacermv = request.POST.get('spacermv', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for chars in djtext:
            if chars not in punctuations:
                analyzed += chars
        djtext = analyzed

    if fullcaps == "on":
        djtext = djtext.upper()

    if newlinermv == "on":
        print(djtext)
        analyzed = ""
        for chars in djtext:
            print(chars)
            if chars != "\n" and chars != "\r":
                analyzed += chars
        print(analyzed)
        djtext = analyzed

    if spacermv == "on":
        analyzed = ""
        for index , chars in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += chars
        djtext = analyzed

    params = {'purpose': 'Correct text', 'analyzed_text': djtext}
    return render(request, 'analyzer.html', params)




