import pygame
from pygame.rect import Rect
from pygame import Surface
from model.Joueur import Joueur
from model.Plateau import Plateau
from utils import cls, de

MAX_JOUEUR = 6

class Partie:
    def __init__(self, screen: Surface) -> None:
        pygame.font.init()
        self.current_joueur = None
        self.screen = screen
        self.plateau = Plateau(screen)
        self.inscription_visible = True
        self.text_entries = {'nom': '', 'prenom': ''}
        self.font = pygame.font.Font(None, 36)
        self.run()

    def run(self):
        self.list_joueur = []

    def update(self):
        self.plateau.update()
    
    def handle_no_button(self):
        self.inscription_visible = False

    def inscription(self):
        new_joueur = True
        while new_joueur:
            nom = input('Votre nom : ')
            prenom = input('Votre prénom : ')

            joueur = Joueur(partie=self, nom=nom, prenom=prenom)

            if joueur:
                confirm_input = input(f"Confirmez-vous l'inscription de {nom} {prenom}? (o/n): ")
                if confirm_input.lower() == 'o':
                    self.list_joueur.append(joueur)
                    print(f"Inscription de {nom} {prenom} réussie.")

                    if len(self.list_joueur) == MAX_JOUEUR:
                        new_joueur = False

                    new_joueur_input = input('Nouveau joueur ? O/n: ')
                    if new_joueur_input.lower() != 'o':
                        new_joueur = False
                else:
                    print("Inscription annulée.")
            else:
                print(f"Impossible d'enregistrer {nom} {prenom}")

        return True
    def inscription_page(self):
     running = True
     active_entry = 'nom'
     new_player = True

     while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                self.handle_event(event, active_entry)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if self.inscription_visible:
                        if active_entry == 'nom':
                            active_entry = 'prenom'
                        else:
                            if self.handle_yes_button():
                                if len(self.list_joueur) < MAX_JOUEUR:
                                    self.text_entries = {'nom': '', 'prenom': ''}
                                    # Switch back to 'Nom' after handling 'Prenom'
                                    active_entry = 'nom'
                                else:
                                    new_player = False
                                    self.inscription_visible = False
                                    running = False
                            else:
                                active_entry = 'nom'
                            self.draw_inscription_page(active_entry)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_point_inside_button(event.pos, 'Yes'):
                        if self.handle_yes_button():
                            if len(self.list_joueur) < MAX_JOUEUR:
                                self.text_entries = {'nom': '', 'prenom': ''}
                                if self.inscription_visible:
                                    active_entry = 'nom'
                                else:
                                    self.inscription_visible = False
                                    running = False
                                    if not new_player and self.list_joueur:
                                        self.current_joueur.start()
                            else:
                                self.inscription_visible = False
                                running = False
                        self.draw_inscription_page(active_entry)
                    elif self.is_point_inside_button(event.pos, 'No'):
                        self.inscription_visible = False
                        running = False

        # Move the drawing outside the event loop
        self.draw_inscription_page(active_entry)

        pygame.display.flip()

     return new_player
    
    def handle_event(self, event, active_entry):
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            if self.inscription_visible:
                if active_entry == 'nom':
                    active_entry = 'prenom'
                else:
                    if self.handle_yes_button():
                        if len(self.list_joueur) < MAX_JOUEUR:
                            self.text_entries = {'nom': '', 'prenom': ''}
                        else:
                            self.inscription_visible = False
                            running = False
                    else:
                        active_entry = 'nom'
        elif event.key == pygame.K_BACKSPACE:
            self.handle_backspace_key(active_entry)
        elif event.key == pygame.K_TAB:
            active_entry = 'prenom' if active_entry == 'nom' else 'nom'
        else:
            self.handle_other_keys(event, active_entry)
     elif event.type == pygame.MOUSEBUTTONDOWN:
        if self.inscription_visible:
            if self.is_point_inside_button(event.pos, 'Yes'):
                if self.handle_yes_button():
                    if len(self.list_joueur) < MAX_JOUEUR:
                        self.text_entries = {'nom': '', 'prenom': ''}
                    else:
                        self.inscription_visible = False
                        running = False
                else:
                    active_entry = 'nom'
            elif self.is_point_inside_button(event.pos, 'No'):
                self.inscription_visible = False
    running = False

    def draw_inscription_page(self, active_entry):
        screen_width, screen_height = self.screen.get_size()
        rect_width, rect_height = 400, 200
        x = (screen_width - rect_width) // 2
        y = (screen_height - rect_height) // 2

        if self.inscription_visible:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(x, y, rect_width, rect_height))

            nom_surface = self.font.render(f"Nom: {self.text_entries['nom']}", True, (255, 255, 255))
            prenom_surface = self.font.render(f"Prénom: {self.text_entries['prenom']}", True, (255, 255, 255))

            nom_rect = nom_surface.get_rect(center=(x + rect_width // 2, y + rect_height // 2 - 20))
            prenom_rect = prenom_surface.get_rect(center=(x + rect_width // 2, y + rect_height // 2 + 20))

            self.screen.blit(nom_surface, nom_rect)
            self.screen.blit(prenom_surface, prenom_rect)

            button_yes_rect = pygame.Rect((screen_width - rect_width) // 2 + 20, (screen_height - rect_height) // 2 + rect_height - 60, 100, 40)
            button_no_rect = pygame.Rect((screen_width - rect_width) // 2 + rect_width - 120, (screen_height - rect_height) // 2 + rect_height - 60, 100, 40)

            pygame.draw.rect(self.screen, (0, 255, 0), button_yes_rect)
            pygame.draw.rect(self.screen, (0, 0, 255), button_no_rect)

            button_yes_text = self.font.render("Oui", True, (255, 255, 255))
            button_no_text = self.font.render("Non", True, (255, 255, 255))

            self.screen.blit(button_yes_text, button_yes_rect.move(10, 5))
            self.screen.blit(button_no_text, button_no_rect.move(20, 5))

        pygame.display.flip()
    
    def is_point_inside_button(self, pos, button_text):
        screen_width, screen_height = self.screen.get_size()
        rect_width, rect_height = 400, 200
        x = (screen_width - rect_width) // 2
        y = (screen_height - rect_height) // 2

        button_yes_rect = pygame.Rect((screen_width - rect_width) // 2 + 20, (screen_height - rect_height) // 2 + rect_height - 60, 100, 40)
        button_no_rect = pygame.Rect((screen_width - rect_width) // 2 + rect_width - 120, (screen_height - rect_height) // 2 + rect_height - 60, 100, 40)

        if button_text.lower() == 'yes':
            return button_yes_rect.collidepoint(pos)
        elif button_text.lower() == 'no':
            return button_no_rect.collidepoint(pos)

        return False

    def handle_enter_key(self, active_entry):
        if active_entry == 'nom':
            self.text_entries['nom'] = ''
        elif active_entry == 'prenom':
            self.text_entries['prenom'] = ''
            if not self.ask_for_another_player():
                self.inscription_visible = False

    def handle_backspace_key(self, active_entry):
        self.text_entries[active_entry] = self.text_entries[active_entry][:-1]

    def handle_other_keys(self, event, active_entry):
        self.text_entries[active_entry] += event.unicode

    def ask_for_another_player(self):
        response = input('Nouveau joueur ? O/n').lower()
        return response != 'n'

    def handle_yes_button(self):
        nom = self.text_entries['nom']
        prenom = self.text_entries['prenom']

        if nom and prenom:
            joueur = Joueur(partie=self, nom=nom, prenom=prenom)
            self.list_joueur.append(joueur)
            self.text_entries['nom'] = ''
            self.text_entries['prenom'] = ''
            return True
        else:
            print("Nom et prénom ne peuvent pas être vides.")
            return False
    
    

    def start(self):
        self.current_joueur = self.list_joueur[de(0, len(self.list_joueur) - 1)]
        self.play()
        
    def play(self):
        if self.current_joueur:
            self.current_joueur.play()
            print('play')
            
    def dashboard(self):
        #cls()
        for joueur in self.list_joueur:
            print(joueur.toString())
            
            print()
            
            if self.current_joueur:
                print('Joueur en cours:', self.show_current_joueur())
            else:
                print('Aucun joueur en cours.')

    def show_current_joueur(self):
        return self.current_joueur.toString() if self.current_joueur else 'Aucun joueur en cours.'
    

    # def inscription_page(self):
    #  running = True
    #  active_entry = 'nom'
    #  new_player = True

    #  while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         else:
    #             self.handle_event(event, active_entry)
    #             if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
    #                 if self.inscription_visible:
    #                     if active_entry == 'nom':
    #                         active_entry = 'prenom'
    #                     else:
    #                         if self.handle_yes_button():
    #                             if len(self.list_joueur) < MAX_JOUEUR:
    #                                 self.text_entries = {'nom': '', 'prenom': ''}
    #                                 # Switch back to 'Nom' after handling 'Prenom'
    #                                 active_entry = 'nom'
    #                             else:
    #                                 new_player = False
    #                                 self.inscription_visible = False
    #                                 running = False
    #                         else:
    #                             active_entry = 'nom'
    #                         self.draw_inscription_page(active_entry)

    #     # Move the drawing outside the event loop
    #     self.draw_inscription_page(active_entry)

    #     pygame.display.flip()

    #  return new_player
