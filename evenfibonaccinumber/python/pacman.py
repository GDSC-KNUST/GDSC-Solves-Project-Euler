previous_num = 1
curr_num = 1
my_list = [1]
total = 0

while curr_num <= 4000000:
    next_num = curr_num + previous_num
    my_list.append(next_num)
    previous_num = curr_num
    curr_num = next_num
    
for n in my_list:
    if n % 2 == 0:
        total += n
print(total)