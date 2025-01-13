import oracledb
from dotenv import load_dotenv
import os
import logging

load_dotenv()

log_file = 'app.log'

if not os.path.exists(log_file):
    with open(log_file, 'w'):
        pass

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def execute_query():
    try:
        with open('query.sql', 'r') as file:
            select_query = file.read()

        with open('update.sql', 'r') as file:
            update_query = file.read()

        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = int(os.getenv('DB_PORT'))
        service_name = os.getenv('DB_SERVICE_NAME')

        connection = oracledb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            service_name=service_name
        )

        cursor = connection.cursor()

        cursor.execute(select_query)
        results = cursor.fetchall()

        if results:
            logging.info(f"Consulta retornou {len(results)} registros. Executando atualizacao...")

            cursor.execute(update_query)
            connection.commit()
            logging.info("Atualizacao executada com sucesso.")
        else:
            logging.info("Consulta nao retornou registros. Nenhuma atualizacao realizada.")

    except oracledb.DatabaseError as e:
        error, = e.args
        logging.error(f"Erro no banco de dados: {str(error)}")

    except Exception as e:
        logging.error(f"Erro inesperado: {str(e)}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


if __name__ == "__main__":
    execute_query()
