def add_to_last_wagon(list_wagons, people):
    list_wagons[-1] += people
    return list_wagons


def add_by_index(list_wagons, index, people):
    list_wagons[index] += people
    return list_wagons


def remove_by_index(list_wagons, index, people):
    list_wagons[index] -= people
    return list_wagons


wagons = int(input())
wagons_list = [0] * wagons

while True:
    tokens = list(input().split())
    command = tokens[0]

    if command == "End":
        break
    elif command == "add":
        people = int(tokens[1])
        add_to_last_wagon(wagons_list, people)
    elif command == "insert":
        index = int(tokens[1])
        people = int(tokens[2])
        add_by_index(wagons_list,index,people)
    elif command == "leave":
        index = int(tokens[1])
        people = int(tokens[2])
        remove_by_index(wagons_list,index,people)

print(wagons_list)
