import pygame
from ball import Player

class Game:
    def __init__(self):
        self.width = 430 #largeur de la fenêtre
        self.height = 670 #hauteur de la fenêtre
        self.window = pygame.display.set_mode((self.width, self.height))
        #crée la fenêtre 
        pygame.display.set_caption("Flappy dunk de Maéva et Raphaël")
        self.clock = pygame.time.Clock() #limite le nombre d'images/secondes
        self.running = True #indique si la boucle principale doit continuer
        self.state = "menu"
        # Etat du jeu : "menu" pour l'instant, plus tard "play"
        self.font_title = pygame.font.SysFont(None, 80)
        # Police pour le titre dans le menu
        self.font_text = pygame.font.SysFont(None, 40)
        # Police pour les textes dans le menu
        self.reset_level()
        # On initialise le niveau (joueur, etc.)
    def reset_level(self):
        # Réinitialise la position du joueur (plus tard ennemi, goal...)
        self.player = Player(100, 100)
        # Crée un joueur au début du niveau, posé sur le sol
    def run(self):
        # Méthode principale qui contient la boucle de jeu
        while self.running:
            for event in pygame.event.get(): #on parcours tous les événements envoyés par pygame
                if event.type == pygame.QUIT: #si l'utilisateur ferme la fenêtre
                    self.running = False #arrête la boucle 

                if self.state == "menu":
                    # Si on est dans le menu
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        # Si on appuie sur ENTREE
                        self.reset_level()
                        # On réinitialise le niveau
                        self.state = "play"
                        # On passe en mode jeu
            if self.state == "menu":
                # Si on est dans l'écran de menu
                self.draw_menu()
                # On dessine le menu
            elif self.state == "play":
                # Si on est dans l'état de jeu
                self.update_game()
                # On met à jour la logique du jeu
                self.draw_game()
                # On dessine le jeu

            background_layers = [
                pygame.image.load("fond-d_ecran.png").convert(),
                pygame.image.load("meteorite.png").convert_alpha()
                    ]

            # Définir la vitesse de défilement pour chaque couche (plus le nombre est petit, plus c'est lent)
            speeds = [1, 2]

            # Position initiale de chaque couche (x, y)
            positions = [(0, 0) for _ in range(len(background_layers))]
            # Mettre à jour la position de chaque couche
            for i in range(len(background_layers)):
                x, y = positions[i]
                x -= speeds[i]  # Défilement vers la gauche (pour un défilement vers la droite, utilise x += speeds[i])

                # Si l'image est complètement sortie de l'écran, la replacer à droite
                if x <= -background_layers[i].get_width():
                    x = 0

                positions[i] = (x, y)

            # Dessiner chaque couche
            for i in range(len(background_layers)):
                # Dessiner l'image à sa position actuelle
                self.window.blit(background_layers[i], positions[i])
                # Dessiner une copie de l'image à droite pour un défilement continu
                self.window.blit(background_layers[i], (positions[i][0] + background_layers[i].get_width(), positions[i][1]))
            """# Charger l'image de fond
            background = pygame.image.load("fond-d_ecran.png").convert()
            self.window.blit(background, (0, 0))"""
            pygame.display.flip() #met à jour l'affichage
            self.clock.tick(60) #limite la boucle à 60 img/sec
        pygame.quit() #ferme pygame quand la boucle est terminée
    def draw_menu(self):
        # Dessine l'écran de menu
        self.window.fill((0, 0, 0))
        # Remplit l'écran de noir
        title = self.font_title.render("Mini Mario", True, (255, 255,
        255))
        # Crée le texte du titre en blanc
        text = self.font_text.render("Appuyez sur ENTREE pour jouer",
        True, (255, 255, 255))
        # Crée le texte d'instruction
        self.window.blit(title, (self.width // 2 - 180, self.height // 2 -
        120))
        # Dessine le titre
        self.window.blit(text, (self.width // 2 - 250, self.height // 2))
        # Dessine le texte d'instruction
    def update_game(self):
        # Met à jour la logique du jeu
        self.player.handle_input()
        # Le joueur gère le clavier
        self.player.apply_gravity(self.ground_y)
        # On applique la gravité et on gère le sol
        self.camera_x = self.player.x - self.width // 2
        # On centre la caméra sur le joueur
        if self.camera_x < 0:
            # On évite de trop aller à gauche
            self.camera_x = 0
            # On limite à 0
    def draw_game(self):
        # Dessine la scène de jeu
        self.window.fill((0, 0, 255))
        # On remplit l'écran de bleu (ciel)
        pygame.draw.rect(
        self.window,
        (139, 69, 19),
        (0 - self.camera_x, self.ground_y, 2000, self.height -
        self.ground_y)
        )
        # On dessine un long sol marron qui défile avec la caméra
        self.player.draw(self.window, self.camera_x)
        # On dessine le joueur


