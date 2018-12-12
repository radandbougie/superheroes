import random

class Ability:
    def __init__(self, name, attack_strength):
        # example: Big Strength
        self.name = name
        # example: 300
        self.attack_strength = attack_strength
    def attack(self):
        min_attack = self.attack_strength // 2
        max_attack = self.attack_strength
        return random.randint(min_attack, max_attack)
    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength
        # Update attack value

class Weapon(Ability):
    def attack(self):
        print("Attacking with", self.name)
        return random.randint(0, self.attack_strength)

class Armor:
    def __init__(self, name, defense):
        # Instantiate name and defense strength
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


class Hero:
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        print("Hero Defending")
        armor = 0
        for item in self.armors:
            armor += item.defense
        return armor

    def take_damage(self, damage_amt):
        print("Hero taking damage", damage_amt)
        self.health -= damage_amt
        print(self.name, "has taken", damage_amt, "damage")
        if self.health <= 0:
            print(self.name, "has fallen!")
            self.deaths += 1
            print(self.deaths)

    def add_kill(self, num_kills):
        print("Hero adding kill")
        self.kills += num_kills

    def attack(self):
        print("Hero attacking")
        total_damage = 0
        for ability in self.abilities:
            print(self.name, "attacks with", ability.name, "!")
            total_damage += ability.attack()
        print(self.name, "does a total of", total_damage, "damage!")
        return total_damage

    def add_ability(self, ability_name, power):
        print("Adding ability", ability_name)
        ability = Ability(ability_name, power)
        self.abilities.append(ability)
        # Append ability to self.abilities

    def add_armor(self, armor):
        self.armors.append(armor)


class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()
        # self.deaths = 0

    def defend(self, damage):
        print("Defending against", damage)
        dps = damage / len(self.heroes)
        deaths = 0
        for hero in self.heroes:
            hero.health -= (dps - hero.defend())
            if hero.health <= 0:
                deaths += 1
        return deaths

    def attack(self, opposing_team):
        print(self.name, "attacking", opposing_team.name)
        if len(opposing_team.heroes) ==0:
            print("There are no heroes on the other team. You win I guess?")
            return 0
        total_damage = 0
        for hero in self.heroes:
            print(hero.name)
            total_damage += hero.attack()
        dps = total_damage / len(opposing_team.heroes)
        dps = 1000
        our_kills = 0
        for hero in opposing_team.heroes:
            hero.take_damage(dps)
            if hero.deaths > 0:
                our_kills += 1
        for hero in self.heroes:
            hero.kills += our_kills
        return total_damage

    def revive_heroes(self):
        print("Reviving heroes of", self.name)
        for hero in self.heroes:
            hero.health = 60

    def add_hero(self, hero):
        self.heroes.append(hero)
        print("\nHero added using team.add_hero():", self.heroes[-1].name)
        # print("\nnew hero list:", self.heroes)

    def remove_hero(self, name):
        print("attempting to remove hero:", name)
        if self.heroes == []:
            print("\nError: there are no heroes in this list")
            return 0
        for myhero in self.heroes:
            if myhero.name == name:
                print("\nfound hero to remove:", myhero.name)
                self.heroes.remove(myhero)
            else:
                print("hero not found")
                return 0

        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """

    def find_hero(self, name):
        print("looking for hero:", name)
        if self.heroes == []:
            print("\nError: there are no heroes in this list")
            return 0
        for myhero in self.heroes:
            if myhero.name == name:
                print("\nhero found:", myhero.name)
                return myhero
            else:
                print("\nhero not found")
                return 0
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """

    def view_all_heroes(self):
        print("\nAll the heroes of", self.name, ": ")
        for myhero in self.heroes:
            print(myhero.name)

class Arena:
    def __init__(self):
        self.team_one = Team("Red Team")
        self.team_two = Team("Blue Team")

    # i tried
    '''
    def build_team(self, team):
        team_name = "Generic Team"
        print("the team name is", team.name)
        team = Team(team_name)
        # add 3 heroes per team with one ability each
        # Making the user do this will be boring af but go off I guess
        for iter in range(1,4):
            print("Choose hero", str(iter))
            # make a hero
            hero_name = "hero" + str(iter)
            new_hero = Hero(hero_name)
            # make a new ability
            new_ability = "ability" + str(iter)
            new_ability_power = 100
            # give new ability to the new hero
            new_hero.add_ability(new_ability, new_ability_power)
            print("Your new hero,", new_hero.name, "has an ability called", new_hero.abilities[0].name, "which has a power level of", new_hero.abilities[0].attack_strength)
            # add new hero to the team
            team.add_hero(new_hero)
        print(team.name)
        '''

    def build_team_one(self):
        hero1 = Hero(input("Name a hero > "))
        hero1.add_ability(input("Name an ability > "), random.randint(1, 5) * 10)
        hero1.add_ability(input("Name another ability > "), random.randint(1, 5) * 10)

        hero2 = Hero(input("Name a hero > "))
        hero2.add_ability(input("Name an ability > "), random.randint(1, 5) * 10)
        hero2.add_ability(input("Name another ability > "), random.randint(1, 5) * 10)

        self.team_one = Team(input("Name this new team > "))
        self.team_one.add_hero(hero1)
        self.team_one.add_hero(hero2)

    def build_team_two(self):
        # why do these have to be different functions that makes no sense
        hero1 = Hero(input("Name a hero > "))
        hero1.add_ability(input("Name an ability > "), random.randint(1, 5) * 10)
        hero1.add_ability(input("Name another ability > "), random.randint(1, 5) * 10)

        hero2 = Hero(input("Name a hero > "))
        hero2.add_ability(input("Name an ability > "), random.randint(1, 5) * 10)
        hero2.add_ability(input("Name another ability > "), random.randint(1, 5) * 10)

        self.team_two = Team(input("Name this new team > "))
        self.team_two.add_hero(hero1)
        self.team_two.add_hero(hero2)

        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)

    def show_stats(self):
        print("Looks like the battle is over.")
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """

arena = Arena()
arena.build_team_one()
arena.build_team_two()

def game_loop(arena):
	arena.team_battle()
	arena.show_stats()
	arena.play_again()

if __name__ == "__main__":
    game_loop(arena)

'''
    # the actual function
def build_team(self, team):
    team_name = input("Player 1: name your team > ")
    team = Team(team_name)
    # add 3 heroes per team with one ability each
    # Making the user do this will be boring af but go off I guess
    for iter in range(1,3):
        print("Choose hero", iter)
        # make a hero
        hero_name = input("Name a hero: > ")
        new_hero = Hero(hero_name)
        # add new hero to the team
        team.add_hero(new_hero)
        # make a new ability
        new_ability = input("Name an ability: > ")
        new_ability_power = input("How strong is this ability? > ")
        # give new ability to the new hero
        new_hero.add_ability(new_ability, new_ability_power)
        print("Your new hero,", new_hero.name, "has an ability called", new_hero.abilities[0].name, "which has a power level of", new_hero.abilities[0].attack_strength)
'''
