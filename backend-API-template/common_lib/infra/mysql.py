import logging
import threading
from contextlib import contextmanager

import sqlparse
from mysql.connector.connection import MySQLConnection
from mysql.connector.pooling import MySQLConnectionPool

from flask import Flask

logger = logging.getLogger(__name__)


class DB(object):

    mysql_host = '127.0.0.1'
    mysql_user = 'root'
    mysql_password = '1234'
    mysql_db = 'sbs_library'
    mysql_pool_size = 10

    _connection_pool = None
    __singleton_lock = threading.Lock()

    def __init__(self):

        if DB._connection_pool:
            return

        with DB.__singleton_lock:
            if not DB._connection_pool:
                DB._connection_pool = MySQLConnectionPool(host=DB.mysql_host,
                                                          user=DB.mysql_user,
                                                          password=DB.mysql_password,
                                                          db=DB.mysql_db,
                                                          charset='utf8',
                                                          pool_name="dbtool_pool",
                                                          pool_size=DB.mysql_pool_size,
                                                          buffered=True)

    @classmethod
    def init_app(cls, app: Flask):
        cls.mysql_host = app.config['MYSQL_HOST']
        cls.mysql_user = app.config['MYSQL_USER']
        cls.mysql_password = app.config['MYSQL_PASSWORD']
        cls.mysql_db = app.config['MYSQL_DB']
        cls.mysql_pool_size = app.config['MYSQL_POOL_SIZE']

    @classmethod
    @contextmanager
    def cursor(cls, buffered=None, raw=None, prepared=None, cursor_class=None,
               dictionary=None, named_tuple=None, pool=True):

        conn = cls._connection_pool.get_connection() if pool else MySQLConnection(host=cls.mysql_host,
                                                                                  user=cls.mysql_user,
                                                                                  password=cls.mysql_password,
                                                                                  db=cls.mysql_db,
                                                                                  charset='utf8',
                                                                                  buffered=True)

        cursor = conn.cursor(buffered=buffered, raw=raw,
                             prepared=prepared, cursor_class=cursor_class,
                             dictionary=dictionary, named_tuple=named_tuple)
        try:
            yield cursor
        except Exception as e:
            conn.rollback()
            if cursor.statement:
                logger.error(sqlparse.format(cursor.statement, reindent=True))
            logger.error(e)
            raise e
        finally:
            conn.commit()
            cursor.close()
            conn.close()
