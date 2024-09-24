import pyautogui
import time
import pandas

pyautogui.hotkey('ctrl','alt','t')
time.sleep(2)
pyautogui.write('cd Documentos')
pyautogui.press('enter')
pyautogui.write('cd projeto_auto')
pyautogui.press('enter')
pyautogui.write('python3 manage.py runserver')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl','alt','t')
time.sleep(2)
pyautogui.write('firefox')
pyautogui.press('enter')
time.sleep(5)
pyautogui.write('127.0.0.1:8000')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=811,y=464)
time.sleep(2)
pyautogui.press('tab', presses=3, interval=1)
time.sleep(4)

tabela = pandas.read_csv('base.csv')

for i in tabela.index:
    cadastrar = str(tabela.loc[i, 'marca'])
    pyautogui.write(cadastrar)
    time.sleep(1)
    pyautogui.press('tab')
    cadastrar = str(tabela.loc[i, 'modelo'])
    pyautogui.write(cadastrar)
    time.sleep(1)
    pyautogui.press('tab')
    cadastrar = int(tabela.loc[i, 'qtde'])
    time.sleep(1)
    pyautogui.write(str(cadastrar))
    pyautogui.press('tab')
    cadastrar = float(tabela.loc[i, 'valor'])
    pyautogui.write(str(cadastrar))
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('tab', presses=3)


    
    

