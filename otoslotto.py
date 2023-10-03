import random

szerencses_szamok = []
felhasznalo_szamai = []

helyes_szamok = 0

print('Üdvözlünk a szerencsés lottószámokban!')
print('Írj be 5 számot:')

for num in range(0,5):
    random_num = random.randint(1, 100)
    szerencses_szamok.append(random_num)

for num in range(0,5):
    user_num = int(input())
    felhasznalo_szamai.append(user_num)

for lucky_num in szerencses_szamok:
    for user_num in felhasznalo_szamai:
        if user_num == lucky_num:
            helyes_szamok = helyes_szamok + 1

print(f'Eltaláltál : {helyes_szamok} számot!')

print(f'Nyertes számok: {szerencses_szamok}')