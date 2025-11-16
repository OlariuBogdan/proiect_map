# --- 1. Importuri ---
from machine import Machine
from settings import *
import ctypes, pygame, sys

# --- 2. Setare Specifică Windows ---
ctypes.windll.user32.SetProcessDPIAware()

# --- 3. Clasa Principală a Jocului ---
class Game:
    def __init__(self):
        """
        Constructorul clasei (rulează o singură dată la început).
        Setează fereastra, încarcă resursele și inițializează obiectele.
        """

        # --- 3a. Inițializare Pygame și Fereastră ---
        pygame.init()
        
        # --- MODIFICARE CHEIE (Doar această linie este schimbată) ---
        # Folosim flag-urile FULLSCREEN și SCALED.
        # 'SCALED' va lua fereastra ta de 1600x1000 și o va întinde
        # pentru a umple monitorul, scalând automat și simbolurile.
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
        
        pygame.display.set_caption('Slot Machine Demo')
        self.clock = pygame.time.Clock()

        # --- 3b. Încărcare Resurse Grafice ---
        self.bg_image = pygame.image.load(BG_IMAGE_PATH).convert_alpha()
        self.grid_image = pygame.image.load(GRID_IMAGE_PATH).convert_alpha()

        # --- 3c. Inițializare Obiecte de Joc (Concept MAP: Compoziție) ---
        self.machine = Machine()
        self.delta_time = 0

        # --- 3d. Sunet ---
        main_sound = pygame.mixer.Sound('audio/track.mp3')
        main_sound.play(loops = -1)

    def run(self):
        """
        Bucla Principală a Jocului (Game Loop).
        """
        self.start_time = pygame.time.get_ticks()

        while True:
            
            # --- 4. Gestionarea Evenimentelor (Input) ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # (Opțional) Adaugă această linie dacă vrei să ieși cu ESCAPE
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # --- 5. Calcularea Delta Time ---
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            # --- 6. Logica de Desenare (Render) și Actualizare (Update) ---
            
            # Ordinea ta originală de desenare
            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            
            # Aici se întâmplă TOATĂ logica jocului (inclusiv input-ul tău!)
            self.machine.update(self.delta_time)
            
            self.screen.blit(self.grid_image, (0, 0))
            self.clock.tick(FPS)

# --- 7. Punctul de Start (Entry Point) ---
if __name__ == '__main__':
    game = Game()
    game.run()