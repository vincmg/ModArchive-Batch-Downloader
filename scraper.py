import urllib.request, sys, os, re

if __name__ == '__main__':
	if sys.argv[1] in ['help', '-h', '--help']:
		print("Usage: python3 scriptname.py save_directory FROM TO")
		sys.exit()

	savedirectory = sys.argv[1]
	find_orig_filename = re.compile("filename=(.+)")

	os.chdir(savedirectory)

	for i in range(int(sys.argv[2]), int(sys.argv[3]) + 1):
		filename, headers = urllib.request.urlretrieve('https://api.modarchive.org/downloads.php?moduleid={}'.format(i), filename=i)
		print("Downloaded moduleid {}".format(filename))

		# there should always be a match unless the website has changed.
		match = find_orig_filename.search(headers.as_string())
		orig_filename = match.group(1)
		print("\tRenaming {} to {}".format(filename, match.group(1)))
		os.rename(filename, orig_filename)
