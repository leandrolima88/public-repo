import sys
import re
import os.path
import definitions
from datetime import *

#Logs
Settings.ActionLogs = True
Settings.InfoLogs = True
Settings.DebugLogs = True
Settings.LogTime = True
Debug.setLogFile(C:UsersPichauDesktopLssBotMacroSikulilogsup_iron_log.txt)

# Settings
setBundlePath('C:\Users\Pichau\Desktop\LssBot\MacroSikuli\Imagens') # Define o diretório das imagens.
dir_cfg = (C:/Users/Pichau/Desktop/LssBot/MacroSikuli/cfg/)
current_file = dir_cfg+'current_farm.txt'
current_farm = (definitions.busca_var(current_file,'=',=,0))
cfg_file = dir_cfg+'cfg_'+current_farm+'.txt'
valida_data = definitions.data_atual()
ctrl_up_resources = (definitions.busca_var(cfg_file,'ctrl_up_resources',=,1))
ctrl_fast_all = (definitions.busca_var(cfg_file,'ctrl_fast_all',=,1))
ctrl_fast_iron_lastdate = (definitions.busca_var(cfg_file,'ctrl_fast_iron_lastdate',=,1))

# Regions
r = (Region(1891,0,610,1080))
r_up = (Region(2063,347,226,208))

# Images
front_01 = (Pattern(front_01.png).similar(0.90))
front_02 = (Pattern(front_02.png).similar(0.90))
up_but = (Pattern(up_but.png).similar(0.90))
aprimorar_but = (Pattern(aprimorar_but.png).similar(0.80))
exit_but = (Pattern(exit_but.png).similar(0.85))
ocioso_but = (Pattern(ocioso_but.png).similar(0.75))
send_but = (Pattern(ocioso_but.png).similar(0.75).targetOffset(200,0))
check_up = (Pattern(check_up.png).similar(0.80))
back_but = (Pattern('back_but.png').similar(0.80))
back_but_big = (Pattern(back_but_big.png).similar(0.80))
dt_but = (Pattern(dt_but.png).similar(0.90))
globo_but = (Pattern(globo_but.png).similar(0.80))
home_but = (Pattern(home_but.png).similar(0.80))
fast_img = (Pattern(fast_img.png).similar(0.80))
cem_img = (Pattern(cem_img.png).similar(0.85))
iniciar_img = (Pattern(iniciar_img.png).similar(0.80))

# Imagens Específicas
oil_search = (Pattern(oil_search_up_iron.png).similar(0.86))

# Moves
print(Setando vars de movimento...)
move_center = Location(2185, 500)
move_rp = Location(2450, 500)
move_lp = Location(1915, 500)
move_tp = Location(2185, 250)
move_bp = Location(2185, 750)

def move(x):
    global move_center
    global move_lp
    global move_rp
    global move_bp
    global move_tp

    if x == 'r':
        print('Movendo para Direita...')
        dragDrop (move_center,move_lp)
    elif x == 'l':
        print('Movendo para Esquerda...')
        dragDrop (move_center,move_rp)
    elif x == 'u':
        print('Movendo para Cima...')
        dragDrop (move_center,move_bp)
    elif x == 'b':
        print('Movendo para Baixo...')
        dragDrop (move_center,move_tp)
    else:
        print('Parametro invalido, indique a direcao com r, l, u, ou b')
        exit(1)

    if not exists(front_01) or not exists(front_02):
        print('Tela principal nao confirmada! Saindo do Script...')
        exit(1)

# Numbers
print(Setando vars gerais...)
recurso = 'Iron'
pump_all = 0
tentativa = 0
pump_allf = 0

def fast():
    print 'Buscando recurso', recurso,'...'

    global pump_allf

    print 'Iniciando processo para LT', recurso ,'Pump.'
    if r.exists(oil_search):
        r.click(Pattern(oil_search).targetOffset(-85,-10))
        if r.exists(fast_img):
            r.click(fast_img)
            if r.exists(cem_img):
                r.click(iniciar_img)
            else:
                r.click(exit_but)
        else:
            if r.exists(dt_but):
                r.click(dt_but)
                r.click(back_but)
    else:
        print recurso,'Pump não encontrada...'
        exit(4)

    print('Iniciando processo para RT', recurso ,'Pump.')
    if r.exists(oil_search):
        r.click(Pattern(oil_search).targetOffset(25,-10))
        if r.exists(fast_img):
            r.click(fast_img)
            if r.exists(cem_img):
                r.click(iniciar_img)
            else:
                r.click(exit_but)
        else:
            if r.exists(dt_but):
                r.click(dt_but)
                r.click(back_but)
    else:
        print recurso,'Pump não encontrada...'
        exit(4)

    print 'Iniciando processo para LB', recurso ,'Pump.'
    if r.exists(oil_search):
        r.click(Pattern(oil_search).targetOffset(-85,45))
        if r.exists(fast_img):
            r.click(fast_img)
            if r.exists(cem_img):
                r.click(iniciar_img)
            else:
                r.click(exit_but)
        else:
            if r.exists(dt_but):
                r.click(dt_but)
                r.click(back_but)
    else:
        print recurso,'Pump não encontrada...'
        exit(4)

    print 'Iniciando processo para RB', recurso ,'Pump.'
    if r.exists(oil_search):
        r.click(Pattern(oil_search).targetOffset(25,50))
        if r.exists(fast_img):
            r.click(fast_img)
            if r.exists(cem_img):
                r.click(iniciar_img)
            else:
                r.click(exit_but)
        else:
            if r.exists(dt_but):
                r.click(dt_but)
                r.click(back_but)
    else:
        print recurso,'Pump não encontrada...'
        exit(4)
    definitions.replace_var(cfg_file,'ctrl_fast_iron_lastdate='+ctrl_fast_iron_lastdate,'ctrl_fast_iron_lastdate='+valida_data)

