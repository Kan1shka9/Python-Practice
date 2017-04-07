items = ["this", "is", 9, 5, "a", 5, "string"]

# Parsing
def parse_list(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass

    return num_list_items, str_list_items

print "Parsing : " + str(parse_list(items)) # TypeError: cannot concatenate 'str' and 'tuple' objects

# Sum
def my_sum(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total

print "Sum: " + str(my_sum(items))

# Average
def my_count(my_num_list):
    count = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            count += 1
    return count

def my_avg(my_num_list):
    the_sum = my_sum(my_num_list)
    return the_sum/(my_count(my_num_list)*1.0)

print "Average: " + str(my_avg(items))
