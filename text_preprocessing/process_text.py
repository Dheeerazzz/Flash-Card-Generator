from pdfminer.layout import LTChar
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar,LTLine,LAParams
import re
import os
# font_size of the main text = 10.5
#target_size = 10.5
path = "C:\\Users\\rishi\\OneDrive\\Desktop\\projects\\Venuratech\\ncert_pdf\\lebo103.pdf"
def seperate_text_by_font(path):
    Extract_Data=[]
    for page_layout in extract_pages(path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    for character in text_line:
                        if isinstance(character, LTChar):
                            Font_size=character.size
                Extract_Data.append([Font_size,(element.get_text())])
    return Extract_Data

def get_only_main_text(dir,target_size=10.5):
    main_text =[]
    context_list = seperate_text_by_font(dir)
    for context in context_list:
        if round(context[0],ndigits=4)== target_size:
            main_text.append(context[1])
    return main_text

def clean_main_text (dir):
    pattern_to_remove = r'\(Figure\s+[^)]*\)'
    main_text_list = get_only_main_text(dir)
    modified_text_list =[]
    for text in main_text_list:
        modified_text = text.replace("\n", " ")
        processed_text = re.sub(pattern_to_remove, '', modified_text)
        modified_text_list.append(processed_text)
    return "\n".join(modified_text_list)
        
print(clean_main_text(path))

