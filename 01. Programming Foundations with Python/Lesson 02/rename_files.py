import os

def rename_files():
	#1 get files from folder
	file_list = os.listdir("prank")
	print(file_list)
	#2 rename each file

rename_files()