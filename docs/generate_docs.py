import os
import re

# Set up paths
input_file = 'api_documentation.md'  # Your input file with Swagger blocks
output_dir = 'grouped_docs'          # Directory to save the grouped files

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the input file and read the contents
with open(input_file, 'r') as file:
    content = file.read()

# Regular expression to match the group headings (e.g., ## Accounts)
group_pattern = re.compile(r'##\s([A-Za-z]+)')

# Split content into sections based on the groups
sections = re.split(group_pattern, content)

# Initialize an empty dictionary to hold the group names and corresponding content
grouped_content = {}

# Iterate over sections to separate group headers and their content
for i in range(1, len(sections), 2):
    group_name = sections[i].strip()  # The group name (e.g., Accounts)
    group_content = sections[i + 1]   # The corresponding Swagger blocks

    # Save the content in the dictionary
    if group_name not in grouped_content:
        grouped_content[group_name] = ""
    grouped_content[group_name] += group_content

# Write each group into a separate file
for group, content in grouped_content.items():
    group_file = os.path.join(output_dir, f'{group}.md')
    with open(group_file, 'w') as file:
        # Write the group header and content
        file.write(f'## {group}\n\n')
        file.write(content)

    print(f'Created file: {group_file}')
