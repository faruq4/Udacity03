
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or '[faruq-udacity-prj-db-server-01.database.windows.net]'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or '[FaruqUdacityPrjDB01]'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or '[faruq]'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '[Miran@2018]'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or '[Faruqudacitystgact01]'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '[TuU1+WEUvU5w37GLHtDK7nVul6lJ5O68cXiQpfjnphtbywdnGmRNe3XowC96ZECtgFhg3hyQNnnz+AStUuGu+A==
]'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or '[faruqudacitystorageactcontainer]'
