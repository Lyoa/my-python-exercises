class Hero:
    def __init__(self):
        self._name = "Duelle"
        self._max_health = 1000
        self._current_health = self._max_health
        self._attack_power = 50

    @property
    def name(self):
        return self._name

    @property
    def max_health(self):
        return self._max_health

    @property
    def current_health(self):
        return self._current_health

    @current_health.setter
    def current_health(self, value):
        if value < 0:
            self._current_health = 0
        else:
            self._current_health = value

    @property
    def attack_power(self):
        return self._attack_power

class Monster:
    def __init__(self, name, max_health, attack_power, hero):
        self.name = name
        self.max_health = max_health
        self._current_health = max_health
        self._attack_power = attack_power
        self.hero = hero

    @property
    def current_health(self):
        return self._current_health

    @current_health.setter
    def current_health(self, value):
        if value < 0:
            self._current_health = 0
        else:
            self._current_health = value

    @property
    def attack_power(self):
        return self._attack_power

    def attack(self):
        self.hero.current_health -= self.attack_power
        return self.hero.current_health

    def defend(self):
        self.current_health -= self.hero.attack_power * 0.1
        if self.current_health <0:
            self.current_health = 0
        return self.current_health
