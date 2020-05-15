#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from mysql_manager import Gera_query
from database_manager import Database
from controller import Controller

class Backend():
    def __init__(self):
        self.database = Database()
        self.gera_query = Gera_query()
        self.controller = Controller()


    def nova_limpeza(self, data):
        try:
            license_plate = data['LicensePlate']
            date = data['Date']
            birth_type = data['BirthType']
            km = data['Km']
            clean_type = data['CleanType']
            dispersers = list(data['CleanType']['LocalsDisperser'])

            car_id = self.database.return_car_id(license_plate)
            columns = self.database.return_columns('limpezas')

            values = [
                car_id,
                date,
                km,
                birth_type,
                clean_type,
                dispersers
            ]

            query = self.gera_query.inserir_na_tabela('limpezas', list(columns.keys()), values)
            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }
    
        except Exception as e:
            self.r = {
                'error' : str(e),
                'status': 400
            }

        return self.r


    def nova_manutencao(self, data):
        try:
            license_plate = data['LicensePlate']
            type = data['Type']
            date = data['Date']
            date_future = ['NextTime']

            car_id = self.database.return_car_id(license_plate)
            columns = self.database.return_columns('limpezas_geral')
            values = car_id
            values.append([x for x in list(data.values())[1:]])

            query = self.gera_query.inserir_na_tabela('limpezas_geral', list(columns.keys()), values)
            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                'error' : str(e),
                'status': 400
            }

        return self.r


    def recusa_notificacao(self, data):
        try:
            license_plate = data['LicensePlate']
            date = data['Date']
            km = data['Km']
        
            columns = self.database.return_columns('notificacoes_recusas')
            car_id = self.database.return_car_id(license_plate)
            values = car_id
            values.append([x for x in list(data.values())[1:]])
            query = self.gera_query.inserir_na_tabela('notificacoes_recusas', columns, [car_id, date, km])

            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                'error' : str(e),
                'status': 400
            }

        return self.r


    def nova_avaliacao(self, data):
        try:
            license_plate = data['LicensePlate']
            rating = data['Rating']
            comment = data['Comment']

            car_id = self.database.return_car_id(license_plate)
            columns = self.database.return_columns('carros_satisfactions')

            query = self.gera_query.inserir_na_tabela('carros_satisfactions', columns, [car_id, rating, comment])
            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }

        except Exception as e:
            self.r = {
                'error' : str(e),
                'status': 400
            }

        return self.r


    def agendar_limpeza(self, carro, date, immediataly = False):
        print('Não implementado')      


    def infos_vehicle(self, data):
        try:
            license_plate = data['LicensePlate']

            car_id = self.database.return_car_id(license_plate)

            query = self.gera_query.buscar_dados_da_tabela('limpezas', True, coluna_verificacao = 'carro', valor_where=car_id)
            last_cleans = self.database.commit_with_return(query)

            self.r = {
                'LastCleans' : last_cleans
            }


    def limpezas_veiculo(self, carro, limpeza):
        try:
            license_plate = data['LicensePlate']
            limpeza_id = data['LimpezaId']

        query = self.gera_query.buscar_dados_da_tabela('limpeza', where= True, coluna_verificacao=['carro'], valor_where=carro)

        limpeza = self.database.commit_with_return(query)

        return limpeza

    
    def info_limpeza(self, data):
        try:
            limpeza_id = data['Limpeza']
    
        except Exception as e:
            self.r = {
                'error' : e
            }

    
    def buscar_manutencao(self, carro, manutencao):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)[0][0]

        query = self.gera_query.buscar_dados_da_tabela('limpezas_geral', where=True, coluna_verificacao=['carro'], valor_where=carro)
        manutencao = self.database.commit_with_return(query)

        return manutencao

    def media_descuido(self, carro):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)[0][0]

        query = 'select id from nascimentos where nascimento = "Notificação"'
        id_notificacao = self.database.commit_with_return(query)

        query = self.gera_query.query_media_descuido(carro, id_notificacao)
        recusas, aceites = self.database.commit_with_return(query)
        total = recusas + aceites

        media = (recusas / total) * 100

        return media


    def relatorio_limpeza_por_motivo(self, carro):
        print('Não implementado')


    def media_avaliacao_carro(self, carro):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)[0][0]

        query = self.gera_query.buscar_rating(carro)
        rating = self.database.commit_with_return(query)

        return rating


    def ultima_limpeza_realizada(self, carro):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)[0][0]

        query = self.gera_query.buscar_ultima_limpeza_realizada(carro)
        ultima_limpeza_realizada = self.database.commit_with_return(query)

        return ultima_limpeza_realizada



        