import zipfile

mi_zip = zipfile.ZipFile('archivo_comprimido', 'w')
mi_zip.write('mi_texto.txt')
mi_zip.close()

unzip = zipfile.ZipFile('archivo_comprimido', 'r')
unzip.extractall()
