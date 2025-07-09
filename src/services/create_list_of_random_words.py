from src.services.get_random_item_from_list import get_random_item_from_list
from src.services.read_words_from_file import read_words_from_file


def create_list_of_random_words(number_of_words: int) -> list[str]:
    all_words: list[str] = read_words_from_file()
    list_of_words: list[str] = []
    for i in range(number_of_words):
        list_of_words.append(get_random_item_from_list(all_words))
    return list_of_words
