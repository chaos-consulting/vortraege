#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Demonstration Dateien lesen und schreiben
'''
import os

def write_file(name):
    '''
        Schreibe eine Datei
        :param filename: Name der zu schreibenden Datei
        :return: Gibt nichts zurück
    '''
    meinedatei = open(name, 'w')
    for i in range(1, 10):
        meinedatei.write('Zeile %d\n' % i)
    meinedatei.close()

def read_file(name):
    '''
        Datei zeilenweise lesen und ausgeben
        :param filename: Name der zu lesenden Datei
        :return: Gibt nichts zurück
    '''
    meinedatei = open(name, 'r')
    for zeile in meinedatei:
        print zeile,
    meinedatei.close()

if __name__ == '__main__':
    DATEI = 'foobar.txt'
    write_file(DATEI)
    read_file(DATEI)

    # Datei löschen
    os.remove(DATEI)
