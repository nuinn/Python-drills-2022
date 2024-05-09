list = ["Mickey", "Will", "Lewis", "Iona", "Anna", "Sophie", "Marc"]
Sev = ["Iona"]
Mad = ["Will", "Anna", "Sophie"]
Spa = ["Mickey", "Lewis", "Marc"]
for employee in list :
    print("Welcome back", employee)
    if employee == "Iona":
        print("¡Olé Sevilla!")
    if employee == "Will" or "Anna" or "Sophie":
        print("¡Viva Madrid!")
    else:
        print("¡a la mierda!")    
