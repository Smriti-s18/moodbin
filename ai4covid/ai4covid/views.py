from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static



import text2emotion as te 

def index(request):
    return render(request, 'index.html')
    
    
def findit(feel):
    tmp=""
    a=te.get_emotion(feel)
    happy=a['Happy']
    sad=a['Sad']
    if sad>happy:
        sad+=a['Surprise']
    else:
        happy+=a['Surprise']  
    sad+=a['Angry']+a['Fear']    
    if happy>sad:
        tmp="happy" #"Hurray! You are so happy"
    elif sad>happy:
        tmp="sad" #"Oops! Don't be so sad"
    else:
        tmp="both" #"Hmm! You are neither Happy nor Sad"
    return tmp

def feeling(request):
    print(request)
    items=request.POST.dict()
    print(items)
    result=findit(items.get("feeling"))
    print(result)
    #return render(request, 'feel/feeling.html',{"items":items})
    response = HttpResponse("<em>%s</em>"%result, content_type="text/plain")
    response = HttpResponse('<br><img tooltip="%s" src="/static/images/%s.gif"></img>'%(result,result))
    return response
