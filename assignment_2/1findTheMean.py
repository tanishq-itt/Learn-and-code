# # given code converted in python
# NQ = list(map(int, input().split()))

# arr = list(map(int, input().split()))

# sumarr = [0] * (NQ[0] + 1)
# sumarr[0] = 0

# for i in range(1, NQ[0] + 1):
#     sumarr[i] = sumarr[i - 1] + arr[i - 1]

# for _ in range(NQ[1]):
#     RL = list(map(int, input().split()))
#     result = (sumarr[RL[1]] - sumarr[RL[0] - 1]) // (RL[1] - RL[0] + 1)
#     print(result)


# code following the SOLID principles and clean code principles


def readInput():
    values = input().split()
    numberOfElements = int(values[0])
    numberOfQueries = int(values[1])
    return numberOfElements, numberOfQueries


def readArray(numberOfElements):
    elements = input().split()
    arrayElements = [int(value) for value in elements]
    return arrayElements


def buildPrefixSum(arrayElements):
    length = len(arrayElements)
    prefixSum = [0] * (length + 1)

    for index in range(1, length + 1):
        prefixSum[index] = prefixSum[index - 1] + arrayElements[index - 1]

    return prefixSum


def processQueries(prefixSum, numberOfQueries):
    for _ in range(numberOfQueries):
        query = input().split()
        leftIndex = int(query[0])
        rightIndex = int(query[1])

        subarraySum = prefixSum[rightIndex] - prefixSum[leftIndex - 1]
        subarrayLength = rightIndex - leftIndex + 1

        result = subarraySum // subarrayLength
        print(result)


def main():
    numberOfElements, numberOfQueries = readInput()
    arrayElements = readArray(numberOfElements)
    prefixSum = buildPrefixSum(arrayElements)
    processQueries(prefixSum, numberOfQueries)


if __name__ == "__main__":
    main()

