def take_magic_damage(health, resist, amp, spell_power):
    totalDmg = spell_power * amp
    actualDmg = totalDmg - resist
    return health - actualDmg
    pass
