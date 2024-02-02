def check_to_do(text):
    if text == "":
        raise Exception("Error - no string provided")
    elif "#TODO" in text:
        return "The inputted text contains "#TODO""
    else:
        return "The inputted text does not contain "#TODO""