__author__ = 'Irrevocable Cascade'

"""Little Merlin wants to become a meteorologist. He measures the temperature of the air each hour so that after several
days he has a long sequence of values.

However, his instruments are not ideal so the measurements are not exact - they randomly jump up and down by several
degrees from the real values.

Observing this, Merlin decided to make his data more smooth. To achieve this he only needs every value to be substituted
by the average of it and its two neighbors. For example, if he have the sequence of 5 values like this:

3 5 6 4 5
Then the second (i.e. 5) should be substituted by (3 + 5 + 6) / 3 = 4.66666666667,
the third (i.e. 6) should be substituted by (5 + 6 + 4) / 3 = 5,
the fourth (i.e. 4) should be substituted by (6 + 4 + 5) / 3 = 5.
By agreement, the first and the last values will remain unchanged.

At the picture above the blue line shows unprocessed data while red represents the smoothing.

You are to write the program which helps Little Merlin in this whimsical algorithm of digital signal processing."""

# Does not add first and last values.
def smooth(filename):
	with open(filename) as file:
		list = file.read().split()

	return [(float(list[i - 1]) + float(list[i]) + float(list[i + 1])) / 3 for i in range(1, len(list) - 1)]


print(smooth('weather.txt'))
