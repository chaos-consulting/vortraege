#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Simulation einer einfachen Kaffeemaschine
'''
import kaffee_funktionen
import time

class Kaffemaschine():
    '''
        Die Maschine
    '''
    getraenke = {}
    def __init__(self):
        '''
            Konstruktordinge
        '''
        print "Konstruktor hier"
        self.getraenke = {
            "1": {"name": "kaffee", "preis": 50},
            "2": {"name": "capuccino", "preis": 100}
        }
        self.auswahl = None

    def __del__(self):
        '''
            Abriss...
        '''
        print "Destruktor hier"

    def State_Auswahl(self, value):
        '''
            State Auswahl

            - Anzeige eines Menüs
            - Einlesen des Getränkewunsches
            - Rückgabe Next_State
            - Rückgabe gewähltes Getränk
        '''
        kaffee_funktionen.zeige_auswahl(self.getraenke)
        self.auswahl = input("Auswahl: ")
        return (self.auswahl, self.State_Bezahlen)

    def State_Bezahlen(self, button):
        '''
            Status Bezahlen

            - Münzen entgegennehmen, bis preis erreicht oder überschritten
            - Rückgabe Next_State
            - Rückgabe Restbetrag
        '''
        betragGegeben = 0
        while betragGegeben < self.getraenke[str(button)]["preis"]:
            einwurf = input("Einwurf: ")
            betragGegeben += einwurf
        if betragGegeben > self.getraenke[str(button)]["preis"]:
            return (betragGegeben - self.getraenke[str(button)]["preis"], self.State_Wechselgeld)
        else:
            return (None, self.State_Zubereitung)

    def State_Wechselgeld(self, rueckgabebetrag):
        '''
            Konstruktordinge
        '''
        print "Rückgabe: %d" % rueckgabebetrag
        return (None, self.State_Zubereitung)

    def State_Zubereitung(self, getraenk):
        '''
            Konstruktordinge
        '''
        print "Zubereitung %s" % self.getraenke[str(self.auswahl)]['name']
        return (None, self.State_Warten)

    def State_Warten(self, value):
        '''
            Konstruktordinge
        '''
        print "Warten"
        time.sleep(5)
        return (None, self.State_Auswahl)
     
if __name__ == "__main__":
    meinautomat = Kaffemaschine()

    next = meinautomat.State_Auswahl
    value = None
    
    while True:
        (value, next) = next(value)
