"""
Módulo principal del sistema de gestión de tickets (interfaz CLI).
"""
from CrudSistemaTickets.models.usuario import Usuario 
from CrudSistemaTickets.models.tecnico import Tecnico 
from CrudSistemaTickets.models.ticket import Ticket 
from CrudSistemaTickets.models.ticket_historial import TicketHistorial 
from CrudSistemaTickets.services.usuario_service import UsuarioService 
from CrudSistemaTickets.services.tecnico_service import TecnicoService 
from CrudSistemaTickets.services.ticket_service import TicketService 
from CrudSistemaTickets.services.ticket_historial_service import TicketHistorialService 

# ===== MENÚS =====

def menu_principal(): 
    print("\n===== SISTEMA DE TICKETS =====")
    print("1. Gestionar Usuarios")
    print("2. Gestionar Técnicos")
    print("3. Gestionar Tickets")
    print("4. Ver Historial de Tickets")
    print("0. Salir")


def menu_usuarios():
    print("\n--- MENÚ USUARIOS ---")
    print("1. Listar Usuarios")
    print("2. Crear Usuario")
    print("3. Buscar Usuario por ID")
    print("4. Actualizar Usuario")
    print("5. Eliminar Usuario")
    print("0. Volver al menú principal")


def menu_tecnicos():
    print("\n--- MENÚ TÉCNICOS ---")
    print("1. Listar Técnicos")
    print("2. Crear Técnico")
    print("3. Buscar Técnico por ID")
    print("4. Actualizar Técnico")
    print("5. Eliminar Técnico")
    print("0. Volver al menú principal")


def menu_tickets():
    print("\n--- MENÚ TICKETS ---")
    print("1. Listar Tickets")
    print("2. Crear Ticket")
    print("3. Buscar Ticket por ID")
    print("4. Actualizar Ticket (y guardar historial)")
    print("5. Eliminar Ticket")
    print("0. Volver al menú principal")


def menu_historial():
    print("\n--- MENÚ HISTORIAL TICKETS ---")
    print("1. Listar TODO el historial")
    print("2. Ver historial de un ticket por ID")
    print("0. Volver al menú principal")


# ===== LÓGICA PRINCIPAL =====

