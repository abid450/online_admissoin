# Generated by Django 5.1 on 2024-08-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_form_model_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_model',
            name='Choise',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
