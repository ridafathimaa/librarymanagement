# Generated by Django 4.2.5 on 2023-10-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_delete_librarian_signup_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='type',
        ),
        migrations.AddField(
            model_name='login',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
