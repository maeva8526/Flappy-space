import pygame# On importe pygame pour utiliser Rect et les fonctions de dessin


class Enemy:# Classe qui représente un ennemi simple
   
    def __init__(self, x, y, x_min, x_max):# Constructeur de l'ennemi
        self.width = 40# Largeur de l'ennemi
        self.height = 40# Hauteur de l'ennemi
        self.x = x# Position horizontale initiale de l'ennemi
        self.y = y# Position verticale de l'ennemi
        self.vx = 2# Vitesse horizontale de l'ennemi
        self.x_min = x_min# Limite minimale de déplacement
        self.x_max = x_max# Limite maximale de déplacement
        self.alive = True# Booleen pour savoir si l'ennemi est vivant
        self.color = (0, 255, 0)# Couleur de l'ennemi (vert)
   
    def update(self):# Met à jour la position de l'ennemi
        if self.alive: # On ne le bouge que s'il est vivant
            self.x += self.vx # On ajoute la vitesse à la position horizontale
        if self.x < self.x_min or self.x > self.x_max: # Si l'ennemi dépasse ses bornes
            self.vx = -self.vx # On inverse sa direction
   
    def get_rect(self): # Renvoie un rectangle de collision pour l'ennemi
        return pygame.Rect(self.x, self.y, self.width, self.height) # Le Rect utilise la position et la taille
   
    def draw(self, surface, camera_x): # Dessine l'ennemi sur la surface donnée
        if self.alive: # On ne dessine que s'il est vivant
            screen_x = self.x - camera_x # Position à l'écran en tenant compte de la caméra
            pygame.draw.rect(surface, self.color, (screen_x, self.y, self.width, self.height)) # On dessine un rectangle vert


   
    def update_game(self): # Met à jour la logique du jeu
        self.player.handle_input() # Gestion des déplacements gauche/droite
        keys = pygame.key.get_pressed() # Lecture du clavier
       
        if keys[pygame.K_SPACE]: # Si la barre d'espace est enfoncée
            self.player.jump() # On fait sauter le joueur
        self.player.apply_gravity(self.ground_y) # Gravité et sol pour le joueur
        self.enemy.update() # Mise à jour de l'ennemi
        player_rect = self.player.get_rect() # Rectangle du joueur
        enemy_rect = self.enemy.get_rect() if self.enemy.alive else None # Rectangle de l'ennemi s'il est vivant
       
        if self.enemy.alive and player_rect.colliderect(enemy_rect): # Si l'ennemi est vivant et que le joueur le touche
            if self.player.vy > 0 and player_rect.bottom <= enemy_rect.top+ 10: # Si le joueur tombe et arrive par dessus
                self.enemy.alive = False # L'ennemi meurt
                self.player.vy = self.player.jump_speed // 2 # Petit rebond du joueur
            else:
                self.state = "menu" # Sinon, on considère que le joueur est mort → retour menu
            self.camera_x = self.player.x - self.width // 2 # Caméra centrée sur le joueur
            if self.camera_x < 0: # On évite de voir avant le début du niveau
                self.camera_x = 0 # On limite à 0
