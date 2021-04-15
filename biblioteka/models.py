from django.db import models
from django.core.validators import MaxValueValidator
from .validators import validate_rok

class Autor(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=20, blank=False)
    data_urodzenia = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=50, blank=False)
    rok_wydania = models.IntegerField(blank=False, validators=[validate_rok])
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-rok_wydania']
        verbose_name = "książka"
        verbose_name_plural = "książki"
        unique_together = ["tytul", "rok_wydania"]
        indexes = [
            models.Index(fields = ['tytul'], name = 'tytul_inx'),
            models.Index(fields = ['tytul', 'rok_wydania']),
        ]
        permissions = [
            ('can_update_ksiazka', "Może zmienić książkę")
        ]
    # def save(self, *args, **kwargs):
    #     if self.rok_wydania > 2020:
    #         raise ValueError("Rok wydania jest większy niż 2020.")
    #     super(Ksiazka, self).save(*args, **kwargs)

#swoj validator:
    def save(self, *args, **kwargs):
        validate_rok(self.rok_wydania)
        super(Ksiazka, self).save(*args,  **kwargs)

    def jest_nowoczesna(self):
        return True if self.rok_wydania > 2000 else False

    def __str__(self):
        return self.tytul