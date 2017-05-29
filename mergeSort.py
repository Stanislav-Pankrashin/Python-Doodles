import sys


def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0
    #print(left)
    while (len(left) > leftIndex) and (len(right) > rightIndex):
        #print(leftIndex, rightIndex)
        #print(left,right)
        leftElement = left[leftIndex].split()
        rightElement = right[rightIndex].split()
        if int(leftElement[0]) == int(rightElement[0]):
            if int(leftElement[1]) <= int(rightElement[1]):
                value = left[leftIndex]
                #print(value)
                result.append(value)
                leftIndex += 1
            else:
                value = right[rightIndex]
                #print(value)
                result.append(value)
                rightIndex += 1
                
            
        elif int(leftElement[0]) <= int(rightElement[0]):
            value = left[leftIndex]
            #print(value)
            result.append(value)
            leftIndex += 1
        else:
            value = right[rightIndex]
            #print(value)
            result.append(value)
            rightIndex += 1

    while len(left) > leftIndex:
        result.append(left[leftIndex])
        leftIndex += 1
    left = []
        
    while len(right) > rightIndex:
        result.append(right[rightIndex])
        rightIndex += 1  
    right = []

    return result



def mergeSort(list):
    if len(list) <= 1:
        return list

    left = []
    right = []

    for i in range(len(list)):
        if i >= len(list) / 2:
            left.append(list[i])
        else:
            right.append(list[i])

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

    

        



