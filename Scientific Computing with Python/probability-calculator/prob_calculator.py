import copy
import random


# Define a class called Hat.
class Hat:

  # Constructor to initialize the contents of the hat.
  def __init__(self, **kwargs):
    # Initialize an empty list for contents.
    self.contents = []  
    # Iterate over the keyword arguments.
    for key, value in kwargs.items():  
      # Repeat for the value of each argument.
      for _ in range(value):  
        # Add a string representing each ball to the contents list.
        self.contents.append(key)  

  # Define a method called draw to randomly draw balls from the hat.
  def draw(self, number):
    # If the number of balls to draw is greater than the number of balls in the hat,
    if number > len(self.contents): 
      # Return all the balls in the hat.
      return self.contents  
    # Create an empty list to hold the drawn balls.
    balls = []  
    # Repeat for the specified number of balls to draw.
    for _ in range(number):  
      # Choose a random ball from the hat.
      choice = random.randrange(len(self.contents))  
      # Remove the chosen ball from the hat and add it to the list of drawn balls.
      balls.append(self.contents.pop(choice))  
    # Return the list of drawn balls.
    return balls  


# Define a function called experiment to perform multiple draws from the hat and calculate the probability of getting the expected balls.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  # Convert the expected balls dictionary into a list of expected counts for each color.
  expected_no_of_balls = []
  for key in expected_balls:
    expected_no_of_balls.append(expected_balls[key])

  # Initialize a counter for the number of successful experiments.
  successes = 0  

  # Repeat the experiment for the specified number of times.
  for _ in range(num_experiments):
    # Create a deep copy of the hat to avoid modifying the original hat.
    new_hat = copy.deepcopy(hat)  
    # Draw the specified number of balls from the hat.
    balls = new_hat.draw(num_balls_drawn)  

    # Create an empty list to hold the counts of each color drawn.
    no_of_balls = []  
    # Iterate over the expected balls dictionary.
    for key in expected_balls:  
      # Count the number of balls drawn for each color and add it to the list.
      no_of_balls.append(balls.count(key))  

    # If the actual counts for each color are greater than or equal to the expected counts,
    if no_of_balls >= expected_no_of_balls:  
      # Increment the counter for successful experiments.
      successes += 1  

  # Return the probability of getting the expected balls.
  return successes / num_experiments  
