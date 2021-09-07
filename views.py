# This is the file made by me..
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
# def index(request):
#     f = open("file.txt")
#     return HttpResponse(f)

def removepunc(text):
    analyzed=""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in text:
        if i in punctuations:
            continue
        analyzed += i
    return analyzed    
def capitalize(text):
    analyzed=""
    for i in text:
        analyzed+=i.upper()
    return analyzed

def removesp(text):
    analyze=""
    for index,char in enumerate(text):
        if char[index]==" " and char[index+1]==" ":
            pass
        analyze+=char[index]
    return text

def removenl(text):
    analyze=""
    for i in text:
        if i =="/n":
            pass
        analyze+=i 
    return analyze               
def analyzetext(request):
    djtext = request.GET.get('text', 'default')
    removepunch = request.GET.get('removepunc', 'off')
    rem_nl = request.GET.get('removenl', 'off')
    capt = request.GET.get('capitalize', 'off')
    rem_sp = request.GET.get('removesp', 'off')   
    print(djtext)
    print(removepunc)
    print(rem_nl)
    print(capt)
    print(rem_sp)
    analyzed=djtext
    test=1
    if(removepunch!="off" and test==1):
        test=0
        analyzed=removepunc(analyzed)
        if(capt!="off"):
            analyzed=capitalize(analyzed)
        if(rem_nl!="off"):
            analyzed=removenl(analyzed)
        if(rem_sp!="off"):
            analyzed=removesp(analyzed)
    if(capt!="off" and test==1):
        test=0
        analyzed=capitalize(analyzed)
        if(removepunch!="off"):
            analyzed=removepunc(analyzed)
        if(rem_nl!="off"):
            analyzed=removenl(analyzed)
        if(rem_sp!="off"):
            analyzed=removesp(analyzed)
    if(rem_nl!="off" and test==1):
        test=0
        analyzed=capitalize(analyzed)
        if(removepunch!="off"):
            analyzed=removepunc(analyzed)
        if(capt!="off"):
            analyzed=removenl(analyzed)
        if(rem_sp!="off"):
            analyzed=removesp(analyzed)        
    if(rem_sp!="off" and test==1):
        test=0
        analyzed=capitalize(analyzed)
        if(removepunch!="off"):
            analyzed=removepunc(analyzed)
        if(capt!="off"):
            analyzed=removenl(analyzed)
        if(rem_nl!="off"):
            analyzed=removesp(analyzed)
    params = {'purpose': 'Analayzed_Text : ', 'analyzed_text': analyzed}
    #return HttpResponse("hello im mudair hayat")
    return render(request, 'analyze.html', params)
# def about(request):
#     return HttpResponse("hello bhae")

# def forhelp():
#     return (open("file.txt"))


# def capitalize(request):
#     file = forhelp()
#     return HttpResponse("capitalized text \n <a href='http://127.0.0.1:8000/'>BACK</a>")


# def spaceremove(request):
#     file = forhelp()
#     return HttpResponse("spaceremoved text \n <a href='http://127.0.0.1:8000/'>BACK</a>")


# def lineremove(request):
#     file = forhelp()
#     return HttpResponse("lineremoved text \n <a href='http://127.0.0.1:8000/'>BACK</a>")


# def charcount(request):
#     file = forhelp()
#     return HttpResponse("charactercounted text \n <a href='http://127.0.0.1:8000/'>BACK</a>")


# def removepunc(request):
#     file = forhelp()
#     return HttpResponse("removepunc text \n <a href='http://127.0.0.1:8000/'>BACK</a>")
