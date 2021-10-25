from random import randrange

cislo = randrange(11) #vždy je to interval n-1
hadac = 11

print('Hádej číslo do 10.')

while (hadac != cislo):
    hadac = int(input())
    if hadac > cislo:
            print('Číslo je moc velké, hádej znovu')
    elif hadac < cislo:
        print('Číslo je moc malé, hádej znovu')
print('Číslo jsi uhodl. Gratuluji')
