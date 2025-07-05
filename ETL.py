import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

connection = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = connection.cursor()


def load_loja():
    excel_path = r"C:\Users\Vinicius Oliveira\Downloads\produtos.xlsx"
    df = pd.read_excel(excel_path)
    for _, row in df.iterrows():
        cursor.execute(
            """ 
        INSERT INTO loja(id_loja, nome_loja, cidade, estado)
        VALUES(%s,%s,%s,%s)
        """, (row['id_loja'], row['nome_loja'], row['cidade'], row['estado'])
        )

    connection.commit()
    print("Data Included !")


def load_user():
    excel_path = r"C:\Users\Vinicius Oliveira\Downloads\usuário.xlsx"
    df = pd.read_excel(excel_path)
    for _, row in df.iterrows():
        cursor.execute(
            """ 
        INSERT INTO usuario(id_usuario, nome_usuario, perfil, loja_acesso,email)
        VALUES(%s,%s,%s,%s,%s)
        """, (row['id_usuario'], row['nome_usuario'], row['perfil'], row['loja_acesso'], row['email'],)

        )

    connection.commit()
    print("Data Included !")


def load_metas():
    excel_path = r"C:\Users\Vinicius Oliveira\Downloads\metas.xlsx"
    df = pd.read_excel(excel_path)
    for _, row in df.iterrows():
        cursor.execute(
            """ 
        INSERT INTO metas(id_meta,id_loja,mes_ano,meta_vendas)
        VALUES(%s,%s,%s,%s)
        """, (row['id_meta'], row['id_loja'], row['mes_ano'], row['meta_vendas'])
        )
    connection.commit()
    print("Data Included")


def load_produtos():
    excel_path = r"C:\Users\Vinicius Oliveira\Downloads\produtos.xlsx"
    df = pd.read_excel(excel_path)
    for _, row in df.iterrows():
        cursor.execute(
            """ 
        INSERT INTO produtos(id_produto,nome_produto, categoria, preco_venda, marca)
        VALUES(%s,%s,%s,%s,%s)
        """, (row['id_produto'], row['nome_produto'], row['categoria'], row['preco_venda'], row['marca'])
        )
    connection.commit()
    print("Data Included")


def load_vendas():
    print("Data Included")


def menu():
    while True:
        print("\n--- MENU ETL ---")
        print("1. Carregar Lojas")
        print("2. Carregar Produtos")
        print("3. Carregar Vendas")
        print("4. Carregar Metas")
        print("5. Carregar Usuários")
        print("0. Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            load_loja()
        elif option == "2":
            load_produtos()
        elif option == "3":
            load_vendas()
        elif option == "4":
            load_metas()
        elif option == "5":
            load_user()
        elif option == "0":
            print("Saindo...")
            return menu()
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    menu()
