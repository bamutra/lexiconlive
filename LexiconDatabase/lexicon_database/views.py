from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import EngDefn, Lemma,Adjective,Adverb,Pos,Verb,Nouns
from .forms import LemmaForm 
from django.http import HttpResponseRedirect


def index(request):
    context = EngDefn.objects.all()
    return HttpResponse("Hello, world. You're at the polls index.")

def insertLemma(request):
    form = LemmaForm()
    if request.method == "POST":
        form = LemmaForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')

    #     lemma_id1 = request.POST['lemma_id']
    #     lemma1 = request.POST['lemma']
    #     syllable_structure1 = request.POST['syllable_structure']
    #     lang = request.POST['lang']
    #     lemma_diac = request.POST['lemma_diac']
    #     tone = request.POST['tone']
    #     b = Lemma(lemma_id={{lemma_id1}},lemma='{{lemma1}}',syllable_structure='{{syllable_structure1}}')
    #     b.save()

    context = {
    'form': form,
    }

        
    return render(request, 'lexicon/insertLemma.html', context)



def Add(request):
    submitted = False
    if request.method == "POST":
        form = LemmaForm()
        form = LemmaForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
            return HttpResponseRedirect('/add?submitted=True')
    else:
        form = LemmaForm()
        if 'submitted' in request.GET: 
            submitted = True

    context = {
    'form': form,
    'submitted': submitted,

    } 
    return render(request, 'lexicon/add.html', context)


def LemmaList(request):
    lemma = Lemma.objects.all()[:100]
   
    context = {
    'lemma': lemma,
    }
    return render(request, 'lexicon/lemma_list.html', context)

def from100to200(request):
    lemma = Lemma.objects.all()[100:200]
   
    context = {
    'lemma': lemma,
    }
    return render(request, 'lexicon/from100to200.html', context)

def LemmaView(request, lemma_id):
    lemma = Lemma.objects.get(pk=lemma_id)
   
    context = {
    'lemma': lemma,
    }
    return render(request, 'lexicon/lemma.html', context)


def LemmaUpdateView(request, lemma_id):
    lemma = Lemma.objects.get(pk=lemma_id)
    form = LemmaForm(request.POST or None, instance=lemma)
    if form.is_valid():
        form.save()
        return redirect('lemma_list')
            

    context = {
    'lemma': lemma,
    'form': form,
    }
    return render(request, 'lexicon/update_lemma.html', context)


def Search(request):
    # lemma = Lemma.objects.get(pk=1)
    # form = LemmaForm(request.POST or None, instance=lemma)
    # if form.is_valid():
    #     form.save()
    #     return redirect('lemma_list')

    if request.method == 'POST':
        searched = request.POST.get('searched')
        lemma = Lemma.objects.filter(lemma__contains=searched)
        context = {
        'searched': searched,
        'lemma': lemma,
        }
        return render(request, 'lexicon/search.html', context)
    else:
        context = {
        # 'searched': searched,
        # 'form': form,
        }
        return render(request, 'lexicon/search.html', context)


def homepage(request):
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
    return render(request, 'lexicon/home.html', context)

