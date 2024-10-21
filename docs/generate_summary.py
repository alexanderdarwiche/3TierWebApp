import os

# Function to update (overwrite) the SUMMARY.md file with a fresh structure and API details
def generate_summary_from_scratch(summary_file, api_versions_info):
    # Fixed base structure for SUMMARY.md
    base_structure = '''# Table of contents

* [Welcome](README.md)
* [Get started](get-started.md)
* [API:s](api-s/README.md)
'''

    # Prepare a string to hold the API version entries
    api_entries = []

    # For each API version, create the API section entries
    for api_version, api_summary_entries in api_versions_info.items():
        api_entries.append(f'  * [API {api_version}](api-s/api-{api_version}/README.md)')
        api_entries.extend([f'    - [{entry}](api-s/api-{api_version}/{entry.lower()}.md)' for entry in api_summary_entries[1:]])

    # Join API entries into a single string
    api_entries_str = '\n'.join(api_entries)

    # Complete the summary structure with documentation sections
    documentation_structure = '''
* [Documentation](documentation/README.md)
  * [Developer resources](documentation/developer-resources.md)
  * [Invoice operations](documentation/invoice-operations.md)
  * [Product guide](documentation/product-guide.md)
  * [Webhooks](documentation/webhooks.md)
* [Changelog](changelog.md)
* [Sandbox](https://younium.gitbook.io/sandbox)
'''

    # Open the SUMMARY.md file in write mode to overwrite any previous content
    with open(summary_file, 'w') as summary:
        # Write the base structure first
        summary.write(base_structure)

        # Write the API entries under API:s
        summary.write(api_entries_str + '\n\n')  # Add a newline after API sections

        # Write the rest of the documentation sections
        summary.write(documentation_structure)

    print(f'Successfully regenerated SUMMARY.md at {summary_file}')


# Function to collect API summary entries for each API version
def collect_api_summary_entries(output_dir, api_version):
    api_summary_entries = []

    # Add README.md to the API section in SUMMARY.md
    api_summary_entries.append(f'* [API {api_version}](api-s/api-{api_version}/README.md)')

    # List all markdown files in the output directory
    try:
        for file_name in os.listdir(output_dir):
            if file_name.endswith('.md') and file_name != 'README.md':
                group_name = file_name.replace('.md', '').capitalize()
                api_summary_entries.append(group_name)  # Append just the name for better formatting
    except FileNotFoundError:
        print(f"Output directory not found: {output_dir}")

    return api_summary_entries


if __name__ == "__main__":
    # Paths to output directories and summary file
    base_dir = 'docs/api-s'
    summary_file = os.path.join('docs', 'SUMMARY.md')
    api_versions_info = {}

    api_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    for api_dir in api_dirs:
        api_version = api_dir.split('-')[-1]  # Extracting version from directory name
        output_dir = os.path.join(base_dir, api_dir)
        api_summary_entries = collect_api_summary_entries(output_dir, api_version)
        api_versions_info[api_version] = api_summary_entries

    # Overwrite and regenerate the SUMMARY.md from scratch
    generate_summary_from_scratch(summary_file, api_versions_info)
