__author__ = 'Irrevocable Cascade'

"""About 2000 years ago there was some war, and during one of its battles defendants were blocked by attackers in the
cave.

To avoid capture they decided to stand in a circle and kill each third until only one person remains - who was supposed
to commit suicide - though he eventually prefer to surrender to enemies. The problem is called after this person - you
may read the full story of Josephus and get math explanation of the problem in wikipedia article.

Your task is to determine for given number of people N and constant step K the position of a person who remains the last
 - i.e. the safe position"""


def josephus(n, k):
    ls = list(range(1, n + 1))
    k -= 1
    i = k
    while len(ls) > 1:
        del ls[i]
        i = (i + k) % len(ls)
    print(ls[0])


print(josephus(10, 3))