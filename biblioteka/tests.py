from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import new_form
from .models import Autor, Ksiazka
from .validators import validate_rok
from django.core.exceptions import ValidationError
from .forms import NaszForm


class BibliotekaTests(TestCase):
    def test_nasz_pierwszy(self):
        assert 1 == 1

    #url
    def test_url_new_form(self):
        url = reverse('new_form')
        self.assertEquals(resolve(url).func, new_form)

    #views
    def test_view_new_form(self):
        client = Client()
        response = client.get(reverse('new_form'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'nasz_form.html')

    #models
    #setUp stworzenie rekordu zeby nie musiec tworzyc modelu w kazdym tescie
    def setUp(self):
        self.autor = Autor.objects.create(imie = "Testowy", nazwisko = "Autor")
        self.ksiazka = Ksiazka.objects.create(tytul = "Testowa", rok_wydania = 2019, autor = self.autor)

    def test_autor_jako_tekst(self):
        self.assertEqual(str(self.autor), "Testowy Autor")

    def test_ksiazka_nie_jest_pusta(self):
        ksiazka = Ksiazka.objects.create(tytul = "Testowa", rok_wydania = 2010, autor = self.autor)
        self.assertNotEqual(ksiazka, None)

    # def test_ksiazka_jest_unikalna(self):
    #     with self.assertRaises(Exception):
    #         Ksiazka.objects.create(tytul = "Testowa", rok_wydania = 2019, autor = self.autor)

    # def test_ksiazki_manager(self):
    #     ksiazki = Ksiazka.ksiazki.nowoczesne()
    #     self.assertGreater(len(ksiazki), 0)

    #funkcje
    def test_funkcja_validate_rok_dziala(self):
        self.assertRaises(ValidationError, validate_rok, 2025)

    def test_funkcja_validate_rok_dziala2(self):
        self.assertEqual(validate_rok(2019), 2019)

    #forms
    def test_nasz_form_valid(self):
        form = NaszForm(data = {
            'imie': "test",
            'rok': 2020,
        })
        self.assertTrue(form.is_valid())

    def test_nasz_form_valid(self):
        form = NaszForm(data = {
            'imie': "test",
            'rok': 2025,
        })
        self.assertFalse(form.is_valid())

#TDD - Test Driven Development
#spos??b pisania kodu zaczynaj??c od test??w
    def test_ksiazka_metoda_jest_nowoczesna(self):
        #powinna zwrocic True jezeli rok jest wiekszy niz 2000
        self.assertTrue(self.ksiazka.jest_nowoczesna())
        #.jest_nowoczesna jeszcze nie istnieje trzeba stworzyc te metode 

    def test_ksiazka_metoda_jest_nowoczesna(self):
        #powinna zwrocic False jezeli rok jest mniejszy lub rowny 2000
        self.assertTrue(self.ksiazka.jest_nowoczesna)
        ksiazka = Ksiazka.objects.create(tytul = "Testowa", rok_wydania = 2000, autor = self.autor)
        self.assertFalse(self.ksiazka.jest_nowoczesna())