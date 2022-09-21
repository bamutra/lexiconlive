from django.db import models


class Pos(models.Model):
    pos_id = models.AutoField(primary_key=True)
    lemma = models.ForeignKey('Lemma', on_delete=models.CASCADE)
    first_level = models.CharField(max_length=45, blank=True, null=True)
    second_level = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'POS'


class Adjective(models.Model):
    adjective_id = models.AutoField(primary_key=True)
    lemma = models.ForeignKey('Lemma', on_delete=models.CASCADE)
    position = models.CharField(max_length=4, blank=True, null=True)
    doesagree = models.CharField(db_column='doesAgree', max_length=5, blank=True, null=True)  # Field name made lowercase.
    isproper = models.CharField(db_column='isProper', max_length=5, blank=True, null=True)  # Field name made lowercase.
    isprepositional = models.CharField(db_column='isPrepositional', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adjective'


class Adverb(models.Model):
    adverb_id = models.AutoField(primary_key=True)
    lemma = models.ForeignKey('Lemma', on_delete=models.CASCADE)
    does_agree = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adverb'


class EngDefn(models.Model):
    lemma = models.ForeignKey('Lemma', on_delete=models.CASCADE)
    defn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eng_defn'


class Lemma(models.Model):
    lemma_id = models.IntegerField(primary_key=True)
    lemma = models.CharField(max_length=100, blank=True, null=True)
    lemma_diac = models.CharField(max_length=100, blank=True, null=True)
    syllable_structure = models.CharField(max_length=200, blank=True, null=True)
    tone = models.CharField(max_length=100, blank=True, null=True)
    lang = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lemma'
class Lemma1(models.Model):
    lemma_id = models.IntegerField(primary_key=True)
    lemma = models.CharField(max_length=100, blank=True, null=True)
    lemma_diac = models.CharField(max_length=100, blank=True, null=True)
    syllable_structure = models.CharField(max_length=200, blank=True, null=True)
    tone = models.CharField(max_length=100, blank=True, null=True)
    lang = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lemma_1'

class Nouns(models.Model):
    noun_id = models.AutoField(primary_key=True)
    lemma = models.ForeignKey(Lemma, on_delete=models.CASCADE)
    nc_particles = models.CharField(max_length=45, blank=True, null=True)
    nc_numerical = models.CharField(max_length=45, blank=True, null=True)
    nc_numerical_pair = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nouns'


class Verb(models.Model):
    lemma = models.ForeignKey(Lemma, on_delete=models.CASCADE)
    lang_conjg = models.CharField(max_length=3, blank=True, null=True)
    conjugation = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verb'
