import datetime
import sys
import sqlite3
import os
import subprocess
from sqlite3 import Error

file = ('c:\\Users\\p746309\\Desktop\\teste.bat')
database_file = ('c:\\Users\\p746309\\Desktop\\Trabalho\\Programas\\SQLite\\base.db')
conn = sqlite3.connect(database_file)
c = conn.cursor()

def create_account(basename,level):
    chk_erro = 0

    cmd_add_cliente = ("insert into base_control (basename, level) values (\'"+basename+"\', "+level+");")

    try:
        c.execute(cmd_add_cliente)
    except sqlite3.Error as erro:
        chk_erro += 1
        print("Ocorreu algum erro de banco de dados. SQLITE-ERRO:", erro.args[0])
        print('Não foi possível cadastrar o cliente [',basename,'].')
        conn.close()
        
    if chk_erro == 0:
        conn.commit()
        print('Info - Cliente [',basename,'] foi cadastrado(a) com sucesso.')


def busca_valor(nome,campo): # Nome / Campo de busca.
    chk_erro = 0
    temp = 'NoValue'
    cmd_busca_valor = ("select "+campo+" from base_control where basename = \'"+nome+"\';")

    try:
        c.execute(cmd_busca_valor)

    except sqlite3.Error as erro:
        print("Ocorreu algum erro de banco de dados. SQLITE-ERRO:", erro.args[0])
        chk_erro += 1
        conn.close()
        exit(1)

    if chk_erro == 0:
        for valor in c.execute(cmd_busca_valor):
            temp = valor[0]
            print('O valor retornado é:', temp)

    return temp

basename = 'Dz9Farm-15'
campo_add = '15'

create_account(basename,campo_add)
#print(ctrl_up_abrigo)

#FOR /F "tokens=* USEBACKQ" %F IN (`sqlite3 base.db "select ctrl_up_resources from base_control where basename = 'Dz9Farm-1'"`) DO (SET var=%F)
#cd C:\Users\p746309\Desktop\Trabalho\Programas\SQLite
#FOR /F "tokens=* USEBACKQ" %%F IN (`sqlite3 base.db "select valor from config where name = 'dir_sql'"`) DO (SET dir_sql=%%F)
#cd %dir_sql%
#add_client(conn,c)

#subprocess.run(file, shell=True, check=True, capture_output=True)

