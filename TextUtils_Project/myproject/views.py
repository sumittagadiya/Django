# this is file created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request) :
    return render(request, 'index.html')
    #return HttpResponse('''<h1>Hello World</h1> ''')

def analyze(request) :
    fetched_text = request.POST.get('text','default')
    removepunc_flag=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc_flag == 'on' :
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in fetched_text:
            if char not in punctuations:
                analyzed = analyzed + char
        fetched_text = analyzed

    if (fullcaps=="on"):
        fetched_text = fetched_text.upper()
    
    if (newlineremover == "on") :
        analyzed = ""
        for char in fetched_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        fetched_text = analyzed

    if (extraspaceremover == "on") :
        analyzed = ""
        for index, char in enumerate(fetched_text):
            if not(fetched_text[index] == " " and fetched_text[index+1]==" "):
                analyzed = analyzed + char
        fetched_text = analyzed
    
    return render(request, 'analyze.html', {'text' : fetched_text})

def about(request) :
    #return HttpResponse("This is all about testing endpoint")
    return render(request, 'about.html')

def contact(request) :
    #return HttpResponse("This is all about testing endpoint")
    return render(request, 'contact.html')

