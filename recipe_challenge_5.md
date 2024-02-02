# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.

Notes:
- Assume only input we receive will be a string - Add error cases if blank string inputted or invalid iterable. 


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def check_to_do(text):
    """
    Check for the string "#TODO" inside text string

    Parameters: 
    text: string containing words 

    Returns:
    "The inputted text containts "#TODO""

    "The inputted does not contain "#TODO""

    Side effects:
    Potential error if non string inputted or blank string inputted
    """
    pass

```

## 3. Create Examples as Tests



```python
"""
Given a string containing the phrase "#TODO"
Returns: "The inputted text containts "#TODO""

"""
check_to_do("This is something i need #TODO") => "The inputted text containts "#TODO""

"""
Given a string not containing the phrase "#TODO"
Returns: "The inputted text does not containts "#TODO"" =>

"""
check_to_do("This is something i need to do") => "The inputted text does not containts "#TODO""

"""
Given a blank string 
Returns: Error - no string provided  
"""

check_to_do("") => "Error - no string provided" 

"""
!! OPTIONAL !!
Given a non string
Returns: Error - "This is not valid text"
"""

check_to_do(12345) => "Error - NON STRING PROVIED 


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