def main():
    """Función principal del sistema."""
    usuario_service = UsuarioService()
    tecnico_service = TecnicoService()
    ticket_service = TicketService()
    historial_service = TicketHistorialService()

    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")

        # ===== USUARIOS =====
        if opcion == "1":
            while True:
                menu_usuarios()
                op_u = input("Seleccione una opción: ")

                if op_u == "1":
                    print("\nListado de usuarios:")
                    usuarios = usuario_service.listar()
                    if usuarios:
                        for u in usuarios:
                            print(
                                f"ID: {u['id_usuario']} | "
                                f"{u['nombre']} {u['apellido']} | "
                                f"Correo: {u['correo']} | "
                                f"Rol: {u['rol']} | "
                                f"Teléfono: {u['telefono']}"
                            )
                    else:
                        print("No hay usuarios registrados.")

                elif op_u == "2":
                    print("\nCREAR USUARIO")
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    correo = input("Correo: ")
                    password_hash = input("Password (hash o simple por ahora): ")
                    rol = input("Rol (admin/usuario) [usuario]: ") or "usuario"
                    telefono = input("Teléfono (opcional): ") or None

                    usuario = Usuario(
                        None, nombre, apellido, correo, password_hash, rol, telefono
                    )
                    if usuario_service.crear(usuario):
                        print("Usuario creado correctamente.")
                    else:
                        print("Error al crear usuario.")

                elif op_u == "3":
                    print("\nBUSCAR USUARIO POR ID")
                    id_usuario = int(input("Ingrese ID: "))
                    usuario = usuario_service.buscar_por_id(id_usuario)
                    if usuario:
                        print(
                            f"ID: {usuario['id_usuario']} | "
                            f"{usuario['nombre']} {usuario['apellido']} | "
                            f"Correo: {usuario['correo']} | "
                            f"Rol: {usuario['rol']} | "
                            f"Teléfono: {usuario['telefono']}"
                        )
                    else:
                        print("Usuario no encontrado.")

                elif op_u == "4":
                    print("\nACTUALIZAR USUARIO")
                    id_usuario = int(input("Ingrese ID del usuario a actualizar: "))
                    existe = usuario_service.buscar_por_id(id_usuario)
                    if not existe:
                        print("Usuario no encontrado.")
                        continue

                    nombre = input(f"Nuevo nombre ({existe['nombre']}): ") or existe["nombre"]
                    apellido = input(f"Nuevo apellido ({existe['apellido']}): ") or existe["apellido"]
                    correo = input(f"Nuevo correo ({existe['correo']}): ") or existe["correo"]
                    password_hash = input("Nuevo password (dejar vacío para mantener): ") or existe["password_hash"]
                    rol = input(f"Nuevo rol ({existe['rol']}): ") or existe["rol"]
                    telefono = input(f"Nuevo teléfono ({existe['telefono']}): ") or existe["telefono"]

                    usuario = Usuario(
                        id_usuario, nombre, apellido, correo, password_hash, rol, telefono
                    )
                    if usuario_service.actualizar(usuario):
                        print("Usuario actualizado correctamente.")
                    else:
                        print("Error al actualizar usuario.")

                elif op_u == "5":
                    print("\nELIMINAR USUARIO")
                    id_usuario = int(input("Ingrese ID: "))
                    ok = usuario_service.eliminar(id_usuario)
                    if ok:
                        print("Usuario eliminado correctamente.")
                    else:
                        print("Usuario no existe o error al eliminar.")
                elif op_u == "0":
                    break
                else:
                    print("Opción no válida.")

        # ===== TÉCNICOS =====
        elif opcion == "2":
            while True:
                menu_tecnicos()
                op_t = input("Seleccione una opción: ")

                if op_t == "1":
                    print("\nListado de técnicos:")
                    tecnicos = tecnico_service.listar()
                    if tecnicos:
                        for t in tecnicos:
                            print(
                                f"ID: {t['id_tecnico']} | "
                                f"Nombre: {t['nombre']} | "
                                f"Especialidad: {t['especialidad']} | "
                                f"Fecha ingreso: {t['fecha_ingreso']}"
                            )
                    else:
                        print("No hay técnicos registrados.")

                elif op_t == "2":
                    print("\nCREAR TÉCNICO")
                    nombre = input("Nombre: ")
                    especialidad = input("Especialidad: ")
                    tecnico = Tecnico(None, nombre, especialidad)
                    if tecnico_service.crear(tecnico):
                        print("Técnico creado correctamente.")
                    else:
                        print("Error al crear técnico.")

                elif op_t == "3":
                    print("\nBUSCAR TÉCNICO POR ID")
                    id_tecnico = int(input("Ingrese ID: "))
                    tecnico = tecnico_service.buscar_por_id(id_tecnico)
                    if tecnico:
                        print(
                            f"ID: {tecnico['id_tecnico']} | "
                            f"Nombre: {tecnico['nombre']} | "
                            f"Especialidad: {tecnico['especialidad']} | "
                            f"Fecha ingreso: {tecnico['fecha_ingreso']}"
                        )
                    else:
                        print("Técnico no encontrado.")

                elif op_t == "4":
                    print("\nACTUALIZAR TÉCNICO")
                    id_tecnico = int(input("Ingrese ID del técnico a actualizar: "))
                    existe = tecnico_service.buscar_por_id(id_tecnico)
                    if not existe:
                        print("Técnico no encontrado.")
                        continue

                    nombre = input(f"Nuevo nombre ({existe['nombre']}): ") or existe["nombre"]
                    especialidad = input(
                        f"Nueva especialidad ({existe['especialidad']}): "
                    ) or existe["especialidad"]

                    tecnico = Tecnico(id_tecnico, nombre, especialidad)
                    if tecnico_service.actualizar(tecnico):
                        print("Técnico actualizado correctamente.")
                    else:
                        print("Error al actualizar técnico.")

                elif op_t == "5":
                    print("\nELIMINAR TÉCNICO")
                    id_tecnico = int(input("Ingrese ID: "))
                    ok = tecnico_service.eliminar(id_tecnico)
                    if ok:
                        print("Técnico eliminado correctamente.")
                    else:
                        print("Técnico no existe o error al eliminar.")
                elif op_t == "0":
                    break
                else:
                    print("Opción no válida.")

        # ===== TICKETS =====
        elif opcion == "3":
            while True:
                menu_tickets()
                op_k = input("Seleccione una opción: ")

                if op_k == "1":
                    print("\nListado de tickets:")
                    tickets = ticket_service.listar()
                    if tickets:
                        for tk in tickets:
                            print(
                                f"ID: {tk['id_ticket']} | "
                                f"Titulo: {tk['titulo']} | "
                                f"Estado: {tk['estado']} | "
                                f"ID Creador: {tk['id_creador']} | "
                                f"ID Técnico: {tk['id_tecnico']} | "
                                f"Fecha: {tk['fecha_creacion']}"
                            )
                    else:
                        print("No hay tickets registrados.")

                elif op_k == "2":
                    print("\nCREAR TICKET")
                    id_creador = int(input("ID Usuario creador: "))
                    id_tecnico_input = input("ID Técnico (opcional, Enter para NULL): ")
                    id_tecnico = int(id_tecnico_input) if id_tecnico_input else None
                    titulo = input("Título: ")
                    descripcion = input("Descripción: ")
                    estado = input("Estado (pendiente/en_proceso/resuelto) [pendiente]: ") or "pendiente"

                    ticket = Ticket(
                        None, id_creador, id_tecnico, titulo, descripcion, estado
                    )
                    if ticket_service.crear(ticket):
                        print("Ticket creado correctamente.")
                    else:
                        print("Error al crear ticket.")

                elif op_k == "3":
                    print("\nBUSCAR TICKET POR ID")
                    id_ticket = int(input("Ingrese ID: "))
                    tk = ticket_service.buscar_por_id(id_ticket)
                    if tk:
                        print(
                            f"ID: {tk['id_ticket']} | "
                            f"Título: {tk['titulo']} | "
                            f"Descripción: {tk['descripcion']} | "
                            f"Estado: {tk['estado']} | "
                            f"ID Creador: {tk['id_creador']} | "
                            f"ID Técnico: {tk['id_tecnico']} | "
                            f"Fecha: {tk['fecha_creacion']}"
                        )
                    else:
                        print("Ticket no encontrado.")

                elif op_k == "4":
                    print("\nACTUALIZAR TICKET")
                    id_ticket = int(input("Ingrese ID del ticket a actualizar: "))
                    existe = ticket_service.buscar_por_id(id_ticket)
                    if not existe:
                        print("Ticket no encontrado.")
                        continue

                    estado_anterior = existe["estado"]

                    id_creador = int(
                        input(f"Nuevo ID creador ({existe['id_creador']}): ")
                        or existe["id_creador"]
                    )
                    id_tecnico_input = input(
                        f"Nuevo ID técnico ({existe['id_tecnico']} - Enter para mantener): "
                    )
                    if id_tecnico_input == "":
                        id_tecnico = existe["id_tecnico"]
                    else:
                        id_tecnico = int(id_tecnico_input)

                    titulo = input(f"Nuevo título ({existe['titulo']}): ") or existe["titulo"]
                    descripcion = (
                        input(f"Nueva descripción ({existe['descripcion']}): ")
                        or existe["descripcion"]
                    )
                    estado = input(
                        f"Nuevo estado ({existe['estado']}): "
                    ) or existe["estado"]

                    ticket = Ticket(
                        id_ticket, id_creador, id_tecnico, titulo, descripcion, estado
                    )
                    if ticket_service.actualizar(ticket):
                        print("Ticket actualizado correctamente.")

                        hist = TicketHistorial(
                            None, id_ticket, estado_anterior, estado
                        )
                        historial_service.crear(hist)
                        print("Historial de cambio registrado.")
                    else:
                        print("Error al actualizar ticket.")

                elif op_k == "5":
                    print("\nELIMINAR TICKET")
                    id_ticket = int(input("Ingrese ID: "))
                    ok = ticket_service.eliminar(id_ticket)
                    if ok:
                        print("Ticket eliminado correctamente.")
                    else:
                        print("Ticket no existe o error al eliminar.")
                elif op_k == "0":
                    break
                else:
                    print("Opción no válida.")
                
        # ===== HISTORIAL =====
        elif opcion == "4":
            while True:
                menu_historial()
                op_h = input("Seleccione una opción: ")

                if op_h == "1":
                    print("\nHistorial completo de tickets:")
                    registros = historial_service.listar()
                    if registros:
                        for h in registros:
                            print(
                                f"ID Historial: {h['id_historial']} | "
                                f"Ticket: {h['id_ticket']} | "
                                f"Estado anterior: {h['estado_anterior']} | "
                                f"Estado nuevo: {h['estado_nuevo']} | "
                                f"Fecha: {h['fecha_cambio']}"
                            )
                    else:
                        print("No hay registros en historial.")

                elif op_h == "2":
                    print("\nHISTORIAL POR TICKET")
                    id_ticket = int(input("Ingrese ID de ticket: "))
                    registros = historial_service.listar_por_ticket(id_ticket)
                    if registros:
                        for h in registros:
                            print(
                                f"ID Historial: {h['id_historial']} | "
                                f"Ticket: {h['id_ticket']} | "
                                f"Estado anterior: {h['estado_anterior']} | "
                                f"Estado nuevo: {h['estado_nuevo']} | "
                                f"Fecha: {h['fecha_cambio']}"
                            )
                    else:
                        print("No hay historial para ese ticket.")
                elif op_h == "0":
                    break
                else:
                    print("Opción no válida.")

        # ===== SALIR =====
        elif opcion == "0":
            print("Saliendo del sistema de tickets...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
