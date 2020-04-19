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


    def recusa_notificacao(self, carro, data, km):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)

        query = self.gera_query.listar_colunas('notificacoes_recusas')
        colunas = self.database.commit_with_return(query)
        colunas = colunas[1:]

        query = self.gera_query.inserir_na_tabela('notificacoes_recusas', colunas, [carro, data, km])
        self.database.commit_without_return(query)

        return 'OK'


    def nova_limpeza(self, carro, data, nascimento, km, tipo = 'Full', objetos_limpos = None):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)

        query = self.gera_query.listar_colunas('limpezas')
        colunas = self.database.commit_with_return(query)
        colunas = colunas[1:]

        limpeza = {
            'carro' : carro,
            'date' : data,
            'nascimento' : nascimento,
            'km' : km, #Km's rodados desde a última limpeza
            'tipo' : tipo,
            'objetos_limpos' : objetos_limpos
        }
        print(limpeza)
        query = self.gera_query.nova_limpeza(limpeza, colunas)
        self.database.commit_without_return(query)
    
        return 'OK'


    def nova_manutencao(self, carro, tipo, date, date_future):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)

        query = self.gera_query.listar_colunas('limpezas_geral')
        colunas = self.database.commit_with_return(query)
        colunas = colunas[1:]

        manutencao = {
            'carro' : carro,
            'tipo' : tipo,
            'date' : date,
            'date_future' : date_future
        }
        query = self.gera_query.nova_manutencao(manutencao, colunas)
        self.database.commit_without_return(query)

        return 'OK'

    def nova_avaliacao(self, carro, nota, comentario):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)

        query = self.gera_query.listar_colunas('carros_satisfactions')
        colunas = self.database.commit_with_return(query)
        colunas = colunas[1:]

        query = self.gera_query.inserir_na_tabela('carros_satisfactions', colunas, [carro, nota, comentario])
        self.database.commit_without_return(query)

        return 'OK'


    def agendar_limpeza(self, carro, date, immediataly = False):
        print('Não implementado')      


    def buscar_limpeza(self, carro, limpeza):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)

        query = self.gera_query.buscar_dados_da_tabela('limpeza', where= True, coluna_verificacao=['carro'], valor_where=carro)

        limpeza = self.database.commit_with_return(query)

        return limpeza

    
    def buscar_manutencao(self, carro, manutencao):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)

        query = self.gera_query.buscar_dados_da_tabela('limpezas_geral', where=True, coluna_verificacao=['carro'], valor_where=carro)
        manutencao = self.database.commit_with_return(query)

        return manutencao

    def media_descuido(self, carro):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)

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
        carro = self.database.commit_with_return(query)

        query = self.gera_query.buscar_rating(carro)
        rating = self.database.commit_with_return(query)

        return rating


    def ultima_limpeza_realizada(self, carro):
        query = self.gera_query.buscar_id_carro(carro)
        carro = self.database.commit_with_return(query)

        query = self.gera_query.buscar_ultima_limpeza_realizada(carro)
        ultima_limpeza_realizada = self.database.commit_with_return(query)

        return ultima_limpeza_realizada



        