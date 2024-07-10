##Robert Fernandez
##Complete
##This program will ask the user to input a sentence to make the upper case change to lower case and vice versa.

sentence = input('Input a sentence with lower, upper, and a special character: ')

new_sentence = ''

for c in sentence:
  if c.islower():
    new_sentence += c.upper()
  elif c.isupper():
    new_sentence += c.lower()
  else:
    new_sentence += c

print(f'orginial: {sentence}')
print(f'new: {new_sentence}')
