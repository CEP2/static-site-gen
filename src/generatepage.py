import os
import re
from markdowntohtmlnode import markdown_to_html_node
from htmlnode import HTMLNode
from copy import copy

def extract_title(markdown):
    md_title = "# " 
    lines = markdown.split('\n')
    for l in lines:
        if len(l) > 2 and l.startswith(md_title):
            return l[2:].strip()
    raise ValueError(f"no md title present {markdown}")
    
def generate_page(from_path, template_path, dest_path):
    print(f"attempting to generate page...\n\tsource: {from_path}\n\tdest: {dest_path}\n\ttemplate:{template_path}")
    try:
        with open(from_path,'r') as from_file:
            markdown = from_file.read()
            with open(template_path,'r') as template_file:
                template = template_file.read()

                html_node = markdown_to_html_node(markdown)
                html = html_node.to_html()
                title = extract_title(markdown)

                output = copy(template)
                #replace tempalte locations
                title_target = "{{ Title }}"
                output = output.replace(title_target, title)

                content_target = "{{ Content }}"
                output = output.replace(content_target, html)
                # output to destination
                try:
                    #check if path exists, otherwise mkdirs
                    parent_folder, file_name = os.path.split(dest_path)
                    print(f"target folder: {parent_folder}\n\tfile: {file_name}")
                    os.makedirs(parent_folder,exist_ok=True)

                    with open(dest_path, "w") as out_file:
                        out_file.write(output)
                except Exception as e:
                    print(f"error writing {dest_path}: {e}")
    except Exception as e:
        print(f"error generating page: {e}")

def generate_pages_recursive(from_path, template_path, dest_path):
    # get list of files
    for file in os.listdir(from_path):
        # set up origin & dest files
    # if file (origin_file)
        # replace md w/html
        # gen page
    # if dir (not file)
        # gen page

    pass

    