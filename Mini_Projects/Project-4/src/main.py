# This module acts as entry point to execute
import argparse
from directory_analyzer import listing_files,searching_files


parser=argparse.ArgumentParser()
parser.add_argument("path",type=str)
args=parser.parse_args()
path=args.path


option=input("Enter 'ls' for listing files in director\nEnter 'sr' for searching files")

match (option):
    case 'ls':
        listing_files(path)
    case 'sr':
        extension=input("Enter the extension to search:")
        searching_files(path,extension)
    

