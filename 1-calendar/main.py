


def calendar(startDay):


    day = 31

    num = 1
    print('\tJanuary\n')
    for i in range(1-(startDay-1),day+1):
        if num > 7:
            print('\n')
            num = 1
        if i < 1:
            i = 0
            num += 1
            print("%s" % f"{format(i,'3d')}\b",end=' ')
        else:
            num += 1
            print(format(i,"2d"),end=' ')

calendar(6)
