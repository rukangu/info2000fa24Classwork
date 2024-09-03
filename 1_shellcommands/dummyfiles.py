import os
import random

# Define the base directory
downloads_dir = "myDownloads"

# Ensure the base directory exists
os.makedirs(downloads_dir, exist_ok=True)

# Define file categories with popular culture and scientific/engineering-inspired names
file_categories = {
    ".mov": [
        "Avengers_Endgame", "Star_Wars_Rogue_One", "Inception", 
        "Interstellar", "Harry_Potter_Goblet_of_Fire", "Lord_of_the_Rings_Two_Towers", 
        "The_Dark_Knight", "Spider_Man_Homecoming", "Guardians_of_the_Galaxy", 
        "Jurassic_Park", "Titanic", "Avatar", "Frozen", "The_Lion_King", 
        "Toy_Story", "Shrek", "Finding_Nemo", "Aladdin", 
        "The_Incredibles", "Monsters_Inc", "Engineering_the_Future", 
        "Physics_of_Interstellar", "AI_Risks_and_Benefits", "Quantum_Computing_Today"
    ],
    ".mp4": [
        "Breaking_Bad_S01E01", "Game_of_Thrones_S08E03", "Stranger_Things_S02E05", 
        "The_Mandalorian_S01E01", "The_Witcher_S01E06", "Sherlock_S03E01", 
        "Westworld_S01E10", "Black_Mirror_S03E04", "The_Crown_S04E05", 
        "The_Office_US_S05E14", "Friends_S10E17", "How_I_Met_Your_Mother_S09E23", 
        "The_Big_Bang_Theory_S12E24", "Rick_and_Morty_S03E07", 
        "The_Simpsons_S10E10", "Family_Guy_S18E13", "South_Park_S22E01", 
        "Stranger_Things_S01E01", "Better_Call_Saul_S02E03", "The_Boys_S02E05", 
        "Engineering_Discoveries", "Robotics_in_Action", "AI_Lecture_Series", 
        "Python_Programming_Tutorials", "Circuit_Design_Workshop"
    ],
    ".jpg": [
        "Spider_Man", "Iron_Man", "Captain_America", 
        "Black_Widow", "Thor", "Hulk", 
        "Hawkeye", "Doctor_Strange", "Black_Panther", 
        "Wonder_Woman", "Superman", "Batman", "Flash", 
        "Aquaman", "Cyborg", "Green_Lantern", 
        "Wolverine", "Deadpool", "Jean_Grey", 
        "Mystique", "Microcontroller_Diagram", "Circuit_Schematic", 
        "3D_Print_Model", "Robot_Arm_Design", "Algorithm_Visualization"
    ],
    ".doc": [
        "Harry_Potter_Summary", "Lord_of_the_Rings_Essay", "Star_Wars_Analysis", 
        "Marvel_Cinematic_Universe_Overview", "DC_Universe_Timeline", "Game_of_Thrones_Plot",
        "Breaking_Bad_Character_Analysis", "Stranger_Things_Theories", "The_Mandalorian_Review",
        "The_Witcher_Lore", "Sherlock_Holmes_Case_Study", "Westworld_Symbolism",
        "Black_Mirror_Impact", "The_Crown_Historical_Accuracy", "The_Office_Humor_Study",
        "Friends_Relationship_Dynamics", "How_I_Met_Your_Mother_Structure", "The_Big_Bang_Theory_Physics",
        "Rick_and_Morty_Psychology", "The_Simpsons_Satire", "Electromagnetism_Homework", 
        "Control_Systems_Assignment", "Robotics_Project_Report", "Thermodynamics_Lab_Report", 
        "AI_Essay", "Quantum_Mechanics_Homework"
    ],
    ".exe": [
        "Spotify_Setup", "Chrome_Installer", "Discord_Setup", 
        "Visual_Studio_Code", "Slack_Installer", "Zoom_Setup", 
        "Notepad_Plus_Plus", "VLC_Player", "Steam_Installer", 
        "GIMP_Installer", "Audacity_Setup", "Blender_Installer", 
        "Unity_Installer", "Unreal_Engine_Setup", "PyCharm_Installer", 
        "Atom_Editor_Setup", "Git_Setup", "Docker_Installer", 
        "NodeJS_Installer", "Python_Setup", "MATLAB_Installer", 
        "SolidWorks_Setup", "AutoCAD_Installer", "ANSYS_Setup", 
        "Multisim_Installer", "LabVIEW_Setup", "Arduino_IDE"
    ],
    ".pdf": [
        "AI_Machine_Learning", "Quantum_Computing_White_Paper", "Modern_Robotics_Textbook", 
        "Control_Systems_Engineering", "Electromagnetic_Field_Theory", "Solid_State_Physics", 
        "VLSI_Design_Tutorials", "Data_Structures_Algorithms", "Neural_Networks_Guide", 
        "Embedded_Systems_Book", "Cybersecurity_Principles", "Digital_Signal_Processing", 
        "Advanced_Circuit_Analysis", "Renewable_Energy_Systems", "Nanotechnology_Research_Paper",
        "Space_Exploration_Technologies", "Thermodynamics_Basics", "Artificial_Intelligence_Ethics",
        "Mathematical_Methods_in_Engineering", "Virtual_Reality_in_Education"
    ]
}

# Function to create dummy files
def create_dummy_files(directory, filename, extension):
    filepath = os.path.join(directory, f"{filename}{extension}")
    with open(filepath, 'w') as f:
        f.write(f"Dummy content for {filename}{extension}")

# Generate the dummy files
for extension, filenames in file_categories.items():
    for filename in filenames:
        # Add a random number suffix to make the names unique
        suffix = random.randint(1, 100)
        full_filename = f"{filename}_{suffix}"
        create_dummy_files(downloads_dir, full_filename, extension)

print(f"Dummy files created in the '{downloads_dir}' directory.")
