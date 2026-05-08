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
                #print(f"pos={enemy.pos:.2f}, hp={enemy.hp:.2f}")

        # 判断胜负
        if enemy.hp <= 0:
            return True
        if enemy.pos >= map_length:
            return False

def find_best_solution():

    positions = list(range(10, 100, 10))

    best = None

    for p1 in positions:

        for p2 in positions:

            enemy = Enemy(100, 2)

            towers = [

                Tower(p1, 10, 5),

                Tower(p2, 10, 5),

            ]

            if simulate(enemy, towers):

                score = p1 + p2  # 越靠前越好（你可以改）

                if best is None or score < best[0]:

                    best = (score, p1, p2)

    if best:

        print(f"Best solution: {best[1]}, {best[2]}")

    else:

        print("No solution")

if __name__ == "__main__":
    find_best_solution()
    enemy = Enemy(100, 2)

    towers = [
        Tower(30, 10, 6),
        Tower(60, 10, 6),
    ]

    result = simulate(enemy, towers)

    print("Win" if result else "Lose")