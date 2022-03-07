import control
#import Windows
import sqlite3


def sqlTables():
	conn = sqlite3.connect('ocrtool.db')

	create = '''CREATE TABLE IF NOT EXISTS "main" (
			 "ID"	INTEGER,
			 "Date"	TEXT,
			 "Encoder"	TEXT NOT NULL,
			 "Prioridade"	INTEGER,
			 "chave_do_projeto"	TEXT NOT NULL UNIQUE,
			 "palavra_chave"	TEXT NOT NULL,
			 "modificacoes"	TEXT,
			 "textoA"	TEXT NOT NULL,
			 "delimitador"	TEXT,
			 "parametros"	TEXT,
			 "Status"	INTEGER,
			 PRIMARY KEY("ID" AUTOINCREMENT)
			 );'''
	cursor = conn.cursor()
	cursor.execute(create)
	conn.commit()

def main():

	#inicializa as tabelas aplicação
	sqlTables()
	#Inicia a janela
	control.main()
	
	#



main()

