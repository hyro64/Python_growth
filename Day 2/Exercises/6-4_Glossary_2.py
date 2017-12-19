glossary = {
	'print':"This is a method used by the language",
	'lists':"A set of information in one place",
	'Loops':"Allow you take the same action within every item in a list",
	'If': "Allows you to examine the current state of program and" +
		" respond appropriatly to that state",
	'Dictionaries': "Connect pieces of related information",
	'For': "The for loop is common way to repeate a process",
	'tuple': "A semi-permanent type of list",
	'Slicing':"An access to a single item",
	'elif-else chain':"The method to acess diffrent possible outcomes",
	'varible':"A methphorical box that holds data in memory",
	}
for term, meaning in sorted(glossary.items()):
	print(term.title() + ":" + meaning)
