def gerador():
    for i in range(10):
        print('i = ', i)
        yield i  #substitua por return e veja o resultado


for j in gerador():
    print('j = ', j)