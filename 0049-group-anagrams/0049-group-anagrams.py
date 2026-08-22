class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            if "".join(sorted(i)) not in seen:
                seen["".join(sorted(i))]=[i]
            else:
                seen["".join(sorted(i))].append(i)

        return list(seen.values())