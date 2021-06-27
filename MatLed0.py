#!/usr/bin/env python3
import time
import wiringpi as w 

P_ANO = [20, 21, 22, 23, 24]
P_CAT = [6, 7, 2, 8, 3, 4, 5]

w.wiringPiSetupGpio()

for cat in range(7):
	w.pinMode( P_CAT[cat], 1 )
	w.digitalWrite( P_CAT[cat], 0)
for ano in range(5):
	w.pinMode( P_ANO[ano], 1 )
	w.digitalWrite( P_ANO[ano], 0 )

for cat in range(7):
	w.digitalWrite( P_CAT[cat], 1 )
	for ano in range(5):
		w.digitalWrite( P_ANO[ano], 1) 
		time.sleep( 0.5 )
		w.digitalWrite( P_ANO[ano], 0 ) 
	w.digitalWrite( P_CAT[cat], 0 )
