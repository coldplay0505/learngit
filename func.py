def my_add(*para):
    ret = 0
    for element in para: ret += element
    return ret

if __name__ == '__main__':
    print(my_add(1,2,3,4,5))
