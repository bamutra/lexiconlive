from django import forms
from django.forms import ModelForm
from lexicon_database.models import Lemma

class LemmaForm(ModelForm):
    class Meta:
        model = Lemma
        # fields = ('lemma',)
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(LemmaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
       



