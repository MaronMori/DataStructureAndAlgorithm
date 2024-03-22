height = int(input())
table = []
deleteItem = []

for i in range(height):
    table.append(input())


def add_location_list(dict_list, key, value):
    for i in dict_list:
        if i.get(key) == value:
            return

    dict_list.append({key: value})


def delete_same_item(dict_list, table):
    for i in dict_list:
        row = list(i.keys())
        index = list(i.values())
        item_list = list(table[int(row[0])])
        item_list[index[0]] = "."
        item_nonlist = "".join(item_list)
        table[int(row[0])] = item_nonlist


def move_item(height, table):
    count = 0
    for i in range(height - 1):
        for x in range(5):
            if not table[i][x] == ".":
                if table[i+1][x] == ".":
                    new_value = table[i][x]
                    now_row = list(table[i])
                    now_row[x] = "."
                    now_row_modified = "".join(now_row)
                    table[i] = now_row_modified
                    target_row = list(table[i+1])
                    target_row[x] = new_value
                    target_row_modified = "".join(target_row)
                    table[i+1] = target_row_modified
                    count += 1
    if not count == 0:
        return True
    else:
        return False

def check_delete_item(height, table):
    count = 0
    for i in range(len(table)):
        for x in range(5):
            if not table[i][x] == ".":
                # もし最終列目なら
                if i == height - 1:
                    if not x == 4:
                        if table[i][x] == table[i][x + 1]:
                            add_location_list(dict_list=deleteItem, key=i, value=x)
                            add_location_list(dict_list=deleteItem, key=i, value=x + 1)
                            count += 1
                else:
                    # 右端
                    if 4 == x:
                        if table[i][x] == table[i + 1][x]:
                            add_location_list(dict_list=deleteItem, key=i, value=x)
                            add_location_list(dict_list=deleteItem, key=i + 1, value=x)
                            count += 1

                    # その他
                    else:
                        if table[i][x] == table[i][x + 1]:
                            add_location_list(dict_list=deleteItem, key=i, value=x)
                            add_location_list(dict_list=deleteItem, key=i, value=x + 1)
                            count += 1
                        if table[i][x] == table[i + 1][x]:
                            add_location_list(dict_list=deleteItem, key=i, value=x)
                            add_location_list(dict_list=deleteItem, key=i + 1, value=x)
                            count += 1

    if not count == 0:
        delete_same_item(deleteItem, table)
        move_result = True
        while move_result:
            move_result = move_item(height, table)
        for row in table:
            print(row)
        print("############")
        return True
    else:
        return False

status = True

while status:
    status = check_delete_item(height, table)

for row in table:
    print(row)