# Testing distribution functions

from random import normalvariate, expovariate


def dist(rep, sum, max, zero):
    if rep < 0:
        rep = 0
    if max < rep:
        max = rep
    if rep == 0:
        zero += 1
    sum += rep
    return sum, max, zero

sum1 = max1 = zero1 = 0
sum2 = max2 = zero2 = 0
sum3 = max3 = zero3 = 0
i = 0
for x in range(0, 66548):
    d1 = round(normalvariate(-1, 3))
    sum1, max1, zero1 = dist(d1, sum1, max1, zero1)

    d2 = round(normalvariate(-3, 4))
    sum2, max2, zero2 = dist(d2, sum2, max2, zero2)

    d3 = round(expovariate(7)*10)
    sum3, max3, zero3 = dist(d3, sum3, max3, zero3)

    # print("%s,      %s,       %s" % (i, d1, d2))
    i += 1
print("i = " + str(i))
print("Sum:      %s     %s     %s" % (sum1, sum2, sum3))
print("Max:      %s        %s        %s   " % (max1, max2, max3))
print("Zero:     %s     %s     %s" % (zero1, zero2, zero3))
print("Non-Zero: %s     %s     %s" % (i-zero1, i-zero2, i-zero3))