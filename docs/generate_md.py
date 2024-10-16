import os
import re

# Set up paths
input_file = 'docs/swaggerblocks.md'  # Your input file with Swagger blocks
output_dir = 'docs/md_references'          # Directory to save the grouped files
summary_file = os.path.join(output_dir, 'SUMMARY.md')  # File for the summary links in the same directory

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

# Write each group into a separate file and prepare summary links
summary_links = []

for group, content in grouped_content.items():
    group_file = os.path.join(output_dir, f'{group}.md')
    with open(group_file, 'w') as file:
        # Write the group header and content
        file.write(f'## {group}\n\n')
        file.write(content)

    print(f'Created file: {group_file}')
    
    # Add link to the summary
    summary_links.append(f'- [{group}](./{group}.md)')

# Write the SUMMARY.md file in the md_references folder
with open(summary_file, 'w') as summary:
    summary.write('# Summary\n\n')
    summary.write('\n'.join(summary_links))

print(f'Created SUMMARY.md: {summary_file}')

# Remove the input file after processing
if os.path.exists(input_file):
    os.remove(input_file)
    print(f'Removed input file: {input_file}')
