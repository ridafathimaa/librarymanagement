# Generated by Django 4.2.5 on 2023-10-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_rename_bookname_book_book_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Librarian',
        ),
        migrations.AddField(
            model_name='signup',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
