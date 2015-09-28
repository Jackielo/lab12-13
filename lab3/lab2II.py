word_input = input.lower('Enter the word: ')

if(word_input == word_input[::-1]):
  print("True")
else:
  print("False")