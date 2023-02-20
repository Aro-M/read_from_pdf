list1 =[
    "Georgia:",
    "North Carolina:",
    "South Carolina:",
    "Massachusetts:",
    "Maryland:",
    "Virginia:",
    "Pennsylvania:",
    "Delaware",
    "New York:",
    "New Jersey:",
    "New Hampshire:",
    "Massachusetts:",
    "Rhode Island:",
    "Connecticut:",
    "New Hampshire:"
   ]
from PyPDF2 import PdfReader
import  re
def open_file(filename,list1):
    reader = PdfReader(filename)
    str_col = reader.pages[3]
    str_col1 = str_col.extract_text()
    str_col2 = reader.pages[4]
    str_col1 += str_col2.extract_text()
    pattern = r'(\w+\s?\w*):\n((?:\s*\w+[,\s]*)*)'
    lines = re.findall(pattern, str_col1)
    data_dic = {}
    for line in lines:
        state = line[0]
        names = []
        for name in line[1].split("\n"):
            if name.strip():
                names.append(name)
                data_dic[state] = names
    return  data_dic
print(open_file("us.pdf",list1))


