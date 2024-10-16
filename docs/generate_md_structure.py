import os

# Function to generate the structure for SUMMARY.md based on the directory and file names
def generate_summary_md():
    summary_lines = ["# Table of contents", "* [API Documentation](README.md)", "* [API reference](api-reference/README.md)"]

    # Recursively traverse the api-reference directory
    for root, dirs, files in os.walk('md_references'):
        # Sort directories and files to maintain a consistent order
        dirs.sort()
        files.sort()

        # Adjust indentation for each folder/file level
        level = root.replace('api-reference', '').count(os.sep)
        indent = '  ' * (level + 1)

        # Add directories (with README.md if exists) to the summary
        if 'README.md' in files:
            relative_path = os.path.join(root, 'README.md').replace('\\', '/')
            section_title = os.path.basename(root).capitalize()
            summary_lines.append(f"{indent}* [{section_title}]({relative_path})")

        # Add files (except README.md) to the summary
        for file in files:
            if file != 'README.md' and file.endswith('.md'):
                relative_path = os.path.join(root, file).replace('\\', '/')
                file_title = os.path.splitext(file)[0].replace('_', ' ').capitalize()
                summary_lines.append(f"{indent}  * [{file_title}]({relative_path})")

    return '\n'.join(summary_lines)

# Function to update the SUMMARY.md file
def update_summary_md():
    summary_content = generate_summary_md()
    with open('SUMMARY.md', 'w') as summary_file:
        summary_file.write(summary_content)

    print("SUMMARY.md has been updated.")

# Call the function to update SUMMARY.md
update_summary_md()
