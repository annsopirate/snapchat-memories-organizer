import os

# --- CONFIGURATION ---
SIMULATION = True
TARGET_FOLDER = r"C:\Users\YourName\Desktop\snapchat_memories"

def delete_pngs():
    count = 0
    print(f"--- Deleting PNGs (Simulation: {SIMULATION}) ---")

    for root, dirs, files in os.walk(TARGET_FOLDER):
        for file in files:
            if file.lower().endswith(".png"):
                path = os.path.join(root, file)
                
                if SIMULATION:
                    print(f"[SIMULATION] Delete: {file}")
                    count += 1
                else:
                    try:
                        os.remove(path)
                        print(f"[DELETED] {file}")
                        count += 1
                    except Exception as e:
                        print(f"[ERROR] {e}")

    print(f"Done! {count} PNGs deleted.")

if __name__ == "__main__":
    delete_pngs()