import os

# Old and new file names
old_name = "Python-Problem-solves-And-Programs/Code With Harry/tobeRenamed.txt"
new_name = "Python-Problem-solves-And-Programs/Code With Harry/renamed_by_python.txt"

# Rename the file
os.rename(old_name, new_name)

print(f"Renamed '{old_name}' to '{new_name}'")
