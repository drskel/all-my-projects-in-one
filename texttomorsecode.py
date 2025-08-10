symbols = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": ".-",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}
def text_to_morse(text):
    morse_code = []
    for char in text.lower():
        if char in symbols:
            morse_code.append(symbols.get(char, '?'))
        elif char == " ":
            morse_code.append(" ")
        else:
            morse_code.appnd('?')
    return " ".join(morse_code)
def maing():
    text = input('text: ')
    morse = text_to_morse(text)
    print(f'morse code: {morse}')
if __name__ == "__main__":
    maing()