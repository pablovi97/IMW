def show_contacts(phone_book):
	for name, number in phone_book.items():
		print(name, number)

def add_contact(phone_book, name, phone):
	phone_book[name] = phone

def remove_contact(phone_book, name):
	del(phone_book[name])

def menu():
	phone_book = {}
	while True:
		print("Menu:")
		print("1. Mostrar Lista De Contactos.")
		print("2. Añadir Contacto.")
		print("3. Borrar Contacto.")
		print("4. Salir.")
		x = int(input("texto"))
		if x == 1:
			show_contacts(phone_book)
		if x == 2:
			name = input("Introduzca un nombre de Contacto")
			if name in phone_book:
				print("El numero ya existe, ponga otro :D")
			else:
				phone = input()
				add_contact(phone_book, name, phone)
		if x == 3:
			name = input("Introduzca un nombre para eliminarlo")
		if name in phone_book:
			remove_contact(phone_book, name)
		if x == 4:
			print("adios")
		break