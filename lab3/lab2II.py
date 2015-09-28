word_input = input('Enter the word: ')
word_input = word_input.lower()
if(word_input == word_input[::-1]):
  print("True")
else:
  print("False")