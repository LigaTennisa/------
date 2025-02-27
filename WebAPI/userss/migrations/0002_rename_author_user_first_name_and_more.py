# Generated by Django 5.0.2 on 2024-04-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='author',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='title',
            new_name='password1',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
