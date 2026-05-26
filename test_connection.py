from database import engine

try:
    connection = engine.connect()
    print("Conexão com PostgreSQL funcionando!")
    connection.close()

except Exception as e:
    print("Erro:", e)