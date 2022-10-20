# Generated by Django 4.0.4 on 2022-05-31 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_name_alter_departamento_shor_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la Empresa'},
        ),
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]