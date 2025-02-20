import os
import chardet

# Detect File Encoding
def detect_encoding(file_path):
	"""Detects the character encoding of a file."""
	with open(file_path, 'rb') as f: #open file in binary mode
		result = chardet.detect(f.read()) # Detect encoding
	return result['encoding']

# Recover Corrupted Text Files
def recover_text_file(file_path):
	"""Attempts to open a corrupted text file with the correct encoding."""
	encoding = detect_encoding(file_path) # Detect encoding
	try:
		with open(file_path, 'r', encoding=encoding, errors="replace") as f:
			content = f.read()
		print("File successfully read!")
		return content
	except Exception as e:
		print(f"Error occurred: {e}")
		return None

# Scan Directory for Deleted or Moved Files
def simulate_deleted_file_recovery(directory):
	"""Scans the directory to find missing or misplaced text files."""
	recovered_files = []
	for root, dirs, files in os.walk(directory): # Traverse directory
		for file in files:
			if file.endswith('.txt'): # Only process .txt files
				file_path = os.path.join(root, file)
				recovered_files.append(file_path)
	return recovered_files

# Main Execution Block
if __name__ == "__main__":
	directory = "test_files" # Directory to scan for text files
	found_files = simulate_deleted_file_recovery(directory) # Find missing files

	for file in found_files:
		print(f"Recovered File: {file}")
		content = recover_text_file(file)
		if content:
			print(content)
