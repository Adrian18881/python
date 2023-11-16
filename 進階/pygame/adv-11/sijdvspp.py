class Player:
    def __init__(self, name, health, attack, defense):
        #初始化設定
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        #self 的意思是創造一個屬於自己的變數

    def take_damage(self, damage):
        #受到傷害
        if damage > self.defense:
            self.health -= damage - self.defense #受到傷害 = 傷害 - 防禦
        return f"{self.name}受到了{damage}店傷害!!"
    
class Mage(Player):
    def __init__(self, name, health, attack, defense, magic_power):
        #初始化法師
        super(). __init__(name, health, attack, defense)
        self.magic_power = magic_power

    def cast_spell(self):
        #施放魔法
        self.magic_power -= 10#消耗魔力，施放魔法攻擊
        return self.attack + self.magic_power


class Warrior(Player):
    def __init__(self, name, health, attack, defense, armor):
        #初始化法師
        super(). __init__(name, health, attack, defense)
        self.armor = armor    

    def use_armor(self):
        self.health += self.armor


player1 = Warrior("戰士小明", 100, 15, 10, 5)
player2 = Mage("法師曉華", 80, 10, 5, 20)

print(f"{player1.name} 血量剩餘: {player1.health}")
print(player1.use_armor())
print(f"{player1.name} 血量剩餘: {player1.health}")

print(f"{player2.name}目前魔力: {player2.magic_power}")
player1.take_damage(player2.cast_spell())
print(f"{player2.name}對{player1.name}施放魔法攻擊")
print(f"{player2.name}目前魔力:{player2.magic_power}")
print(f"{player1.name}血量剩餘:{player1.health}")

    

    
#新增一個玩家
player1 = Player("你在哈囉", 100, 100, 9)
print(f"玩家名稱: {player1.name}")
print(f"玩家血量: {player1.health}")
print(f"玩家攻擊: {player1.attack}")
print(f"玩家防禦: {player1.defense}")

player2 = Player("你好", 50, 10, 5)
print(f"玩家名稱: {player2.name}")
print(f"玩家血量: {player2.health}")
print(f"玩家攻擊: {player2.attack}")
print(f"玩家防禦: {player2.defense}")

#玩家1 攻擊 玩家2
print(player2.take_damage(player1.attack))
print(f"玩家2血量剩餘: {player2.health}")

