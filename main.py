# A simple script to estimate the expected value of taking the max of a three six-sided dice roll, plotting a histogram of the results.

import random
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

class Dice:
    def __init__(self, sides, number_of_dice):
        self.sides = sides
        self.number_of_dice = number_of_dice

    def roll(self):
        values = []
        for i in range(0, self.number_of_dice):
            values.append(random.randint(1, self.sides))
        return values

    def repeated_game(self, number_of_games):
        results = []
        for i in range(0, number_of_games):
            results.append(max(self.roll()))
        return results

def format_y_axis(value, _):
    """Custom formatter for y-axis labels."""
    if value >= 1_000_000:
        return f'{value / 1_000_000:.1f}M'
    elif value >= 1_000:
        return f'{value / 1_000:.1f}k'
    else:
        return str(int(value))

if __name__ == '__main__':
    dice = Dice(6, 3)
    data = dice.repeated_game(10_000_000)  # Example with a large number of games
    print('Expected value = ' + str(sum(data) / len(data)))

    bins = [0.5 + i for i in range(7)]  # Creates bins like [0.5, 1.5, 2.5, ..., 6.5]
    plt.hist(data, bins=bins, color='skyblue', edgecolor='black', rwidth=0.8)

    plt.xticks(range(1, 7))  # Set x-ticks to exactly 1-6
    plt.xlabel('Game outcome')
    plt.ylabel('Frequency')
    plt.title('Dice Game Histogram')

    # Apply the custom y-axis formatter
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_y_axis))

    plt.show()



