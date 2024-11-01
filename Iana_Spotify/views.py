from django.shortcuts import render, redirect
from .forms import Artista, CancionFavorita, CancionSimilar

def home_view(request):
    return render(request, 'Iana_Spotify/insertar_datos.html')

def insertar_datos(request):
    if request.method == 'POST':
        print(request.POST)  # Para ver todos los datos recibidos
        
        # Guardar los artistas, eliminar espacios y convertir a minúsculas
        artista1_nombre = request.POST.get('artista1').strip().lower()
        artista2_nombre = request.POST.get('artista2').strip().lower()
        artista3_nombre = request.POST.get('artista3').strip().lower()

        # Crear o obtener los artistas
        artista1, _ = Artista.objects.get_or_create(nombre=artista1_nombre)
        artista2, _ = Artista.objects.get_or_create(nombre=artista2_nombre)
        artista3, _ = Artista.objects.get_or_create(nombre=artista3_nombre)

        # Guardar las canciones favoritas para el primer artista
        for i in range(1, 6):
            cancion_favorita_titulo = request.POST.get(f'cancion{i}_artista1').strip()
            if cancion_favorita_titulo:
                CancionFavorita.objects.create(artista=artista1, titulo=cancion_favorita_titulo)

        # Guardar las canciones favoritas para el segundo artista
        for i in range(1, 6):
            cancion_favorita_titulo = request.POST.get(f'cancion{i}_artista2').strip()
            if cancion_favorita_titulo:
                CancionFavorita.objects.create(artista=artista2, titulo=cancion_favorita_titulo)

        # Guardar las canciones favoritas para el tercer artista
        for i in range(1, 6):
            cancion_favorita_titulo = request.POST.get(f'cancion{i}_artista3').strip()
            if cancion_favorita_titulo:
                CancionFavorita.objects.create(artista=artista3, titulo=cancion_favorita_titulo)

        # Función para manejar la adición de canciones similares
        def agregar_canciones_similares(artista, offset):
            for i in range(1, 6):
                cancion_similar_titulo = request.POST.get(f'similars{i + offset}').strip()
                artista_similar_nombre = request.POST.get(f'similars_artist{i + offset}').strip().lower()  # Convertir a minúsculas
                if cancion_similar_titulo and artista_similar_nombre:
                    # Asegurarse de que no se cree un artista duplicado
                    artista_similar, _ = Artista.objects.get_or_create(nombre=artista_similar_nombre)
                    
                    # Crear la canción similar y relacionarla con el artista principal
                    CancionSimilar.objects.create(
                        titulo=cancion_similar_titulo,
                        artista=artista_similar,
                        artista_principal=artista  # Relacionar con el artista principal
                    )

        # Agregar canciones similares para cada artista
        agregar_canciones_similares(artista1, 0)   # Para el primer artista
        agregar_canciones_similares(artista2, 5)   # Para el segundo artista
        agregar_canciones_similares(artista3, 10)  # Para el tercer artista

        return redirect('success')  # Redirige a una página de éxito o donde desees

    return render(request, 'Iana_Spotify/insertar_datos.html')



def success_view(request):
    return render(request, 'exito.html')