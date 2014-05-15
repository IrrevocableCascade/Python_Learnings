__author__ = 'Irrevocable Cascade'

"""About 2000 years ago there was some war, and during one of its battles defendants were blocked by attackers in the
cave.

To avoid capture they decided to stand in a circle and kill each third until only one person remains - who was supposed
to commit suicide - though he eventually prefer to surrender to enemies. The problem is called after this person - you
may read the full story of Josephus and get math explanation of the problem in wikipedia article.

Your task is to determine for given number of people N and constant step K the position of a person who remains the last
 - i.e. the safe position"""

import math

def josephus(n, k):
	people = list(range(1, n + 1))
	kill_list = []
	last_index = 0
	start_offset = 1

	while len(people) >= 1:
		if last_index % k != 0:
			start_offset = n - last_index
			last_index = 0

		for i in range(k - start_offset, len(people) - 1, k):
				if i + last_index < people[len(people) - 1]:
					kill_list.insert(0, i)
				else:
					kill_list.insert(0, math.ceil(i % k) - 1)
					last_index = 0

		last_index = i


		for j in kill_list:
			del people[j]

		del kill_list[:]



josephus(10,3)