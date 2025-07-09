def read_words_from_file() -> list[str]:
    """
    Reads words from the words.txt file and returns them as a list of str.
    """
    with open("./data/words.txt", "r") as file:
        words = file.readlines()
        for i in range(len(words)):
            words[i] = words[i][:-1]
        return words
