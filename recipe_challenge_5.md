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


from lib.check_to_do import *
import pytest

"""
Given a string containing the phrase "#TODO"
Returns: "The inputted text contains "#TODO""

"""
def test_check_to_do_text_contains_todo():
    result = check_to_do("This text contains #TODO")
    assert result == "The inputted text contains "#TODO""

"""
Given a string not containing the phrase "#TODO"
Returns: "The inputted text does not contains "#TODO"" =>
"""
def test_check_to_do_text_does_not_contain_todo():
    result = check_to_do("This text contains to do")
    assert result == "The inputted text does not contain "#TODO""

"""
Given a blank string 
Returns: Error - no string provided  
"""

def test_check_blank_text():
    with pytest.raises(Exception) as err:
        check_to_do("")
    error_message = str(err.value)
    assert error_message == "Error - no string provided"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

def check_to_do(text):
    if text == "":
        raise Exception("Error - no string provided")
    elif "#TODO" in text:
        return "The inputted text containts "#TODO""
    else:
        return "The inputted text does not contain "#TODO""
