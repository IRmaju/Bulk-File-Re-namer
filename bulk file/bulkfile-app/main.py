import streamlit as st
import os

def rename_files(folder_path, prefix, file_extension):
    # If the folder_path is a file, process that file directly
    if os.path.isfile(folder_path):
        files_to_rename = [folder_path]
    else:
        # If it's a directory, get all files with the specified extension
        files_to_rename = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(file_extension)]

    # Debug: Print the list of files to rename
    st.write("Files to rename:", files_to_rename)

    # Renaming files
    for count, file_path in enumerate(files_to_rename, start=1):
        if os.path.isfile(file_path):
            directory, filename = os.path.split(file_path)
            new_name = f"{prefix}{count}{file_extension}"
            new_path = os.path.join(directory, new_name)
            
            # Debug: Print renaming action
            st.write(f"Renaming: {file_path} → {new_path}")
            
            os.rename(file_path, new_path)
            st.write(f"✅ Renamed: {filename} → {new_name}")

# Streamlit interface
st.title("Bulk File Renamer")
folder_path = st.text_input("Enter the full folder path:")
prefix = st.text_input("Enter a prefix for the new filenames:")
file_extension = st.text_input("Enter the file extension (e.g., .txt, .jpg, .pdf):")

if st.button("Rename Files"):
    if folder_path and prefix and file_extension:
        rename_files(folder_path, prefix, file_extension)
    else:
        st.error("Please provide all inputs.")
