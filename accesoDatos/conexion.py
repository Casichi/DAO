from accesoDatos.logger_base import log
from psycopg2 import pool
import sys


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Mlmgow12'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONE = 1
    _MAX_CONE = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONE, cls._MAX_CONE,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creacion de pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'Ocurrio un error al obtener el pool {e }')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool {conexion}')
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        ##putconn regresa la conexion abierta en obtener_pool al pool de conexiones
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos  la conexion al pool: {conexion}')

    @classmethod
    def cerrar_Conexiones(cls):
        cls.obtenerPool().closeall()

9
if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
    conexion2 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion2)
    conexion3 = Conexion.obtener_conexion()
    conexion4 = Conexion.obtener_conexion()
    conexion5 = Conexion.obtener_conexion()
    conexion6 = Conexion.obtener_conexion()
