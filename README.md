# Downloaded File Sorter
A simple Python script to sort files in the user's downloads folder.

## Requirements
- Python 3.6 or higher
## Installation
- Download or clone the repository to your local machine
- Navigate to the directory where the script is located
- Run the script with the command python file_sorter.py
## How it works
- The script reads the user's downloads folder and creates a list of files in the folder
- It then iterates through each file and checks the file extension to determine the file type (image, document, program, audio, compressed, video, or other)
- The file is then moved to the corresponding directory (e.g. images go to the "pictures" folder)
- If the corresponding directory does not exist, it is created
## Customization
You can change the directory where the files will be sorted by modifying the arrange_dir variable at the top of the script. You can also modify the directory names by changing the variables comp_fold, program_fold, document_fold, audio_fold, pictures_fold, and videos_fold.

## Note
The script currently only works for Windows systems and only checks for specific file extensions. You can add or remove file extensions by modifying the regular expressions in the check_file_type function.
