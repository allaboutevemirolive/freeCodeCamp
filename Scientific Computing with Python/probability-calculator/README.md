### Assignment

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat. 

First, create a `Hat` class in `prob_calculator.py`. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:
```
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a `contents` instance variable. `contents` should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is `{"red": 2, "blue": 1}`, `contents` should be `["red", "red", "blue"]`.

The `Hat` class should have a `draw` method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from `contents` and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an `experiment` function in `prob_calculator.py` (not inside the `Hat` class). This function should accept the following arguments:
* `hat`: A hat object containing balls that should be copied inside the function.
* `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set `expected_balls` to `{"blue":2, "red":1}`.
* `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
* `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The `experiment` function should return a probability. 

For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball when you draw 5 balls from a hat containing 6 black, 4 red, and 3 green. To do this, we perform `N` experiments, count how many times `M` we get at least 2 red balls and 1 green ball, and estimate the probability as `M/N`. Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.

Here is how you would call the `experiment` function based on the example above with 2000 experiments:

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

<br>

[FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator)

___

>What is `**kwargs` in the code?


In the given code, `**kwargs` is a special syntax used in the parameter list of the __init__ method of the Hat class. 

It allows passing a variable number of keyword arguments (i.e., arguments passed with a keyword) to the constructor of the Hat object.

When using **kwargs, `any number of keyword arguments can be passed to the constructor`, and they will be collected into a dictionary called kwargs. The keys of the dictionary are the argument names, and the values are the argument values.

For example, if we create a Hat object like this:

```
hat1 = Hat(yellow=3, blue=2, green=6)
```
Then `**kwargs` will collect the arguments yellow=3, blue=2, and green=6 into a dictionary called kwargs. The resulting dictionary will look like this:

```
{
  "yellow": 3,
  "blue": 2,
  "green": 6
}
```
Inside the __init__ method, the code loops over the items of the kwargs dictionary, and for each key-value pair, it adds the corresponding number of balls to the contents list.

___

>I don't understand this code : for key, value in kwargs.items()


kwargs stands for keyword arguments, which is a dictionary-like object that contains the arguments that were passed to a function.

In this code, `kwargs.items()` returns a list of tuples, where each tuple contains a key-value pair from kwargs. Then, the for loop iterates over each tuple in the list, and unpacks the key-value pairs into key and value variables, respectively.

So, for example, if we create a Hat object like this:

```
hat = Hat(yellow=3, blue=2, green=6)
```
then kwargs will be a dictionary-like object containing the key-value pairs: 
```
{"yellow": 3, "blue": 2, "green": 6} 
```
The for loop will iterate over each tuple in `kwargs.items()`, so `key ` and `value` will take on the following values in each iteration:
```
key="yellow", value=3
key="blue", value=2
key="green", value=6
```
Then, for each key-value pair, the loop will append key to `self.contents` value number of times, effectively creating a list of strings containing one item for each ball in the hat.
___

>What is deepcopy?

deepcopy is a function provided by the Python copy module that creates a deep copy of a mutable object.
``` 
A deep copy creates a new object with a new memory address that is a complete copy of the original object, including all sub-objects. 
```
This means that changes made to the copy will not affect the original object, even if the original object contains nested mutable objects.

In contrast, a shallow copy creates a new object with a new memory address, but any mutable objects within the copied object are not duplicated. Instead, the new object contains references to the same mutable objects as the original object. This means that changes made to a mutable object within the copy will also affect the original object.