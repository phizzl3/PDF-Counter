__version__ = "1.0.0"

import os
import pypdf
import tkinter as tk
from tkinter import filedialog, messagebox


def count_pdfs_and_pages(folder_path):
    """
    Counts the number of PDF files and their total pages within a given folder and its subdirectories.
    Args:
        folder_path (str): The path to the folder to search for PDF files.
    Returns:
        tuple:
            total_files (int): The total number of PDF files found.
            total_pages (int): The total number of pages across all PDF files.
            exceptions (list of str): A list of error messages for files that could not be processed.
    Notes:
        - Only files with a ".pdf" extension (case-insensitive) are counted.
        - If a PDF file cannot be read or processed, the exception is recorded in the exceptions list.
    """
    total_files = 0
    total_pages = 0
    exceptions = []

    # Walk through all subdirectories
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".pdf"):
                total_files += 1
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "rb") as pdf_file:
                        reader = pypdf.PdfReader(pdf_file)
                        total_pages += len(reader.pages)
                except Exception as e:
                    exceptions.append(f"{file_path}: {e}")

    return total_files, total_pages, exceptions


def select_folder():
    folder = filedialog.askdirectory()
    result_text.set("Scanning...")
    root.update_idletasks()
    if folder:
        total_files, total_pages, exceptions = count_pdfs_and_pages(folder)
        result = (
            f"Total PDF files found: {total_files}\n"
            f"Total pages across all PDFs: {total_pages}\n"
        )
        if exceptions:
            result += (
                "\nFiles with errors (Not included in total count):\n"
                + "\n".join(exceptions)
            )
        result_text.set(result)
    else:
        messagebox.showerror("Error", "No folder selected.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PDF Counter")

    instruction_label = tk.Label(
        root,
        text="\nPlease select the folder to scan for PDF files:",
        font=("Arial", 12),
    )
    instruction_label.pack(padx=10, pady=(10, 0))
    result_text = tk.StringVar()
    result_label = tk.Label(
        root, textvariable=result_text, justify="left", font=("Arial", 14)
    )
    result_label.pack(padx=10, pady=10)

    select_button = tk.Button(
        root, text="Select Folder", command=select_folder, font=("Arial", 12)
    )
    select_button.pack(padx=10, pady=10)

    root.mainloop()
