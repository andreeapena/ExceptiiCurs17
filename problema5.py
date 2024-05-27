
# Scrieti o functie care citeste un string de la tastatura si afiseaza lungimea lui. Tratati cazul in care textul nu este string

def citesteString():
    try:
        text=input('StringulCitit= ')
        lungime=len(text)
        print(f'lungimea stringului este {lungime}')
    except ValueError as e:
        print(e)

citesteString()
# Fiind dat un dictionar {"a":1,"b":2,"c":3} scrieti o functie care primeste ca parametru cheia si returneaza valoarea