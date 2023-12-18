from random import randrange

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

    
    def carregarDestinos(self):

        nome_arquivo = 'destinos.txt'
        try:
            arquivo = open(nome_arquivo, 'r', encoding='utf-8')
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
            if self.comum + self.incomum + self.raro + self.epico + self.lendario <= 1:
                break
            destino = randrange(1, self.comum + self.incomum + self.raro + self.epico + self.lendario)
            
            if destino <= self.comum and len(self.listComuns) > 0:
                print(" " * 6 + "*** Destino Comum ***")
                self.sortearDestino(self.listComuns)

                if self.comum - 4 > 0:
                    self.comum -= 4
                    if len(self.listIncomuns) > 0 and len(self.listRaros) > 0:
                        self.incomum += 3
                        self.raro += 1
                    
                    elif len(self.listIncomuns) > 0:
                        self.incomum += 4
                    
                    elif len(self.listRaros) > 0:
                        self.raro += 4
                    
                    else:
                        self.comum += 4     
                       
                if len(self.listComuns) <= 0:
                    self.comum = 0
            
            elif destino > self.comum and destino <= (self.comum + self.incomum) and len(self.listIncomuns) > 0:
                print(" " * 6 + "*** Destino Incomum ***")
                self.sortearDestino(self.listIncomuns)

                if self.incomum - 3 > 0:
                    self.incomum -= 3
                    if len(self.listRaros) > 0 and len(self.listEpicos) > 0:
                        self.raro += 2
                        self.epico += 1
                    
                    elif len(self.listRaros) > 0:
                        self.raro += 3
                    
                    elif len(self.listEpicos) > 0:
                        self.epico += 3
                    
                    else:
                        self.incomum += 3    
                       
                if len(self.listIncomuns) <= 0:
                    self.incomum = 0
            
            elif destino > (self.comum + self.incomum) and destino <= (self.comum + self.incomum + self.raro) and len(self.listRaros) > 0:
                print(" " * 6 + "*** Destino Raro ***")
                self.sortearDestino(self.listRaros)

                if self.raro - 2 > 0:
                    self.raro -= 2
                    if len(self.listEpicos) > 0 and len(self.listLendarios) > 0:
                        self.epico += 1
                        self.lendario += 1
                    
                    elif len(self.listEpicos) > 0:
                        self.epico += 2

                    elif len(self.listLendarios) > 0:
                        self.lendario += 2
                    
                    else:
                        self.raro += 3

                if len(self.listRaros) <= 0:
                    self.raro = 0
            
            elif destino > (self.comum + self.incomum + self.raro) and destino <= (self.comum + self.incomum + self.raro + self.epico) and len(self.listEpicos) > 0:
                print(" " * 6 + "*** Destino Epico ***")
                self.sortearDestino(self.listEpicos)

                if self.epico - 2 > 0:
                    self.epico -= 2
                    if len(self.listLendarios) > 0:
                        self.lendario += 2
                    
                    else:
                        self.epico += 2

                if len(self.listEpicos) <= 0:
                    self.epico = 0
            
            elif len(self.listLendarios) > 0:
                print(" " * 6 + "*** Destino Lendario ***")
                self.sortearDestino(self.listLendarios)

                if self.lendario - 5 > 0:
                    self.lendario -= 5
                    if len(self.listComuns) > 0:
                        self.comum += 5
                    
                    else:
                        self.lendario += 5
                
                if len(self.listLendarios) <= 0:
                    self.lendario = 0
            
            else:
                break
