import pyautogui
import funcoes_querys as qrs
import loginSAP
import subprocess
import os
pyautogui.FAILSAFE=True

loginSAP.login()
qrs.z4fm1301()
qrs.z4fm2301()
qrs.fmeddw()
#qrs.fmrp()   >   PAUSADO!