# Define funcao de Busca de recurso

def findoil():
    print 'Buscando recurso', recurso,'.'

    global pump_all

    print 'Iniciando upgrade do recurso', recurso ,'LT.'
    if r.exists(oil_search):
        r.click(Pattern(oil_search).targetOffset(-85,-10))
        if r.exists(up_but):
            r.click(up_but)
            if r_up.exists(check_up) and r.exists (aprimorar_but):
                r.click(aprimorar_but)
                if r.exists(ocioso_but):
                    r.click(send_but)
                else:
                    r.click(exit_but)
                    print ('Todos os contrutores estao ocupados...')
                    reset_pos()
                    exit(5)
            else:
                r.click(back_but)
        else:
            if r.exists(dt_but):
                r.click(dt_but)
                r.click(back_but)
    else:
        print 'Recurso', recurso,'não encontrado...'
        exit(4)

    print('Iniciando upgrade do recurso', recurso ,'RT.')
    if r.exists(oil_search):
        r.click(Pattern(oil_search).targetOffset(25,-10))
        if r.exists(up_but):
            r.click(up_but)
            if r_up.exists(check_up) and r.exists (aprimorar_but):
                r.click(aprimorar_but)
                if r.exists(ocioso_but):
                    r.click(send_but)
                else:
                    r.click(exit_but)
                    print ('Todos os contrutores estao ocupados...')
                    reset_pos()
                    exit(5)
            else:
                r.click(back_but)
        else:
            if r.exists(dt_but):
                r.click(dt_but)
                r.click(back_but)
    else:
        print 'Recurso', recurso,'não encontrado...'
        exit(4)

    print('Iniciando upgrade do recurso', recurso ,'LB.')
    if r.exists(oil_search):
        r.click(Pattern(oil_search).targetOffset(-85,45))
        if r.exists(up_but):
            r.click(up_but)
            if r_up.exists(check_up) and r.exists (aprimorar_but):
                r.click(aprimorar_but)
                if r.exists(ocioso_but):
                    r.click(send_but)
                else:
                    r.click(exit_but)
                    print ('Todos os contrutores estao ocupados...')
                    reset_pos()
                    exit(5)
            else:
                r.click(back_but)
        else:
            if r.exists(dt_but):
                r.click(dt_but)
                r.click(back_but)
    else:
        print 'Recurso', recurso,'não encontrado...'
        exit(4)

    print('Iniciando upgrade do recurso', recurso ,'RB.')
    if r.exists(oil_search):
        r.click(Pattern(oil_search).targetOffset(25,50))
        if r.exists(up_but):
            r.click(up_but)
            if r_up.exists(check_up) and r.exists (aprimorar_but):
                r.click(aprimorar_but)
                if r.exists(ocioso_but):
                    r.click(send_but)
                else:
                    r.click(exit_but)
                    print ('Todos os contrutores estao ocupados...')
                    reset_pos()
                    exit(5)
            else:
                r.click(back_but)
        else:
            if r.exists(dt_but):
                r.click(dt_but)
                r.click(back_but)
    else:
        print recurso,'Pump não encontrada...'
        exit(4)

def check_slots():
    if r.exists(front_01):
        click(front_01)
        if not r.exists(ocioso_but):
            r.click(exit_but)
            print ('Todos os contrutores estao ocupados...')
            exit(5)
        else:
            print ('Existem slots disponíveis...')
            r.click(exit_but)

def check_front():
    print 'Confirmando tela principal..'
    while not r.exists(front_01) or not r.exists(front_02) :
        print('Tela principal nao encontrada...')
        type(Key.ESC)
    print('Tela principal confirmada!')

def reset_pos():
    print('Resetando Posicao...')
    print('Buscando botao Globo...')
    if r.exists(globo_but):
        print('Botao Globo encontrado, clicando...')
        r.click(globo_but)
        print('Clique Realizado...')
        while r.exists(home_but):
            print('Buscando botao Home...')
            r.click(home_but)
            print('Clique Realizado...')
            break

check_front()
check_slots()

if (pump_all < 1):
    print 'Procurando',recurso,'Pumps...'
    move('r')
    if r.exists(oil_search):
        dragDrop (oil_search,move_center)
        pump_all+=1
        if ctrl_fast_all =='E':
            if ctrl_fast_iron_lastdate == valida_data:
                print('Recurso rapido ja foi realizado hoje.')
            else:
                fast()
        else:
            print('Recurso rapido esta desativado.')
        if ctrl_up_resources == 'E':
            findoil()
        else:
            print 'O upgrade do recurso', recurso, 'esta desativado.'
        reset_pos()
        check_front()
else:
    print 'Pumps',recurso,'ja foi encontrado.'

if (pump_all < 1):
    print 'Procurando',recurso,'Pumps...'
    move('r')
    if r.exists(oil_search):
        dragDrop (oil_search,move_center)
        pump_all+=1
        if ctrl_fast_all =='E':
            if ctrl_fast_iron_lastdate == valida_data:
                print('Recurso rapido ja foi realizado hoje.')
            else:
                fast()
        else:
            print('Recurso rapido esta desativado.')
        if ctrl_up_resources == 'E':
            findoil()
        else:
            print 'O upgrade do recurso', recurso, 'esta desativado.'
        reset_pos()
        check_front()
else:
    print 'Pumps',recurso,'ja foi encontrado.'

print('Scritp Finalizado...')
exit(0)
