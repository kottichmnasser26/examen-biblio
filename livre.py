titre=input("titre de livre")
exemplaires=int(input("Nombre d'exemplaires"))
print("livre",titre)
print("exemplaires disponibles",exemplaires)
#emprunt d'un livre
exemplaires=exemplaires-1
print("apres emprunt :",exemplaires,"exemplaires(s) disponibles(s)")