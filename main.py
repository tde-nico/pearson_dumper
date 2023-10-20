from lib_pdf import combine_pages, download_pages


def download(book: str, save_path: str) -> None:
	combine_pages(download_pages(book), save_path)


def main():
	book = input('foxitAssetURL: ')
	save_path = input('Where to save (default: output.pdf): ')
	if save_path == '':
		save_path = 'output.pdf'
	print('Download Starting...')
	download(book, save_path)
	input('All Done (Press Enter to Exit)')


if __name__ == "__main__":
	main()
