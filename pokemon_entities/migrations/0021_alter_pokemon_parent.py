# Generated by Django 4.2 on 2023-04-20 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_alter_pokemon_parent_alter_pokemonentity_pokemon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kids', to='pokemon_entities.pokemon', verbose_name='эволюция'),
        ),
    ]
