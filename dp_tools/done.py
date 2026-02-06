from knapsack import knapsack
if __name__ == '__main__':
    '''n = int(input())
    values = list(map(int, input().split()))
    weights = list(map(int, input().split()))'''
    e=knapsack([1,2,3],[1,2,3],5)
    for i in range(len(e)):
        for j in range(len(e[i])):
            print(e[i][j], end=' ')
        print()