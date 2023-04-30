#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
cadena = "Hola, esta es mi primer cadena!"
numero = 42
lista = ['Pera', 'Manzana', 'Uva', 'Platano', 5]
valor_booleano = True
print(cadena)
print(numero)
print(lista)
print(valor_booleano)
#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
primeras_tres_letras = cadena[0:3]
print(primeras_tres_letras)

#Exercise 3: Use an index to grab the first element from your list.
primer_elemento = lista[0]
print(primer_elemento)

#Exercise 4: Create a new number variable that adds 10 to your original number.
num_agregar = numero + 10
print(num_agregar)

#Exercise 5: Use an index to get the last element in your list.
ultimo_elemento = lista[-1]
print(ultimo_elemento)

#Exercise 6: Use split to transform the following string into a list.
#names = 'harry,alex,susie,jared,gail,conner'
names = 'harry,alex,susie,jared,gail,conner'
lista_names = names.split(',')
print(lista_names)

#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
primer_palabra = cadena[:4]
primer_palabra_mayusculas = primer_palabra.upper()
resto_cadena = cadena[5:]
nueva_cadena = primer_palabra_mayusculas + resto_cadena
print(nueva_cadena)
#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
print(f"Mi número favorito es {numero}.")

#Exercise 9: Print “hello world”.
print("hello world")