# Generated by Django 4.1.4 on 2022-12-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_auteur_book_description_book_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='prix',
            field=models.IntegerField(null=True),
        ),
    ]
