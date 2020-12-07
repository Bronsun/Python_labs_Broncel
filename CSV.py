import pandas as pd

'''
df = pd.DataFrame({
    'Godziny':[7,8,9,10,11,12,13,14,15,16,17,18,19],
    'Poniedziałek':"",
    'Wtorek':" ",
    'Środa':" ",
    'Czwartek':" ",
    'Piątek':" ",
    'Sobota':" ",
    'Niedziela':" ",
    
})
'''
file = pd.read_csv("Plan Zajęć.csv")

print("Twój plan zajęć. Co chcesz zrobić: \n")
print("1.Dodać lekcje \n")
print("2.Usunąć lekcję \n")
print("3.Poprawić błąd \n")
print("4. Wyświetl plan \n")


x = input("Wpisz numer: ")

if x == '1':
    day = int(input('Wpisz dzień (1-pon,2-wt,3-sr,4-czw itd) itd): '))
    hour = int(input('Które to są zajęcia (1,2,3): '))
    text = input('Wpisz swoje zajęcia: ')
    file.iloc[hour,day] = text
    file.to_csv("Plan Zajęć.csv")

if x =='2':
    day = int(input('Wpisz dzień (1-pon,2-wt,3-sr,4-czw itd) itd): '))
    hour = int(input('Które to są zajęcia (1,2,3): '))
    x = input("Czy na pewno chcesz to usunąć? (Tak/Nie): ").lower()

    if x == "tak":
        file.iloc[hour,day]= " "
        file.to_csv("Plan Zajęć.csv")
        print(file)
    else:
        print("Dobranoc")
if x =='3':
    day = int(input('Wpisz dzień (1-pon,2-wt,3-sr,4-czw itd) itd): '))
    hour = int(input('Które to są zajęcia (1,2,3): '))
    text = input('Wpisz swoje zajęcia: ')
    d  = file.iloc[hour,day] = text
    d.to_csv("Plan Zajęć.csv")
    print(file)
if x =='4':
    print(file)
else:
    print("Błędny znak")