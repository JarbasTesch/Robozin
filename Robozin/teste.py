import pyautogui
import subprocess
import time
import pandas as pd
import funcoes_imgs as fcs
from datetime import datetime
import os

pyautogui.FAILSAFE=True

fcs.clicar_centro("fmeddw_excel_carregou.png")
pyautogui.hotkey("alt","f4")
fcs.clicar_centro("voltarSAP.png")