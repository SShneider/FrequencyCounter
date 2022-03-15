##USE THIS FILE TO MODIFY DEFAULT PROGRAM BEHAVIOR##

#if you want to display interface for argument input set USER_MENU_ENABLED to True.
#if you want the program to batch process or process through command line arguments only set it to False
USER_MENU_ENABLED = True

#if it is a part of an automated pipeline the program will behave using the following settings:

DEFAULT_MINIMUM_LENGTH_WORDS = 1 #only words of this length or above(inclusive) are returned
STOP_WORDS = []	#filters out any stopword
DEFAULT_DISPLAY_X_MOST_POPULAR_WORDS = -1 #how many (-1 = all)
DEFAULT_SAVE_OUTPUT_BEHAVIOR = True 	#default value if command line args arent passed

RAISE_EXCEPTIONS = True #whether you want errors to be raised, can interruput batch process
SAVE_LOGS = True
PRINT_EXCEPTIONS = True #prints exceptions into the terminal. Independent of RAISE_EXCEPTIONS

