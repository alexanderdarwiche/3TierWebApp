import json
import os

# Function to categorize paths based on the first segment
def categorize_paths(paths):
    categories = {}
    
    # Categorize paths based on the first segment of the path (e.g., '/accounts/', '/orders/')
    for path, methods in paths.items():
        category = path.split('/')[1]  # Assuming category is always the first segment in the path
        if category not in categories:
            categories[category] = {}
        categories[category][path] = methods
    
    return categories

# Function to generate Swagger blocks for the OpenAPI JSON file
def generate_swagger_blocks(openapi_file, asset_file_name):
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
                swagger_block = f"""{{% swagger src="../../.gitbook/assets/{asset_file_name}" path="{path}" method="{method}" expanded="true" %}}
[openapi.json](./{openapi_file})
{{% endswagger %}}"""
                swagger_blocks.append(swagger_block)
        
        # Add a separator between categories
        swagger_blocks.append("\n---\n")
    
    return swagger_blocks

# Function to save Swagger blocks to a markdown file
def save_swagger_blocks(swagger_blocks, output_file):
    title = "# API Documentation\n\n"
    
    with open(output_file, 'w') as file:
        file.write(title)
        file.write("\n\n".join(swagger_blocks))

if __name__ == "__main__":
    # Determine whether we're in production or sandbox based on environment variable
    api_environment = os.getenv('API_ENVIRONMENT', 'production')  # Default to production if not set
    
    if api_environment == 'production':
        # Production environment paths
        openapi_file_1 = 'docs/.gitbook/assets/younium.json'
        openapi_file_2 = 'docs/.gitbook/assets/youniumv2.json'
        output_file_1 = 'docs/swaggerblocks_younium.md'
        output_file_2 = 'docs/swaggerblocks_youniumv2.md'
    else:
        # Sandbox environment paths
        openapi_file_1 = 'docs-sandbox/.gitbook/assets/younium.json'
        openapi_file_2 = 'docs-sandbox/.gitbook/assets/youniumv2.json'
        output_file_1 = 'docs-sandbox/swaggerblocks_younium-sandbox.md'
        output_file_2 = 'docs-sandbox/swaggerblocks_youniumv2-sandbox.md'
    
    # Generate Swagger blocks for both files
    swagger_blocks_younium = generate_swagger_blocks(openapi_file_1, os.path.basename(openapi_file_1))
    swagger_blocks_youniumv2 = generate_swagger_blocks(openapi_file_2, os.path.basename(openapi_file_2))
    
    # Save each set of Swagger blocks to its respective file
    save_swagger_blocks(swagger_blocks_younium, output_file_1)
    save_swagger_blocks(swagger_blocks_youniumv2, output_file_2)
    
    print(f"Swagger blocks saved to {output_file_1} and {output_file_2}")
