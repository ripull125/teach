def get_nums():
    x = input("How many numbers do you want to input?")
    list = []
    for i in range(x):
        more = input("Add x more numbers")
        list.append(more)
    return list

def main():
    lst = get_num()
    print("The mean of the numbers is: ", sum(lst)/len(lst))
    