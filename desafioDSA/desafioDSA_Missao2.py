# Desafio  DSA missao 2
# *** JLCF ***
# Numeros Primos

class nprim:

    # Escolher o tamanho da amostra
    def __init__(self, tmnh):
        self.tmnh = tmnh
        self.amo = [2]
        self.prm = []

# Aqui aplica-se o crivo de Eratóstenes para separar os pares menos o 2
    def calcula(self,tmnh):
        r = self.tmnh
        for i in range(2,r,2):
            k = 1 + i
            self.amo.append(k)
        return self.amo

# Aqui aplica-se o Crivo de Eratótenes para retirar os multiplos de 3, 5 e 7
    def sepaprimo(self,amo):
        self.prm = self.amo
        for np in self.prm:
            if np > 3 and np % 3 == 0:
                self.prm.remove(np)
        for np in self.prm:
            if np > 5 and np % 5 == 0:
                self.prm.remove(np)
        for np in self.prm:
            if np > 7 and np % 7 == 0:
                self.prm.remove(np)
        for np in self.prn:
            if np > 11 and np % 11 == 0:
                self.prm.remove(np)
        return self.prm






def main():
    print("PROGRAMA DE AMOSTRAGEM DE NUMEROS PRIMOS ")
    print("\n AMOSTRA MÁXIMA VAI ATE 160")

    print("\nPor favor escolha o tamnho da amostra")
    amoa = int (input("Digitar tamnho => "))

    cll = nprim(amoa)

    cll.calcula(amoa)
    t = cll.amo
    cll.sepaprimo(t)
    t2 = cll.prm
    qtd = len(t2)


    print("\nResposta \n")
   # print("\n ",t)
    print("\nMais filtro - Resultado ")
    print("\n",t2)
    print("\nExistem %d numeros primos nesta amostra" %(qtd))



if __name__ == "__main__":
    main()