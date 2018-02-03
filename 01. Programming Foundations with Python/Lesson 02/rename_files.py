import os

def rename_files():
	#1 get files from folder
	file_list = os.listdir("prank")
	saved_path = os.getcwd()
	print("Current working directory: " + saved_path)
	os.chdir("prank")
	
	#2 rename each file
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()