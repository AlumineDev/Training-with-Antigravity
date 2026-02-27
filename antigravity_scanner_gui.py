import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from collections import Counter

class AntigravityScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Antigravity | File Intelligence Scanner")
        self.root.geometry("600x500")
        self.root.configure(bg="#0a0a0c")
        
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background="#1a1a1c", foreground="white", fieldbackground="#1a1a1c", borderwidth=0)
        style.map("Treeview", background=[('selected', '#7c4dff')])

        # UI Header
        self.header = tk.Label(root, text="ANTIGRAVITY SCANNER", font=("Outfit", 18, "bold"), fg="#ff9100", bg="#0a0a0c")
        self.header.pack(pady=20)

        # Folder Selection
        self.btn_frame = tk.Frame(root, bg="#0a0a0c")
        self.btn_frame.pack(pady=10)
        
        self.select_btn = tk.Button(self.btn_frame, text="Select Folder to Scan", command=self.select_folder, 
                                   bg="#7c4dff", fg="white", font=("Outfit", 10, "bold"), padx=20, pady=10, border=0)
        self.select_btn.pack(side=tk.LEFT, padx=5)

        # Status Label
        self.status_var = tk.StringVar(value="Ready to scan...")
        self.status_label = tk.Label(root, textvariable=self.status_var, fg="#b0b0b0", bg="#0a0a0c")
        self.status_label.pack(pady=5)

        # Results Treeview
        columns = ("Extension", "Count")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
        self.tree.heading("Extension", text="File Type")
        self.tree.heading("Count", text="Number of Files")
        self.tree.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Total Info
        self.info_label = tk.Label(root, text="", fg="#00e5ff", bg="#0a0a0c", font=("Outfit", 10))
        self.info_label.pack(pady=10)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.scan_folder(folder_path)

    def scan_folder(self, path):
        # Clear previous results
        for i in self.tree.get_children():
            self.tree.delete(i)
            
        self.status_var.set(f"Scanning: {path}...")
        self.root.update_idletasks()

        extension_counter = Counter()
        total_files = 0
        total_size = 0

        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    total_files += 1
                    file_path = Path(root) / file
                    ext = file_path.suffix.lower() if file_path.suffix else "[No Extension]"
                    extension_counter[ext] += 1
                    try:
                        total_size += file_path.stat().st_size
                    except:
                        pass

            # Update Table
            for ext, count in extension_counter.most_common():
                self.tree.insert("", tk.END, values=(ext, count))

            size_mb = total_size / (1024*1024)
            self.info_label.config(text=f"Total Files: {total_files}  |  Total Size: {size_mb:.2f} MB")
            self.status_var.set("Scan Complete!")
            
        except Exception as e:
            messagebox.showerror("Scan Error", str(e))
            self.status_var.set("Error during scan.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AntigravityScanner(root)
    root.mainloop()
