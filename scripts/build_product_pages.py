import os
import glob
import yaml
from jinja2 import Environment, FileSystemLoader

def main():
    """Finds all product YAML files and generates corresponding RST files using a template."""
    
    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('docs/_templates'))
    template = env.get_template('references.rst.j2')

    products_dir = 'products'
    output_base_dir = 'docs'

    product_files = glob.glob(os.path.join(products_dir, '*.yaml'))
    
    if not product_files:
        print("No product YAML files found.")
        return

    print(f"Found {len(product_files)} product(s) to process.")

    for product_file in product_files:
        print(f"Processing {product_file}...")
        with open(product_file, 'r') as f:
            product_data = yaml.safe_load(f)

        product_title = product_data.get('product_title')
        if not product_title:
            print(f"  -> Skipping {product_file} because it's missing 'product_title'.")
            continue

        # Render the template with the product data
        rst_content = template.render(product_data)
        
        # Define the output path
        output_dir = os.path.join(output_base_dir, 'products', product_title)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'References.rst')

        # Write the rendered content to the file
        with open(output_path, 'w') as f:
            f.write(rst_content)
        
        print(f"  -> Generated documentation at {output_path}")

if __name__ == '__main__':
    main()