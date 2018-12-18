# **** JLCF ****
# Missao 4  DSA  Algoritmo de Classificação


# Importação de bibliotecas

from tkinter import *

# Criação das classes
class ordena():
    # inicializacao da classe
    def __init__(self, lstor):
        self.lstor = lstor

    def classfica(self):

        self.lordenada = []
        original = self.lstor

        for i in range(0,(len(original))):
            nm = min(original)
            self.lordenada.append(nm)
            original.remove(nm)


        return self.lordenada


# Função MAIN
def main():
    janela = Tk()

    janela.title("Classificação de uma lista ") # personaliza o titulo da janela


    # Definição do Tamanho da janela
    janela.geometry("500x300+200+200")
    janela["bg"] = "white"   # Define cor da janela

    #Descrição do programa para o usuário
    lb1= Label(janela, text = "Este programa ordena o sorteio dos 06 numeros da MengaSena", bg="pink")
    lb1.place(x=30, y=10)

    lb2= Label(janela, text = "Abaixo digitar os valores na ordem de sorteio", bg = "gray")
    lb2.place(x=30, y=30)
    lb3= Label(janela, text = "Digitar os 06 numeros separados por Virgulas", bg = "gray")
    lb3.place(x=30, y= 48)
    lb4= Label(janela, text = "Numeros digitados")
    lb4.place(x=30, y= 85)
    # Texto de apresentaçao do resultado
    lb5= Label(janela, text = "Os numeors ordenados do menor para o maior são: ", bg = "green")
    lb5.place(x=30, y=100)
    lb6= Label(janela, text = "Resultado", )
    lb6.place(x=30, y=130)


    def bt_click():
        g =(ed1.get())

        # Aqui vamos transformar a string em numeros
        lorig = []
        g2 =  g.split(",")
        for str in g2:
            z = int(str)
            lorig.append(z)

        k = lorig
        lb4["text"] = k
        # Passa o valor para o objeto
        cll = ordena(lorig)
        cll.classfica()


        lb6["text"] = cll.lordenada


    # Entrada de dados pelo usuario
    ed1 = Entry(janela)
    ed1.place(x=30, y=65)

    # Botao de entrada de dados
    bt1 = Button(janela, width=6, text="OK", command = bt_click)
    bt1.place(x=200, y=65)
    # passa a lista entrada para ordenaçao



    janela.mainloop()


# Chamada da Função MAIN
if __name__ == '__main__':
    main()