import os

def create_project_structure(base_dir="project-name"):
    """
    Create a professional data science project folder structure.
    
    Args:
        base_dir (str): The root directory name for the project.
    """
    # Define the folder structure
    folders = [
        "data/raw",
        "data/processed",
        "notebooks",
        "src",
        "models",
        "docs",
        "tests"
    ]
    
    # Create base directory
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Created base directory: {base_dir}")
    else:
        print(f"Base directory already exists: {base_dir}")
    
    # Create subfolders
    for folder in folders:
        path = os.path.join(base_dir, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Ensured folder exists: {path}")
    
    # Create starter files
    starter_files = {
        "README.md": "# Project Title\n\nProject description goes here.\n",
        "requirements.txt": "# Add your dependencies here\npandas\nscikit-learn\nmatplotlib\nseaborn\n",
        ".gitignore": "*.ipynb_checkpoints\n__pycache__/\ndata/raw/*\n*.log\n"
    }
    
    for filename, content in starter_files.items():
        file_path = os.path.join(base_dir, filename)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content)
            print(f"Created starter file: {file_path}")
        else:
            print(f"Starter file already exists: {file_path}")

    print("\n✅ Project structure setup complete!")

# Run the function
create_project_structure("CUSTOMER-CHURN-ANALYSIS-PREDICTION")
