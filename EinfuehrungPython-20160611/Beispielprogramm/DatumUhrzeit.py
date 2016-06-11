#!/usr/bin/env python
# https://docs.python.org/2/library/datetime.html
import datetime

''' Aktuelles Datum und Zeit setzen '''
jetzt = datetime.datetime.now()

''' Ausgabe in Standarddarstellung '''
print jetzt.strftime('%c')

''' Ausgabe im ISO 8601 Format '''
print jetzt.isoformat()

''' Ausgabe in eigenem Format '''
print jetzt.strftime('%Y%m%d-%H%M')

''' Datum vorgeben '''
irgendwann = datetime.date(2017,1,1)
print irgendwann.strftime('%c')
