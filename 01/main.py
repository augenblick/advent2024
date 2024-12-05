import heapq

def main():

    # part 1
    answerSum = 0
    (list1, list2) = getLists()
    (heap1, heap2) = createHeaps(list1, list2)

    for index in range(len(heap1)):
        list1Element = heapq.heappop(heap1)
        list2Element = heapq.heappop(heap2)

        answerSum += abs(int(list1Element) - int(list2Element))

    # part 2
    (list1B, list2B) = getLists()
    part2Sum = 0

    for item in list1B:
        occurenceCount = 0
        for identifier in list2B:
            if (int(identifier) == int(item)):
                occurenceCount += 1

        part2Sum += int(item) * int(occurenceCount)


    # drumroll...
    print('part 1 answer: ', answerSum)
    print('part 2 answer: ', part2Sum)


def getLists():
    # two lists
    list1 = []
    list2 = []

    input = open('./input/input.txt', 'r')
    inputList = input.readlines()

    for line in inputList:
        elements = line.split('   ')
        list1.append(elements[0])
        list2.append(elements[1])

    return (list1, list2)

def createHeaps(list1, list2):
    

    # make into min heaps
    heapq.heapify(list1)
    heapq.heapify(list2)

    return (list1, list2)


if __name__ == "__main__":
    main()