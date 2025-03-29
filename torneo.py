
participantes = []  


participantes.append("Alex")  
participantes.append("Sofia")  
participantes.append("Juan")   


participantes.extend(["Luna", "Max"]) 
print("Participantes del torneo:", participantes)


juego = ("FIFA", "Deportes", 1993) 


print(f"El juego {juego[0]} es del género {juego[1]} y fue lanzado en {juego[2]}.") 

equipos = set()  

equipos.add("Leones")  
equipos.add("Pumas")   
equipos.add("Tigres")  
equipos.add("Leones")  

print("Equipos registrados:", equipos)


puntajes = {
    "Alex": 100,    
    "Sofia": 85,   
    "Juan": 120,   
    "Luna": 90,    
    "Max": 110      

print("Puntajes del torneo:", puntajes)


participantes.remove("Juan")  }
print("Participantes después de la retirada de Juan:", participantes)


print("Año de lanzamiento del juego:", juego[2])  


equipos.add("Águilas")  
print("¿Águilas está en los equipos?", "Águilas" in equipos)  


puntajes["Max"] = 150  

print("Puntajes actualizados:", puntajes)


nombre = input("Ingresa el nombre del participante: ")
puntaje = int(input("Ingresa el puntaje del participante: "))  

puntajes[nombre] = puntaje 

print("Puntajes actualizados:", puntajes)
