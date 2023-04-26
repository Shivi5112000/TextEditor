from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html' )
def analyze(request):
    #get the text
    djtext=request.POST.get('txtarea', 'default')
    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')  # removepunc-> name given in html code
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    count=request.POST.get('count', 'off')
    #Check which checkbox is on
    if removepunc =="on":
        punctuations='''!()-_{}[];:'"\<>,./?@#$%^&*~+'''
        analyzed=""

        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzedText':analyzed}
        djtext=analyzed

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzedText': analyzed}
        djtext=analyzed

    if newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed New Lines', 'analyzedText': analyzed}
        djtext=analyzed

    if extraspaceremover == 'on':
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Extra Space Removed', 'analyzedText': analyzed}

    if(removepunc!= "on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please select the operation")
    return render(request, 'analyze.html', params)
