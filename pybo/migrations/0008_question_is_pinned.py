# Generated by Django 4.0.3 on 2024-08-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_remove_question_is_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_pinned',
            field=models.BooleanField(default=False),
        ),
    ]