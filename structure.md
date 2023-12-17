
# BDD

**joueurs**
    id, nom, prenom

**themes**
    id, nom

**questions**
    id, theme_id, texte, (difficulte), reponse

**reponses**
    question_id, texte, reponse *(bool)*

# Pour choisir une question aléatoirement :

SELECT texte_question FROM questions ORDER BY RANDOM() LIMIT 1;  (avec rajouts de WHERE pour filtrer les catégories)