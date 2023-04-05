from pygame.mixer import Sound


class SoundProcessor:
    def __init__(self):
        self.shoot_sound_effect = Sound("sounds/shoot.wav")
        self.ship_hit_sound_effect = Sound("sounds/ship_hit.wav")

    def play_shoot(self):
        self.shoot_sound_effect.play()

    def play_ship_hit(self):
        self.ship_hit_sound_effect.play()
