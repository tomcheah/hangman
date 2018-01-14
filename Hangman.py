def play():
	def guess_func():
		nonlocal user_guesses, life, guess
		print('Incorrect letters: ' + str(user_guesses))
		print('Guess a letter.')
		letter = input()
		if letter == 'exit()':
			exity()

		if len(letter) > 1:
			print('Invalid input. Please try again.')
			print('')
			guess_func()

		if letter in word_bank:
			for index in range(len(word)): 
				if letter == word_bank[index]:
					guess[index] = letter

			# temp = [letter if letter == x else '_' for x in word_bank]
			# guess = [x if x != '_' else x for x in temp]
			pretty_print(guess)
		else:
			lose_life(letter)
			# life -= 1
			# user_guesses += letter
			# #fix pluralirty
			# #put this in a function. test whether the guess was already in the "guessed letters" one. >> take care of it
			# print('Incorrect letter. You have ' + str(life) + ' guesses remaining.')
			# print('')
			# pretty_print(guess)

		print(' ')

	def lose_life(letter):
		nonlocal user_guesses, life, guess
		if letter in user_guesses:
			print('You have already guessed this letter.')
			print(user_guesses)
		else: 
			life -= 1
			user_guesses += [letter] 
			plurality(life)
			print('')
			pretty_print(guess)

	def plurality(life): 
		if life == 1:
			print('Incorrect letter. You have 1 life remaining.')
		else:
			print('Incorrect letter. You have ' + str(life) + ' lives remaining.')

	def exity():
		print('Would you like to exit the game? (Y/N)')
		reply = input()
		if reply == 'Y':
			quit()
		else: 
			guess_func()

	user_guesses = []
	life = 6

	print('Welcome to Hangman!')
	print('Type in a word.')
	word = input()
	for x in range(25):
		print('')

	word_bank = [letter for letter in word]
	guess = ['_' for letter in word]
	pretty_print(guess)
	print('') 
	print('The word is ' + str(len(guess)) + ' letters long.')
	while '_' in guess and life > 0:
		guess_func()
	if life > 0:
		print('Congratulations! You have guessed the word correctly.')
		replay()
	else: 
		print('You have died.')
		print("The word was '" + word + "'.")
		replay()

def replay():
	print('Would you like to play again? (Y/N)')
	reply = input()
	if reply == 'Y':
		play()
	else:
		return

def pretty_print(guess_list):
	for letter in guess_list:
		print(letter, end = ' ')
	print('')


# print('_________')
# print('|        |')
# print('|        |')
# print('|        O')
# print("|       /|\\")
# print('|        |')
# print('|       / \\')
# print('|         ')
# print('|         ')
# print('|         ')
# print('|____')



