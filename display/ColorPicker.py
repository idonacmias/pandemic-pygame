
import pygame

class ColorPicker:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rad = height // 2
        self.pwidth = width - self.rad * 2
        self.p = 0

    def get_color(self):
        color = pygame.Color(0)
        color.hsla = (int(self.p * self.pwidth), 100, 50, 100)
        return color

    def update(self):
        moude_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if moude_buttons[0] and self.rect.collidepoint(mouse_pos):
            self.p = (mouse_pos[0] - self.rect.left - self.rad) / self.pwidth
            self.p = (max(0, min(self.p, 1)))

    def draw(self, screen):
        self.draw_spectrum()
        screen.blit(self.image, self.rect)
        center = self.rect.left + self.rad + self.p * self.pwidth, self.rect.centery
        pygame.draw.circle(screen, self.get_color(), center, self.rect.height // 2)


    def draw_spectrum(self):
        for i in range(self.pwidth):
            color = pygame.Color(0)
            color.hsla = (int(360 * i / self.pwidth), 100, 50, 100)
            pygame.draw.rect(self.image, color, (i+self.rad, self.rect.height // 3, 1, self.rect.height - 2 * self.rect.height // 3))
        
