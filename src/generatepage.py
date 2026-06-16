import os
import re
def extract_title(markdown):
    md_title = "^# .*$" # regex pattern
    match = re.match(md_title, markdown)
    if match is None:
        raise ValueError(f"no md title present")
    else:
        title = match[0]
        if len(title) <= 2:
            raise ValueError ("no title content")
    return title[2:].strip()
    
def generate_page(from_path, template_path, dest_path):
    print(f"attempting togenerate page...\n\tsource: {from_path}\n\tdest: {dest_path}\n\ttemplate:{template_path}")

    
    with open(from_path,'r') as from_file:
        from_contents = os.read(from_file)

        with open(template_path,'r') as template_file:
            template_contents = os.read(template_file)

    