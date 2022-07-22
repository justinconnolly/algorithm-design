def find_happy_number(num, num_set):
    if num == 1:
        return True
    if num in num_set:
        return False
    sum = 0
    num_set.add(num)
    while num > 0:
        digit = num % 10
        sum += digit ** 2
        num //= 10
    return find_happy_number(sum, num_set)