inventory = {"laptop": 5, "mouse": 10, "keyboard": 0}
orders = [
    ("laptop", 2),
    ("mouse", 15),
    ("keyboard", 1),
    ("monitor", 3),
]

for product, qty in orders:
    match product:
        # ---------------- NOT IN INVENTORY ----------------
        case p if p not in inventory:
            print(f"{p}: not in inventory")

        # ---------------- ENOUGH STOCK ----------------
        case p if inventory[p] >= qty:
            inventory[p] -= qty
            print(f"{p}: shipped {qty}, {inventory[p]} left")

        # ---------------- NOT ENOUGH STOCK ----------------
        case p:
            stock = inventory[p]
            print(f"{p}: only {stock} in stock, cannot ship {qty}")
