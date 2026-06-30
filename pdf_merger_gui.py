# from pypdf import PdfWriter

# merger = PdfWriter()

# pdfs = ["file1.pdf", "file2.pdf", "file3.pdf"]  # List of PDF files to merge

# for pdf in pdfs:
#     merger.append(pdf)

# merger.write("merged.pdf")
# merger.close()

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter


def select_pdfs():
    files = filedialog.askopenfilenames(
        title="Select PDF files to merge", filetypes=[("PDF files", "*.pdf")]
    )
    if files:
        # Changed: Appends files instead of wiping the list,
        # allowing you to pick files from multiple folders.
        for file in files:
            if file not in pdf_list.get(0, tk.END):
                pdf_list.insert(tk.END, file)


def move_up():
    try:
        selected_index = pdf_list.curselection()[0]
        if selected_index == 0:
            return  # Already at the top

        # Get text of the selected item
        text = pdf_list.get(selected_index)
        # Delete it from current position
        pdf_list.delete(selected_index)
        # Insert it one position higher
        pdf_list.insert(selected_index - 1, text)
        # Keep the item highlighted
        pdf_list.select_set(selected_index - 1)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a file to move.")


def move_down():
    try:
        selected_index = pdf_list.curselection()[0]
        if selected_index == pdf_list.size() - 1:
            return  # Already at the bottom

        text = pdf_list.get(selected_index)
        pdf_list.delete(selected_index)
        pdf_list.insert(selected_index + 1, text)
        pdf_list.select_set(selected_index + 1)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a file to move.")


def clear_list():
    pdf_list.delete(0, tk.END)


def merge_pdfs():
    pdfs = list(pdf_list.get(0, tk.END))
    if not pdfs:
        messagebox.showerror("Error", "No PDF files selected!")
        return
    if len(pdfs) < 2:
        messagebox.showerror("Error", "Select at least 2 PDFs to merge.")
        return

    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save merged PDF as",
    )

    if output_file:
        merger = PdfWriter()
        try:
            for pdf in pdfs:
                merger.append(pdf)

            merger.write(output_file)
            merger.close()
            messagebox.showinfo(
                "Success",
                f"PDFs merged successfully into {os.path.basename(output_file)}",
            )
            clear_list()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


# --- GUI Setup ---
root = tk.Tk()
root.title("PDF Merger & Sorter")
root.geometry("450x400")

# Top controls
select_button = tk.Button(root, text="Select PDF Files", command=select_pdfs)
select_button.pack(pady=10)

# Main Listbox (Changed selectmode to SINGLE for easier sorting logic)
pdf_list = tk.Listbox(root, selectmode=tk.SINGLE, width=60, height=12)
pdf_list.pack(pady=5)

# Sorting & Control Buttons Layout
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

up_button = tk.Button(button_frame, text="🔼 Move Up", command=move_up)
up_button.pack(side=tk.LEFT, padx=5)

down_button = tk.Button(button_frame, text="🔽 Move Down", command=move_down)
down_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="🗑️ Clear List", command=clear_list)
clear_button.pack(side=tk.LEFT, padx=5)

# Action button
merge_button = tk.Button(
    root,
    text="Merge PDFs",
    command=merge_pdfs,
    bg="#008CBA",
    fg="white",
    font=("Arial", 10, "bold"),
)
merge_button.pack(pady=15)

root.mainloop()