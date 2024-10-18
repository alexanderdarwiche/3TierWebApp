import os
import re

# Set up paths
input_file = 'docs/swaggerblocks.md'  # Your input file with Swagger blocks
output_dir = 'docs/api-s/api-2.0'     # Directory to save the grouped files
summary_file = os.path.join('docs', 'SUMMARY.md')  # Path for SUMMARY.md
api_version = '2.0'  # Set the API version
api_section_marker = f'[API {api_version}]'  # Marker for API section

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
api_summary_entries = []

# Write the README.md for the API version
readme_file = os.path.join(output_dir, 'README.md')
with open(readme_file, 'w') as readme:
    readme.write(f"description: 'Younium API - Version: {api_version}'\n")
    readme.write('---\n\n')
    readme.write(f"# API {api_version}\n")
print(f'Created README.md for API version {api_version}')

# Add README.md to the API section in SUMMARY.md
api_summary_entries.append(f'* [API {api_version}](api-s/api-{api_version}/README.md)')

# Iterate over sections to separate group headers and their content
for i in range(1, len(sections), 2):
    group_name = sections[i].strip()  # The group name (e.g., Accounts)
    group_content = sections[i + 1]   # The corresponding Swagger blocks

    # Save the content in the dictionary
    if group_name not in grouped_content:
        grouped_content[group_name] = ""
    grouped_content[group_name] += group_content

# Write each group into a separate file and build the API part of the SUMMARY.md
for group, content in grouped_content.items():
    group_file = os.path.join(output_dir, f'{group.lower()}.md')  # Convert group names to lowercase for file paths
    with open(group_file, 'w') as file:
        # Write the group header and content
        file.write(f'## {group}\n\n')
        file.write(content)

    # Add the group to the API section in SUMMARY.md with the correct relative path (no "docs/" prefix)
    api_summary_entries.append(f'  - [{group}](api-s/api-{api_version}/{group.lower()}.md)')
    
    # Add nested entries for sub-paths
    for line in content.splitlines():
        match = re.match(r'^\s*-\s*\[(.*?)\]\s*\((.*?)\)', line)
        if match:
            sub_path_name = match.group(1)
            sub_path_file = f'api-s/api-{api_version}/{group.lower()}.md'
            api_summary_entries.append(f'    - [{sub_path_name}]({sub_path_file})')

    print(f'Created file: {group_file}')

# Read the existing SUMMARY.md file
if os.path.exists(summary_file):
    with open(summary_file, 'r') as summary:
        summary_content = summary.read()
else:
    summary_content = ''

# Remove the entire [API 2.0] section
if api_section_marker in summary_content:
    # Regex to match the [API 2.0] section and everything that follows until the next top-level marker (e.g., another heading)
    api_section_regex = re.compile(rf'(\* {re.escape(api_section_marker)}[\s\S]*?)(\* \[[A-Za-z0-9\s]+\]\([^\)]*\))', re.MULTILINE)
    summary_content = re.sub(api_section_regex, r'\2', summary_content)

# Split the content to insert the new API section after the [API:s] marker
api_s_marker = '[API:s](api-s/README.md)'
summary_parts = summary_content.split(api_s_marker)

# The first part is everything before the API section, the second part is everything after (if exists)
summary_before_api = summary_parts[0] if len(summary_parts) > 0 else ''
summary_after_api = summary_parts[1] if len(summary_parts) > 1 else ''

# Rebuild the SUMMARY.md with proper nesting for API 2.0 under API:s
with open(summary_file, 'w') as summary:
    # Write content before [API:s]
    summary.write(summary_before_api)
    
    # Re-insert the [API:s] marker
    summary.write(f'{api_s_marker}\n\n')
    
    # Properly indent and nest API 2.0 section under API:s
    summary.write('  * [API 2.0](api-s/api-2.0/README.md)\n')  # Nested under API:s with two spaces for indentation
    summary.write('\n'.join([f'    {entry}' for entry in api_summary_entries[1:]]))  # Indent all other entries under API 2.0 by 4 spaces
    
    # Append remaining content after [API:s]
    summary.write(summary_after_api)

print(f'Updated SUMMARY.md at {summary_file}')

# Remove the swaggerblocks.md file after processing
os.remove(input_file)
print(f'Removed {input_file}')
