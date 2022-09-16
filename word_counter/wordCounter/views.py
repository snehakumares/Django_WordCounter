from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def wordcounter(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({} , request))

def count(request):
    words = request.POST['words']
    count = len(words.split())
    template = loader.get_template('result.html')
    context = {
        "count" : count,
        "words" : words,
    }
    return HttpResponse(template.render(context, request))