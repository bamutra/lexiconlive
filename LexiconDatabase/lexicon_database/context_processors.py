from django.shortcuts import render
from django.http import HttpResponse
from .models import EngDefn, Lemma,Adjective,Adverb,Pos,Verb,Nouns

def lemma_processor(request):
    lemma = Lemma.objects.all()[:5]
    engdfn = EngDefn.objects.all()[:5]
    noun = Nouns.objects.all()[:5]
    adjective = Adjective.objects.all()[:5]
    verb = Verb.objects.all()[:5]
    adverb = Adverb.objects.all()[:5]
    pos = Pos.objects.all()[:5]
    context = {
    'lemma': lemma,
    'engdfn': engdfn, 
    'noun': noun,
    'adjective': adjective,
    'verb': verb,
    'adverb': adverb,
    'pos': pos,
    }
    return render(request, 'lexicon/engdfn.html', context)