# Generated by Django 5.2.3 on 2025-07-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resturant', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]
