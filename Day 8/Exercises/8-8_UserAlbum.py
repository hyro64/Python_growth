def make_album(artist, album, tracks = ''):
	"""Returns a dictionary of albums"""
	completed_album = {"Artist: ": artist, "Album: ": album}
	if tracks:
		completed_album['tracks'] = tracks
	return completed_album 

while True:
	artist = input("\n Enter the artist name: \nEnter 'q' to quit\n")
	if artist == 'q':
		break	
	album = input("\nEnter the album name: \nEnter 'q' to quit\n")
	if album =='q':
		break
	tracks = input("\nEnter the amount of tracks: \nEnter 'q' to quit\n")
	if tracks =='q':
		break
		
	completed_album = make_album(artist,album, tracks)
	print(completed_album)
