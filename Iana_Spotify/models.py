from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.nombre
class CancionFavorita(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name="canciones_favoritas")
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"

class CancionSimilar(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, null=True, blank=True)  # Permitir nulos
    artista_principal = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name="canciones_similares", null= True)

    def __str__(self):
        return self.titulo


