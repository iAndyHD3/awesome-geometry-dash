#this should really be fixed in the library but dev seems inactive
#so im just making a wrapper
from slmd import sort_string

def find_contents_table(content, lineCount):
    # Split the content by lines
    
    # Find the index of the line containing "contents"
    for i, line in enumerate(lineCount):
        if "contents" in line.lower():
            return i
    
    # If "contents" table not found, return -1
    return -1

def main(filename):
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        lineCount = content.split('\n')

    # Find the index of the "contents" table
    contents_table_index = find_contents_table(content, lineCount)

    # If "contents" table found, get the content after it
    if contents_table_index != -1:
        lines = content.splitlines()
        for i in range(contents_table_index, len(lineCount)):
            if not lines[i]:
                contents_table_index = i
                break
        
        content_after_contents = '\n'.join(lines[contents_table_index + 1:])
        sorted_content_after_contents = sort_string(content_after_contents, case_sensitive=False)

        # Insert the sorted content back after the "contents" table
        lines = lines[:contents_table_index + 1] + sorted_content_after_contents.splitlines()
        result = '\n'.join(lines)
    else:
        # If "contents" table not found, sort the whole content
        result = sort_string(content, case_sensitive=False)

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(result)

if __name__ == '__main__':
    filename = "README.md"
    main(filename)
