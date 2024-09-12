name = input('What is your name?')
birth_month = input('What is your birth month?')
name_length = len(name)
print(f'Hello, {name}!')
print(f'There are {len(name)} letters in your name')
# can put simple expressions in format strings
# They are your friend
if birth_month.lower() == 'august':
    print('Happy birthday month!')