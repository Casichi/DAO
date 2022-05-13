from accesoDatos.PersonaDAO import PersonaDAO
from conexion import Conexion
from Persona import Persona
from accesoDatos.logger_base import log

class Person:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtener_cursor() as cursor:3
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada {persona}')
                return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    persona1 = Persona(1,'Pedro', 'Najera', 'pnajera@mail.com')
    #personas_insertadas = Person.insertar(persona1)
    personas_actualizar = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas insertadas: {personas_actualizar}')

    # Seleccionar objetos
    #personas = Person.seleccionar()
    #for persona in personas:
        #log.debug(persona)