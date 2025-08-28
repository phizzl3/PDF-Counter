import os
import pypdf


def count_pdfs_and_pages(folder_path):
    total_files = 0
    total_pages = 0

    print()

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
                    print(
                        f"Could not read {file_path}: {e}. Add it manually if needed.\n"
                    )

    print(f"Total PDF files found: {total_files}")
    print(f"Total pages across all PDFs: {total_pages}\n")


if __name__ == "__main__":
    folder = input("\nEnter the folder path containing PDF files: ").strip('"')
    if os.path.isdir(folder):
        print(f"\nScanning folder: {folder}")
        count_pdfs_and_pages(folder)
    else:
        print("Invalid folder path.")
