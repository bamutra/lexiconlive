from django.urls import path

from . import views

urlpatterns = [
    path('test', views.index, name='index'),
    path('', views.homepage, name='home'),
    path('insert', views.insertLemma, name='insertLemma'),
    path('add', views.Add, name='add'),
    path('lemmas', views.LemmaList, name='lemma_list'),
    path('search', views.Search, name='search'),
    path('from100to200', views.from100to200, name='from100to200'),
    path('lemma/<lemma_id>', views.LemmaView, name='lemma'),
    path('update/<lemma_id>', views.LemmaUpdateView, name='update_lemma'),
]