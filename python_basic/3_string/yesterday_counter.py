f = open("yesterday.txt", "r")
yesterday_lyric = ""
while 1:
	line = f.readline()
	# print(line)
	if not line:
		break
	yesterday_lyric = yesterday_lyric + line.strip() + "\n"
	# print (yesterday_lyric)
f.close()

small_n_of_yesterday = yesterday_lyric.capitalize().count("Yesterday")
titled_n_of_yesterday = yesterday_lyric.lower().count("yesterday")
big_n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")

print ("Number of a Word 'Yesterday'" , small_n_of_yesterday)
print ("Number of a Word 'Yesterday'" , titled_n_of_yesterday)
print (f"Number of a Word 'YESTERDAY' {big_n_of_yesterday} ")