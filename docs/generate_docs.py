import json
from collections import defaultdict

def generate_swagger_blocks(openapi_file):
    # Load the OpenAPI JSON file
    with open(openapi_file, 'r') as file:
        data = json.load(file)
    
    # Extract paths and methods
    paths = data.get('paths', {})

    # Organize paths under their "categories"
    categorized_paths = defaultdict(lambda: defaultdict(list))

    for path, methods in paths.items():
        # Assuming first part of path is the category (e.g., /accounts/invoices -> Accounts)
        parts = path.strip('/').split('/')
        if len(parts) > 1:
            category = parts[0].capitalize()  # First part as category (capitalize for uniformity)
            subcategory = parts[1].capitalize()  # Second part as subcategory
        else:
            category = parts[0].capitalize()
            subcategory = None

        # Add methods under category/subcategory
        for method in methods.keys():
            if subcategory:
                categorized_paths[category][subcategory].append((path, method))
            else:
                categorized_paths[category]['General'].append((path, method))
    
    swagger_blocks = []
    
    # Generate the Markdown documentation structure
    for category, subcategories in categorized_paths.items():
        swagger_blocks.append(f"## {category}\n")
        for subcategory, endpoints in subcategories.items():
            swagger_blocks.append(f"### {subcategory}\n")
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
