import re


class Solutions:  # jangan di copy
    def solution(s):
        # Receive Input as List
        input = s
        print(input)

        # Convert input to lowercase
        convert_lower = input.lower()

        # Split convert_lower to list
        split = (list(convert_lower))

        lexicon = {
            "a": "100000",
            "b": "110000",
            "c": "100100",
            "d": "100110",
            "e": "100010",
            "f": "110100",
            "g": "110110",
            "h": "110010",
            "i": "010100",
            "j": "010110",
            "k": "101000",
            "l": "111000",
            "m": "101100",
            "n": "101110",
            "o": "101010",
            "p": "111100",
            "q": "111110",
            "r": "111010",
            "s": "011100",
            "t": "011110",
            "u": "101001",
            "v": "111001",
            "w": "010111",
            "x": "101101",
            "y": "101111",
            "z": "101011",
            " ": "000000",
        }

        # Find letters and translate from lexicon
        find = list(map(lexicon.get, split))

        # Find the capital inside input and convert to lowercase
        find_capital = re.findall('([A-Z])', input)
        print(find_capital)
        for word in range(len(find_capital)):
            find_capital[word] = find_capital[word].lower()
        find_capital_lexed = list(map(lexicon.get, find_capital))

        # Replace
        modified_base_list = [next(("000001" + y for y in find_capital_lexed if y == x), x) for x in find]

        # Print result
        result = ''.join(modified_base_list)

Solutions.solution("The quick brown fox jumps over the lazy dog")