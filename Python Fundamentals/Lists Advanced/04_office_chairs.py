rooms_count = int(input())
free_chairs = 0
chairs_enough = True

for room in range(1, rooms_count + 1):
    chairs_people = input().split(" ")
    chairs = len(chairs_people[0])
    people = int(chairs_people[1])
    if chairs >= people:
        free_chairs += chairs - people
    else:
        chairs_needed = people - chairs
        chairs_enough = False
        print(f"{chairs_needed} more chairs needed in room {room}")
if chairs_enough:
    print(f"Game On, {free_chairs} free chairs left")
