import logging
from django.dispatch import receiver, Signal
from .models import Autor


#własny log
autor_log = logging.getLogger("autor_log")
autor_log.setLevel(logging.DEBUG)
log_handler = logging.FileHandler('logs/autor.log')
log_handler.setLevel(logging.DEBUG)
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #asctime-czas wydarzenia
log_handler.setFormatter(formater) #dodanie formatu do logu
autor_log.addHandler(log_handler) #dołączanie handlera do loga


@receiver([post_save], sender=Autor)
def autor_po_zapisaniu(sender, instance, **kwargs):
    print('wlasnie zapisalismy autora')
    print(instance.imie)
    #włozenie do pliku
    autor_log.info("Stworzono autora: {} {} ".format(instance.imie, instance.nazwisko))