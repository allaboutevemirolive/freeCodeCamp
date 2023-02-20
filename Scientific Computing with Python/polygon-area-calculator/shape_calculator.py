class Rectangle:
  # Initialize a Rectangle object with width and height attributes
  def __init__(self, width, height):
    self.width = width
    self.height = height

  # Return a string representation of the Rectangle object
  def __str__(self):
    return "Rectangle(width=" + str(self.width) + \
           ", height=" + str(self.height) + ")"

  # Set the width attribute of the Rectangle object
  def set_width(self, width):
    self.width = width

  # Set the height attribute of the Rectangle object
  def set_height(self, height):
    self.height = height

  # Return the area of the Rectangle object (width * height)
  def get_area(self):
    return self.width * self.height

  # Return the perimeter of the Rectangle object (2 * width + 2 * height)
  def get_perimeter(self):
    return 2 * (self.width + self.height)

  # Return the diagonal of the Rectangle object ((width ** 2 + height ** 2) ** .5)
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  # Return a string representation of the Rectangle object as a picture made of asterisks (*)
  def get_picture(self):
    # If the Rectangle is too big, return "Too big for picture."
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    # Otherwise, create a string representation of the Rectangle as a picture of asterisks
    rectangle = ("*" * self.width + "\n") * self.height
    return rectangle

  # Return the number of times another shape (rectangle or square) can fit inside this Rectangle
  def get_amount_inside(self, shape):
    max_width = self.width // shape.width
    max_height = self.height // shape.height
    return max_width * max_height


class Square(Rectangle):
  # Initialize a Square object with a side length, which sets the width and height attributes to that length
  def __init__(self, length):
    super().__init__(length, length)

  # Return a string representation of the Square object
  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  # Set the side length of the Square object
  def set_side(self, side):
    self.width = side
    self.height = side

  # Override the set_width method of the Rectangle class to set both the width and height to the same value
  def set_width(self, side):
    self.width = side
    self.height = side

  # Override the set_height method of the Rectangle class to set both the width and height to the same value
  def set_height(self, side):
    self.width = side
    self.height = side