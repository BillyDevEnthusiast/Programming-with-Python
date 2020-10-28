def loading_bar(number: int):
    load_stripes = number // 10
    percentage = load_stripes * 10
    list_dots = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    index = -1
    for i in range(load_stripes):
        if load_stripes != 0:
            index += 1
            list_dots[index] = "%"
    return list_dots


load_lvl = int(input())
percentage1 = (load_lvl // 10) * 10
res = loading_bar(load_lvl)

if res != ["%","%","%","%","%","%","%","%","%","%"]:
    res = "".join(res)    
    print(f"{percentage1}% [{res}]")
    print("Still loading...")
else:
    res = "".join(res)    
    print("100% Complete!")
    print(f"[{res}]")
