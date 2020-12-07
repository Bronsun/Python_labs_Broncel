import os, os.path

DIR = '/tmp' # <--- w folderze /dev jest zero folderów bo nie istnieje
print (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))