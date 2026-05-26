# Objeto:
# Representação de algo do mundo real, com
# características (atributos) e comportamentos (métodos).
# 
# CLASSE:
# Molde para criar objetos
#
# Instância = Objeto criado a partir de uma classe

class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        print (f'{self.modelo} esta acelerando...')

    def frear(self):
        self.velocidade = 0
        print (f'{self.modelo} esta parando...')

    def estado(self):
        if self.velocidade <= 0:
            print (f'{self.modelo} esta parado!')
        else:
            print (f'{self.modelo} esta movimento a uma velocidade de {self.velocidade} km/h!')



c1 = Carro('branco','gol','2000')
c2 = Carro('azul','palio','2018')
c3 = Carro('amarelo','stilo', '2023')

c1.estado()
c1.acelerar()
c1.acelerar()
c1.acelerar()
c1.estado()
c1.frear()
c1.estado()

c2.estado()
c3.estado()