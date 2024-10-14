import json
import os

def generate_markdown(json_file, output_file):
    with open(json_file) as f:
        spec = json.load(f)

    markdown_content = f"# API Documentation\n\n"

    for path, methods in spec.get('paths', {}).items():
        for method, details in methods.items():
            markdown_content += f"## {method.upper()} {path}\n"
            markdown_content += f"**Summary:** {details.get('summary', 'No summary available.')}\n\n"

            # Add parameters
            if 'parameters' in details:
                markdown_content += "**Parameters:**\n"
                for param in details['parameters']:
                    if param.get('in') == 'path':
                        markdown_content += f"- **{param['name']}** (path): {param.get('description', 'No description')}\n"
                    elif param.get('in') == 'body':
                        markdown_content += f"- **{param['name']}** (body): {param.get('description', 'No description')}\n"
                markdown_content += "\n"

            # Add responses
            markdown_content += "**Responses:**\n"
            for code, response in details.get('responses', {}).items():
                markdown_content += f"- **{code}**: {response.get('description', 'No description')}\n"
            markdown_content += "\n---\n\n"

    # Write to Markdown file
    with open(output_file, 'w') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    json_file = './openapi.json'  # Path to your OpenAPI JSON file
    output_file = './apidocs.md'  # Output Markdown file
    generate_markdown(json_file, output_file)
