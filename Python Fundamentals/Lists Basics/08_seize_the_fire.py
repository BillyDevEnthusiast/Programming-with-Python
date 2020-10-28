fire_rate = input().split("#")
water_amount = int(input())

effort_level = 0
total_fire = 0
cells = []
print("Cells:")
for fire in fire_rate:
    if water_amount <= 0:
        break
    fire_data = fire.split(" = ")
    fire_name = fire_data[0]
    fire_level = int(fire_data[1])
    if fire_name == "High":
        if 81 <= fire_level <= 125:
            if water_amount >= fire_level:
                water_amount -= fire_level
                effort_level += fire_level * 0.25
                total_fire += fire_level
                print(f" - {fire_level}")
        else:
            continue
    elif fire_name == "Medium":
        if 51 <= fire_level <= 80:
            if water_amount >= fire_level:
                water_amount -= fire_level
                effort_level += fire_level * 0.25
                total_fire += fire_level
                print(f" - {fire_level}")
        else:
            continue
    else:
        if 1 <= fire_level <= 50:
            if water_amount >= fire_level:
                water_amount -= fire_level
                effort_level += fire_level * 0.25
                total_fire += fire_level
                print(f" - {fire_level}")
        else:
            continue
print(f"Effort: {effort_level:.2f}")
print(f"Total Fire: {total_fire}")
