#! /usr/bin/env python

print("blabla")
dist_km: float = float(input("Distancia percorrida em km = "))
time_min: float = float(input("Tempo necessario para percorre em min = "))
dist_m: float = 1000 * dist_km
time_s: float = 60 * time_min
time_h: float = time_min / 60

speed_kmph: float = dist_km / time_h
speed_mps: float = dist_m / time_s

print(f"Velocidade km/h = {speed_kmph:.2f}")
print(f"Velocidade m/s = {speed_mps:.2f}")
