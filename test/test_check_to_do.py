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

# """
# !! OPTIONAL !!
# Given a non string
# Returns: Error - "This is not valid text"
# """

# check_to_do(12345) => "Error - NON STRING PROVIED 