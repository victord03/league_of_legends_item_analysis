
trinity_force = {
    "Name": "Trinity Force",
    "Cost": 3_333,
    "Raw Stats": {
        "Attack Damage": 35,
        "Attack Speed": 30,
        "Health": 300,
        "Ability Haste": 20,
    },
    "Mythic Passive": {
        "Effect": "Grants legendary items Attack Damage, Ability Haste, Movement Speed.",
    },
    "Passives": {
        "Threefold Strike": {
            "Unique": True,
            "Effect": "Attacks grant Movement Speed. If the target is an enemy champion, increase your base Attack Damage.",
            "Stacking": True
        },
        "Spellblade": {
            "Unique": True,
            "Effect": "After using an ability, your next Attack is enhanced with additional damage",
            "Stacking": False
        }
    },
}

dead_mans_place = {
    "Name": "Dead Man's Plate",
    "Cost": 2_900,
    "Raw Stats": {
        "Health": 300,
        "Armor": 45,
        "Movement Speed": 5,
    },
    "Passives": {
        "Shipwrecker": {
            "Unique": True,
            "Effect": "While moving, build up Movement Speed. Your next attack discharges built up Movement Speed to deal damage. If dealt by a melee champion at top speed, the attack also Slows the target",
            "Stacking": False
        },
    },
}
