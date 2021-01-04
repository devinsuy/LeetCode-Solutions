from collections import defaultdict
from copy import deepcopy

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Base case
        if len(s) == 0:
            return 0

        # For each substring, maintain a seen and distinct
        # set using sliding window
        distinct_len = 0

        # Map (left, right) indicies tuple to number of distinct
        cache = {}

        for left in range(len(s)):
            seen = defaultdict(int)
            distinct = set([])
            for right in range(left+1, len(s)+1):
                added_char = s[right-1]
                prev_solve = (left-1, right)

                # Lookup result of previously solved subproblem excluding
                # the character removed in the current subproblem
                if prev_solve in cache:
                    seen = cache[prev_solve][0]
                    distinct = cache[prev_solve][1]
                    removed_char = s[left-1]
                    # print("For", s[left:right], "compare to", s[left-1:right])
                    # print(seen)
                    # print(distinct)

                    # The current subproblem only differs by the leading character
                    seen[removed_char] -= 1
                    new_count = seen[removed_char]
                    # print("New count of", added_char, ":", new_count)
                    if new_count == 1:
                        # distinct_len += (len(distinct) + 1)
                        distinct.add(removed_char)
                        # print("!Added", (len(distinct) + 1))
                    elif new_count == 0:
                        # distinct_len += (len(distinct) + - 1)
                        distinct.remove(removed_char)
                        # print("@Added", (len(distinct) - 1))
                    else:
                        pass
                        # print("#Added", (len(distinct)))
                    
                    distinct_len += len(distinct)

                    # Cache values for this substring
                    cache[(left,right)] = (seen, distinct)

                
                # Solve subproblem for first time
                else:
                    seen[added_char] += 1
                    if seen[added_char] > 1:
                        if added_char in distinct:
                            distinct.remove(added_char)
                    else:
                        distinct.add(added_char)
                    distinct_len += len(distinct)

                    # Save result for lookup
                    cache[(left, right)] = (deepcopy(seen), deepcopy(distinct))

        return distinct_len



# Expected: 10
# "A","B","C","AB","BC" and "ABC"
s = "ABC"

# Expected: 8
s = "ABA"

# Expected: 92
s = "LEETCODE"

sol = Solution()
print(sol.uniqueLetterString(s))