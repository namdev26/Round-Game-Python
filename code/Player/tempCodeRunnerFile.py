
    def spawn_bullet(self, angle):
        Bullet((sprites.all_sprites, sprites.Bullet_sprites), self.rect.center, angle= angle, 
               homing= self.homing, explode= self.bullet_explode, speed= self.bullet_speed, size= self.bullet_size, 
               gravity= self.bullet_gravity, player = self, slow= self.bullet_slow, bounce_time= self.bullet_bounce, dmg= self.dmg)
    #move
    def move(self, dt):
        key = pygame.key.get_pressed()
        self.vel.x = (int(key[pygame.K_d]) - int(key[pygame.K_a])) * self.speed
        bam_tuong = False
        #di chuyen trai phai