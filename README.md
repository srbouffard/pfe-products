# PFE Products - Source of Truth

This repository serves as the central **source of truth** for all products owned by the Platform Engineering (PFE) team. It contains structured data files that define key information for each product, such as ownership, component lists, and relevant links.

The primary goal of this repository is to eliminate knowledge silos and provide a single, reliable reference point for everyone. The data is used to automatically generate and update documentation on our team Read the Docs site.

---

> This repo is WIP and exploratory ideas still to be refined further!


## 🤖 The Automated Workflow

This repository uses a "docs-as-code" approach. The workflow is fully automated:

1.  **Update a Product**: A team member adds or updates a product's `product-name.yaml` file in the `/products` directory via a Pull Request.
2.  **Merge**: Once the PR is reviewed and merged, a GitHub Action is triggered.
3.  **Generate Docs**: The action uses templates to generate up-to-date documentation files (`.rst`).
4.  **Create a PR**: The action then automatically opens a Pull Request in our team with the new files.
5.  **Publish**: Once the documentation PR is approved and merged, the changes are published to our live docs site.

---

## 📂 Repository Structure

Here is a breakdown of the key files and directories in this project:

* `README.md`: You are here! This file provides the main overview of the project.
* `CONTRIBUTING.md`: Detailed instructions on how to add or update product definitions.
* `/products/`: Contains all the product definition YAML files, with one file per product. This is the core data of the repository.
* `/docs/`: Contains templates and configuration (`conf.py`) for generating the documentation pages.
* `/scripts/`: Holds the Python script (`build_product_pages.py`) responsible for converting the YAML data into documentation files.
* `/.github/workflows/`: Defines the GitHub Actions CI/CD pipeline that automates the entire documentation generation and PR creation process.
* `.gitignore`: Specifies which files and folders should be ignored by Git.

---

## 🚀 How to Contribute

We encourage all team members to help keep this information current! The process is simple and follows standard Git practices.

**To add or update a product, please follow the instructions in our [CONTRIBUTING.md](CONTRIBUTING.md) file.**

The `CONTRIBUTING.md` file contains:
* Step-by-step instructions for submitting a change.
* The complete YAML schema to ensure all necessary information is included.

---

## 🔗 Quick Links

| Resource                        | Link                                                                      |
| ------------------------------- | ------------------------------------------------------------------------- |
| **Official Documentation Site** | [PFE RTD](https://canonical-platform-engineering.readthedocs-hosted.com/latest/)         |
| **Documentation Repo (RTD)** | [github.com/canonical/platform-engineering-docs](https://github.com/canonical/platform-engineering-docs) |

---