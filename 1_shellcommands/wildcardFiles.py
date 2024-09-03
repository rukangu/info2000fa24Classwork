import os

# Define the directory where the files will be created
wildcards_demo_dir = "Wildcard_Demo"

# Ensure the directory exists
os.makedirs(wildcards_demo_dir, exist_ok=True)

# Define the file patterns to create
file_patterns = {
    "simple_text_files": [
        "file1.txt", "file2.txt", "file3.txt",
        "document1.txt", "document2.txt", "notes.txt"
    ],
    "images": [
        "image001.jpg", "image002.jpg", "photo01.jpg",
        "screenshot1.png", "screenshot2.png", "diagram1.png"
    ],
    "logs_and_configs": [
        "logfile1.log", "logfile2.log", "system_config.conf",
        "app_config.conf", "backup_2021.log", "backup_2022.log"
    ],
    "mixed_extensions": [
        "project1.doc", "project2.doc", "presentation.ppt", 
        "report.pdf", "summary.pdf", "data_analysis.xls"
    ],
    "random_files": [
        "randomfile1.tmp", "randomfile2.tmp", "tempfile1.tmp", 
        "backup1.bak", "backup2.bak", "archive1.zip", "archive2.zip"
    ]
}

# Function to create dummy files with content based on their name
def create_dummy_files(directory, filenames):
    for filename in filenames:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            f.write(f"Dummy content for {filename}")

# Generate the files
for category, filenames in file_patterns.items():
    create_dummy_files(wildcards_demo_dir, filenames)

print(f"Wildcard demo files created in the '{wildcards_demo_dir}' directory.")
