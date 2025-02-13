import folium


from django.shortcuts import render
from pokemon_entities.models import PokemonEntity
from pokemon_entities.models import Pokemon
from django.utils import timezone
from django.shortcuts import get_object_or_404


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_on_page = []
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    time_now = timezone.now()
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=time_now,
        disappeared_at__gte=time_now
    )
    for pokemon_entity in pokemon_entities:
        pokemon = pokemon_entity.pokemon
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon.image.path
        )
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title_rus,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemons_on_page = {
        "pokemon_id": pokemon.id,
        "description": pokemon.description,
        "title_ru": pokemon.title_rus,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "img_url": pokemon.image.url
    }
    if pokemon.parent:
        pokemons_on_page["previous_evolution"] = {
            "title_ru": pokemon.parent.title_rus,
            "pokemon_id": pokemon.parent.id,
            "img_url": pokemon.parent.image.url,
        }
    kid = pokemon.kids.first()
    if kid:
        pokemons_on_page["next_evolution"] = {
            "title_ru": kid.title_rus,
            "pokemon_id": kid.id,
            "img_url": kid.image.url,
        }
    time_now = timezone.now()
    pokemon_entities = pokemon.entities.filter(
        appeared_at__lte=time_now,
        disappeared_at__gte=time_now
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon.image.path
        )

    return render(request, "pokemon.html", context={
        'map': folium_map._repr_html_(), 'pokemon': pokemons_on_page
    })
