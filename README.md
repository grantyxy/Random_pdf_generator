# Random PDF Generator
## Features
- A generator that can generate random content pdf in conjunction with the vocabulary
- You can choose your own location for the generated files and choose your own lexical lists
- Support OS of binary: Windows only(currently), link: [Windows binray release](https://github.com/grantyxy/Random_pdf_generator/releases/tag/v1.0)
## Tutorial
- Run `/pdf_generator/random_pdf_generator.py`
- The program will ask you whether you want to choose your own location for the file generation:
  - If you enter your own path, the file will be stored in the location of your choice
  - If not, then the program will automatically create a folder named random_pdf_files on your computer's desktop to store the generated files
- Next the program will ask you if you want to use your own word list:
  - If you are using your own word list, please enter the path to your own word list file
  - If not, then the program will use the built-in word list file to generate the file for you
## Notes
- Each PDF will use Times New Roman font with a font size of 12.
- If you want to use your own thesaurus file, please keep the thesaurus file in the following format:  
  `word1`  
  `word2`  
  `...`  
  `wordn`  
  For example, like this:  
  `Deep`  
  `dark`  
  `fantasy`  
  `Van`  
  `Darkholme`
- If any developer can make it into a Python package, I would be very grateful.
  
  
