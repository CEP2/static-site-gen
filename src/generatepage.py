import os
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
    
def generate_page(from_path, template_path, dest_path, basepath=None):
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

                if basepath:
                    # update href & src with basepath
                    output = output.replace("href=\"/",f"href=\"{basepath}")
                    output = output.replace("src=\"/",f"src=\"{basepath}")
                # output to destination
                try:
                    #check if path exists, otherwise mkdirs
                    parent_folder, file_name = os.path.split(dest_path)
                    os.makedirs(parent_folder,exist_ok=True)

                    with open(dest_path, "w") as out_file:
                        out_file.write(output)
                except Exception as e:
                    print(f"error writing {dest_path}: {e}")
    except Exception as e:
        print(f"error generating page: {e}")

def generate_pages_recursive(from_path, template_path, dest_path, basepath=None):
    # get list of files
    for file in os.listdir(from_path):
        # set up origin & dest files
        from_file = os.path.join(from_path, file)
        dest_file = os.path.join(dest_path, file)
        # if file (origin_file)
        if os.path.isfile(from_file):
            # replace md w/html
            dest_file = dest_file.replace(".md", ".html")
            # gen page
            generate_page(from_file, template_path, dest_file, basepath)
        # if dir (not file)
        else:
            # gen page recursive w/folder names
            generate_pages_recursive(from_file, template_path, dest_file, basepath)

    