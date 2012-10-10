def bSearch(Phrase, SortedList):
	Low = 0
	High = len(SortedList) - 1
	Mid = (High + Low) // 2
	if (Phrase < SortedList[Low]) or (Phrase > SortedList[High]):
		return "Item isn't in the givin list"
	if (High == 2):
		if (Phrase == SortedList[0]):
			return SortedList[0]
		else: 
			return SortedList[1]
	if Phrase < Mid:
		bSearch(Phrase,SortedList[0 : Mid])
	else:
		bSearch(Phrase, SortedList[Mid : High])

# A unit test to test the algorithm 


def main():
	my_list = [34,32,34,234,23,42,43,234,234,2,423,41,3,12,123,13,13,12,3,423,42,4]
	my_list = sorted(my_list)
	Sort = bSearch(2, my_list)
	print Sort



if __name__ == "__main__":
    main()
