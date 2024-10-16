def save_swagger_docs(categorized_paths, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    summary_content = ["# Summary\n", "* [API Documentation](README.md)"]
    
    # Generate markdown files for each category and method
    for category, subcategories in categorized_paths.items():
        category_dir = os.path.join(output_dir, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        summary_content.append(f"* [{category}]({category}/README.md)")
        
        category_readme = [f"# {category} API\n"]

        # Handle subcategories
        for subcategory, endpoints in subcategories.items():
            subcategory_dir = os.path.join(category_dir, subcategory) if subcategory else category_dir
            if not os.path.exists(subcategory_dir):
                os.makedirs(subcategory_dir)
            
            subcategory_readme = [f"# {subcategory.capitalize()} API\n"]

            for endpoint, method in endpoints:
                filename = endpoint.strip('/').split('/')[-1] + '.md'
                method_file = os.path.join(subcategory_dir, filename)
                
                swagger_block = f"""{{% swagger src="../openapi.json" path="{endpoint}" method="{method}" expanded="true" %}}
{{% endswagger %}}"""
                
                with open(method_file, 'w') as file:
                    file.write(f"# {method.upper()} {endpoint}\n")
                    file.write(swagger_block)
                
                subcategory_readme.append(f"* [{method.upper()} {endpoint}]({filename})")
            
            if subcategory:
                with open(os.path.join(subcategory_dir, 'README.md'), 'w') as file:
                    file.write("\n".join(subcategory_readme))

        with open(os.path.join(category_dir, 'README.md'), 'w') as file:
            file.write("\n".join(category_readme))
    
    # Write summary for GitBook
    with open(os.path.join(output_dir, 'SUMMARY.md'), 'w') as file:
        file.write("\n".join(summary_content))
