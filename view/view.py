class View:
    def mostrar_contacto(self, contacto):
        print('****** Datos del contacto *******')
        print('Nombre: ', contacto.nombre)
        print('Teléfono', contacto.tel)
        print('Correo: ', contacto.correo)
        print('Dirección', contacto.dir)
        print('*********************************')

    def mostrar_contactos(self, contactos):
        print('********* Contactos *************')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('*********************************')

    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'se ha agregado a la base de datos! ')

    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'se ha borrado de la base de datos')

    def actualizar_contacto(self, contacto_o, contacto_n):
        print(contacto_o.nombre, 'se ha modificado correctamente!')

    def contacto_ya_existe(self, contacto):
        print('El contacto', contacto.id_contacto, 'Ya existe en la base de datos')
    
    def contacto_no_existe(self, id_contacto):
        print('El contacto',id_contacto, 'No existe en la base de datos')

    def mostrar_cita(self, cita):
        print('****** Datos del cita *******')
        print('Asunto: ', cita.asunto)
        print('Lugar', cita.lugar)
        print('Hora: ', cita.hora)
        print('Fecha', cita.fecha)
        print('*********************************')

    def mostrar_citas(self, citas):
        print('********* citas *************')
        for c in citas:
            print(c.asunto, c.lugar, c.hora, c.fecha)
        print('*********************************')

    def agregar_cita(self, cita):
        print(cita.asunto, 'se ha agregado a la base de datos! ')

    def borrar_cita(self, cita):
        print(cita.asunto, 'se ha borrado de la base de datos')

    def modificar_cita(self, cita_o, cita_n):
        print(cita_o.asunto, 'se ha modificado correctamente!')

    def cita_ya_existe(self, cita):
        print(cita.id_cita, 'Ya existe en la base de datos')
    
    def cita_no_existe(self, id_cita):
        print(id_cita, 'No existe en la base de datos')

    # General views
    def start(self):
        print('Esto es un ejemplo sencillo de MVC')

    def end(self):
        print('Hasta la vista')

    def opcion_no_valida(self):
        print('Opcion no valida')

    def menu(self):
        print('1. Agregar contacto')
        print('2. Buscar contacto')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Mostrar citas')
        print('6. Crear cita')
        print('7. Modificar cita')
        print('8. Borrar cita')
        print('0. Salir')
        print()