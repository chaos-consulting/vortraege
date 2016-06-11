#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Modul mit Hilfsfunktionen
'''

def zeige_auswahl(getraenke):
    '''
        Anzeige der Getränkeauswahl
        :param getraenke: { "1": {"name": xxx, "preis": yyy}}
    '''
    for button in getraenke:
        print("(%s) %-15s %3d" % (button, getraenke[button]["name"], getraenke[button]["preis"]))

if __name__ == "__main__":
    g = {"1": {"name": "kaffee", "preis": 50}, "2": {"name": "capuccino", "preis": 100}}
    zeige_auswahl(g)
