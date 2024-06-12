import pyautogui
import subprocess
import time
import pandas as pd
import funcoes_imgs as fcs

pyautogui.FAILSAFE=True

def login():
    subprocess.Popen([r'C:\Program Files (x86)\SAP\NWBC65\NWBC'])

    login = pd.read_excel(r"C:\Users\jbtesch\Documents\usuario.xlsx")
    usuario = "0" + str(login.loc[0, "usuario"])
    senha = login.loc[0, "senha"]

    fcs.clicar_centro("logoSAP.png")
    fcs.preencher_campo_direita("usuarioSAP.png", str(usuario))
    fcs.preencher_campo_direita("senhaSAP.png", str(senha))
    pyautogui.press("enter")
    time.sleep(3)
