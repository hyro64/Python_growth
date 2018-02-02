def make_album(artist, album, tracks = ''):
	"""Returns a dictionary of albums"""
	completed_album = {"Artist: ": artist, "Album: ": album}
	if tracks:
		completed_album['tracks'] = tracks
	return completed_album
	
completed = make_album("jimi","Voodoo Child", tracks = 12)

print(completed)
