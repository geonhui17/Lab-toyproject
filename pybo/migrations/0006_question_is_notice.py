# Generated by Django 4.0.3 on 2024-08-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_answer_voter_question_voter_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_notice',
            field=models.BooleanField(default=False),
        ),
    ]
