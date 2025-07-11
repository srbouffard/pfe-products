# Contributing to PFE Products

Thank you for helping keep our product information up-to-date! This document outlines how to add or update a product definition.

---

## How to Add or Update a Product

1.  **Create a Branch**: From the `main` branch, create a new branch for your changes (e.g., `git checkout -b update-my-product`).
2.  **Add or Edit**:
    * **To add a new product**, copy `template.yaml` to the `/products` directory and rename it (e.g., `/products/new-product.yaml`).
    * **To edit an existing product**, open its corresponding file in the `/products` directory.
3.  **Fill in the Details**: Populate the YAML fields according to the official schema. For a detailed explanation of each field, please refer to the **[PRODUCT_SCHEMA.md](PRODUCT_SCHEMA.md)**.
4.  **Test Locally**: Follow the "Local Testing" instructions below to ensure your changes render correctly. This is a crucial step.
5.  **Commit and Push**: Commit your changes and push them to your branch on GitHub.
6.  **Open a Pull Request**: Create a Pull Request against the `main` branch. Please include a brief description of your changes.

---

## Local Testing and Validation

Before you open a Pull Request, you must validate that your changes render correctly. Our `Makefile` and `uv` make this easy.

1.  **Install `uv`**: If you don't have it, install it with one command:
    ```bash
    sudo snap install astral-uv --classic
    ```

2.  **Set Up the Environment**: Run this command once to create a virtual environment and install all dependencies.
    ```bash
    make setup
    ```

3.  **Generate and Preview**: After making your changes to a YAML file, run this command to generate the documentation and build the HTML preview.
    ```bash
    make preview
    ```

4.  **View in Browser**: Open the generated homepage to see your changes.
    ```bash
    # On macOS, you might use: open docs/_build/html/index.html
    # On Linux, you might use: xdg-open docs/_build/html/index.html
    # On Windows, you might use: start docs/_build/html/index.html
    ```

With this setup, a new contributor can get started with just two commands: `make setup` and `make preview`.