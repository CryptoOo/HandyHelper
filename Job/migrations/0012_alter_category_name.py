# Generated by Django 4.0 on 2021-12-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0011_alter_category_name_remove_job_jobcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Coding', 'Coding'), ('Garden', 'Garden'), ('Buying things', 'Buying things'), ('Electronic', 'Electronic'), ('Pet Care', 'Pet Care'), ('Other', 'Other')], max_length=20, unique=True),
        ),
    ]
