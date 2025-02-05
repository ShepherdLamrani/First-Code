weight = 41.5
cost_ground_premium = 125
# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight <=10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Ground Shipping Cost: $", cost_ground)
print("Ground Shipping Premium $", cost_ground_premium)

# Drone Shipping
if weight <= 2:
  drone_ground = weight * 4.5 + 0
elif weight <= 6:
  drone_ground = weight * 9.00 + 0
elif weight <=10:
  drone_ground = weight * 12.00 + 0
else:
  drone_ground = weight * 14.25 + 0
print("Drone Shipping Cost: $", drone_ground)