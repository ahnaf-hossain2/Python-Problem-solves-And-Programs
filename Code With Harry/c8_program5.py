# Write a python function to remove a given word from a list and strip it at the same time.

def remove_and_strip(words_list, word_to_remove):
    """
    This function removes a given word from the list and strips leading/trailing spaces from the remaining words.

    :param words_list: List of words
    :param word_to_remove: Word to be removed from the list
    :return: New list with the word removed and remaining words stripped of leading/trailing spaces
    """
    # Strip leading/trailing spaces from each word and remove the specified word
    new_list = [item.strip() for item in words_list if item.strip() != word_to_remove]
    return new_list

# Example usage
words_list = [" Harry ", " Larry ", " Carry ", " Marie "]
print(remove_and_strip(words_list, "Carry"))

# Normal method
# words_list = [" Harry ", " Larry ", " Carry ", " Marie "]
# words_list.remove("Carry")
# words_list = [i.strip() for i in words_list]
# print(words_list)
