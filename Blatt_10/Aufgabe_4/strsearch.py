#
# In Zusammenarbeit mit Simon Wagner, Toni Kandziora, Daniel Heisig, Felix Scholzen entstanden
#

def search(wholeString, pattern):
    matches = []
    patternIdx = 0
    for i, c in enumerate(wholeString):
        if pattern[patternIdx] == c:
            patternIdx += 1
            if patternIdx == len(pattern):
                matches.append(i-len(pattern)+1)
                patternIdx = 0
        elif pattern[0] == c:
            patternIdx = 1
        else:
            patternIdx = 0
    return matches


def main():
    searchstr = "abcdabcfgabbcabcsacbabbabc"
    pattern = "abc"

    matches = search(searchstr, pattern)
    closematches = [m+len(pattern)-1 for m in matches]

    for i, c in enumerate(searchstr):
        if i in matches:
            print("[", end="")
        print(c, end="")
        if i in closematches:
            print("]", end="")

    print()


main()
