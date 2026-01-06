# File Type Identifier (Magic Number Based)

A beginner-friendly cybersecurity tool that detects disguised or spoofed files by analyzing file magic numbers instead of trusting file extensions.

Attackers often rename malicious scripts or executables as images (.jpg, .png) or documents to trick users. This tool helps identify such files using static file analysis.

---

## Why this tool exists

File extensions are easy to fake.  
A file named `photo.jpg` does not necessarily mean it is an image.

Attackers commonly:
- Rename shell scripts or executables to `.jpg`, `.png`, or `.pdf`
- Rely on users clicking the file without verifying its real type
- Use this technique in phishing and malware delivery

Operating systems identify files using **magic numbers** (hidden bytes at the beginning of a file), not extensions.  
This tool checks the real file type using magic numbers and compares it with the extension.

---

## How attackers create fake files

A shell script or executable can be created and renamed like this:

#!/bin/bash  
echo malicious code  

Saved as:

photo.jpg  

To a normal user, it looks like an image.  
To the system, it is still a shell script or executable.

---

## How this tool works

1. Reads the first few bytes of the file (magic number)
2. Identifies the real file type
3. Extracts the file extension
4. Uses the system `file` command for verification
5. Compares extension vs actual file type
6. Warns if a mismatch is detected

The file is never executed. Only static analysis is performed.

---

## Project structure

file-type-identifier  
├── file_identifier.py  
├── magic_db.py  
├── utils.py  
├── README.md  
├── requirements.txt  
└── samples  

---

## Supported systems

- Linux
- macOS
- Windows

Note: On Windows, the tool may have limited functionality if the `file` command is not available.

---

## How to run the tool

From the project directory:

python file_identifier.py  

You will be prompted to enter a file path.

---

## How to get file path on macOS

Method 1 (recommended):  
Drag the file from Finder and drop it into the terminal when prompted. Press Enter.

Method 2:  
Right-click the file, hold the Option (⌥) key, click “Copy … as Pathname”, then paste it in the terminal.

---

## How to get file path on Linux
Method 1 (recommended):
Drag the file from the file manager (Nautilus, Dolphin, etc.) and drop it into the terminal. Press Enter.

Method 2:
Right-click the file → Properties → copy the Location path and append the file name.

---

## How to get file path on Windows

Method 1 (recommended):
Click on the file in File Explorer
Click the address bar at the top
Copy the folder path
Append the file name manually

Method 2:
Open File Explorer
Hold the Shift key
Right-click the file
Click “Copy as path”
Paste it into the terminal and press Enter


---

## Testing with a fake file (important)

To simulate a spoofed file, create a fake image that is actually a shell script.

From the project directory:

cd samples  
printf '#!/bin/bash\necho fake image\n' > fake.jpg  
cd ..  

Verify using the system:

file samples/fake.jpg  

Expected output:

Bourne-Again shell script  

Now run the tool:

python file_identifier.py  

Enter:

samples/fake.jpg  

Expected result:

🚨 ALERT: File extension does NOT match actual file type!

---

## Testing with a real file

Place a real image inside the `samples` folder and run the tool.

Expected result:

✅ File type appears consistent.

---

## Security notes

- This tool performs static analysis only
- Files are never executed
- Safe for learning and defensive security research

---

## Skills demonstrated

- Magic number and file signature analysis
- Static malware detection concepts
- Python scripting
- Linux/macOS security tooling
- Defensive cybersecurity practices

---

## Future improvements

- Directory scanning
- More file signatures
- Hash-based detection
- JSON output
- VirusTotal API integration

---

## Disclaimer

This project is intended for educational and defensive cybersecurity purposes only.
