import pygame

class Player:
    def __init__(self, x, y, image_path):
        # Charger l'image de la soucoupe
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect(center=(x, y))

        self.height = 60
        self.can_jump = True

        # Physique
        self.vy = 0                 # vitesse verticale
        self.gravity = 0.3          # gravité
        self.jump_strength = -7     # saut

    """def jump(self):
        #Lancer un saut vers le haut.
        self.vy = self.jump_strength"""
    def jump(self):
        if self.can_jump:
            self.vy = self.jump_strength


    def update(self):
        """Mettre à jour la position du joueur."""
        self.vy += self.gravity
        self.rect.y += self.vy

    def draw(self, window):
        """Dessin de la soucoupe dans la fenêtre."""
        window.blit(self.image, self.rect)

    """def apply_gravity(self, ground_y):
        # Applique la gravité et gère la collision avec le sol
        self.vy += self.gravity
        # On ajoute la gravité à la vitesse verticale
        self.rect.y += self.vy
        # On met à jour la position verticale
        # Limite sol
        if self.rect.bottom + self.height >= ground_y:
            self.rect.bottom = ground_y - self.height
            self.vy = 0

        # Limite plafond
        if self.rect.top <= 0:
            self.rect.top = 0
            self.vy = 0"""
    def apply_gravity(self, ground_y):
        # Gravité
        self.vy += self.gravity
        self.rect.y += self.vy

        # ---- SOL ----
        if self.rect.bottom + self.height >= ground_y:
            self.rect.bottom = ground_y - self.height
            self.vy = 0
            self.can_jump = False  # ❌ pas de saut au sol

        # ---- PLAFOND ----
        elif self.rect.top <= 0:
            self.rect.top = 0
            self.vy = 0
            self.can_jump = False  # ❌ pas de saut au plafond

        else:
            # Dans les airs → peut sauter uniquement si vitesse < 0 (pendant un vrai saut)
            self.can_jump = True

