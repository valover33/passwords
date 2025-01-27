import random
def main():
    result = ""
    rand_num_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    nat_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    rand_num = random.choice(rand_num_list)
    for i in nat_num_list:
        if i <= rand_num // 2:
            for j in  nat_num_list:
                if (rand_num % (i + j)) == 0 and i < j:
                    result = result + "%s%s" % (i, j)
                    if (i + j) > rand_num:
                        break
        else:
            break
    print(rand_num)
    print(result)

if __name__ == '__main__':
    main()
