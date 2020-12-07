from PIL import Image
import os,sys,re



def one_image(jpeg,png):
    Image.open(jpeg).save(png)
    


def whole_directory(folder1,folder2):
    path = os.path.abspath(folder1)
    folder = os.path.abspath(folder2)
    if not os.path.exists(folder):
        os.mkdir(folder)

    if os.path.exists(path):
        for filename in os.listdir(path):
            if filename.endswith('.jpg,.jpeg'):
                image = Image.open(os.path.join(path,filename))
                pattern= r'(.*)\.'
                data = re.search(pattern,filename)
                image.save(f'{folder}/{data.group(1)}.png')
    else:
        print(f'Folder nie istnieje')

print("Wybierz opcję:\n")
print("1.Konwersja jednego zdjęcia\n")
print("2.Konwersja całego folderu\n")
number = int(input("Wpisz cyfrę: "))

if number == 1:
    jpeg = str(input("Wpisz nazwę obrazku JPEG: "))
    png = str(input("Wpisz nazwę jaka ma być po konwersji na PNG: "))
    one_image(jpeg,png)

elif number ==2 :
    jpeg = str(input("Wpisz sciezke do folderu gdzie znajdują się jpeg: "))
    png = str(input("Wpisz ściezkę do folder, w którym mają być zapisane png: "))
    whole_directory(jpeg,png)

else:
    print("Błędny numer") 
