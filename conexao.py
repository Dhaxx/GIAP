import psycopg2 as pg
import psycopg2.extras 
import fdb

conexao_origem = pg.connect(
    host="localhost",
    port="5432",
    database="SBS",
    user="postgres",
    password="xxxx",
    options="-c search_path=sicop_sbs"
)

conexao_destino = fdb.connect(dsn="D:\Fiorilli\SCPI_8\Cidades\PM - SBS\ARQ2023\SCPI2023.FDB", user='xxxx', 
                              password='xxxx', port=3050, charset='WIN1252')

cur = conexao_origem.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
cur_d = conexao_destino.cursor()

def commit():
    conexao_destino.commit()
    print("Commited")

def get_cursor(conexao):
    return conexao.cursor()