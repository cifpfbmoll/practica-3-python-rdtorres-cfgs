# Pida al usuario el precio de un producto y el nombre del producto
# y muestre el mensaje con el precio del IVA (21%). Por ejemplo:
# “Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros en total”.

producto = str(input("¿Que te has comprado? "))
precio = int(input("¿Cuanto te ha costado? "))
precioiva = int(((precio * 21)/100) + precio)
final = str(print('Tú', producto,'vale ', precio, 'y con el IVA se queda en', precioiva, 'euros en total.'))
