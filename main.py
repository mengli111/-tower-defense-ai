class Enemy:
    def __init__(self, hp, speed):
        self.hp = hp
        self.speed = speed
        self.pos = 0
        self.blocked = False   # 是否被挡住


class Tower:
    def __init__(self, position, range_, dps, block=0):
        self.position = position
        self.range = range_
        self.dps = dps
        self.block = block   # 能挡几个敌人（0=远程，1=近战）


def simulate(enemies, towers):
    time_step = 0.1
    map_length = 100

    while True:
        all_dead = True

        # =====================
        # 1. 敌人先移动
        # =====================
        for e in enemies:
            print([round(e.pos,1) for e in enemies])
            if e.hp > 0:
                e.pos += e.speed * time_step
                all_dead = False

                if e.pos >= map_length:
                    return False

        # =====================
        # 2. 处理阻挡（关键修复）
        # =====================
        for t in towers:
            if t.block > 0:
                targets = [
                    e for e in enemies
                    if e.hp > 0 and abs(e.pos - t.position) <= 2
                ]

                targets.sort(key=lambda e: -e.pos)

                for e in targets[:t.block]:
                    # 👉 拉回到塔前（关键）
                    e.pos = min(e.pos, t.position)
                    e.blocked = True

        # =====================
        # 3. 塔攻击
        # =====================
        for t in towers:
            if t.dps > 0:
                targets = [
                    e for e in enemies
                    if e.hp > 0 and abs(e.pos - t.position) <= t.range
                ]

                if targets:
                    target = max(targets, key=lambda e: e.pos)
                    target.hp -= t.dps * time_step

        if all_dead:
            return True

def find_solution():
    positions = list(range(20, 90, 10))

    for p_block in positions:
        for p_dps1 in positions:
            for p_dps2 in positions:

                enemies = [
                    Enemy(100, 2),
                    Enemy(100, 2),
                ]

                towers = [
                    Tower(p_block, 1, 0, block=1),
                    Tower(p_dps1, 10, 5),
                    Tower(p_dps2, 10, 5),
                ]

                if simulate(enemies, towers):
                    print("Found:", p_block, p_dps1, p_dps2)
                    return

    print("No solution")

if __name__ == "__main__":
    enemies = [
        Enemy(100, 2),
        Enemy(100, 2),
    ]

    towers = [
        Tower(50, 1, 0, block=1),   # 近战（挡人）
        Tower(40, 10, 5),           # 输出塔
        Tower(60, 10, 5),
    ]

    result = simulate(enemies, towers)
    print("Win" if result else "Lose")