cars_number = int(input())

cars_total = {}

for car in range(cars_number):
    cars = input().split("|")
    model = cars[0]
    mileage = int(cars[1])
    fuel = int(cars[2])

    if model not in cars_total:
        cars_total[model] = []
    cars_total[model].append(mileage)
    cars_total[model].append(fuel)

command_list = input()
while command_list != "Stop":
    command_list = command_list.split(" : ")
    command = command_list[0]
    model_car = command_list[1]

    if command == "Drive":
        distance = int(command_list[2])
        fuel_car = int(command_list[3])

        if cars_total[model_car][1] < fuel_car:
            print("Not enough fuel to make that ride")
            command_list = input()
            continue
        else:
            cars_total[model_car][1] -= fuel_car
            cars_total[model_car][0] += distance
        print(f"{model_car} driven for {distance} kilometers. {fuel_car} liters of fuel consumed.")

        if cars_total[model_car][0] >= 100000:
            print(f"Time to sell the {model_car}!")
            cars_total.pop(model_car)

    elif command == "Refuel":
        fuel_car = int(command_list[2])
        if cars_total[model_car][1] < 75:
            old_fuel = cars_total[model_car][1]
            cars_total[model_car][1] += fuel_car
            refueled_with = fuel_car

            if cars_total[model_car][1] > 75:
                cars_total[model_car][1] = 75
                refueled_with = 75 - old_fuel

            print(f"{model_car} refueled with {refueled_with} liters")


    elif command == "Revert":
        kilometres = int(command_list[2])
        cars_total[model_car][0] -= kilometres

        if cars_total[model_car][0] < 10000:
            cars_total[model_car][0] = 10000
            command_list = input()
            continue
        else:
            print(f"{model_car} mileage decreased by {kilometres} kilometers")

    command_list = input()

new_dict_cars = sorted(cars_total.items(), key=lambda x: x[1], reverse=True)
new_dict_cars = dict(new_dict_cars)
for car in new_dict_cars:
    print(f"{car} -> Mileage: {cars_total[car][0]} kms, Fuel in the tank: {cars_total[car][1]} lt.")
