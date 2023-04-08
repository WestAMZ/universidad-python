# Podemos agregar un hint (una pista) del tipo de datos
# unicamente con fines de lectura ya que el tipo se define por el valor
x : str = 10

# como valor es int, no vale de nada el hint agregado (ya que no le cambiará el tipo)
print(x)
# Obtener el tipo de una variable en memoría
print(x)
print(type(x))

x = "Hola mundo"
print(x)
print(type(x))


x = 10.00
print(x)
print(type(x))

# python el case sensitive por tanto en el caso de los valores 
# bool deben escribirse en mayusculas

x = True
print(x)
print(type(x))

#? NOTA: se puede optener ayuda de la documentación de una función con el método help(función)
#? print(help(print))

# Output

# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.

# None

numero1 = 1
numero2 = 2

# Usamos la función int() para desde texto
print("Suma",int(numero1) + int(numero2))