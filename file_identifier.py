import os
from magic_db import MAGIC_NUMBERS
from utils import run_file_command

def read_magic_bytes(path, size=16):
    with open(path, "rb") as file:
        return file.read(size)

def detect_magic_type(header_bytes):
    for magic, file_type in MAGIC_NUMBERS.items():
        if header_bytes.startswith(magic):
            return file_type
    return "Unknown"

def get_file_extension(path):
    return os.path.splitext(path)[1].lower()

def analyze_file(path):
    print("\n========== File Type Analysis ==========\n")

    header = read_magic_bytes(path)
    detected_type = detect_magic_type(header)
    extension = get_file_extension(path)
    file_cmd_result = run_file_command(path)

    print(f"File Path       : {path}")
    print(f"File Extension  : {extension}")
    print(f"Magic Detection : {detected_type}")
    print(f"file Command    : {file_cmd_result}")

    if detected_type == "Unknown":
        print("\n⚠️  WARNING: Unknown file type. Manual inspection recommended.")
    elif extension in [".jpg", ".jpeg", ".png"] and "Image" not in detected_type:
        print("\n🚨 ALERT: File extension does NOT match actual file type!")
    else:
        print("\n✅ File type appears consistent.")

if __name__ == "__main__":
    file_path = input("Enter file path to analyze: ").strip()

    if os.path.exists(file_path):
        analyze_file(file_path)
    else:
        print("❌ File not found. Please check the path.")
