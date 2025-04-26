#asignacion de valor literal

correo_remitente="rafaupelipb@gmail.com"
correo_destinatario="lunaprima@gmail.com"
contraseña="202527"
asunto_del_mensaje="Lista de precios Abril 2025"
mensaje_contenido="Favor enviar respuesta, luego de revisar, Gracias"
adjuntar="Archivo adjuntado"
fecha="5 de abril 2025"
hora="04:33"


print("Correo del remitente:", correo_remitente,)
print("correo_destinatario:", correo_destinatario)
print("contraseña:",contraseña)
print("Asunto del mensaje:", asunto_del_mensaje)
print("Mensaje_contenido:", mensaje_contenido)
print("adjuntar:", adjuntar)
print("fecha:", fecha)
print("HORA:", hora)

import random
radio=random.randint(1,15)
areac=3.14*radio**2
print(f"el area del circulo cuyo radio es {radio} es {areac}")

print("|")
print("|")
print("Ejercicio del àrea de un triàngulo")
base=random.randint(1,25)
altura=random.randint(10,25)
area=base*altura

print(f"la base{base} altura {altura}, area{area}")


import random
cantidad=random.randint(10,100)
precio_BCV=72
precio_promedio=84
total_BCV=precio_BCV*cantidad
total_promedio=precio_promedio*cantidad

print(f"""Para comprar{cantidad}dòlares a BCV,
      DEBE PAGAR{total_BCV}Bolìvares""")
print(f"""Para comprar{cantidad}dòlares a 
      PROMEDIO, DEBE PAGAR {total_promedio} Bolivares""")







      