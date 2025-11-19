import pygame


class Player: # Classe qui représente le joueur contrôlé par l'utilisateur
    def __init__(self, x, y): # Constructeur : x et y sont la position initiale du joueur
        self.width = 40 # Largeur du joueur
        self.height = 60 # Hauteur du joueur
        self.x = x # Position horizontale du joueur
        self.y = y # Position verticale du joueur
        self.vy = 0 # Vitesse verticale (pour gérer le saut et la gravité)
        self.speed_x = 5 # Vitesse de déplacement horizontal
        self.jump_speed = -18 # Vitesse verticale vers le haut lors du saut
        self.gravity = 1 # Intensité de la gravité
        self.on_ground = True # Indique si le joueur est sur le sol (True au départ)
        self.color = (255, 0, 0) # Couleur rouge pour dessiner le joueur
   
    def handle_input(self): # Gère les entrées clavier pour déplacer le joueur
        keys = pygame.key.get_pressed() # Récupère l'état de toutes les touches du clavier
        if keys[pygame.K_LEFT]: # Si la flèche gauche est enfoncée
            self.x -= self.speed_x # On se déplace vers la gauche
        if keys[pygame.K_RIGHT]: # Si la flèche droite est enfoncée
            self.x += self.speed_x # On se déplace vers la droite
   
    def apply_gravity(self, ground_y): # Applique la gravité et gère la collision avec le sol
        self.vy += self.gravity # On ajoute la gravité à la vitesse verticale
        self.y += self.vy # On met à jour la position verticale
        if self.y + self.height >= ground_y: # Si le bas du joueur passe sous le sol
            self.y = ground_y - self.height # On replace le joueur juste sur le sol
            self.vy = 0 # On annule la vitesse verticale
            self.on_ground = True # On indique qu'il est au sol
        else:
            self.on_ground = False # Sinon, il est en l'air
   
    def jump(self):
 # Fait sauter le joueur si il est au sol
        if self.on_ground: # On ne saute que si on est au sol
            self.vy = self.jump_speed # On donne une vitesse vers le haut
            self.on_ground = False # On indique qu'il n'est plus au sol
   
    def get_rect(self): # Renvoie un rectangle Pygame pour gérer les collisions
        return pygame.Rect(self.x, self.y, self.width, self.height) # Le rectangle est défini par la position et la taille du joueur
   
    def draw(self, surface, camera_x): # Dessine le joueur sur la surface donnée, avec la caméra
        screen_x = self.x - camera_x # Position horizontale à l'écran (on enlève camera_x)
        pygame.draw.rect(surface, self.color, (screen_x, self.y,self.width, self.height)) # On dessine un rectangle rouge pour représenter le joueur

