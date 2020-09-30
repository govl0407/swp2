import time
import random
import sys
sys.setrecursionlimit(10**6)

#선형탐색
def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

#이진탐색

def recbinsearch(L, l, u, target):
    list_len = len(L)
    mid = int(list_len/2)
    # 키값과 중간값이 같을때 
    if L[mid] == target or len(L) ==1:
        return -1
    elif L[mid]> target :
        L[mid:] = []
        recbinsearch(L, 0, len(numbers), target)
    elif L[mid]< target :
        L[:mid] = []
        recbinsearch(L, 0, len(numbers), target)

#랜덤 리스트 생성
numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

#찾을 숫자
numoftargets = int(input("Enter the number of targets: "))
targets = []

for i in range(numoftargets):
    targets += [random.randint(0, 999999)]




ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
print("sequential search %d: not found %d time %.6f" % (numoftargets, cnt, ts))



ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("binary search %d: not found %d time %.6f" % (numoftargets, cnt, ts))
