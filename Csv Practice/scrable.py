# this program returns the points accumulated by a player based on the words  they use in playing scrable
import random

numbers_a  = range(1,13)
numbers_b = random.sample(range(1000), 12)

print(numbers_b)
plt.plot(numbers_a, numbers_b)
plt.show()

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
names_heights = zip(names, heights)
print(list(names_heights))

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key: value for key,value in zip(letters, points)}
letters_to_points[" "] = 0

def score_word (word):
    point_total = 0
    for letter in word:
        for key in list(letters_to_points):
            if letter == key:
                point_total += letters_to_points.get(key, 0)
    return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
#print(player_to_words.items())
for player in player_to_words.keys():
    player_points = 0
    for word in player_to_words.get(player, 0):
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)

def play_word (player, word):
    player_to_words[player].append(word)
play_word ("player1", "MEXICO")
#print(player_to_words)

def update_point_totals():
    for player in player_to_words.keys():
        player_points = 0
        for word in player_to_words.get(player, 0):
            player_points += score_word(word)
        player_to_points[player] = player_points

update_point_totals()

print(player_to_points)

