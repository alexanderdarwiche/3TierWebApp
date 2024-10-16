import json
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

    swagger_blocks = []
    
    # Generate the Markdown documentation structure with categories
    for category, endpoints in categorized_paths.items():
        swagger_blocks.append(f"## {category}\n")
        for endpoint, method in endpoints:
            swagger_block = f"""{{% swagger src="./openapi.json" path="{endpoint}" method="{method}" expanded="true" %}}
[openapi.json](./{openapi_file})
{{% endswagger %}}"""
            swagger_blocks.append(swagger_block)

    return swagger_blocks

def save_swagger_blocks(swagger_blocks, output_file):
    title = "# API Documentation\n\n"

    with open(output_file, 'w') as file:
        file.write(title)
        file.write("\n\n".join(swagger_blocks))

if __name__ == "__main__":
    openapi_file = 'docs/openapi.json'  # Adjusted path to your OpenAPI file
    output_file = 'docs/apidocs.md'     # Adjusted output markdown file
    
    swagger_blocks = generate_swagger_blocks(openapi_file)
    save_swagger_blocks(swagger_blocks, output_file)
    
    print(f"Swagger blocks saved to {output_file}")
