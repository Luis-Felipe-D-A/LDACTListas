

M = ["LuisD", "Karen", "Maria", "Jesus", "James", "Falcao"]

Menu = int (input("Escojer una opcion del Menu: \n1. Crear Personas \n 2. Elimir Personaje \n 3. Lista de personas \n 4. Buscar persona "))

if Menu == 1:
    print (M)
    m1 = input("ingresa persona:   ")
    M.append(m1)
    print (M)
if Menu == 2:
    print(M )
    m2=input("ingrese el nombre que quiere Eliminar:")
    M.remove(m2)
    print(M)
if Menu ==3:
     print(M)
if Menu ==4:
    print (M)
    m3 = input("Ingrese el nombre de la persona que quiere buscar en el menu:")         
    if m3 in M:
        print ("L persona esta dentro de la lista ")
    else:
        print ("La persona no esta en la lista")     