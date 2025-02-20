# 📝 Simple Text Recovery Tool  

A Python-based tool to recover and fix corrupted text files by detecting and applying the correct character encoding.  

## 📌 Features  
- Scans directories for lost or misplaced `.txt` files  
- Automatically detects and applies the correct encoding  
- Recovers readable content from corrupted text files  

## 🚀 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/bbetulkaya/Chasing_the_Data_Recovery_Scripts/00_text-recovery-tool.git
cd 00_text-recovery-tool

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt

### 3️⃣ Run the Tool
```bash
python3 recovery.py

## 🛠 How It Works
- The tool scans the test_files directory for .txt files.
- It attempts to detect their encoding using chardet.
- If the file is readable, its content is displayed.

## 📂 Folder Structure
```bash
📂 text-recovery-tool  
 ├── 📂 test_files      # Directory containing text files to recover  
 ├── 🔹 recovery.py     # Main Python script  
 ├── 🔹 requirements.txt # Dependencies    
 └── 🔹 README.md       # Project documentation  

## 🤝 Contributing

Feel free to submit pull requests or report issues!
