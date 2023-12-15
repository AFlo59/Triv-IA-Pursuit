import sqlite3


class ConnectBdd:
    def __init__(self) -> None:
        self.con = sqlite3.connect("triviapursuit.db")
        

    def create_table(self, sql):
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        self.commit()


    def create_joueur(self, sql, joueur):
        self.cur = self.con.cursor() 
        self.cur.execute(sql, joueur)
        print(self.cur.lastrowid)
        self.commit()

    def create_theme(self, sql, categories):
        self.cur = self.con.cursor()
        self.cur.execute(sql, categories)
        self.commit()
    
    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()

    
    