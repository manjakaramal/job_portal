# Generated by Django 5.1.1 on 2024-09-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_api', '0023_alter_itpark_name_alter_job_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='facebook',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='google_map',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='instagram',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='image_url',
            field=models.URLField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='source',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
