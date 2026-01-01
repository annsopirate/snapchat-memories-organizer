import os
import shutil

# --- CONFIGURATION ---
SIMULATION = True  # Set to False to actually move folders
# REPLACE THE PATH BELOW WITH YOUR ACTUAL FOLDER PATH
TARGET_FOLDER = r"C:\Users\YourName\Desktop\snapchat_memories"

def group_by_year():
    if not os.path.exists(TARGET_FOLDER):
        print(f"ERROR: Folder not found: {TARGET_FOLDER}")
        print("Please edit the script and set the correct TARGET_FOLDER path.")
        return

    count_moved = 0
    print(f"--- Grouping by Year (Simulation: {SIMULATION}) ---")

    # List all items in the target folder
    for item in os.listdir(TARGET_FOLDER):
        item_path = os.path.join(TARGET_FOLDER, item)

        # We only process directories
        if not os.path.isdir(item_path):
            continue

        # Split folder name by spaces (e.g., "January 2018" -> ["January", "2018"])
        parts = item.split()

        # Check if the folder name consists of 2 parts and the second part looks like a Year
        if len(parts) == 2 and parts[1].isdigit() and len(parts[1]) == 4:
            year = parts[1]
            
            # Destination path (The "Year" folder)
            year_folder_path = os.path.join(TARGET_FOLDER, year)
            
            # Final path for the month folder inside the year folder
            dest_path = os.path.join(year_folder_path, item)

            if SIMULATION:
                print(f"[SIMULATION] Move '{item}' -> '{year}/{item}'")
            else:
                # Create the Year folder if it doesn't exist
                if not os.path.exists(year_folder_path):
                    os.makedirs(year_folder_path)
                
                try:
                    shutil.move(item_path, dest_path)
                    print(f"[OK] Moved: {item} -> {year}")
                    count_moved += 1
                except Exception as e:
                    print(f"[ERROR] Could not move {item}: {e}")

    print(f"Done! {count_moved} folders grouped into years.")

if __name__ == "__main__":
    group_by_year()