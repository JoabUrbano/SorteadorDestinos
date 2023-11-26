from random import randrange
import time

class SorteioRaridade():
    def __init__(self):
        self.comum = 40
        self.incomum = 30
        self.raro = 15
        self.epico = 10
        self.lendario = 5
        self.listComuns = []
        self.listIncomuns = []
        self.listRaros = []
        self.listEpicos = []
        self.listLendarios = []

        self.tempoLimite = 5
        self.tempoInicial = time.time()
    
    def carregarDestinos(self):

        nome_arquivo = 'destinos.txt'
        try:
            arquivo = open(nome_arquivo, 'r', encoding=('raw_unicode_escape'))
            destino = ''
            list = []
            for linha in arquivo.readlines():
                destino = linha.strip()
                if(destino == "incomum"):
                    self.listComuns = list
                    list = []
                
                elif(destino == "raro"):
                    self.listIncomuns = list
                    list = []
                
                elif(destino == "epico"):
                    self.listRaros = list
                    list = []
                
                elif(destino == "lendario"):
                    self.listEpicos = list
                    list = []
                
                elif(destino == "end"):
                    self.listLendarios = list
                
                else:
                    list.append(destino)

        except FileNotFoundError:
            print("Arquivo inexistente.")

        except Exception as erro:            
            msg = 'ERRO: ' + str(erro)
            print(msg)

        finally:
            try:
                arquivo.close()

            except Exception as erro:
                print(erro)

    def sortearDestino(self, list):

        destinoSorteado = randrange(0, len(list))
        print("Sorteado: " + list[destinoSorteado])
        list.pop(destinoSorteado)

    def sortear(self, numItens):

        self.carregarDestinos()

        for _ in range(numItens):
            destino = randrange(1, 101)
            
            if destino > 0 and destino <= self.comum and len(self.listComuns) > 0:
                print(" " * 6 + "*** Destino Comum ***")
                self.sortearDestino(self.listComuns)
                self.comum -= 4
                self.incomum += 3
                self.raro += 1
            
            elif destino > self.comum and destino <= (self.comum + self.incomum) and len(self.listIncomuns) > 0:
                print(" " * 6 + "*** Destino Incomum ***")
                self.sortearDestino(self.listIncomuns)
                self.incomum -= 3
                self.raro += 2
                self.epico += 1
            
            elif destino > (self.comum + self.incomum) and destino <= (self.comum + self.incomum + self.raro) and len(self.listRaros) > 0:
                print(" " * 6 + "*** Destino Raro ***")
                self.sortearDestino(self.listRaros)
                self.raro -= 2
                self.epico += 1
                self.lendario += 1
            
            elif destino > (self.comum + self.incomum + self.raro) and destino <= (self.comum + self.incomum + self.raro + self.epico) and len(self.listEpicos) > 0:
                print(" " * 6 + "*** Destino Epico ***")
                self.sortearDestino(self.listEpicos)
                self.epico -= 2
                self.lendario += 2
            
            elif len(self.listLendarios) > 0:
                print(" " * 6 + "*** Destino Lendario ***")
                self.sortearDestino(self.listLendarios)
                self.lendario -= 5
                self.comum += 5
            
            else:
                numItens += 1
            
            if time.time() - self.tempoInicial > self.tempoLimite:
                print("Tempo limite atingido. Encerrando o loop.")
                break
