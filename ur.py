import pygame 
import math 
import datetime  

# Initialisering af Pygame og skærmstørrelse
pygame.init()
WIDTH = 400
HEIGHT = 400             
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analogt ur")

# Laver farver i RGB-format - farvernes navne gør koden let at læse og ændre senere
WHITE = (255, 255, 255)                  
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Definerer urets midtpunkt og radius for urskiven
CENTER = (WIDTH // 2, HEIGHT // 2)        # Finder midten af skærmen
RADIUS = 150                              # Radius som gør det nemt at justere urets størrelse

# Funktion til at tegne timerne på urskiven
def draw_hour_marks():
    for hour in range(12):               
        angle = math.radians((hour / 12) * 360 - 90)  # Beregning af vinklen for hver time
        x = CENTER[0] + RADIUS * math.cos(angle)      # X-koordinat baseret på radius og vinkel
        y = CENTER[1] + RADIUS * math.sin(angle)      # Y-koordinat baseret på radius og vinkel
        pygame.draw.circle(screen, BLACK, (int(x), int(y)), 5) # Tegner små cirkler som markeringer for tiden

# Funktion til at tegne visere (time, minut, sekund) på urskiven
def draw_hand(length, angle, color, width=3):
    angle = math.radians(angle - 90)      
    x = CENTER[0] + length * math.cos(angle)          # X-koordinat baseret på vinkel og længde af viseren
    y = CENTER[1] + length * math.sin(angle)          # Y-koordinat baseret på vinkel og længde af viseren
    pygame.draw.line(screen, color, CENTER, (int(x), int(y)), width) # Tegner viseren fra centrum til slutpunktet

running = True
while running:
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            running = False

    # Henter den nuværende tid
    now = datetime.datetime.now()          # Bruger datetime til at hente timer, minutter, sekunder
    hour = now.hour % 12                   # Justerer timerne til 12-timers format
    minute = now.minute                    # Minutter nu
    second = now.second                    # Sekunder nu

    # Beregner vinklen for hver viser
    hour_angle = (hour + minute / 60) * 30   # Timevinkel baseret på 12 timer = 360 grader (30 grader per time)
    minute_angle = (minute + second / 60) * 6 # Minutvinkel, 60 minutter = 360 grader (6 grader per minut)
    second_angle = second * 6                 # Sekundvinkel, 60 sekunder = 360 grader (6 grader per sekund)

    # Tegner baggrunden og urskiven
    screen.fill(WHITE)                      
    pygame.draw.circle(screen, BLACK, CENTER, RADIUS + 10, 2) # Tegner urskiven

    # Tegner time-markeringer
    draw_hour_marks()

    # Tegner hver af viserne for timer, minutter og sekunder
    draw_hand(RADIUS - 50, hour_angle, BLACK, 6)  # Timeviseren, kortere og tykkere
    draw_hand(RADIUS - 30, minute_angle, BLUE, 4) # Minutviseren, længere og lidt tyndere
    draw_hand(RADIUS - 20, second_angle, RED, 2)  # Sekundviseren, længst og tyndest

    # Opdaterer skærmen for at vise den aktuelle tid
    pygame.display.flip()                   
    

# Afslutter Pygame, når programmet lukkes
pygame.quit()
