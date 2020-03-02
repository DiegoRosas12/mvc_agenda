from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller

# contactos = []

# c1 = Contacto(1, "Juan Pérez", '464-123-1234', 'pg@gmail.com', 'salamanca')
# c2 = Contacto(2, "Ponchito Sierra", '477-123-1234', 'ponchito33@gmail.com', 'leon')

# t1 = Cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase se sistemas de la informacion')



# contactos.append(c1)
# contactos.append(c2)



# cita = Cita(1, 1, 'Universidad de Gto', '02/07/20', '12:00', 'Clase')
# # print(cita.id_cita)
# # print(cita.id_contacto)
# # print(cita.lugar)
# # print(cita.fecha)
# # print(cita.hora)
# # print(cita.asunto)

# # buscar = input("ingrese nombre de contacto\n")

# # for c in contactos:
# #     if c.nombre.lower() == buscar.lower():
# #         print(c1.id_contacto)
# #         print(c1.nombre)
# #         print(c1.tel)
# #         print(c1.correo)
# #         print(c1.dir)
# #         break
# # else:
# #     print("contacto no encontrado")

# m = model()
# m.agregar_contacto(1, "Juan Pérez", '464-123-1234', 'pg@gmail.com', 'salamanca')
# m.agregar_contacto(2, "Juanito Romero", '464-123-1234', 'pg@gmail.com', 'salamanca')
# m.agregar_contacto(3, "Ponchito Sierra", '477-123-1234', 'ponchito33@gmail.com', 'leon')
# m.agregar_contacto(4, "Paco Martínez", '477-123-1234', 'ponchito33@gmail.com', 'leon')
# m.agregar_contacto(5, "Brenda Horta", '477-123-1234', 'ponchito33@gmail.com', 'leon')

# m.agregar_cita(1, 1, 'escuela', '03/05/20', '13:00', 'Reunión escuela')
# m.agregar_cita(2, 2, 'Universidad', '03/05/20', '15:00', 'Reunión universidad')
# m.agregar_cita(3, 2, 'Tokio', '13/01/20', '09:00', 'Comida')
# m.agregar_cita(4, 3, 'Londres', '23/08/21', '10:00', 'Cena')


# # m.actualizar_contacto(2, 'Sara Juarez', '1234-12312', 'nuevocorreo@gmail.com', 'París, France')

# # print("Buscar contacto por letras\n")

# # m.buscar_contacto_letra('P')
# # m.borrar_contacto(2)
# citas = m.buscar_cita_fecha('03/05/20')
# citas = m.buscar_cita_fecha_comprension('03/05/20')

# # for x in citas:
# #     print(x.asunto, x.hora, x.lugar)

# v = View()
# s = m.leer_todos_contactos()
# v.mostrar_contactos(s)
# c = m.leer_contacto(1)
# v.mostrar_contacto(c)
# f, c = m.borrar_contacto(1)
# if f:
#     v.borrar_contacto(c)
# else:
#     v.contacto_no_existe(1)

# cita = m.leer_cita(2)
# v.mostrar_cita(cita)
# f ,c = m.borrar_cita(2)
# if f:
#     v.borrar_cita(c)
# else:
#     v.cita_no_existe(2)

cont = Controller()
cont.start()

cont.menu()