import pyautogui
import subprocess
import time
import pandas as pd
import funcoes_imgs as fcs
from datetime import datetime
import os

pyautogui.FAILSAFE=True

def z4fm1301():

    fcs.preencher_campo_direita("urlSAP.png", "z4fm1301")
    pyautogui.press("enter")
    fcs.preencher_campo_direita("z4fm1301_campo1.png", "U_ELETNUC")
    fcs.preencher_campo_direita("z4fm1301_campo2.png", "PDG_IU")
    pyautogui.press("f8")
    fcs.encontrar_imagem("z4fm1301_carregou.png")

    encontrou = fcs.encontrar_imagem_sl("z4fm1301_navbar.png")
    if encontrou:
        fcs.clicar_centro("navbarSAP.png")

    time.sleep(1)
    fcs.clicar_centro("menuSAP.png")
    fcs.clicar_centro("sistemaSAP.png")
    fcs.clicar_centro("listaSAP.png")
    fcs.clicar_centro("gravarSAP.png")
    fcs.clicar_centro("fileSAP.png")
    fcs.clicar_esquerda("txt_tabSAP.png")
    pyautogui.press("enter")
    fcs.preencher_campo_direita("diretorioSAP.png",
                                r"C:\SINCRONIZAR PC-ONEDRIVE\eletronuclear.gov.br\DCC FONTES DE DADOS - Documentos\Requisições SAP\Z4FM1301")
    fcs.preencher_campo_direita("nome_fileSAP.png", "Z4FM1301.txt")
    fcs.clicar_centro("substituirSAP.png")
    fcs.encontrar_imagem("exportadoSAP.png")
    fcs.clicar_centro("voltarSAP.png")
    pyautogui.press("enter")
    fcs.clicar_centro("voltarSAP.png")

def z4fm2301():
    fcs.preencher_campo_direita("urlSAP.png", "z4fm2301")
    pyautogui.press("enter")
    fcs.preencher_campo_direita("z4fm1301_campo2.png", "ENUC_itot2")
    fcs.preencher_campo_direita("z4fm2301_campo1.png", "ENUC.24")
    pyautogui.press("f8")
    fcs.encontrar_imagem("z4fm2301_carregou.png")
    time.sleep(1)

    encontrou = fcs.encontrar_imagem_sl("z4fm2301_navbar.png")
    if encontrou:
        fcs.clicar_centro("navbarSAP.png")

    time.sleep(1)
    fcs.clicar_centro("menuSAP.png")
    fcs.clicar_centro("sistemaSAP.png")
    fcs.clicar_centro("listaSAP.png")
    fcs.clicar_centro("gravarSAP.png")
    fcs.clicar_centro("fileSAP.png")
    fcs.clicar_esquerda("txt_tabSAP.png")
    pyautogui.press("enter")
    fcs.preencher_campo_direita("diretorioSAP.png",
                                r"C:\SINCRONIZAR PC-ONEDRIVE\eletronuclear.gov.br\DCC FONTES DE DADOS - Documentos\Requisições SAP\Z4FM2301")
    fcs.preencher_campo_direita("nome_fileSAP.png", "2301 - Bater com BI.txt")
    fcs.clicar_centro("substituirSAP.png")
    fcs.encontrar_imagem("exportadoSAP.png")
    fcs.clicar_centro("voltarSAP.png")
    pyautogui.press("enter")
    fcs.clicar_centro("voltarSAP.png")

def fmeddw():
    fcs.preencher_campo_direita("urlSAP.png", "fmeddw")
    pyautogui.press("enter")
    fcs.encontrar_imagem("url_fmeddw_carregou.png")

    encontrou = fcs.encontrar_imagem_sl("fmeddw_campo1.png")
    if encontrou:
        fcs.preencher_campo_direita("fmeddw_campo1.png", "fce1")
        pyautogui.press("enter")

    fcs.preencher_campo_direita("fmeddw_campo2.png", "2024")
    fcs.preencher_campo_direita("fmeddw_campo3.png", "jbcodcc")
    pyautogui.press("f8")
    fcs.encontrar_imagem("fmeddw_carregou.png")
    pyautogui.hotkey("ctrl", "shift", "f7")
    fcs.encontrar_imagem("atalho_salvar_carregou.png")
    pyautogui.press("enter")
    fcs.preencher_campo_direita("diretorioSAP2.png",
                                r"C:\SINCRONIZAR PC-ONEDRIVE\eletronuclear.gov.br\DCC FONTES DE DADOS - Documentos\Requisições SAP")
    pyautogui.press("enter")
    fcs.clicar_centro("fmeddw_folder.png")
    pyautogui.press("enter")
    fcs.preencher_campo_direita("nome_fileSAP2.png", "fmeddw.xlsx")
    pyautogui.press("enter")
    fcs.clicar_centro("substituirSAP2.png")
    fcs.clicar_centro("fmeddw_excel_carregou.png")
    pyautogui.hotkey("alt","f4")
    fcs.clicar_centro("voltarSAP.png")
    time.sleep(1)
    fcs.clicar_centro("voltarSAP.png")

def fmrp():
    fcs.preencher_campo_direita("urlSAP.png", "fmrp_rffmep1ax")
    pyautogui.press("enter")
    fcs.encontrar_imagem("url_fmrp_carregou.png")
    fcs.preencher_campo_direita("fmrp_campo1.png", "2033")
    fcs.preencher_campo_direita("fmrp_campo2.png", " 2147483646")
    fcs.preencher_campo_direita("fmeddw_campo3.png", "jbcodcc2")
    pyautogui.press("f8")
    fcs.encontrar_imagem("fmrp_carregou.png")
    fcs.clicar_centro("menuSAP.png")
    fcs.clicar_centro("listaSAP.png")
    fcs.clicar_centro("exportarSAP.png")
    fcs.clicar_centro("planilhaSAP.png")
    fcs.encontrar_imagem("planilha_carregou.png")
    pyautogui.press("enter")
    fcs.preencher_campo_direita("diretorioSAP2.png",
                                r"C:\SINCRONIZAR PC-ONEDRIVE\eletronuclear.gov.br\DCC FONTES DE DADOS - Documentos\Requisições SAP\FMRP_RFFMEP1AX")
    pyautogui.press("enter")
    fcs.preencher_campo_direita("nome_fileSAP2.png", "fmrp_rffmep1ax.xlsx")
    pyautogui.press("enter")
    fcs.clicar_centro("substituirSAP2.png")
    fcs.encontrar_imagem("exportadoSAP.png")

    #fcs.clicar_centro("fmeddw_excel_carregou.png")
    #pyautogui.hotkey("alt", "f4")

    fcs.clicar_centro("voltarSAP.png")
    time.sleep(1)
    fcs.clicar_centro("voltarSAP.png")

