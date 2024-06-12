import pyautogui
import time
import pyperclip
import os

#sl = sem loop

diretorio_imgs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs")

def encontrar_imagem(imagem):
    imagem= os.path.join(diretorio_imgs, imagem)
    while True:
        try:
            pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
            break  # se executou o de cima, posso sair do loop
        except:
            time.sleep(1)  # se deu erro, vou esperar mais 1 seg

    encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
    return encontrou

def encontrar_imagem_sl(imagem):
    imagem = os.path.join(diretorio_imgs, imagem)
    try:
        encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
        if encontrou:
            return encontrou
    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada:", imagem)
    return None


def direita(posicoes_imagem):
    return posicoes_imagem[0] + posicoes_imagem[2], posicoes_imagem[1] + posicoes_imagem[3]/2

def clicar_direita(imagem):
    imagem = os.path.join(diretorio_imgs, imagem)
    while True:
        try:
            pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
            break  # se executou o de cima, posso sair do loop
        except:
            time.sleep(1)  # se deu erro, vou esperar mais 1 seg
    encontrou = encontrar_imagem(imagem)
    pyautogui.click(direita(encontrou))

def preencher_campo_direita(imagem, texto):
    imagem = os.path.join(diretorio_imgs, imagem)
    while True:
        try:
            pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
            break  # se executou o de cima, posso sair do loop
        except:
            time.sleep(1)  # se deu erro, vou esperar mais 1 seg

    encontrou = encontrar_imagem(imagem)
    pyautogui.click(direita(encontrou))
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "v")

def esquerda(posicoes_imagem):
    return posicoes_imagem[0], posicoes_imagem[1] + posicoes_imagem[3]/2

def clicar_esquerda(imagem):
    imagem = os.path.join(diretorio_imgs, imagem)
    while True:
        try:
            pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
            break  # se executou o de cima, posso sair do loop
        except:
            time.sleep(1)  # se deu erro, vou esperar mais 1 seg
    encontrou = encontrar_imagem(imagem)
    pyautogui.click(esquerda(encontrou))

def clicar_centro(imagem):
    imagem = os.path.join(diretorio_imgs, imagem)
    while True:
        try:
            pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
            break  # se executou o de cima, posso sair do loop
        except:
            time.sleep(1)  # se deu erro, vou esperar mais 1 seg
    encontrou = encontrar_imagem(imagem)
    pyautogui.click(pyautogui.center(encontrou))


def encontrar_navbar(navbar):
    navbar = os.path.join(diretorio_imgs, navbar)
    try:
        pyautogui.locateOnScreen(navbar, grayscale=True, confidence=0.9)
        clicar_centro("navbarSAP.png")
    except:
        print("sem barra de navegação")