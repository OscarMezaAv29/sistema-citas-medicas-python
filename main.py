print("\nOscar Alejandro Meza Avendaño")
print("9° A")
print("Desarrollo para Dispositivos Inteligentes")

from doctores import acciones

print("""
Acciones disponibles:
    - Registrarse
    - Login
""")

hazEl = acciones.Acciones()
accion = input("¿Qué quieres hacer?: ")

if accion == "Registrarse":
    hazEl.registro()
elif accion == "Login":
    hazEl.login()