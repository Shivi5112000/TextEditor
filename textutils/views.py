from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html' )

    #return HttpResponse('''Home ''')

def analyze(request):
    #get the text
    djtext=request.GET.get('txtarea', 'default')

    # Check checkbox value
    removepunc = request.GET.get('removepunc', 'off')  # removepunc-> name given in html code
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover=request.GET.get('newlineremover', 'off')
    extraspaceremover=request.GET.get('extraspaceremover', 'off')
    count=request.GET.get('count', 'off')
    #Check which checkbox is on
    if removepunc =="on":
        punctuations='''!()-_{}[];:'"\<>,./?@#$%^&*~+'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzedText':analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzedText': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed=analyzed+char
        params = {'purpose': 'Removed New Lines', 'analyzedText': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == 'on':
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Extra Space Removed', 'analyzedText': analyzed}
        return render(request, 'analyze.html', params)

    # elif count=='on':
    #     analyzed=djtext.count00
    #     params = {'purpose': 'No. of Characters', 'analyzedText': analyzed}
    #     return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
# def capitalizefirst(request):
#     return HttpResponse('''capitalize first <a href='/'>Back</a>''')
#
#
# def newlineremove(request):
#     return HttpResponse('''new line remove <a href='/'>Back</a>''')
#
# def   spaceremove(request):
#     return HttpResponse('''space remove <a href='/'>Back</a>''')
#
# def charcount(request):
#     return HttpResponse('''Character count <a href='/'>Back</a>''')
