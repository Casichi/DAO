from accesoDatos.logger_base import log

class Persona:

    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return f'''
        Persona: 
        id {self._id_persona},Nombre {self.nombre}
        Apellido {self.apellido}, Email {self.email}
        '''

if __name__ == '__main__':
    p = Persona(2, 'alex', 'chilel', 'a@mail.com')
    log.debug(p)
    persona1 = Persona(nombre='Isa', apellido='vlqz', email='isa@mail.com')
    log.debug(persona1)
    #print(p)
