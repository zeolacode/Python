from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
    
    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
        "janeiro", "fevereiro", "março",
        "abril", "maio", "junho",
        "julho", "agosto", "setembro",
        "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1 
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro



"""
%A retorna os dias da semana por extenso, como Sunday;

%d exibe os dias do mês com números de 01 a 31;

%m retorna meses em números de 01 a 12;

%y mostra o ano com apenas dois dígitos;

%Y apresenta o ano em formato de quatro números;

%H retorna o horário no formato decimal, como 00, 001 e etc;

%M exibe os minutos de forma decimal;

%S apresenta os segundos em decimal.
"""