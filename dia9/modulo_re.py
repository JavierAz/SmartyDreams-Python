"""
Caracteres especiales
/d digito numerico
/w caracter alfanumerico
/s espacio en blanco
/D NO numerico
/W NO alfanumerico
/S no espacio en blanco

Cuantificadores
+ 1 o mas veces
{n} se repite n veces
{n,m} se repite de n a m veces
{n,} desde n hacia arriba
* 0 o mas veces
? 1 o 0
"""
import re

texto = 'Esta es una frase inventada porque la que aparecio estaba muy larga 658-598-997'

patron = 'frase'
busqueda = re.findall(patron, texto)

for i in re.finditer(patron, texto):
    print(i.span())

numero = re.compile(r'\d{3}-\d{3}-\d{3}')
res = re.search(numero, texto)
print(res.group())


# ejercicio 1
def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


# ejercicio 2
def saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")


# ejercicio 3
def cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
