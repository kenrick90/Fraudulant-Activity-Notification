#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.

def median(current_sorting_list, d, medianposition):
    counter, left = 0,0
    while counter < medianposition:
        counter += current_sorting_list[left]
        left+=1
    right=left
    left -= 1

    if d%2 !=0 or counter>medianposition:
        return left
    else:
        while current_sorting_list[right] == 0:
            right +=1
        return (left +right)/2



def activityNotifications(expenditure, d):
    notifications=0
    current_position=0
    last_position=d
    current_sorting_list=[0]*201
    for i in range(d):
        current_sorting_list[expenditure[i]] += 1
    length = len(expenditure)
    if d % 2 == 0:
        median_position= int(d/2)
    else:
        median_position=int(d/2) + 1

    # print("median position is ", median_position)

    for i in range(d,length):
        med= median(current_sorting_list,d,median_position)
        # print("med is ",med)
        # print("expenditure is ",expenditure[i])
        if expenditure[i] >= 2 * med:
            notifications += 1
        current_sorting_list[expenditure[current_position]] -= 1
        current_sorting_list[expenditure[last_position]] += 1
        current_position += 1
        last_position += 1
    return notifications

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result=activityNotifications(expenditure, d)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
