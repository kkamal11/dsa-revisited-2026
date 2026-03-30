def longest_common_prefix(words: list) -> str:
    prefix = words[0]
    for i in range(1, len(words)):
        mini = min(len(prefix), len(words[i]))
        idx = 0
        for j in range(mini):
            if prefix[j] == words[i][j]:
                idx += 1
            else:
                break
        prefix = prefix[:idx]
    return prefix


def longest_common_prefix_optimised(words: list) -> str:
    prefix = words[0]
    for i in range(1, len(words)):
        mini = min(len(prefix), len(words[i]))
        idx = 0
        for j in range(mini):
            if prefix[j] == words[i][j]:
                idx += 1
            else:
                break
        if idx == 0:
            return ""
        prefix = prefix[:idx]
    return prefix


words = ["flower", "flow", "floweight"]
print(longest_common_prefix(words=words))
print(sorted(words))
