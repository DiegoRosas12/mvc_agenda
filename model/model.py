from .contacto import Contacto
from .cita import Cita


class Model:
    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0

    # Contacto methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.esta_id(id_contacto)
        if not e:
            c = Contacto(id_contacto, nombre, tel, correo, dir)
            self.contactos.append(c)
            return True, c
        return False, c
    
    def leer_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)
        return e, c

    def leer_todos_contactos(self):
        return self.contactos

    # Buscar contactos que empiezan con una letra y devuelve una lista de contactos
    def leer_contactos_letra(self, inicial):
        # lista = [c for c in self.contactos if c.nombre.loweer.startwith(inicial)]
        lista_nombres = []
        print("Contactos que inician con ",inicial)
        for c in self.contactos:
            if c.nombre[:1].lower() == inicial.lower():
                print(c.nombre)
                lista_nombres.append(c)
        return lista_nombres



    def actualizar_contacto(self, id_contacto, n_nombre = None, n_tel = None, n_correo = None, n_dir = None):
        e, c = self.esta_id(id_contacto)
        if e:
            if not n_nombre == None:
                c.nombre = n_nombre
            if not n_tel == None:
                c.tel = n_tel
            if not n_correo == None:
                c.correo = n_correo
            if not n_dir == None:
                c.dir = n_dir
            return True
        return False


    def borrar_contacto(self, id_contacto):
        e, contacto = self.esta_id(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for i in lista_temp:
                self.citas.remove(i)
            return True, contacto
        return False, 0
    
    # Cita methods
    def esta_id_cita(self, id_cita):
        for c in self.citas:
            if c.id_cita == id_cita:
                return True, c
        return False, 0
        
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if not self.esta_id_cita(id_cita)[0] and self.esta_id(id_contacto):
            c = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
            self.citas.append(c)
            return True, c
        return False, 0
    
    def leer_cita(self, id_cita):
        e, c = self.esta_id_cita(id_cita)
        return e, c
    
    def leer_todas_citas():
        return self.citas

    # Buscar citas de la misma fecha
    def buscar_cita_fecha(self, n_fecha):
        listaCitas = []
        for c in self.citas:
            if c.fecha == n_fecha:
                listaCitas.append(c)
        return listaCitas

    def buscar_cita_fecha_comprension(self, n_fecha):
        listaCitas = [c for c in self.citas if c.fecha == n_fecha]
        return listaCitas


    def actualizar_cita(self, id_cita, n_id_contacto = None, n_lugar = None, n_fecha = None, n_hora = None, n_asunto = None):
        e, c = self.esta_id_cita(id_cita)
        if e:
            if not n_id_contacto == None:
                c.id_contacto = n_id_contacto
            if not n_lugar == None:
                c.lugar = n_lugar
            if not n_fecha == None:
                c.fecha = n_fecha
            if not n_hora == None:
                c.hora = n_hora
            if not n_asunto == None:
                c.asunto = n_asunto
            return True
        return False

    def borrar_cita(self, id_cita):
        e, c = self.esta_id(id_cita)
        if e:
            self.citas.remove(c)
            return True, c
        return False, 0

    