weight = 0.7

# Ground Shipping
cost_ground = 20
if weight <= 2:
    cost_ground += 1.5 * weight
elif weight <= 6:
    cost_ground += 3 * weight
elif weight <= 10:
    cost_ground += 4 * weight
else:
    cost_ground += 4.75 * weight
print("Ground Shipping:", cost_ground)

# Premium Ground Shipping
cost_premium = 125.0
print("Premium Ground Shipping:", cost_premium)

# Drone Shipping

if weight <= 2:
    cost_drone = 4.5 * weight
elif weight <= 6:
    cost_drone = 9 * weight
elif weight <= 10:
    cost_drone = 12 * weight
else:
    cost_drone = 14.25 * weight

print("Drone Shipping:", cost_drone)

# Ground Shipping is the cheapest for a
# 4.8 pound package at $34.40

# Premium Ground Shipping is the cheapest
# for a 41.5 pound package at $125.00
