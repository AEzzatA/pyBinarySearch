def bSearch(Phrase, SortedList):
	if (Phrase < SortedList[0]) or (Phrase > SortedList[len(SortedList)-1]):
		return "Item isn't in the givin list"
		#sys.exit(0) #Import sys and un-comment these lines if you want!
	if (len(SortedList) == 2):
		if (Phrase == SortedList[0]):
			return SortedList[0]
			#sys.exit()
		else: 
			return SortedList[1]
			#sys.exit(0)
	if(Phrase < (len(SortedList)/2)):
		bSearch(Phrase,SortedList[0:len(SortedList)/2 -1])
	else:
		bSearch(Phrase, SortedList[len(SortedList)/2 : len(SortedList)-1])
