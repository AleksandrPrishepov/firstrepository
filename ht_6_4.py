zp = 100
summ_prod = 0

while summ_prod <= zp:
    coast_prod = int(input())
    summ_prod = summ_prod + coast_prod
    if summ_prod > zp:
        print('Стоп, Джон')
        print('У джона осталось', zp -(summ_prod - coast_prod))
    elif summ_prod == zp:
        print('Джон потратил все полностью')
