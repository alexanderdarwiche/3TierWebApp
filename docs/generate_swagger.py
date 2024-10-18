import json
import os

def categorize_paths(paths):
    categories = {}
    
    # Categorize paths based on the first segment of the path (e.g., '/accounts/', '/orders/')
    for path, methods in paths.items():
        category = path.split('/')[1]  # Assuming category is always the first segment in the path
        if category not in categories:
            categories[category] = {}
        categories[category][path] = methods
    
    return categories

def generate_swagger_blocks(openapi_file):
    # Load the OpenAPI JSON file
    with open(openapi_file, 'r') as file:
        data = json.load(file)
    
    # Extract paths and methods
    paths = data.get('paths', {})
    
    # Categorize paths
    categorized_paths = categorize_paths(paths)
    
    swagger_blocks = []
    
    for category, paths in categorized_paths.items():
        # Category title
        swagger_blocks.append(f"## {category.capitalize()}\n")
        
        for path, methods in paths.items():
            for method in methods.keys():
                # Escape curly braces by doubling them and generate swagger block
                swagger_block = f"""{{% swagger src="../../.gitbook/assets/younium.json" path="{path}" method="{method}" expanded="true" %}}
[openapi.json](./{openapi_file})
{{% endswagger %}}"""
                swagger_blocks.append(swagger_block)
        
        # Add a separator between categories
        swagger_blocks.append("\n---\n")
    
    return swagger_blocks

def save_swagger_blocks(swagger_blocks, output_file):
    title = "# API Documentation\n\n"
    
    with open(output_file, 'w') as file:
        file.write(title)
        file.write("\n\n".join(swagger_blocks))

if __name__ == "__main__":
    openapi_file = 'docs/.gitbook/assets/younium.json'  # Adjusted path to your OpenAPI file
    output_file = 'docs/swaggerblocks.md'     # Adjusted output markdown file
    
    swagger_blocks = generate_swagger_blocks(openapi_file)
    save_swagger_blocks(swagger_blocks, output_file)
    
    print(f"Swagger blocks saved to {output_file}")