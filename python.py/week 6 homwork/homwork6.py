high_score_board = []

def record_game(player, *scores, bonus=0, multiplier=1.0):
    if len(scores) == 0:
        return (player, 0, 0, "no rounds played")
    if any(s < 0 for s in scores):
        return (player, 0, 0, "negative score not allowed")

    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)

    high_score_board.append((player, total))
    sorted_board = sorted(high_score_board, key=lambda x: x[1], reverse=True)
    rank = sorted_board.index((player, total)) + 1

    status = "high score!" if rank == 1 else f"rank {rank}"
    return (player, rounds, total, status)


print(record_game("Alice", 10, 20, 15, bonus=5, multiplier=1.2))
print(record_game("Bob", 5, 7, 9, 12))
print(record_game("Charlie", 30, 10, bonus=10))
print(record_game("David", -5, 10))
print(record_game("Eve"))

print(high_score_board)
