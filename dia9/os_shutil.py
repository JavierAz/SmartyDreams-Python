import os, shutil, send2trash

# es un pwd
print(os.getcwd())
# lista los archivos, en una lista
print(os.listdir())

# mueve los archivos
shutil.move('curso.txt', '/home/javier/Documents')

# lo manda a papelera
send2trash.send2trash('curso.txt')
