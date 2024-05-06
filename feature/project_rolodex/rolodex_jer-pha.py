from re import search, sub


def rolodex():
	"""
	Allow users to search for a name/number in name_number.txt and
	return the matching number/name, if found. They should be able to
	exit the search by typing 'quit.'
	"""
	people = []

	def import_file(filename: str) -> list[tuple[str, str]]:

		"""
		Import a filename and return a list of tuples that are pairs
		of names and numbers found on the file. The file will always have
		a 10-digit number with two hyphens at the end of each line,
		which means the last 12 characters on the line are the number.
		The space before the number should be removed when creating
		pairs.

		To improve user search, the lowercase version of all names will be
		saved, along with the number without the hyphens.
		"""
		with open(filename) as file:
			for line in file:
				people.append((
					line.rstrip()[:-13],
					line.rstrip()[:-13].lower(),
					line.rstrip()[-12:],
					line.rstrip()[-12:].replace('-', ''),
				))

		file.close()


	def user_input() -> None:
		"""
		Process user input. If they type 'quit' then the process should
		exit. If their input contains letters, check for names in the
		list of pairs. If a name is found, return its matching number.
		If the input does not contain letters, check for the number,
		regardless of characters/whitespace.

		If either the name or number is not found, inform the user and
		take another input. If the input is found, inform the user the
		matching name/number.
		"""
		open_rolodex = True

		while open_rolodex:
			text = input()
			text_lower = text.strip().lower()

			if text_lower in ('quit', 'n'):
				print('Thank you for using the Rolodex!')
				open_rolodex = False
				break
			elif text_lower == 'y':
				print('Please enter another name or number:')
				continue

			is_name = search('[a-z]', text_lower)
			result = ''

			if is_name:
				i = 1
			else:
				i = 3
				text_lower = sub('[^0-9]', '', text_lower)

			for person in people:
				if person[i] == text_lower and is_name:
					result = f"{person[0]}'s phone number is {person[2]}."
					break
				elif person[i] == text_lower:
					result = f"{person[2]} is {person[0]}'s phone number."
					break

			if result:
				print(result)
			else:
				print(f'{text} was not found in the Rolodex.')

			print('Would you like to search again? y/n')


	def start() -> None:
		import_file('name_number.txt')
		print('Welcome to the Rolodex! Please enter a name or number:')
		user_input()


	start()


if __name__ == '__main__':
	rolodex()
