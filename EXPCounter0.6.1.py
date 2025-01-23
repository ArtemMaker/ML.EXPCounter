
import os

print("EXPCounter 0.6.1, By Artem") 
print("") 
rebirths = int(input("Rebirth/Перерождения: ")) 
rebirths2 = rebirths + 20
os.system('cls') 
print("EXPCounter 0.6.1, By Artem") 
print("") 
print("1. Ancient Jungle Rock/Камень Джунглей") 
print("2. Muscle King Rock/Камень Короля Мыщц") 
print("3. Legends Rock/Камень Легенд")
print("4. Inferno Rock/Адский Камень") 
rock = int(input("Rock/Камень: "))
rock2 = 0
if rock == 1:
 rock2 = 16.25  
if rock == 2:
 rock2 = 12.5
if rock == 3:
 rock2 = 2.5
if rock == 4:
 rock2 = 1.125   
os.system('cls') 
exp = rebirths2 * rock2
print("EXPCounter 0.6.1, By Artem") 
print("") 
print(f"Your Rebirths/Ваши Перерождения: {rebirths}") 
print(f"EXP/Опыт: {exp}") 
print("")
if exp >= 0:
    print(f"1 Level/Уровень, {exp} EXP/Опыта") 
if exp >= 1250:
    exp = exp - 1250
    print(f"2 Level/Уровень, {exp} EXP/Опыта")
if exp >= 2500:
    exp = exp - 2500
    print(f"3 Level/Уровень, {exp} EXP/Опыта")
if exp >= 3750:
    exp = exp - 3750
    print(f"4 Level/Уровень, {exp} EXP/Опыта")
if exp >= 5000:
    exp = exp - 5000
    print(f"5 Level/Уровень, {exp} EXP/Опыта")
if exp >= 6750:
    exp = exp - 6250
    print(f"6 Level/Уровень, {exp} EXP/Опыта")
if exp >= 7500:
    exp = exp - 7500
    print(f"7 Level/Уровень, {exp} EXP/Опыта")
if exp >= 8750:
    exp = exp - 8750
    print(f"8 Level/Уровень, {exp} EXP/Опыта")
if exp >= 10000:
    exp = exp - 10000
    print(f"9 Level/Уровень, {exp} EXP/Опыта")
if exp >= 11250:
    exp = exp - 11250
    print(f"10 Level/Уровень, {exp} EXP/Опыта")
if exp >= 12500:
    exp = exp - 12500
    print(f"11 Level/Уровень, {exp} EXP/Опыта")
if exp >= 13750:
    exp = exp - 13750
    print(f"12 Level/Уровень, {exp} EXP/Опыта")
if exp >= 15000:
    exp = exp - 15000
    print(f"13 Level/Уровень, {exp} EXP/Опыта")
if exp >= 16250:
    exp = exp - 16250
    print(f"14 Level/Уровень, {exp} EXP/Опыта")
if exp >= 17500:
    exp = exp - 17500
    print(f"15 Level/Уровень, {exp} EXP/Опыта")
if exp >= 18750:
    exp = exp - 18750
    print(f"16 Level/Уровень, {exp} EXP/Опыта")
if exp >= 20000:
    exp = exp - 20000
    print(f"17 Level/Уровень, {exp} EXP/Опыта")
if exp >= 21250:
    exp = exp - 21250
    print(f"18 Level/Уровень, {exp} EXP/Опыта")
if exp >= 22500:
    exp = exp - 22500
    print(f"19 Level/Уровень, {exp} EXP/Опыта")
if exp >= 23750:
    exp = exp - 23750
    print(f"20 Level/Уровень, {exp} EXP/Опыта")
    
input()        