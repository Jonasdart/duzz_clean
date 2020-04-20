import MySQLdb as mdb
import configparser
from mysql_manager import Gera_query

class Database():
    def __init__(self):
        self.gerador_de_query = Gera_query()
        self.connected = False


    def connect(self):
        if not self.connected:
            credencials = self.authenticate()
            address = credencials.get('AddressBank')
            name = credencials.get('NameBank')
            user = credencials.get('UserBank')
            password = credencials.get('PasswordBank')
        
            try:
                self.bank = mdb.connect(address, user, password, name)
            except:
                self.conected = False
                raise
            else:
                self.cursor = self.bank.cursor()
                self.conected = True

        return {
            'Database' : self.bank,
            'Cursor'   : self.cursor
        }
    
    def disconnect(self):
        if self.connected:
            try:
                self.bank.close()
            except:
                raise Exception('Database connection not initialized')
        
        self.conected = False
        return True

    def authenticate(self):
        """
        Utiliza as informações presentes no glpi.cfg para\n
        retorná-las em forma de lista como credenciais
        Retorno -> Lista:\n
        [0] IP banco, [1] Usuario Banco\n
        [2] Senha Usuario, [3] Nome Banco
        """
        config = configparser.ConfigParser()
        config.read('conf.cfg')

        address_bank = config.get('config_bank', 'address_bank')
        name_bank = config.get('config_bank', 'name_bank')
        user_bank = config.get('config_bank', 'user_bank')
        password_bank = config.get('config_bank', 'password_bank')
        if password_bank == "''":
            password_bank = ''

        return {
            'AddressBank' : address_bank,
            'NameBank' : name_bank,
            'UserBank' : user_bank,
            'PasswordBank' : password_bank
        }


    def commit_without_return(self, query):
        print(query)
        self.connect()
        try:
            print('exe')
            self.cursor.execute(query)
        except:
            raise
        else:
            self.bank.commit()
            self.disconnect()
            return True

    def commit_with_return(self, query):
        results = None
        self.connect()
        try:
            self.cursor.execute(query)
        except:
            raise
        else:
            results = self.cursor.fetchall()
            self.disconnect()

        return results