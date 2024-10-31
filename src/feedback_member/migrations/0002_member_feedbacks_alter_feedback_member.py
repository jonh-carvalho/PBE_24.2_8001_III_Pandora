# Generated by Django 5.1.2 on 2024-10-31 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='feedbacks',
            field=models.ManyToManyField(related_name='member_feedbacks', to='feedback_member.feedback'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='feedback_member.member'),
        ),
    ]
