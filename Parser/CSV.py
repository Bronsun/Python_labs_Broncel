import pandas as pd


df = pd.DataFrame({
    'Marka':[],
    'Model':[],
    'Cena':[],
    'Pojemność pamięci':[],
    'Bateria':[],    
})

file = pd.read_csv("Phones.csv")

print("Twoje telefony. Co chcesz zrobić: \n")
print("1.Dodać telefon \n")
print("2.Usunąć telefon \n")
print("3. Wyświetl plik \n")


x = input("Wpisz numer: ")

if x == '1':
    marka = input("Podaj marke telefonu: ")
    model = input("Podaj model telefonu: ")
    cena = input("Podaj cenę telefonu: ")
    pojemnosc = input("Podaj pojemnosc pamieci: ")
    bateria = input ("Podaj pojemnosc baterii: ")

    data = [{'Marka':marka,'Model':model,'Cena':cena,'Pojemność pamięci':pojemnosc,'Bateria':bateria}]
    new = df.append(data,ignore_index=True,sort=False)
    new.to_csv("Phones.csv",mode='a',header=False)

if x =='2':
    id = int(input("Podaj numer wiersza, który chcesz usunąć: "))
    file.drop(df.columns[[id]],axis=1)    

if x =='3':
    print(file)
