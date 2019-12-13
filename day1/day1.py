def mass_to_fuel(mass):
    return int(mass / 3) - 2


def fuel_to_fuel(mass):
    if mass <= 8:
        return 0
    else:
        return mass_to_fuel(mass) + fuel_to_fuel(mass_to_fuel(mass))


total = 0
for line in open('input', 'r'):
    fuel = mass_to_fuel(int(line))
    total += fuel + fuel_to_fuel(fuel)

print(total)
