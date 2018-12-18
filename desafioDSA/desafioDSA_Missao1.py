# programa python para aulas DSA
# Desafio DSA  - Missao 1
from typing import List, Any


class palavra:


    # metodo que pica uma palavra em letras
    def __init__(self,entrada):
        self.entrada = entrada
        self.k2 = []

    def moepalavra(self,entrada):
        k = entrada
        d = len(k)
        cont = 0
        cont2 = 0
        e = 0
        for i in range(0, (d - 1)):
            e = e + 1
            for j in range(e, (d)):
                if k[i] == k[j]:
                    cont += 1
                    ltr = k[i]
                    if ltr not in self.k2:
                        self.k2.append(ltr)

            else:
                cont2 += 1

        return cont, self.k2




def main():
    plv = input("Digite uma unica string -> ")
    cll = palavra(plv)

    # Aqui se cria o objeto

    cll.moepalavra(plv)
    resp = cll.k2
    kl = len(resp)
    print("A palavra ", plv, " tem %d letras iguais" %(kl))



# Executa  o programa


if __name__ == "__main__":
    main()
