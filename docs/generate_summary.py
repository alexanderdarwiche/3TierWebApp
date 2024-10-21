import os

# Function to update (overwrite) the SUMMARY.md file with a fresh structure and API details
def generate_summary_from_scratch(summary_file, api_versions_info):
    # Fixed base structure for SUMMARY.md
    base_structure = '''# Table of contents

* [Welcome](README.md)
* [Get started](get-started.md)
* [API:s](api-s/README.md)

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
        # Write the fixed base structure first
        summary.write(base_structure)

        # For each API version, append the API sections to the file
        for api_version, api_summary_entries in api_versions_info.items():
            summary.write(f'  * [API {api_version}](api-s/api-{api_version}/README.md)\n')  # Nested under API:s
            summary.write('\n'.join([f'    {entry}' for entry in api_summary_entries[1:]]))  # Indent entries
            summary.write('\n')  # Add a newline after each API version section

    print(f'Successfully regenerated SUMMARY.md at {summary_file}')


# Function to collect API summary entries for each API version
def collect_api_summary_entries(output_dir, api_version):
    api_summary_entries = []

    # Add README.md to the API section in SUMMARY.md
    api_summary_entries.append(f'* [API {api_version}](api-s/api-{api_version}/README.md)')

    # List all markdown files in the output directory
    for file_name in os.listdir(output_dir):
        if file_name.endswith('.md') and file_name != 'README.md':
            group_name = file_name.replace('.md', '').capitalize()
            api_summary_entries.append(f'  - [{group_name}](api-s/api-{api_version}/{file_name})')

    return api_summary_entries


if __name__ == "__main__":
    # Paths to output directories and summary file
    output_dir_1 = 'docs/api-s/api-2.0'  # Output directory for Younium v1 API
    output_dir_2 = 'docs/api-s/api-2.1'  # Output directory for Younium v2 API
    summary_file = os.path.join('docs', 'SUMMARY.md')  # Path for SUMMARY.md

    # Collect API summary entries for both API versions
    api_summary_entries_1 = collect_api_summary_entries(output_dir_1, '2.0')
    api_summary_entries_2 = collect_api_summary_entries(output_dir_2, '2.1')

    # Prepare a dictionary with all API version info
    api_versions_info = {
        '2.0': api_summary_entries_1,
        '2.1': api_summary_entries_2
    }

    # Overwrite and regenerate the SUMMARY.md from scratch
    generate_summary_from_scratch(summary_file, api_versions_info)
