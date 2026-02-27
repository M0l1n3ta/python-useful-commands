from typing import Dict

# Alfabeto Morse basado en la tabla de Wikipedia (es).
TEXT_TO_MORSE: Dict[str, str] = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    '"': ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    "!": "-.-.--",
    "(": "-.--.",
    ")": "-.--.-",
    "+": ".-.-.",
    ";": "-.-.-.",
    "_": "..--.-",
    "$": "...-..-",
    "&": ".-...",
}

MORSE_TO_TEXT: Dict[str, str] = {value: key for key, value in TEXT_TO_MORSE.items()}


def is_morse(text: str) -> bool:
    normalized = text.replace("—", "-").strip()
    if not normalized:
        return False

    return set(normalized) <= {".", "-", " "}


def text_to_morse(text: str) -> str:
    words = []
    for word in text.upper().split():
        letters = [TEXT_TO_MORSE[char] for char in word if char in TEXT_TO_MORSE]
        if letters:
            words.append(" ".join(letters))

    return "  ".join(words)


def morse_to_text(morse: str) -> str:
    normalized = morse.replace("—", "-").strip()
    words = []

    for morse_word in normalized.split("  "):
        letters = [MORSE_TO_TEXT[letter] for letter in morse_word.split() if letter in MORSE_TO_TEXT]
        if letters:
            words.append("".join(letters))

    return " ".join(words)


def transform(text: str) -> str:
    if is_morse(text):
        return morse_to_text(text)

    return text_to_morse(text)


def main() -> None:
    text_example = "Hola mundo"
    morse_example = ".... --- .-.. .-  -- ..- -. -.. ---"

    print(f"Texto: {text_example}")
    print(f"Morse: {transform(text_example)}")
    print()
    print(f"Morse: {morse_example}")
    print(f"Texto: {transform(morse_example)}")


    print("Texto: SOS")
    print(f"Morse: {transform('SOS')}")

if __name__ == "__main__":
    main()
