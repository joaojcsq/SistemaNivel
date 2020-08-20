from tkinter import *
from tkinter import ttk
import serial
from numpy import interp

root = Tk()


class LerDist:
    def create_porta(self):
        aux = '/dev/ttyUSB0'
        self.portaUSB = serial.Serial(aux, 9600)

    def sen_command(self, cod):
        aux = str(cod)
        self.portaUSB.write(aux.encode())

    def read_command(self):
        msg = self.portaUSB.readline()  # read everything in the input buffer
        dist = str(msg)
        dist = dist.replace("b'", '')
        dist = dist.replace("'", "")
        dist = dist.split("f")
        return dist


class Sistema(LerDist):
    def __init__(self):
        self.root = root
        self.tela()
        self.menus()
        self.frames()
        self.tanques()
        self.create_porta()
        self.SensorUltrassom()

        root.mainloop()

    def tela(self):
        self.root.title("Sistema de Nível")
        self.root.configure(background='#0A7F99')
        self.root.geometry("1300x700")
        self.root.minsize(width=1300, height=700)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu1 = Menu(self.root, tearoff=0)
        filemenu2 = Menu(self.root, tearoff=0)

        def Quit():
            self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu1)
        menubar.add_cascade(label="Sobre", menu=filemenu2)

        filemenu1.add_command(label="Enviar dados por E-mail")
        filemenu1.add_command(label="Gerar relatório")
        filemenu1.add_separator()
        filemenu1.add_command(label="Sair", command=Quit)

        filemenu2.add_command(label="O programa")

    def frames(self):
        self.frame_1 = Frame(self.root,
                             bd=4,
                             bg='#dfe3ee',
                             highlightbackground='#000000',
                             highlightthickness=2)
        self.frame_1.place(relx=0.005,
                           rely=0.01,
                           relwidth=0.12,
                           relheight=0.97)

        self.frame_2 = Frame(self.root,
                             bd=4,
                             bg='#dfe3ee',
                             highlightbackground='#000000',
                             highlightthickness=2)
        self.frame_2.place(relx=0.13,
                           rely=0.01,
                           relwidth=0.86,
                           relheight=0.97)

    def tanques(self):
        self.tanque_1 = ttk.Progressbar(self.frame_2,
                                        orient=VERTICAL,
                                        length=100,
                                        mode='determinate')
        self.tanque_1.place(relx=0.4,
                            rely=0.1,
                            relwidth=0.2,
                            relheight=0.3
                            )
        self.tanque_1['value'] = 0

        self.tanque_2 = ttk.Progressbar(self.frame_2,
                                        orient=VERTICAL,
                                        length=100,
                                        mode='determinate')
        self.tanque_2.place(relx=0.4,
                            rely=0.6,
                            relwidth=0.2,
                            relheight=0.3
                            )
        self.tanque_2['value'] = 100

    def niveis(self, distancia):
        distancia = float(interp(distancia, [0, 25], [0, 90]))
        self.tanque_1['value'] = distancia
        self.tanque_2['value'] = 100 - distancia

    def SensorUltrassom(self):
        self.entry = Entry(self.frame_2,
                           justify='center',
                           relief='groove')
        self.entry.place(relx=0.02,
                         rely=0.1,
                         relwidth=0.05
                         )
        self.sen_command(1)
        dist = self.read_command()
        self.entry.insert(0, dist[0])
        self.niveis(dist[0])
        root.after(100, self.SensorUltrassom)

    def variaveis(self):
        pass


Sistema()
