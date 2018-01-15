import os

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
			return

		if letter in word_bank:
			for index in range(len(word)): 
				if letter == word_bank[index]:
					guess[index] = letter
			pretty_print(guess)
		else:
			lose_life(letter)
		print(' ')

	def lose_life(letter):
		nonlocal user_guesses, life, guess, gui_response
		if letter in user_guesses:
			print('You have already guessed this letter.')
			print(user_guesses)
		else: 
			life -= 1
			user_guesses += [letter]
			if gui_response == True:
				print_man(life) 
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
	print('Would you like to play a graphical version of the game? (Y/N)')
	gui = input()
	gui_response = True
	if gui == 'Y':
		gui_response = True
	else:
		gui_response = False

	print('Type in a word.')
	word = input()

	for x in range(25):
		print('')
	os.system('cls' if os.name == 'nt' else 'clear') #Clearing the screen.


	word_bank = [letter for letter in word]
	guess = ['_' for letter in word]

	if gui_response == True:
		print_man(life)

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

def print_man(life):
	if life == 0: 
		print('_________')
		print('|        |')
		print('|        |')
		print('|        ☹')
		print("|       /|\\")
		print('|       / \\')
		print('|         ')
		print('|         ')
		print('|         ')
		print('|____')
	if life == 1: 
		print('_________')
		print('|        |')
		print('|        |')
		print('|        O')
		print("|       /|\\")
		print('|       / ')
		print('|         ')
		print('|         ')
		print('|         ')
		print('|____')	
	if life == 2: 
		print('_________')
		print('|        |')
		print('|        |')
		print('|        O')
		print("|       /|\\")
		print('|       	 ')
		print('|         ')
		print('|         ')
		print('|         ')
		print('|____')
	if life == 3: 
		print('_________')
		print('|        |')
		print('|        |')
		print('|        O')
		print("|       /|")
		print('|         ')
		print('|         ')
		print('|         ')
		print('|         ')
		print('|____')
	if life == 4: 
		print('_________')
		print('|        |')
		print('|        |')
		print('|        O')
		print("|       / ")
		print('|         ')
		print('|         ')
		print('|         ')
		print('|         ')
		print('|____')
	if life == 5: 
		print('_________')
		print('|        |')
		print('|        |')
		print('|        O')
		print("|         ")
		print('|         ')
		print('|         ')
		print('|         ')
		print('|         ')
		print('|____')	
	if life == 6: 
		print('_________')
		print('|        |')
		print('|        |')
		print('|         ')
		print("|         ")
		print('|         ')
		print('|         ')
		print('|         ')
		print('|         ')
		print('|____')
			
play()




