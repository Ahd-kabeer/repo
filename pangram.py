
def checkPangram(s):
	List = []
	
	for i in range(26):
		List.append(False)
		
	# converting the sentence to lowercase and iterating
	# over the sentence
	for c in s.lower():
		if not c == " ":

			# make the corresponding entry True
			List[ord(c) -ord('a')]= True
			
	# check if any character is missing then return False
	for ch in List:
		if ch == False:
			return False
	return True

# Driver Program to test above functions
sentence = "Glib jocks quiz nymph to vex dwarf"

if (checkPangram(sentence)):
	print ("'"+ sentence+ "' is a pangram")
else:
	print ("'"+ sentence+ "' isn't a pangram")


