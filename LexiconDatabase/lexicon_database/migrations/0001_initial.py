# Generated by Django 4.1 on 2022-08-24 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjective',
            fields=[
                ('adjective_id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.CharField(blank=True, max_length=4, null=True)),
                ('doesagree', models.CharField(blank=True, db_column='doesAgree', max_length=5, null=True)),
                ('isproper', models.CharField(blank=True, db_column='isProper', max_length=5, null=True)),
                ('isprepositional', models.CharField(blank=True, db_column='isPrepositional', max_length=5, null=True)),
            ],
            options={
                'db_table': 'adjective',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Adverb',
            fields=[
                ('adverb_id', models.AutoField(primary_key=True, serialize=False)),
                ('does_agree', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'adverb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EngDefn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defn', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'eng_defn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lemma',
            fields=[
                ('lemma_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lemma', models.CharField(blank=True, max_length=100, null=True)),
                ('lemma_diac', models.CharField(blank=True, max_length=100, null=True)),
                ('syllable_structure', models.CharField(blank=True, max_length=200, null=True)),
                ('tone', models.CharField(blank=True, max_length=100, null=True)),
                ('lang', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'lemma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nouns',
            fields=[
                ('noun_id', models.AutoField(primary_key=True, serialize=False)),
                ('nc_particles', models.CharField(blank=True, max_length=45, null=True)),
                ('nc_numerical', models.CharField(blank=True, max_length=45, null=True)),
                ('nc_numerical_pair', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'nouns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pos',
            fields=[
                ('pos_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_level', models.CharField(blank=True, max_length=45, null=True)),
                ('second_level', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'POS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_conjg', models.CharField(blank=True, max_length=3, null=True)),
                ('conjugation', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'verb',
                'managed': False,
            },
        ),
    ]
