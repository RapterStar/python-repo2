# -*- coding: utf-8 -*-
print("Ile ważysz?")
waga = int(input())
if (waga >= 80):
    print("Twoja waga jest duża!")
else:
    print("Dobra waga!")

print("Ile masz lat?")
wiek = int(input())
if(wiek >= 18):
    print("Jesteś pełnoletni.")
else:
    print("Troche ci zostało do pełnoletności.")

print("Jaki masz wzrost?")
wzrost = int(input())
if(wzrost >= 180):
    print("Jesteś wysoki.")
BMI = waga/(wzrost**2)
print("Twoje BMI wynosi:", BMI * 10000)





