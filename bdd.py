from connectbdd import ConnectBdd


table = ConnectBdd()
table.create_table(("""
    CREATE TABLE IF NOT EXISTS joueurs (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT            
    )
"""))
            
table.create_table(("""
    CREATE TABLE IF NOT EXISTS themes (
        theme_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT
            
    )
"""))
             
table.create_table(("""
    CREATE TABLE IF NOT EXISTS questions (
        questions_id INTEGER PRIMARY KEY AUTOINCREMENT,
        texte_question TEXT,
        reponse TEXT,
        choix1 INTEGER,
        choix2 INTEGER,
        choix3 INTEGER,
        choix4 INTEGER,
        theme_id INTEGER,
        FOREIGN KEY (theme_id) REFERENCES themes(theme_id)
    )
"""))
    
table.create_table(("""
    CREATE TABLE IF NOT EXISTS reponses (
        reponse_id INTEGER PRIMARY KEY AUTOINCREMENT,
        texte_reponse TEXT,
        reponse INTEGER,
        questions_id INTEGER,
        FOREIGN KEY (questions_id) REFERENCES questions(questions_id)
    )
"""))




