import json
import os
from collections import defaultdict

def generate_swagger_blocks(openapi_file):
    # Load the OpenAPI JSON file
    with open(openapi_file, 'r') as file:
        data = json.load(file)
    
    # Extract paths and methods
    paths = data.get('paths', {})

    # Organize paths into categories based on the first part of the path
    categorized_paths = defaultdict(list)

    for path, methods in paths.items():
        # Use the first part of the path as the category (e.g., /accounts/invoices -> Accounts)
        category = path.strip('/').split('/')[0].capitalize()

        # Add all methods (GET, POST, etc.) for that category
        for method in methods.keys():
            categorized_paths[category].append((path, method))

    return categorized_paths

def save_swagger_docs(categorized_paths, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    sidebar_content = ["# Table of Contents\n", "* [API Documentation](README.md)"]
    
    # Generate markdown files for each category and method
    for category, endpoints in categorized_paths.items():
        category_dir = os.path.join(output_dir, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        sidebar_content.append(f"* [{category}]({category}/README.md)")
        
        category_readme = [f"# {category} API\n"]

        for endpoint, method in endpoints:
            filename = endpoint.strip('/').split('/')[-1] + '.md'
            method_file = os.path.join(category_dir, filename)
            
            swagger_block = f"""{{% swagger src="../openapi.json" path="{endpoint}" method="{method}" expanded="true" %}}
{{% endswagger %}}"""
            
            with open(method_file, 'w') as file:
                file.write(f"# {method.upper()} {endpoint}\n")
                file.write(swagger_block)
            
            category_readme.append(f"* [{method.upper()} {endpoint}]({filename})")
        
        with open(os.path.join(category_dir, 'README.md'), 'w') as file:
            file.write("\n".join(category_readme))
    
    # Write sidebar or summary for GitBook
    with open(os.path.join(output_dir, '_sidebar.md'), 'w') as file:
        file.write("\n".join(sidebar_content))

if __name__ == "__main__":
    openapi_file = 'docs/openapi.json'  # Path to your OpenAPI file
    output_dir = 'docs'                # Directory to save markdown files
    
    categorized_paths = generate_swagger_blocks(openapi_file)
    save_swagger_docs(categorized_paths, output_dir)
    
    print(f"Documentation generated in {output_dir}")
