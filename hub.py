import configparser as cp
import pandas as pd
from dataRetriver import *
import webbrowser
import tkinter as tk
from functools import partial
from tkinter import PhotoImage
from PIL import Image,ImageTk

class Hub:

    def __init__(self,root):
        self.config = cp.ConfigParser()
        self.config.read('configs/config.cfg')
        self.d_r = Retriver(self.config.get("PATHS","csv_path"))
        self.root = root
        self.root.title("Company Hub")
        self.root.geometry("400x300")  # Imposta una dimensione per la finestra, se necessario
        # Crea un pannello (Frame) per contenere i record
        self.panel = tk.Frame(self.root)
        self.panel.pack(padx=10, pady=10, fill="both", expand=True)
        self.__create_record_widgets(self.panel)


    def __clickEvent(self,record):
        print(f"You selected {record["Name"]}")
        #webbrowser.open(record["Link"])

    def __create_record_widgets(self,parent):
        df = self.d_r.getCsvData()
        for record in df.itertuples(index=False):
            if record.Image == "nan" or record.Image == None:
                image = PhotoImage(record.Image)
            else:
                image = PhotoImage(self.config.get("PATHS","placeholder_path"))  
            button = tk.Button(
            parent,
            text=f"{record.Name}\n{record.Description}",
            image=image,
            compound="top",  # Immagine sopra al testo
            command=partial(self.__clickEvent, record),
            width=20,
            height=100  # Imposta un'altezza fissa se necessario
        )
        #button.image = image  # Conserva una riferimento all'immagine per evitare che venga distrutta dal garbage collector
        button.pack(pady=5, fill="x", padx=10)  # Usa 'fill="x"' per far sì che il pannello si adatti



root = tk.Tk()
hub = Hub(root)
root.mainloop()