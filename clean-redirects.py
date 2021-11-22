import argparse
import re
import requests
import time
from pathlib import Path

def cleanFile(in_file = "input.txt", out_file = None, limit = None, verbose=False):
	if(limit):
		limit = int(limit)
	if not out_file:
		name_parts = in_file.split('.')
		out_file = "".join(name_parts[:-1]) + '-output.' + "".join(name_parts[-1])

	text = Path(in_file).read_text()

	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',text)

	count = 0
	for url in urls:
		count += 1
		responses = requests.get(url)
		text = text.replace(url, responses.url)
		if verbose:
			print(url, "=>", responses.url)
		if limit and count >= limit:
			break
	with open(out_file, "w") as out:
	    out.write(text)

def main():
	parser = argparse.ArgumentParser(prog='clean-redirects', description='parse all links within a file and replace them with the final destination URL if they had redirects')
	parser.add_argument('--file', '-f', help='Path to the input file ')
	parser.add_argument('--out', '-o', help='Path to output file')
	parser.add_argument('--verbose', '-v', help='Display detailed log')
	parser.add_argument('--limit', '-l', help='Limits the number of urls processed (starting from the begining)')
	args = parser.parse_args()
	cleanFile(in_file=args.file, out_file=args.out, limit=args.limit, verbose=args.verbose)
if __name__ == "__main__":
    main()