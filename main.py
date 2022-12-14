from tkinter import *
import sqlite3
from pandas import *

# #Criando o Banco de Dados:
conexao = sqlite3.connect('clientes.db')
cor1 = '#B0C4DE'
#arquivo = open('clientes.xlsx', '+a')
# # Criando o cursor:
c = conexao.cursor()

# # Criando a tabela:
c.execute("""CREATE TABLE IF NOT EXISTS  clientes (
     nome text,
     sobrenome text,
    email text,
    telefone text
     )""")

# #Commit as mudanças:conexao.commit()

# #Fechar o banco de dados:
conexao.close()

# criação da tela
janela = Tk()
janela.title('Cadastro de Clientes')
janela.configure(background=cor1)
janela. geometry("400x400")

def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:email,:telefone)",
              {
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get()
              })

# Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_email.delete(0,"end")
    entry_telefone.delete(0,"end")

def exporta_clientes():
  conexao = sqlite3.connect('clientes.db')
  c = conexao.cursor()

  # Inserir dados na tabela:
  c.execute("SELECT * FROM clientes")
  clientes_cadastrados = c.fetchall()
  # print(clientes_cadastrados)
  clientes_cadastrados=DataFrame(clientes_cadastrados,columns=['nome','sobrenome','email','telefone'])
  
  banco_clientes=clientes_cadastrados.values.tolist()
  print(banco_clientes)
  clientes_cadastrados.to_excel('clientes.xlsx')

  # Commit as mudanças:
  conexao.commit()

  # Fechar o banco de dados:
  conexao.close()




janela.mainloop()
