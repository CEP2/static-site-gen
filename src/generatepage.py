def extract_title(markdown):
    md_title = "# "
    if markdown.startswith(md_title):
        return markdown[len(md_title):]