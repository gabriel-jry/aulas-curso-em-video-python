import pygame

caminho = r'C:\Users\gabri\Desktop\Estudos\Python\Curso em video\ex021.mp3'

pygame.init()
pygame.mixer.music.load(caminho)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(30)

pygame.quit()
