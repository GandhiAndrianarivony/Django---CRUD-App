# Generated by Django 4.0.10 on 2023-04-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(blank=True, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Publié'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Titre'),
        ),
    ]
