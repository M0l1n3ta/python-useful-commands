def is_anagram(word_one: str, word_two: str) -> bool:
    # If they are the same word ignoring case, it's not considered an anagram
    if word_one.lower() == word_two.lower():
        return False

    return sorted(word_one.lower()) == sorted(word_two.lower())


def main():
    print(f'"amor" es anagrama de "roma\": {is_anagram("amor", "roma")}')


if __name__ == "__main__":
    main()
