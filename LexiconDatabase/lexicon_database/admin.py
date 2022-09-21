from django.contrib import admin

# Register your models here.
from lexicon_database.models import Lemma,Pos,EngDefn,Verb,Adjective,Adverb,Nouns
admin.site.register(Lemma)
admin.site.register(Pos)
admin.site.register(Verb)
admin.site.register(Adjective)
admin.site.register(Adverb)
admin.site.register(Nouns)