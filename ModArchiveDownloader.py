import urllib.request, sys, os, re, argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Tool to download a range of modules from ModArchive, specified by their moduleid number')
	parser.add_argument('save_directory')
	parser.add_argument('FROM')
	parser.add_argument('TO')

	args = parser.parse_args()

	savedirectory = args.save_directory
	find_orig_filename = re.compile("filename=(.+)")

	os.chdir(savedirectory)

	for i in range(int(args.FROM), int(args.TO) + 1):
		filename, headers = urllib.request.urlretrieve('https://api.modarchive.org/downloads.php?moduleid={}'.format(i), filename="moduleid_{}".format(i))

		match = find_orig_filename.search(headers.as_string())

		# there are some moduleid numbers that can't be found
		if match is not None:
			orig_filename = match.group(1)
			print("Downloaded {}".format(orig_filename))
			print("\tRenaming {} to {}".format(filename, match.group(1)))
			os.rename(filename, orig_filename)
		else:
			print("\tCould not download {}".format(filename))
