from view.view import View
from model.model import Model

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    # Contacto controller
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        b, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if b:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre = None, n_tel = None, n_correo = None, n_dir = None):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else: 
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)
        
    def insertar_contactos(self):
        self.agregar_contacto(1, "Juan Pérez", '464-123-1234', 'pg@gmail.com', 'salamanca')
        self.agregar_contacto(2, "Juanito Romero", '464-123-1234', 'pg@gmail.com', 'salamanca')
        self.agregar_contacto(3, "Ponchito Sierra", '477-123-1234', 'ponchito33@gmail.com', 'leon')
        self.agregar_contacto(4, "Paco Martínez", '477-123-1234', 'ponchito33@gmail.com', 'leon')
        self.agregar_contacto(5, "Amanda Horta", '477-123-1234', 'ponchito33@gmail.com', 'leon')
    
    # cita controller
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        b, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if b:
            self.view.agregar_cita(c)
        else:
            self.view.cita_ya_existe(c)

    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    

    def buscar_cita_fecha(self, n_fecha):
        c = self.model.buscar_cita_fecha(n_fecha)
        self.view.mostrar_citas(c)

    def insertar_citas(self):
        self.agregar_cita(1, 1, 'escuela', '03/05/20', '13:00', 'Reunión escuela')
        self.agregar_cita(2, 2, 'Universidad', '03/05/20', '15:00', 'Reunión universidad')
        self.agregar_cita(3, 2, 'Tokio', '13/01/20', '09:00', 'Comida')
        self.agregar_cita(4, 3, 'Londres', '23/08/21', '10:00', 'Cena')

    def start(self):
        # Display a welcome message
        self.view.start()
        # Insert data in model
        self.insertar_contactos()
        self.insertar_citas()
        # Show all contacts in DB
        # self.leer_todos_contactos()
        # self.leer_contactos_letra('a')

    def menu(self):
        # Display menu
        self.view.menu()
        o = input('Selecciona una opcion (1-9)')
        if o == '1':
            id_contacto = input("id_contacto: ")
            nombre = input("nombre: ")
            tel = input("tel: ")
            correo = input("correo: ")
            dir = input("dir: ")
            self.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if o == '2':
            pass
        if o == '3':
            pass
        if o == '4':
            pass
        if o == '5':
            pass
        if o == '6':
            pass
        if o == '7':
            pass
        if o == '8':
            pass
        if o == '0':
            self.view.end()
        else:
            self.menu()
    