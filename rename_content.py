import os

# --- CONFIGURATION ---
SIMULATION = True
TARGET_FOLDER = r"C:\Users\YourName\Desktop\snapchat_memories"

def rename_content():
    count_files = 0
    print(f"--- Renaming Started (Simulation: {SIMULATION}) ---")

    for root, dirs, files in os.walk(TARGET_FOLDER):
        folder_name = os.path.basename(root)

        # Process only folders that look like UUID dates (long name starting with digits)
        if len(folder_name) > 15 and folder_name[:8].isdigit():
            files.sort()
            local_renamed = 0
            
            for index, file in enumerate(files):
                if file.startswith("."): continue
                ext = os.path.splitext(file)[1]
                
                # Rename to match folder name (e.g., 20180803_...-1.jpg)
                if index == 0: new_name = f"{folder_name}{ext}"
                else: new_name = f"{folder_name}-{index + 1}{ext}"

                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_name)

                if file == new_name: continue

                if SIMULATION:
                    print(f"[SIMULATION] In '{folder_name}': Rename '{file}' -> '{new_name}'")
                else:
                    try:
                        os.rename(old_path, new_path)
                        local_renamed += 1
                    except Exception as e:
                        print(f"[ERROR] {file}: {e}")
            
            if local_renamed > 0: count_files += local_renamed

    print(f"Done! {count_files} files renamed.")

if __name__ == "__main__":
    rename_content()