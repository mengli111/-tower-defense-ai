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


def simulate(enemies, towers):
    time_step = 0.1
    map_length = 100

    while True:
        all_dead = True

        # 敌人移动
        for e in enemies:
            if e.hp > 0:
                e.pos += e.speed * time_step
                all_dead = False

                if e.pos >= map_length:
                    return False  # 有敌人漏了

        # 塔攻击（关键逻辑）
        for t in towers:
            # 找范围内的敌人
            targets = [
                e for e in enemies
                if e.hp > 0 and abs(e.pos - t.position) <= t.range
            ]

            if targets:
                # 👉 先用最简单策略：打“最前面的敌人”
                target = max(targets, key=lambda e: e.pos)
                target.hp -= t.dps * time_step

        if all_dead:
            return True

def find_solution():
    positions = list(range(10, 100, 10))

    for p1 in positions:
        for p2 in positions:
            enemies = [
                Enemy(100, 2),
                Enemy(120, 1.5),
            ]

            towers = [
                Tower(p1, 10, 6),
                Tower(p2, 10, 6),
            ]

            if simulate(enemies, towers):
                print(f"Found solution: {p1}, {p2}")
                return

    print("No solution found")

if __name__ == "__main__":
    enemies = [
        Enemy(100, 2),
        Enemy(120, 1.5),
    ]

    towers = [
        Tower(30, 10, 6),
        Tower(60, 10, 6),
    ]

    result = simulate(enemies, towers)
    print("Win" if result else "Lose")