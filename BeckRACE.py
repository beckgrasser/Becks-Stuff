
import random
#Eleven

class Greyhound:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.lanes = random.randint(1,5)

    def move(self):
        # Simulate the greyhound's movement
        self.position += random.randint(2, 7)

    def __str__(self):
        return f"{self.name} is at position {self.position}."


def main():
    # Create greyhounds
    greyhounds = [Greyhound("Eleven"), Greyhound("Lucas"), Greyhound("Will"), Greyhound("Dustin"), Greyhound("Mike")]

    # Race distance (1 mile)
    race_distance = 1609  # meters (1 mile is approximately 1609 meters)

    # Simulate the race
    i = 0
    winner = None
    while not winner:
        i=i+1
        for greyhound in greyhounds:
            greyhound.move()
            if greyhound.position >= race_distance:
                winner = greyhound
                winnerL = greyhound.lanes
                
                break

    # Print the results
    i_min = i / 60
    print(f"The winner of the race is {winner.name}!")
    print(f"It took {i_min} minutes!")
    print(f"Winner was in lane {winner.lanes}")
if __name__ == "__main__":
    main()