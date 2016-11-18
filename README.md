[![Build Status](https://travis-ci.org/erral/setlem3-tdd.svg?branch=master)](https://travis-ci.org/erral/setlem3-tdd)

# Tenis jokoaren kata

Instalatzeko:

    $ virtualenv .
    $ source bin/activate
    $ pip install -r requirements.txt

Testak exekutatu:

    $ pytest test_biltzarra.py

Testak automatikoki exekutatzeko programatzen ari zaren artean eta
beren berri notifikazioen bidez edukitzeko

    $ ptw --runner "pytest test_biltzarra1.py" --onpass "/usr/bin/notify-send \"Passed\"" --onfail "/usr/bin/notify-send \"Not passed\""
