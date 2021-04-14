from django.shortcuts import render
from django.http import HttpResponse
from .models import Ksiazka, Autor
from django.db import transaction
from django.core.mail import send_mail
from django.contrib import messages
from .forms import NaszForm

def glowna(request):
    autor = {'imie': "Walter", 'nazwisko': "White"}
    ksiazka = {'tytul': "niebieskie cuda", "rok_wydania": 2017}
    dodaj_do_bazy(autor, ksiazka)
    return HttpResponse('Home site')


@transaction.non_atomic_requests
def dodaj_do_bazy(autor, ksiazka):
    with transaction.atomic():
        nowy_autor = Autor.objects.create(**autor)
        nowa_ksiazka = Ksiazka(**ksiazka)
        nowa_ksiazka.autor = nowy_autor
        nowa_ksiazka.save()


def email(request):
    if request.method == "POST":
        if request.POST.get('email', False): #sprawdzenie czy mamy mail z form
            email = request.POST['email'] #przechwycenie i zapisanie emaila 
            wiadomosc = "jakas wiadomosc" + email
            ksiazki = Ksiazka.objects.all()
            for ksiazka in ksiazki:
                wiadomosc += '\n\r' + ksiazka.tytul
            try:
                send_mail(
                    'topic', wiadomosc, email, ['odbiorca@email.pl']
                    )
                messages.success(request, "Mail został wysłany")
            except:
                messages.error(request, "Mail nie został wysłany")
    return render(request, 'email_form.html')

def new_form(request):
    if request.method == 'POST': #jesli jest juz POST (czyli strona się odświeży i mamy już dane)
        form = NaszForm(request.POST) #form zawierający dane pobrane
        if form.is_valid():
            print('Form is valid')  
    else:
        form = NaszForm() #budowanie nowego form jeśli nie ma go POST
    return render(request, 'nasz_form.html', {'form': form})