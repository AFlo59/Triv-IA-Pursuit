import pygame
from .Case import Case, TYPE_CASE
from .Case_Sprite import CaseSprite

ROWS = 9
COLS = 9

THEME_COLORS = {
    1: (255, 0, 0),    # Rouge
    2: (0, 0, 255),    # Bleu
    3: (225, 240, 9),  # Jaune
    4: (217, 9, 240),  # Violet
    5: (9, 240, 56),   # Vert
    6: (240, 163, 9),  # Orange
}
themes = [('🟥', 1), ('🟦', 2), ('🟨', 3), ('🟪', 4), ('🟩', 5), ('🟧', 6)]
camemberts = [('🍓', 1), ('💙', 2), ('💛', 3), ('💜', 4), ('💚', 5), ('🧡', 6)]
next_pos_possible = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

class Plateau:
    def __init__(self, theme_colors) -> None:
        print('plateau')
        self.cases = []
        self.all_sprites = pygame.sprite.Group()
        self.theme_colors = theme_colors  # Pass THEME_COLORS to Plateau
        self.render()

    def render(self):
        self.setup()
        graf = ''
        for row in self.cases:
            for item in row:
                # Use plain numbers instead of emoji characters for display
                graf = f'{graf}{item.theme} '
            graf = f'{graf}\r\n'

        print(graf)
    
    def setup(self):
     i = 0

     for row in range(ROWS):
        row_items = []
        if i == len(themes) - 1:
            i = 0

        for col in range(COLS):
            theme_number = themes[i][1]

            # Vérifie la couleur de thème des cases adjacentes
            adjacent_themes = set()

            # Check if col is greater than 0 before accessing row_items[col - 1]
            if col > 0:
                adjacent_themes.add(row_items[col - 1].theme)
            if row > 0:
                adjacent_themes.add(self.cases[row - 1][col].theme)

            while theme_number in adjacent_themes:
                # Choisissez un autre thème jusqu'à ce qu'il soit différent des thèmes adjacents
                i = (i + 1) % len(themes)
                theme_number = themes[i][1]

            case = Case((col, row), TYPE_CASE['theme'], theme_number, themes[i][0], theme_colors=self.theme_colors)
            row_items.append(case)
            sprite = CaseSprite(case, self.theme_colors)  # Passe THEME_COLORS à CaseSprite
            self.all_sprites.add(sprite)  # Ajoute le sprite au groupe

        # Move this line outside the inner loop
        self.cases.append(row_items)




    # def setup(self):
    #     i = 0
    #     for row in range(ROWS):
    #         row_items = []
    #         if i == len(themes) - 1:
    #             i = 0

    #         for col in range(COLS):
    #             if (
    #                 (col == row == 0) or
    #                 (col == COLS // 2 and row == 0) or
    #                 (col == COLS - 1 and row == 0) or
    #                 (row == ROWS - 1 and col == 0) or
    #                 (row == ROWS - 1 and col == COLS // 2) or
    #                 (row == ROWS - 1 and col == COLS - 1)
    #             ):
    #                 item = camemberts.pop()
    #                 c = Case(position=(col, row), type_case=TYPE_CASE['theme'], theme=item[1], graf=item[0], theme_colors=self.theme_colors)
    #                 row_items.append(c)
    #                 sprite = CaseSprite(c, self.theme_colors)  # Pass THEME_COLORS to CaseSprite
    #                 self.all_sprites.add(sprite)  # Add the sprite to the group
    #             elif col == 0:  # First column
    #                 row_items.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0], theme_colors=self.theme_colors))
    #                 sprite = CaseSprite(row_items[-1], self.theme_colors)  # Pass THEME_COLORS to CaseSprite
    #                 self.all_sprites.add(sprite)  # Add the sprite to the group
    #             elif row == 0 or row == ROWS // 2:  # First row and middle row
    #                 row_items.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0], theme_colors=self.theme_colors))
    #                 sprite = CaseSprite(row_items[-1], self.theme_colors)  # Pass THEME_COLORS to CaseSprite
    #                 self.all_sprites.add(sprite)  # Add the sprite to the group
    #             elif row == ROWS - 1:  # Last row
    #                 row_items.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0], theme_colors=self.theme_colors))
    #             elif col == COLS - 1 or col == COLS // 2:  # Last column and middle column
    #                 row_items.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0], theme_colors=self.theme_colors))
    #                 sprite = CaseSprite(row_items[-1], self.theme_colors)  # Pass THEME_COLORS to CaseSprite
    #                 self.all_sprites.add(sprite)  # Add the sprite to the group
    #             elif col == row or (col + row) + 1 == ROWS:  # Diagonals
    #                 row_items.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0], theme_colors=self.theme_colors))
    #                 sprite = CaseSprite(row_items[-1], self.theme_colors)  # Pass THEME_COLORS to CaseSprite
    #                 self.all_sprites.add(sprite)  # Add the sprite to the group
    #             else:
    #                 row_items.append(Case((col, row), TYPE_CASE['null']))

    #             sprite = CaseSprite(row_items[-1], self.theme_colors)  # Pass THEME_COLORS to CaseSprite
    #             self.all_sprites.add(sprite)

    #         self.cases.append(row_items)

    def move_joueur(self, position, nb_case):
        x, y = position
        new_x = x + nb_case
        new_y = y + nb_case
        # Check if the new position is outside the board
        if not (0 <= new_x < COLS and 0 <= new_y < ROWS):
            print("Cannot move outside the board.")
            return None  # Return None to indicate an invalid move
        case = self.cases[new_y][new_x]
        return case





# import pygame
# from .Case import Case, TYPE_CASE
# from .Case_Sprite import CaseSprite

# ROWS = 9
# COLS = 9

