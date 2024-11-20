import configparser as cp
import pandas as pd
from dataRetriver import *
import webbrowser
import tkinter as tk
from functools import partial
from tkinter import PhotoImage
from PIL import Image,ImageTk
import os
class Hub:

    def __init__(self,root):
        self.config = cp.ConfigParser()
        self.config.read('configs/config.cfg')
        self.d_r = Retriver(self.config.get("PATHS","csv_path"))
        self.root = root
        self.root.title("Company Hub")
        self.root.geometry("400x400")  # Imposta una dimensione per la finestra, se necessario
        # Crea un pannello (Frame) per contenere i record
        self.canvas = tk.Canvas(root)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.__create_record_widgets()

    def __clickEvent(self,record):
        print(f"You selected {record.Name}")
        webbrowser.open(record.Link)

    def __create_record_widgets(self):
        df = self.d_r.getCsvData()
        for record in df.itertuples(index=False):
            button = tk.Button(
            self.scrollable_frame,
            text=f"{record.Name}\n{record.Description}",
            command=lambda r=record: self.__clickEvent(r),
            width = 50,
            height=10,  # Imposta un'altezza fissa se necessario
            anchor="center"
            )
            button.pack(pady=5, fill="x", padx=10)  # Usa 'fill="x"' per far sì che il pannello si adatti



root = tk.Tk()
hub = Hub(root)
root.mainloop()