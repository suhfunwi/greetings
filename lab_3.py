def camelcase(sentence):
    # Convert sentence to camelCase
    title_case = sentence.title()
#     Uppercase letter of each word
    upper_camel_cased = title_case.replace(' ', '')
#     removes spaces
#     Lowercase first letter, join with rest of string
#     Slices don't produce index out of bounds errors
#     So this still works on empty strings, strings of length 1
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]


def banner():
    """Display program name"""
    message = 'Awesome camelcase program!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

def instructions():
    print('Enter a sentence and this program will convert it to camelcase.')


def main():
    banner()
    instructions()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()

