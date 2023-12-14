# Python POO
## main
- partie
- de
- joueur
- plateau
    - case

## partie
- -list_joueur
- run()
- inscription()
- start()
    >- **cas 1:** la partie choisit le joueur qui commence
    >- **cas 2:** la partie choisit le joueur qui lance en premier le dé, le plus grand nombre démarre la partie
- next_joueur()

## de
- random([1-]) *-> int*
    > Utilisé pour lancer le dé et avancer (1-6)
    > Utilisé pour une couleur/thème pour choisir une question (1-..)

## joueur
- -score
- -case_actuelle
- lance_de()
- set_question(question)
-- set_score(reponse)

## plateau
- -list_cases: *typeof case*
- render_case()
    
## case
- -position
- set(type_de_case)
    - -> case_theme
    - -> case_gain
    - -> case_raccourci
    - -> case_null
- get_question()

---

# BDD

**joueurs**
    id, nom, prenom

**themes**
    id, nom

**questions**
    id, theme_id, texte, reponse

**reponses**
    question_id, texte, reponse *(bool)*