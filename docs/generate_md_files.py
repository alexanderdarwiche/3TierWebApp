import os
import re

# Function to process Swagger blocks and generate markdown files
def generate_md_files(input_file, output_dir, api_version):
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

    # Write the README.md for the API version
    readme_file = os.path.join(output_dir, 'README.md')
    with open(readme_file, 'w') as readme:
        # Add the layout section at the beginning of the file
        readme.write('---\n')
        readme.write(f"layout:\n")
        readme.write(f"  title:\n")
        readme.write(f"    visible: true\n")
        readme.write(f"  description:\n")
        readme.write(f"    visible: true\n")
        readme.write(f"  tableOfContents:\n")
        readme.write(f"    visible: true\n")
        readme.write(f"  outline:\n")
        readme.write(f"    visible: true\n")
        readme.write(f"  pagination:\n")
        readme.write(f"    visible: false\n")
        readme.write('---\n\n')

        # Add the description and API version title
        readme.write(f"description: 'Younium API - Version: {api_version}'\n")
        readme.write(f"# API {api_version}\n")
    print(f'Created README.md for API version {api_version}')

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
        group_file = os.path.join(output_dir, f'{group.lower()}.md')  # Convert group names to lowercase for file paths
        with open(group_file, 'w') as file:
            # Write the group header and content
            file.write(f'## {group}\n\n')
            file.write(content)
        print(f'Created file: {group_file}')

    # Remove the swaggerblocks.md file after processing
    os.remove(input_file)
    print(f'Removed {input_file}')

if __name__ == "__main__":
    # Paths to Swagger block files and API version
    swaggerblocks_file_1 = 'docs/swaggerblocks_younium.md'  # For Younium v1
    swaggerblocks_file_2 = 'docs/swaggerblocks_youniumv2.md'  # For Younium v2
    output_dir_1 = 'docs/api-s/api-2.0'  # Output directory for Younium v1 API
    output_dir_2 = 'docs/api-s/api-2.1'  # Output directory for Younium v2 API

    # Generate Markdown files for both API versions
    generate_md_files(swaggerblocks_file_1, output_dir_1, '2.0')
    generate_md_files(swaggerblocks_file_2, output_dir_2, '2.1')
