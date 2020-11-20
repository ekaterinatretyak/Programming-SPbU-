# from collections import defaultdict
#
# class Solution:
#
#     def groupAnagrams(self, strs):
#         groupings = defaultdict(list)
#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             groupings[sorted_word].append(word)
#
#         return groupings.values()
#
# res = Solution()
# print(res)

def quicksort(mystring):
    if not mystring:
        return ""
    return (quicksort("".joined(x) for x in mystring[1:] if x < mystring[0])
            + [mystring[0]] +
            quicksort([x for x in mystring[1:] if x >= mystring[0]]))

print(quicksort("94kspd1fe"))