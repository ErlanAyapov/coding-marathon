distance_num = 0

def hamming_distance(text1, text2):
	global distance_num

	for x in range(len(text1)):
		
		if not text1[x] == text2[x]:
			distance_num += 1

	return distance_num 