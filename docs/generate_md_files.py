def process_swaggerblocks(input_file, output_dir, api_version, summary_file):
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

    # Iterate over sections to separate group headers and their content
    for i in range(1, len(sections), 2):
        group_name = sections[i].strip()  # The group name (e.g., Accounts)
        group_content = sections[i + 1]   # The corresponding Swagger blocks

        # Save the content in the dictionary
        if group_name not in grouped_content:
            grouped_content[group_name] = ""
        grouped_content[group_name] += group_content

    # Write the README.md for the API version (this will include the table of sections/endpoints)
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
        readme.write("Here are the endpoints in this section:\n\n")

        # Start the table structure for API sections
        readme.write("|  |  |  |\n")  # Create three columns
        readme.write("| --- | --- | --- |\n")  # Divider for columns

        # Prepare the group names dynamically from the grouped content
        group_names = list(grouped_content.keys())

        # Generate the table rows dynamically for the API sections
        for i in range(0, len(group_names), 3):
            row_sections = group_names[i:i+3]  # Take sections in groups of 3
            row_links = [f"[{section}](./{section.lower()}.md)" for section in row_sections]  # Create links
            row_output = ' | '.join(row_links)  # Join them with markdown table syntax
            readme.write(f"| {row_output} |\n")  # Write the row

    print(f'Created README.md for API version {api_version}')

    # Read the existing SUMMARY.md file
    if os.path.exists(summary_file):
        with open(summary_file, 'r') as summary:
            summary_content = summary.read()
    else:
        summary_content = ''

    # Remove the entire [API {api_version}] section if it exists
    if api_section_marker in summary_content:
        # Regex to match the [API {api_version}] section and everything that follows until the next top-level marker (e.g., another heading)
        api_section_regex = re.compile(rf'(\* {re.escape(api_section_marker)}[\s\S]*?)(\* \[[A-Za-z0-9\s]+\]\([^\)]*\))', re.MULTILINE)
        summary_content = re.sub(api_section_regex, r'\2', summary_content)

    # Split the content to insert the new API section after the [API:s] marker
    api_s_marker = '[API:s](api-s/README.md)'
    summary_parts = summary_content.split(api_s_marker)

    # The first part is everything before the API section, the second part is everything after (if exists)
    summary_before_api = summary_parts[0] if len(summary_parts) > 0 else ''
    summary_after_api = summary_parts[1] if len(summary_parts) > 1 else ''

    # Rebuild the SUMMARY.md with proper nesting for the API version under API:s
    with open(summary_file, 'w') as summary:
        # Write content before [API:s]
        summary.write(summary_before_api)
        
        # Re-insert the [API:s] marker
        summary.write(f'{api_s_marker}\n\n')
        
        # Properly indent and nest the API version section under API:s
        summary.write(f'  * [API {api_version}](api-s/api-{api_version}/README.md)\n')  # Nested under API:s with two spaces for indentation

        # Append remaining content after [API:s]
        summary.write(summary_after_api)

    print(f'Updated SUMMARY.md at {summary_file}')

    # Remove the swaggerblocks.md file after processing
    os.remove(input_file)
    print(f'Removed {input_file}')

# Example usage
if __name__ == "__main__":
    # Paths to Swagger block files and API version
    swaggerblocks_file_1 = 'docs/swaggerblocks_younium.md'  # For Younium v1
    swaggerblocks_file_2 = 'docs/swaggerblocks_youniumv2.md'  # For Younium v2
    output_dir_1 = 'docs/api-s/api-2.0'  # Output directory for Younium v1 API
    output_dir_2 = 'docs/api-s/api-2.1'  # Output directory for Younium v2 API
    summary_file = os.path.join('docs', 'SUMMARY.md')  # Path for SUMMARY.md

    # Process both API versions
    process_swaggerblocks(swaggerblocks_file_1, output_dir_1, '2.0', summary_file)
    process_swaggerblocks(swaggerblocks_file_2, output_dir_2, '2.1', summary_file)
