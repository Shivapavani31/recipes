# Generated by Django 5.1.3 on 2025-02-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonveg', '0002_beef_meat_pork_seafood'),
    ]

    operations = [
        migrations.AddField(
            model_name='beef',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chicken',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meat',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pork',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seafood',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
