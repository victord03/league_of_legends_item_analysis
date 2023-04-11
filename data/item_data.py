

hp = {"Name": "Health", "Cost": 400, "Amount": 150, "Value type": "Flat"}
hp_regen = {"Name": "Health Regen", "Cost": 300, "Amount": 100, "Value type": "Percentage"}
mana = {"Name": "Mana", "Cost": 350, "Amount": 250, "Value type": "Flat"}
mana_regen = {"Name": "Mana Regen", "Cost": 250, "Amount": 50, "Value type": "Percentage"}
armor = {"Name": "Armor", "Cost": 300, "Amount": 15, "Value type": "Flat"}
mr = {"Name": "Magic Resistance", "Cost": 450, "Amount": 25, "Value type": "Flat"}
attack = {"Name": "Attack Damage", "Cost": 350, "Amount": 10, "Value type": "Flat"}
ap = {"Name": "AP", "Cost": 435, "Amount": 20, "Value type": "Flat"}
mov_sp = {"Name": "Movement Speed", "Cost": 300, "Amount": 25, "Value type": "Flat"}
att_sp = {"Name": "Attack Speed", "Cost": 300, "Amount": 12, "Value type": "Percentage"}
crit_chance = {"Name": "Critical Chance", "Cost": 600, "Amount": 15, "Value type": "Percentage"}


raw_data_flat = {
    "Hp Regen": {"Cost": 300, "Amount": 100, "Value type": "Percentage"},
    "Hp": {"Cost": 400, "Amount": 150, "Value type": "Flat"},

    "Mana Regen": {"Cost": 250, "Amount": 50, "Value type": "Percentage"},
    "Mana": {"Cost": 350, "Amount": 250, "Value type": "Flat"},

    "Attack": {"Cost": 350, "Amount": 10, "Value type": "Flat"},

    "Ap": {"Cost": 435, "Amount": 20, "Value type": "Flat"},

    "Armor": {"Cost": 300, "Amount": 15, "Value type": "Flat"},
    "Mr": {"Cost": 450, "Amount": 25, "Value type": "Flat"},

    "Movement Speed": {"Cost": 300, "Amount": 25, "Value type": "Flat"},
}

raw_data_percent = {
    "Attack Speed": {"Cost": 300, "Amount": 12, "Value type": "Percentage"},
    "Critical Strike": {"Cost": 600, "Amount": 15, "Value type": "Percentage"},
}
