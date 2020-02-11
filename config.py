# encoding:utf8

# dialect+driver://username:password@host:port/database

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'password'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'test'

# Use a Python3 syntax to concatenate various parameters of the connection data

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST
                                             , PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = True
