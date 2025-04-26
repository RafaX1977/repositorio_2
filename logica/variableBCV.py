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

