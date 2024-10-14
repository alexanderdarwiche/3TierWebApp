import json

def generate_swagger_blocks(openapi_file):
    # Load the OpenAPI JSON file
    with open(openapi_file, 'r') as file:
        data = json.load(file)
    
    # Extract paths and methods
    paths = data.get('paths', {})
    
    swagger_blocks = []
    
    for path, methods in paths.items():
        for method in methods.keys():
            # Escape curly braces by doubling them
            swagger_block = f"""{{% swagger src="./{openapi_file}" path="{path}" method="{method}" expanded="true" %}}
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
    openapi_file = 'openapi.json'  # Adjusted path to your OpenAPI file
    output_file = 'apidocs.md'     # Adjusted output markdown file
    
    swagger_blocks = generate_swagger_blocks(openapi_file)
    save_swagger_blocks(swagger_blocks, output_file)
    
    print(f"Swagger blocks saved to {output_file}")
