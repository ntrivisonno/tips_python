def count_characters(input_string):
    """
    Counts the characters in a given string.

    Args:
        input_string (str): The string to count characters in.

    Returns:
        int: The number of characters in the string.
    """
    return len(input_string)

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    character_count = count_characters(user_input)
    print(f"The string contains {character_count} characters.")
