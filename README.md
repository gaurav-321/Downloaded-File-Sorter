# File Sorter 📚

## Description
File Sorter is a Python script designed to organize files in your user's Downloads folder based on their file types. This tool helps keep your system tidy and makes finding specific files easier.

## Features
- **Automatic Organization:** Sorts files into respective folders (e.g., images, documents, videos).
- **User-Friendly:** Simple installation and usage instructions.
- **No External Dependencies:** Built using Python standard library, making it lightweight and easy to run.

## Installation
To use File Sorter, follow these steps:

1. Ensure you have Python 3.6 or higher installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/gag3301v/File-Sorter.git
   ```
3. Navigate to the project directory:
   ```bash
   cd File-Sorter
   ```

## Usage
Here’s how you can use the `file_sorter.py` script:

```python
# Import the main function from file_sorter module
from file_sorter import sort_files

# Call the function to organize files in your Downloads folder
sort_files()
```

The script will print the destination path of each file before moving it, ensuring you know where each file has been sorted.

## Configuration
No additional configuration is required. The script uses Python's built-in `os` and `shutil` modules for file operations.

## Tests
Tests are not available at this time. However, you can manually run the script to ensure it works as expected.

## Project Structure
```
File-Sorter/
├── README.md
├── files_manager.py
└── file_sorter.py
```

- `README.md`: This file.
- `files_manager.py`: Contains utility functions for organizing files.
- `file_sorter.py`: The main script that orchestrates the sorting process.

## Contributing
Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request. Follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive messages.
4. Push your branch and create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for using File Sorter! 🌟