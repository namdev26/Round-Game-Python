List_of_skills = []

def Barrage(player):
    player.bullet_per_shoot += 4
    player.max_ammo += 5
    player.dmg_scale -= 0.7
    player.reload = 250
List_of_skills.append(Barrage)