# THEME_COLORS = {
#     1: (255, 0, 0),    # Rouge
#     2: (0, 0, 255),    # Bleu
#     3: (225, 240, 9),  # Jaune
#     4: (217, 9, 240),  # Violet
#     5: (9, 240, 56),   # Vert
#     6: (240, 163, 9)   # Orange
# }

# themes = [('🟥', 1), ('🟦', 2), ('🟨', 3), ('🟪', 4), ('🟩', 5), ('🟧', 6)]
# camemberts = [('🍓', 1), ('💙', 2), ('💛', 3), ('💜', 4), ('💚', 5), ('🧡', 6)]
# next_pos_possible = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

# class Plateau:
#     def __init__(self, theme_colors) -> None:
#         print('plateau')
#         self.cases = []
#         self.all_sprites = pygame.sprite.Group()
#         self.theme_colors = theme_colors  # Pass THEME_COLORS to Plateau
#         self.render()

#     def render(self):
#         self.setup()
#         graf = ''
#         for row in self.cases:
#             for item in row:
#                 graf = f'{graf}{item.graf}'
#             graf = f'{graf}\r\n'

#         print(graf)

#     def setup(self):
#         i = 0
#         for row in range(ROWS):
#             rowItems = []
#             if i == len(themes) - 1:
#                 i = 0

#             for col in range(COLS):
#                 if ((col == row == 0) or
#                     (col == COLS // 2 and row == 0) or
#                     (col == COLS - 1 and row == 0) or
#                     (row == ROWS - 1 and col == 0) or
#                     (row == ROWS - 1 and col == COLS // 2) or
#                     (row == ROWS - 1 and col == COLS - 1)):

#                     item = camemberts.pop()
#                     c = Case(position=(col, row), type_case=TYPE_CASE['theme'], theme=item[1], graf=item[0])
#                     rowItems.append(c)
#                 elif col == 0:  # First column
#                     rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
#                 elif row == 0 or row == ROWS // 2:  # First row and middle row
#                     rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
#                 elif row == ROWS - 1:  # Last row
#                     rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
#                 elif col == COLS - 1 or col == COLS // 2:  # Last column and middle column
#                     rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
#                 elif col == row or (col + row) + 1 == ROWS:  # Diagonals
#                     rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
#                 else:
#                     rowItems.append(Case((col, row), TYPE_CASE['null']))

#                 sprite = CaseSprite(rowItems[-1], self.theme_colors)  # Pass THEME_COLORS to CaseSprite
#                 self.all_sprites.add(sprite)

#             i += 1
#             if i == len(themes) - 1:
#                 i = 0

#             self.cases.append(rowItems)

#     def move_joueur(self, position, nb_case):
#         x, y = position
#         new_x = x + nb_case
#         new_y = y + nb_case

#         # Check if the new position is outside the board
#         if not (0 <= new_x < COLS and 0 <= new_y < ROWS):
#             print("Cannot move outside the board.")
#             return None  # Return None to indicate an invalid move

#         case = self.cases[new_y][new_x]
#         return case


        
    # def setup(self):
    #     i = 0
    #     for row in range(ROWS):
    #         rowItems = []
    #         if i == len(themes) - 1:
    #             i = 0

    #         for col in range(COLS):
    #             if ((col == row == 0) or
    #                 (col == COLS // 2 and row == 0) or
    #                 (col == COLS - 1 and row == 0) or

    #                 (row == ROWS - 1 and col == 0) or
    #                 (row == ROWS - 1 and col == COLS // 2) or
    #                 (row == ROWS - 1 and col == COLS - 1)):
    #                     item = camemberts.pop()
    #                     c = Case(position=(col, row), type_case=TYPE_CASE['theme'], theme=item[1], graf=item[0])
    #                     rowItems.append(c)
    #                     sprite = CaseSprite(c)  # Créez le sprite pour la case
    #                     self.all_sprites.add(sprite)  # Ajoutez le sprite au groupe
    #             elif col == 0: # Première colonne
    #                 rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
    #                 sprite = CaseSprite(rowItems[-1])  # Créez le sprite pour la case
    #                 self.all_sprites.add(sprite)  # Ajoutez le sprite au groupe
    #             elif row == 0 or row == ROWS // 2: # Première ligne et ligne du milieu
    #                 rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
    #                 sprite = CaseSprite(rowItems[-1])  # Créez le sprite pour la case
    #                 self.all_sprites.add(sprite)  # Ajoutez le sprite au groupe
    #             elif row == ROWS - 1: # Dernière ligne
    #                 rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
    #             elif col == COLS - 1 or col == COLS // 2: # Dernière colonne et colonne du milieu
    #                 rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
    #                 sprite = CaseSprite(rowItems[-1])  # Créez le sprite pour la case
    #                 self.all_sprites.add(sprite)  # Ajoutez le sprite au groupe
    #             elif col == row or (col + row) + 1 == ROWS: # Diagonales
    #                 rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
    #                 sprite = CaseSprite(rowItems[-1])  # Créez le sprite pour la case
    #                 self.all_sprites.add(sprite)  # Ajoutez le sprite au groupe
    #             else:
    #                 rowItems.append(Case((col, row), TYPE_CASE['null']))

    #             i += 1
    #             if i == len(themes) - 1:
    #                 i = 0

    #         self.cases.append(rowItems)
        
    # def move_joueur(self, position, nb_case):
    #     x, y = position
    #     new_x = x + nb_case
    #     new_y = y + nb_case

    #     # Check if the new position is outside the board
    #     if not (0 <= new_x < COLS and 0 <= new_y < ROWS):
    #         print("Cannot move outside the board.")
    #         return None  # Return None to indicate an invalid move

    #     case = self.cases[new_y][new_x]
    #     return case