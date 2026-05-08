class Enemy:
    def __init__(self, hp, speed):
        self.hp = hp
        self.speed = speed
        self.pos = 0


class Tower:
    def __init__(self, position, range_, dps):
        self.position = position
        self.range = range_
        self.dps = dps


def simulate(enemy, towers):
    time_step = 0.1
    map_length = 100

    while True:
        # 敌人移动
        enemy.pos += enemy.speed * time_step

        # 塔攻击
        for t in towers:
            if abs(enemy.pos - t.position) <= t.range:
                enemy.hp -= t.dps * time_step

        # 判断胜负
        if enemy.hp <= 0:
            return True
        if enemy.pos >= map_length:
            return False


if __name__ == "__main__":
    enemy = Enemy(100, 2)

    towers = [
        Tower(30, 10, 5),
        Tower(60, 10, 5),
    ]

    result = simulate(enemy, towers)

    print("Win" if result else "Lose")