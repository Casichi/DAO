from Persona import Persona
from PersonaDAO import PersonaDAO
from logger_base import log


opcion = None

while opcion != 5:
    try:
        print('''
        Opciones:
        1.-Listar Personas
        2.-Agregar Personas
        3.-Actualizar Persons
        4.- Eliminar Persona
        5.-Salir
        ''')
        opcion = int(input('Escribe tu opcion (1-4): '))

        if opcion ==1:
            personas = PersonaDAO.seleccionar()
            for persona in personas:
                log.debug(persona)
        elif opcion ==2:
            nombre_var = input('Escribe el nombre de la persona \n')
            apellido_var = input('Ingresa el apellido de la persona')
            email_var = input('Ingresa el email del la persona')
            persona = Persona(nombre= nombre_var, apellido= apellido_var, email=email_var )
            personas_insertadas = PersonaDAO.insertar(persona)
            log.debug(f'Personas insertadas {personas_insertadas}')
        elif opcion == 3:
            id_persona_var = int(input('ingresa el id de la persona'))
            nombre_var = input('Escribe el nombre de la persona \n')
            apellido_var = input('Ingresa el apellido de la persona')
            email_var = input('Ingresa el email del la persona')
            persona = Persona(id_persona_var, nombre_var, apellido_var, email_var)
            PersonaDAO.actualizar(persona)
        elif opcion ==4:
            id_persona_var = int(input('ingresa el id de la persona a eliminar'))
            persona = Persona(id_persona_var)
            PersonaDAO.eliminar(persona)
    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
    else:
        print('Salimos del programa')