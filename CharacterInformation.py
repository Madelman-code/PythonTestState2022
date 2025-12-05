import Character

def main():
    hero_name = ""
    Hero_id = ""
    hero_hero_shift = 0
    hero_pay = 0.0

    boss_name= ''
    boss_id = ''
    boss_level = 0
    boss_hp = 0.0
    boss_attack_damage = 0.0
    boss_lifespan = 0.0

    print ('Hero Data Entry:')
    hero_name = input('Enter the hero name: ')
    hero_id = input('Enter the character ID number: ')
    hero_level = int(input('Enter the hero level: '))
    hero_loot = float(input('Enter the hero loot value: '))

    hero = Character.Hero(hero_name, hero_id, hero_level, hero_loot)

    print('\nBoss Data Entry:')
    boss_name = input('Enter the boss name: ')
    boss_id = input('Enter the character ID number: ')
    boss_level = int(input('Enter the boss level: '))
    boss_hp = float(input('Enter the boss HP value: '))
    boss_attack_damage = float(input('Enter the boss attack damage value: '))

    boss = Character.Boss(boss_name, boss_id, boss_level, boss_hp, boss_attack_damage)
    
    print('\nHero Information:')
    print(f'Name: {hero.get_name()}')
    print(f'ID: {hero.get_id()}')
    print(f'Level: {hero.get_level()}')
    print(f'Loot: ${hero.get_loot():.2f}')

    print('\nBoss Information:')
    print(f'Name: {boss.get_name()}')
    print(f'ID: {boss.get_id()}')
    print(f'Level: {boss.get_level()}')
    print(f'HP: {boss.get_hp()}')
    print(f'Attack Damage: {boss.get_attack_damage()}')
    print(f'Lifespan: {boss.get_lifespan():.2f} attacks')

if __name__ == "__main__":
    main()