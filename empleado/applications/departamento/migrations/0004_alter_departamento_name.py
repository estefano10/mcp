# Generated by Django 4.0.4 on 2022-10-18 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_alter_departamento_options_alter_departamento_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='Nombre'),
        ),
    ]
