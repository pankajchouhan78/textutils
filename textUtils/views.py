from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def analyzee(request):
    if request.method=="POST":
        djtext = request.POST.get('text')
        upper = request.POST.get('ucase','off')
        lower = request.POST.get('lcase','off')
        removep = request.POST.get('rp','off')
        removesp = request.POST.get('rs','off')
        newLiner = request.POST.get('nlr','off')
        charcount = request.POST.get('cc','off')

        if upper=='on':
            analyzed=""
            for char in djtext:
                analyzed+=char.upper()
            dct={'operation':"Upper case",'ans':analyzed}
            #return render (request,"analyzee.html",dct)
            djtext=analyzed
    
        if lower=="on":
            analyzed=""
            for char in djtext:
                analyzed+=char.lower()
            dct={'operation':"LOWER CASE",'ans':analyzed}
            #return render(request,"analyzee.html",dct)
            djtext=analyzed
    
        if removep=='on':
            analyzed=""
            punctuations='''!()=-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in djtext:
                if char not in punctuations:
                    analyzed+=char
            dct={'operation':"REMOVE PUNCTUATIONS",'ans':analyzed}
            #return render(request,"analyzee.html",dct)
            djtext=analyzed

        if removesp=='on':
            analyzed=""
            for index,char in enumerate(djtext):
                if not(index==" " and index+1==" "):
                    analyzed+=char
            dct={'operation':"REMOVE EXTRA SPACES",'ans':analyzed}
            #return render(request,"analyzee.html",dct)
            djtext=analyzed
    
        if newLiner=='on':
            analyzed=""
            for char in djtext:
                if not(char=="\n"):
                    analyzed+=char
            dct={'operation':"NEW LINE REMOVE",'ans':analyzed}
            #return render(request,"analyzee.html",dct)
            djtext=analyzed
    
        if charcount=='on':
            count=0
            for char in djtext:
                count+=1
            a="In " + djtext + " there are " + str(count) + " charctor"
            dct={'operation':"CHARACTOR COUNT",'ans':a}
            #return render(request,"analyzee.html",dct)
            djtext=analyzed

        if (upper!='on' and lower!='on' and removesp!="on" and newLiner!="on" and charcount!="on" and removep!="on"):
            messages.info(request,"Please select any option")
            return redirect('/')
    return render(request,"analyzee.html",dct)