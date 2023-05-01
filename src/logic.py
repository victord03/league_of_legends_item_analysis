
def has_got_a_mythic(item: dict) -> bool:
    if item.get("Mythic Passive"):
        return True
    else:
        return False

def give_number_of_passives(item: dict) -> int:
    return len(list(item["Passives"].keys()))

def calculate_worth_of_raw_stats(item: dict, stats_cost: dict) -> float:

    stats = item["Raw Stats"]
    total_worth_of_stats = 0

    for stat_name, stat_amount in stats.items():
        total_worth_of_stats += round(stat_amount * stats_cost[stat_name], 2)

    return total_worth_of_stats
