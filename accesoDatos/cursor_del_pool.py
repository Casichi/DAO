from accesoDatos.conexion import Conexion
from logger_base import log


class CursorDelPool:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    #tipodeExcepcion, valor_excepcion, detalle_excepcion
    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('se ejecuta metodo __exit__')
        if exc_type:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback {exc_val}, {exc_type} {exc_tb}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transaccion')
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug(f'dentro del bloque with')
        cursor.execute('DELETE FROM persona WHERE id_persona=18')

        #log.debug(cursor.fetchall())


