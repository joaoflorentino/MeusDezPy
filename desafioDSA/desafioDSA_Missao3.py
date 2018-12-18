# Desafio DSA missão 3
# **** JLCF ****
# Movimento de robo na tela


# Importação de bibliotecas

from functools import partial
from tkinter import *
import time

# inicia a classe de montagem do pĺano limite do robo
class moveto:
    def __init__(self, coordenadas, direcao):
        self.coordenadas=coordenadas
        self.direcao=direcao


    def planta(self):
        self.janela = Tk()
        # Aqui dimensionamos a área do canvas
        self.c = Canvas(self.janela, width=800, height=600,bd=0, bg="red", highlightthickness=0)
        self.c.pack()


        # Criando o robozinho
        def robobo():
            # Canvas cria o corpo do robo e o texto
            id= self.c.create_rectangle(0,0,15,15, fill = "green", tags="rb")
            id2= self.c.create_text(40,7, text="<- Robo", tags="rb")
            # Aqui simulamos o movimento do Robo
            x = y = 2
            for loops in range(250):
                time.sleep(0.035)
                self.c.move("rb",x,y)
                self.c.update()


        # Comportamento do botao OK
        def vai_agora():
            print("Partiu o Robo - Vá com Deus !!")

            lb["text"] = "INICIA MOVIMENTO"
            robobo()


        # Dimensão da Janela 800x600+50+50
        self.janela.geometry("800x600+50+50")
        self.janela.title("Espaço de movimento do robo")
        self.janela["bg"] = "red"

        # criar botao que dispara o movimento do robo
        bt = Button(self.janela, width = 20, text = "OK", command=vai_agora)
        bt.place(x=20,y=545)

        # Descrição do botão atraves de um label
        lb = Label(self.janela, text = "Clicar no botão acima para mover o Robo")
        lb.place(x=20, y=570)


        self.janela.mainloop()



def main():
    print(" Programa Desafio 3 Move Robo")
    cll = moveto(10,10)

    cll.planta()



if __name__ == '__main__':
    main()
