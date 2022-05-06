# 2022-05-07
# 동일한 단어 그룹화하기
from typing import List
import collections
import sys


def groupAnagrams(strs: List[str]) -> List[List[str]]: #그룹애너그램 활용
    anagrams = collections.defaultdict(list) #초기 dict값 부여
    for word in strs:
        anagrams[''.join(sorted(word))].append(word) # 단어를 정렬하여 합친다. 단어를 삽입
    return list(anagrams.values()) #딕셔너리의 value값을 반환


s = []
n = int(sys.stdin.readline().rstrip()) # 입력할 단어 개수 입력
for _ in range(n):
    s.append(sys.stdin.readline().rstrip()) # 단어입력
print(len(groupAnagrams(s))) # 집합의 수를 
