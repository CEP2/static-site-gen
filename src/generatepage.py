import os
import re
from markdowntohtmlnode import markdown_to_html_node
from htmlnode import HTMLNode
from copy import copy

def extract_title(markdown):
    md_title = "^# .*$" # regex pattern
    match = re.match(md_title, markdown)
    if match is None:
        raise ValueError(f"no md title present {markdown}")
    else:
        title = match[0]
        if len(title) <= 2:
            raise ValueError ("no title content")
    # may need to replace title line with nothing
    return title[2:].strip()
    
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

                content_target = "{{ Content}}"
                output = output.replace(content_target, html)
                # output to destination
                try:
                    with open(dest_path, "w") as out_file:
                        pass
                except Exception as e:
                    print(f"error opening {dest_path}: {e}")
    except Exception as e:
        print(f"error generating page: {e}")

    