import pyautogui
import subprocess
import time
import pandas as pd
import funcoes_imgs as fcs
import funcoes_querys as qrs
import loginSAP
import tkinter as tk



janela = tk.Tk()
janela.title("Robozin")
janela.geometry('200x250')

botao_login = tk.Button(janela, text='LOGIN SAP', command=loginSAP.login, fg='green', bg='grey')
botao_login.grid(column=1, row=1)

# Linha 2 é deixada em branco, pulando-a

botao_1301 = tk.Button(janela, text="teste 1301", command=qrs.z4fm1301_conf)
botao_1301.grid(column=0, row=3)

botao_2301 = tk.Button(janela, text="teste 1301", command=qrs.z4fm2301_conf)
botao_2301.grid(column=2, row=3)

janela.mainloop()