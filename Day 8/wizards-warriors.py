from abc import ABC, abstractmethod


# Base class for all characters
class Character(ABC):
    @abstractmethod
    def __str__(self):
        pass

    def vulnerable(self):
        return False


# Warrior class inheriting from Character
class Warrior(Character):
    def __str__(self):
        return "Character is a Warrior"

    def vulnerable(self):
        return super().vulnerable()

    def damage_points(self, target):
        if target.vulnerable():
            return 10
        return 6


# Wizard class inheriting from Character
class Wizard(Character):
    def __init__(self):
        self.spell_prepared = False

    def __str__(self):
        return "Character is a Wizard"

    def prepare_spell(self):
        self.spell_prepared = True

    def vulnerable(self):
        return not self.spell_prepared

    def damage_points(self):
        if self.spell_prepared:
            self.spell_prepared = False
            return 12
        return 3


# usage:
if __name__ == "__main__":
    # 1: Describe a character
    warrior = Warrior()
    print(warrior)  # Output: "Character is a Warrior"

    # 2: Make characters not vulnerable by default
    print(f"is Warrior vulnerable: {warrior.vulnerable()}")  # Output: False

    # 3: Allow Wizards to prepare a spell
    wizard = Wizard()
    print(
        f"is Wizard vulnerable: {wizard.vulnerable()}"
    )  # Output: isWizard vulnerable: False (wizard.vulnerable())
    wizard.prepare_spell()

    # 4: Make Wizards vulnerable when not having prepared a spell
    print(f"is Wizard vulnerable: {wizard.vulnerable()}")  # Output: False

    # 5: Calculate the damage points for a Wizard
    wizard.prepare_spell()
    print(wizard.damage_points())  # Output: 12

    # 6: Calculate the damage points for a Warrior
    warrior = Warrior()
    warrior2 = Warrior()
    print("Warrior attacks wizard", warrior.damage_points(wizard))

    wizard2 = Wizard()

    print("Warrior attacks warrior", warrior.damage_points(warrior2))

    print("Wizard attacks wizard", wizard.damage_points(wizard2))
