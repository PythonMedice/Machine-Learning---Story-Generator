import os
import docx

file_names = []

def get_list(path):
    """Creates a list of file names in a directory."""
    files = os.listdir(path)
    for f in files:
        file_names.append(f)

get_list('/users/scatt/desktop/python_projects/AI Paper/')
del file_names[-1]
del file_names[-1]
print(file_names)
"""
Had to add two del statements. The main .py file and other non .docx files
break the loop.
"""


fullText = []
def getText(list_name):
    """Strips text only from docx and puts everything into a list."""
    for filename in list_name:
        try:
            doc = docx.Document(filename)
            for para in doc.paragraphs:
                fullText.append(para.text)
        except FileNotFoundError:
            continue


all_text = []
def collect_all_text(list_name):
    """Collect text lists from all papers and combine."""
    for text in list_name:
        all_text.append(text)
    #print(all_text)
    with open("all_text.txt", "w") as output:
        output.write(str(all_text))

getText(file_names)
collect_all_text(fullText)
