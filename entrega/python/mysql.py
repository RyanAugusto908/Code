import pymysql

class MySQL:
    def __init__(self, host="localhost", user="root", password="", database="biblioteca"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None

    def conectar(self):
        self.conexao = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.DictCursor
        )

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            self.conexao = None

    def executar_query(self, query):
        with self.conexao.cursor() as cursor:
            try:
                cursor.execute(query)
            except Exception as e:
                self.conexao.rollback()
                print(f"Erro ao executar query: {e}")
            else:
                if cursor.description:
                    return cursor.fetchall()
                else:
                    self.conexao.commit()
                    return cursor.lastrowid