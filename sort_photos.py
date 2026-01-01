import os
import shutil

# --- CONFIGURATION ---
SIMULATION = True  # Set to False to actually move files
TARGET_FOLDER = r"C:\Users\YourName\Desktop\snapchat_memories"

MONTHS = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

YEARS = [str(y) for y in range(2010, 2030)]

def sort_files():
    if not os.path.exists(TARGET_FOLDER):
        print(f"Error: Folder not found: {TARGET_FOLDER}")
        print("Please edit the script and set the correct TARGET_FOLDER path.")
        return

    count = 0
    print(f"--- Sorting Started (Simulation: {SIMULATION}) ---")

    for item in os.listdir(TARGET_FOLDER):
        if item.endswith(".py"): continue
        if len(item) < 8 or not item[:8].isdigit(): continue

        year = item[0:4]
        month_digit = item[4:6]

        if year in YEARS and month_digit in MONTHS:
            month_name = MONTHS[month_digit]
            folder_name = f"{month_name} {year}"
            
            dest_folder = os.path.join(TARGET_FOLDER, folder_name)
            src_path = os.path.join(TARGET_FOLDER, item)
            dest_path = os.path.join(dest_folder, item)

            if src_path == dest_folder: continue

            if SIMULATION:
                print(f"[SIMULATION] Move '{item}' -> '{folder_name}/'")
            else:
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                try:
                    shutil.move(src_path, dest_path)
                    count += 1
                    print(f"[OK] {item} -> {folder_name}")
                except Exception as e:
                    print(f"[ERROR] {item}: {e}")

    print(f"Done! {count} items moved.")

if __name__ == "__main__":
    sort_files()