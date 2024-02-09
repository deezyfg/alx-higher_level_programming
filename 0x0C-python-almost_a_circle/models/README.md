# Models

This folder contains implementations of various geometric shapes.

## Base

**File:** `base.py`

**Description:** Defines the `base` class for all models. It manages the ID attribute and ensures uniqueness across all objects.

### Attributes:

- `__nb_objects` (int): Tracks the number of instantiated `Base` objects.

### Methods:

- `__init__(self, id=None)`: Initializes a new `Base` instance with a unique ID. If ID is not provided, it increments the object counter to generate a new ID.

- `to_json_string(list_dictionaries)`: Returns the JSON serialization of a list of dictionaries.

- `save_to_file(list_objs)`: Writes the JSON serialization of a list of objects to a file.

- `from_json_string(json_string)`: Deserializes a JSON string and returns a list of dictionaries.

- `create(**dictionary)`: Instantiates a class from a dictionary of attributes.

- `load_from_file()`: Loads classes instantiated from a file of JSON strings.

- `save_to_file_csv(list_objs)`: Writes the CSV serialization of a list of objects to a file.

- `load_from_file_csv()`: Loads instances instantiated from a CSV file.

- `draw(list_rectangles, list_squares)`: Draws Rectangles and Squares using the `turtle module`.

## Rectangle

**File:** `rectangle.py`

**Description:** Represents a `rectangle`, inheriting from the `Base` class.

### Attributes:

- `width`: The width of the rectangle.
- `height`: The height of the rectangle.
- `x`: The x-coordinate of the rectangle's position.
- `y`: The y-coordinate of the rectangle's position.

### Methods:

- Inherits all methods from the `Base` class.
- `area()`: Calculates the area of the rectangle.
- `display()`: Displays the `rectangle` as a series of '#' characters.
- `update(*args, **kwargs)`: Updates the attributes of the `rectangle`.
- `to_dictionary()`: Returns the dictionary representation of the `rectangle`.

## Square

**File:** `square.py`

**Description:** Represents a `square`, inheriting from the `Rectangle` class.

### Attributes:

- Inherits all attributes from the `Rectangle` class.

### Methods:

- Inherits all methods from the `Rectangle` class.
- `update(*args, **kwargs)`: Updates the attributes of the `square`.
- `to_dictionary()`: Returns the dictionary representation of the `square`.