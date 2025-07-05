import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )


def load_loja():
    excel_path = r"C:\Users\Vinicius Oliveira\Downloads\produtos.xlsx"
    df = pd.read_excel(excel_path)

    conn = get_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            """ 
        INSERT INTO loja(id_loja, nome_loja, cidade, estado)
        VALUES(%s,%s,%s,%s)
        """, (row['id_loja'], row['nome_loja'], row['cidade'], row['estado'])
        )
    conn.commit()
    conn.close()
    print("✅ Lojas carregadas com sucesso.")


def load_user():
    excel_path = r"C:\Users\Vinicius Oliveira\Downloads\usuário.xlsx"
    df = pd.read_excel(excel_path)

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """ 
        INSERT INTO usuario(id_usuario, nome_usuario, perfil, loja_acesso,email)
        VALUES(%s,%s,%s,%s,%s)
        """, (row['id_usuario'], row['nome_usuario'], row['perfil'], row['loja_acesso'], row['email'],)

        )

    conn.commit()
    conn.close()
    print("✅ Usuários carregadas com sucesso.")


def load_metas():
    excel_path = r"C:\Users\Vinicius Oliveira\Downloads\metas.xlsx"
    df = pd.read_excel(excel_path)

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """ 
        INSERT INTO metas(id_meta,id_loja,mes_ano,meta_vendas)
        VALUES(%s,%s,%s,%s)
        """, (row['id_meta'], row['id_loja'], row['mes_ano'], row['meta_vendas'])
        )
    conn.commit()
    conn.close()
    print("✅ Metas carregadas com sucesso.")


def load_produtos():
    excel_path = r"C:\Users\Vinicius Oliveira\Downloads\produtos.xlsx"
    df = pd.read_excel(excel_path)
    conn = get_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            """ 
        INSERT INTO produtos(id_produto,nome_produto, categoria, preco_venda, marca)
        VALUES(%s,%s,%s,%s,%s)
        """, (row['id_produto'], row['nome_produto'], row['categoria'], row['preco_venda'], row['marca'])
        )
    conn.commit()
    conn.close()
    print("✅ Produtos carregadas com sucesso.")


def load_vendas():
    excel_path = r"C:\Users\Vinicius Oliveira\Downloads\vendas.xlsx"
    df = pd.read_excel(excel_path)
    conn = get_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            """ 
        INSERT INTO vendas(id_venda,data_venda, id_loja, id_produto, quantidade, valor_unitario, canal_venda, 
        status_venda)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """, (row['id_venda'], row['data_venda'], row['id_loja'], row['id_produto'], row['quantidade'],
              row['valor_unitario'], row['canal_venda'], row['status_venda'])
        )
    conn.commit()
    conn.close()
    print("✅ Vendas carregadas com sucesso.")


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
