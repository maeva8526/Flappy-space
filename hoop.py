import pygame
# On importe pygame pour utiliser Rect et les fonctions de dessin
class Enemy:
    # Classe qui représente un ennemi simple
    def __init__(self, x, y, x_min, x_max):
        # Constructeur de l'ennemi
        self.width = 40
        # Largeur de l'ennemi
        self.height = 40
        # Hauteur de l'ennemi
        self.x = x
        # Position horizontale initiale de l'ennemi
        self.y = y
        # Position verticale de l'ennemi
        self.vx = 2
        # Vitesse horizontale de l'ennemi
        self.x_min = x_min
        # Limite minimale de déplacement
        self.x_max = x_max
        # Limite maximale de déplacement
        self.alive = True
        # Booleen pour savoir si l'ennemi est vivant
        self.color = (0, 255, 0)
        # Couleur de l'ennemi (vert)
    def update(self):
        # Met à jour la position de l'ennemi
        if self.alive:
            # On ne le bouge que s'il est vivant
            self.x += self.vx
            # On ajoute la vitesse à la position horizontale
        if self.x < self.x_min or self.x > self.x_max:
        # Si l'ennemi dépasse ses bornes
            self.vx = -self.vx
            # On inverse sa direction
    def get_rect(self):
        # Renvoie un rectangle de collision pour l'ennemi
        return pygame.Rect(self.x, self.y, self.width, self.height)
        # Le Rect utilise la position et la taille
    def draw(self, surface, camera_x):
        # Dessine l'ennemi sur la surface donnée
        if self.alive:
            # On ne dessine que s'il est vivant
            screen_x = self.x - camera_x
            # Position à l'écran en tenant compte de la caméra
            pygame.draw.rect(surface, self.color, (screen_x, self.y,
            self.width, self.height))
            # On dessine un rectangle vert