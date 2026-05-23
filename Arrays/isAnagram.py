def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    return len(count) == 0


def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def isAnagram(self, s: str, t: str) -> bool:
    mapp = {}
    for ch in s:
        mapp[ch] = mapp.get(ch, 0) + 1

    for ch in t:
        if ch not in mapp or mapp[ch] == 0:
            return False

        mapp[ch] -= 1

    for k in mapp:
        if mapp[k] != 0:
            return False

    return True
