import sqlite3

con = sqlite3.connect("triviapursuit.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS joueurs (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT            
    )
""")
            
cur.execute("""
    CREATE TABLE IF NOT EXISTS themes (
        theme_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT
            
    )
""")
    
            
cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        questions_id INTEGER PRIMARY KEY AUTOINCREMENT,
        texte_question TEXT,
        reponse TEXT,
        theme_id INTEGER,
        FOREIGN KEY (theme_id) REFERENCES themes(theme_id)
    )
""")
    
cur.execute("""
    CREATE TABLE IF NOT EXISTS reponses (
        reponse_id INTEGER PRIMARY KEY AUTOINCREMENT,
        texte_reponse TEXT,
        reponse INTEGER,
        questions_id INTEGER,
        FOREIGN KEY (questions_id) REFERENCES questions(questions_id)
    )
""")

con.commit()
con.close()