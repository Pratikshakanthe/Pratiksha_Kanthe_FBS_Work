##Calculate the cost of painting the following building’s walls (both interior andexterior). You need to accept area (one wall) and cost of both interior anexterior wall.
#(Note: 1. Below diagram is of two joint rooms.
#2. It is upper view of building.)


wall_area = float(input("Enter area of one wall : "))
interior_cost= float(input("Enter cost of painting interior wall : "))
exterior_cost = float(input("Enter cost of painting exterior wall : "))


total_walls = 8

total_interior_cost = total_walls * interior_cost * wall_area
total_exterior_cost = total_walls * exterior_cost * wall_area


print("Total cost to paint interior walls:" ,total_interior_cost)
print("Total cost to paint exterior walls:", total_exterior_cost)
print("Total painting cost:", total_interior_cost + total_exterior_cost)
