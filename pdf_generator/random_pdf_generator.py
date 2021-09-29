import os
import random
import string
import time

from fpdf import FPDF


def delete_folder_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
    return


# def generate_random_lowercase():
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(10))
#
#
# def generate_random_uppercase():
#     letters = string.ascii_uppercase
#     return ''.join(random.choice(letters) for i in range(10))
#
#
# def generate_random_ascii():
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for i in range(10))
#
#
# def generate_random_digits():
#     letters = string.digits
#     return ''.join(random.choice(letters) for i in range(10))
#
#
# def generate_random_punctuation():
#     letters = string.punctuation
#     return ''.join(random.choice(letters) for i in range(10))
#
#
# def generate_random_string(length=1000):
#     letters = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.digits + \
#               string.punctuation
#     return "".join(random.choice(letters) for _ in range(length)) if length is not None \
#         else "".join(random.choice(letters) for _ in range(1000))

# Generate the random filename, default length is 10
def generate_random_filename():
    length = 10
    letters = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.digits
    file_name = "".join(random.choice(letters) for _ in range(length))
    return file_name


def get_word_list(word_list_file):
    with open(word_list_file, "r") as fh:
        word_list = [x for x in fh.read().split("\n")]
        return word_list


def generate_random_paragraph(word_list_file):
    word_list = open(word_list_file.strip('"'), "r").read().split("\n")
    s = " ".join(random.choice(word_list) for _ in range(22))
    s += "."
    s = s.capitalize()
    return s


def generate_random_pdf(save_path, word_list_file="most common words.txt"):
    if word_list_file == "":
        word_list_file = "most common words.txt"
    pdf = FPDF()
    pdf.set_font("Times", size=12)
    pdf.add_page()
    for _ in range(52):
        pdf.cell(50, 10, txt=generate_random_paragraph(word_list_file), ln=1)
    file_name = generate_random_filename()
    pdf.output(save_path + f"/{file_name}.pdf")


if __name__ == "__main__":
    path = input("Please enter the folder path where the randomly generated files are stored: "
                 "(If you do not enter the path, "
                 "a result folder will be generated on your computer desktop to store the generated files.)").strip('"')
    if path != "":
        delete_folder_files(path)
    else:
        parent_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        path = os.path.join(parent_dir, "random_pdf_files")
        os.mkdir(path)
    run_times = int(input("How many files you want to generate? "))
    have_own_word_list = input("You have your own lexicon? If yes, input the path of lexicon; "
                               "if not please left blank, program will use default lexicon file")
    start = time.perf_counter()
    if have_own_word_list is not None:
        for i in range(run_times):
            generate_random_pdf(path, have_own_word_list)
    else:
        for i in range(run_times):
            generate_random_pdf(path)
    end = time.perf_counter()
    print(f"Time used: {end - start:.2f}s")
