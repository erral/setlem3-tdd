# Tenis jokoaren kata

Instalatzeko:

    $ virtualenv .
    $ pip install -r requirements.txt

Testak exekutatu:

    $ pytest

Testak automatikoki exekutatzeko programatzen ari zaren artean eta
beren berri notifikazioen bidez edukitzeko

    $ ptw --runner "pytest test_biltzarra1.py" --onpass "/usr/bin/notify-send \"Passed\"" --onfail "/usr/bin/notify-send \"Not passed\""
