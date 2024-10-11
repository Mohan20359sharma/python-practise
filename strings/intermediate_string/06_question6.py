def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s.find(prefix) !=0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


strs = input("Enter string: ").split()
print(longest_common_prefix(strs))
