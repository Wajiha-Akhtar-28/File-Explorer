from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os
import shutil
from cryptography.fernet import Fernet
import zipfile

# File Operations
def create_file():
    file_path = fd.askdirectory(title="Select the location where you want to create the file")
    if file_path:
        create_wn = Toplevel(root)
        create_wn.title("Create File")
        create_wn.geometry("250x70")
        create_wn.resizable(0, 0)
        Label(create_wn, text='Enter the name of the new file:', font=("Times New Roman", 10)).place(x=0, y=0)
        new_file_name = Entry(create_wn, width=40, font=("Times New Roman", 10))
        new_file_name.place(x=0, y=30)

        def create():
            new_file = os.path.join(file_path, new_file_name.get())
            try:
                with open(new_file, 'w') as f:
                    f.write("")  # Create an empty file
                mb.showinfo("File Created", f"File '{new_file_name.get()}' has been created successfully!")
                create_wn.destroy()
            except FileExistsError:
                mb.showerror("Error", f"A file with the name '{new_file_name.get()}' already exists.")
            except Exception as e:
                mb.showerror("Error", f"An error occurred: {e}")

        Button(create_wn, text="Create", command=create).place(x=200, y=30)
        
# Backend functions
def open_file():
   file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")])
   os.startfile(os.path.abspath(file))

def copy_file():
   file_to_copy = fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")])
   dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?")
   try:
       shutil.copy(file_to_copy, dir_to_copy_to)
       mb.showinfo(title='File copied!', message='Your desired file has been copied to your desired location')
   except:
       mb.showerror(title='Error!', message='We were unable to copy your file to the desired location. Please try again')

def delete_file():
   file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])
   os.remove(os.path.abspath(file))
   mb.showinfo(title='File deleted', message='Your desired file has been deleted')
   
def move_file():
   file_to_move = fd.askdirectory(title='Select the file you want to move')
   mb.showinfo(message='You just selected the file to move, now please select the desired destination where you want to move the file to')
   destination = fd.askdirectory(title='Where to move the file to')
   try:
       shutil.move(file_to_move, destination)
       mb.showinfo("File moved", 'Your desired file has been moved to the location you wanted')
   except:
       mb.showerror('Error', 'We could not move your file. Please make sure that the destination exists')

def rename_file():
    file = fd.askopenfilename(title='Choose a file to rename', filetypes=[("All files", "*.*")])
    if not file:
        return

    rename_wn = Toplevel(root)
    rename_wn.title("Rename the file")
    rename_wn.geometry("300x100")
    rename_wn.resizable(0, 0)

    Label(rename_wn, text='Enter the new name of the file:', font=("Times New Roman", 10)).place(x=10, y=10)
    new_name = Entry(rename_wn, width=40, font=("Times New Roman", 10))
    new_name.place(x=10, y=40)

    def rename():
        new_file_name = os.path.join(os.path.dirname(file), new_name.get() + os.path.splitext(file)[1])
        try:
            os.rename(file, new_file_name)
            mb.showinfo(title="File Renamed", message='Your file has been renamed successfully.')
            rename_wn.destroy()
        except Exception as e:
            mb.showerror("Error", f"An error occurred: {e}")

    Button(rename_wn, text="OK", command=rename, width=10, font=("Times New Roman", 10)).place(x=200, y=40)
    
def create_folder():
    folder_path = fd.askdirectory(title="Select the location where you want to create the folder")
    if folder_path:
        create_wn = Toplevel(root)
        create_wn.title("Create Folder")
        create_wn.geometry("250x70")
        create_wn.resizable(0, 0)
        Label(create_wn, text='Enter the name of the new folder:', font=("Times New Roman", 10)).place(x=0, y=0)
        new_folder_name = Entry(create_wn, width=40, font=("Times New Roman", 10))
        new_folder_name.place(x=0, y=30)
        
        def create():
            new_folder = os.path.join(folder_path, new_folder_name.get())
            try:
                os.makedirs(new_folder)
                mb.showinfo("Folder Created", f"Folder '{new_folder_name.get()}' has been created successfully!")
                create_wn.destroy()
            except FileExistsError:
                mb.showerror("Error", f"A folder with the name '{new_folder_name.get()}' already exists.")
            except Exception as e:
                mb.showerror("Error", f"An error occurred: {e}")
        
        Button(create_wn, text="Create", command=create).place(x=200, y=30)

def open_folder():
   folder = fd.askdirectory(title="Select Folder to open")
   os.startfile(folder)
   
def copy_folder():
    folder_to_copy = fd.askdirectory(title='Choose a folder to copy')
    if not folder_to_copy:
        return
    destination = fd.askdirectory(title='Select the destination to copy the folder to')
    if not destination:
        return
    try:
        shutil.copytree(folder_to_copy, os.path.join(destination, os.path.basename(folder_to_copy)))
        mb.showinfo("Folder Copied", "The folder has been successfully copied!")
    except FileExistsError:
        mb.showerror("Error", "A folder with the same name already exists at the destination.")
    except Exception as e:
        mb.showerror("Error", f"An error occurred: {e}")

def delete_folder():
   folder_to_delete = fd.askdirectory(title='Choose a folder to delete')
   os.rmdir(folder_to_delete)
   mb.showinfo("Folder Deleted", "Your desired folder has been deleted")

def move_folder():
   folder_to_move = fd.askdirectory(title='Select the folder you want to move')
   mb.showinfo(message='You just selected the folder to move, now please select the desired destination where you want to move the folder to')
   destination = fd.askdirectory(title='Where to move the folder to')
   try:
       shutil.move(folder_to_move, destination)
       mb.showinfo("Folder moved", 'Your desired folder has been moved to the location you wanted')
   except:
       mb.showerror('Error', 'We could not move your folder. Please make sure that the destination exists')
       
def rename_folder():
    folder_to_rename = fd.askdirectory(title='Choose a folder to rename')
    if not folder_to_rename:
        return

    rename_wn = Toplevel(root)
    rename_wn.title("Rename Folder")
    rename_wn.geometry("300x100")
    rename_wn.resizable(0, 0)

    Label(rename_wn, text='Enter the new name of the folder:', font=("Times New Roman", 10)).place(x=10, y=10)
    new_name = Entry(rename_wn, width=40, font=("Times New Roman", 10))
    new_name.place(x=10, y=40)

    def rename():
        new_folder_path = os.path.join(os.path.dirname(folder_to_rename), new_name.get())
        try:
            os.rename(folder_to_rename, new_folder_path)
            mb.showinfo("Folder Renamed", "The folder has been successfully renamed!")
            rename_wn.destroy()
        except FileExistsError:
            mb.showerror("Error", "A folder with the same name already exists.")
        except Exception as e:
            mb.showerror("Error", f"An error occurred: {e}")

    Button(rename_wn, text="OK", command=rename, width=10, font=("Times New Roman", 10)).place(x=200, y=40)

# Encryption Key Setup
if not os.path.exists("filekey.key"):
    with open("filekey.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open("filekey.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

def encrypt_file():
    file = fd.askopenfilename(title='Choose a file to encrypt', filetypes=[("All files", "*.*")])
    if file:
        try:
            with open(file, 'rb') as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file, 'wb') as f:
                f.write(encrypted_data)
            mb.showinfo("Success", "File has been encrypted successfully!")
        except Exception as e:
            mb.showerror("Error", f"An error occurred: {e}")


def decrypt_file():
    file = fd.askopenfilename(title='Choose a file to decrypt', filetypes=[("All files", "*.*")])
    if file:
        try:
            with open(file, 'rb') as f:
                encrypted_data = f.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            with open(file, 'wb') as f:
                f.write(decrypted_data)
            mb.showinfo("Success", "File has been decrypted successfully!")
        except Exception as e:
            mb.showerror("Error", f"An error occurred: {e}")


def compress_file():
    file = fd.askopenfilename(title='Choose a file to compress', filetypes=[("All files", "*.*")])
    if file:
        compressed_file = file + '.zip'
        try:
            with zipfile.ZipFile(compressed_file, 'w') as zipf:
                zipf.write(file, os.path.basename(file), compress_type=zipfile.ZIP_DEFLATED)
            mb.showinfo("Success", f"File has been compressed to {compressed_file}")
        except Exception as e:
            mb.showerror("Error", f"An error occurred: {e}")


import zipfile

def decompress_file():
    # Ask the user to select a file to decompress
    compressed_file = fd.askopenfilename(title="Select a file to decompress", filetypes=[("Zip files", "*.zip")])
    if not compressed_file:
        return  # User canceled the operation

    # Ask the user to select a destination folder for extraction
    destination = fd.askdirectory(title="Select a destination to extract the files")
    if not destination:
        return  # User canceled the operation

    # Try to extract the files
    try:
        with zipfile.ZipFile(compressed_file, 'r') as zipf:
            # Check if the file is a valid zip archive
            if zipf.testzip() is not None:
                mb.showerror("Error", "The zip file is corrupted and cannot be decompressed.")
                return

            # Extract all files to the chosen destination
            zipf.extractall(destination)
        mb.showinfo("File Decompressed", f"Files have been extracted to: {destination}")
    except zipfile.BadZipFile:
        mb.showerror("Error", "The selected file is not a valid zip file.")
    except PermissionError:
        mb.showerror("Error", "Permission denied. Ensure you have access to the destination folder.")
    except Exception as e:
        mb.showerror("Error", f"An error occurred: {e}")

def list_files_in_folder():
   i = 0
   folder = fd.askdirectory(title='Select the folder whose files you want to list')
   files = os.listdir(os.path.abspath(folder))
   list_files_wn = Toplevel(root)
   list_files_wn.title(f'Files in {folder}')
   list_files_wn.geometry('250x250')
   list_files_wn.resizable(0, 0)
   listbox = Listbox(list_files_wn, selectbackground='SteelBlue', font=("Georgia", 10))
   listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
   scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
   scrollbar.pack(side=RIGHT, fill=Y)
   listbox.config(yscrollcommand=scrollbar.set)
   while i < len(files):
       listbox.insert(END, files[i])
       i += 1
# GUI Variables
title = 'File Explorer'
background = 'wheat'
button_font = ("Times New Roman", 13)
button_background = 'coral'

# Initialize the window
root = Tk()
root.title(title)
root.geometry('520x420')
root.resizable(0, 0)
root.config(bg=background)

# Components
Label(root, text=title, font=("roboto", 15), bg=background, wraplength=250).place(x=200, y=10)
Button(root, text='Create a file', width=20, font=button_font, bg=button_background, command=create_file).place(x=30, y=50)
Button(root, text='Open a file', width=20, font=button_font, bg=button_background, command=open_file).place(x=30, y=90)
Button(root, text='Rename a file', width=20, font=button_font, bg=button_background, command=rename_file).place(x=30, y=130)
Button(root, text='Delete a file', width=20, font=button_font, bg=button_background, command=delete_file).place(x=30, y=170)
Button(root, text='Move a file', width=20, font=button_font, bg=button_background, command=move_file).place(x=30, y=210)
Button(root, text='Copy a file', width=20, font=button_font, bg=button_background, command=copy_file).place(x=30, y=250)
Button(root, text='Encrypt a file', width=20, font=button_font, bg=button_background, command=encrypt_file).place(x=30, y=290)
Button(root, text='Decrypt a file', width=20, font=button_font, bg=button_background, command=decrypt_file).place(x=30, y=330)
Button(root, text='Compress a file', width=20, font=button_font, bg=button_background, command=compress_file).place(x=300, y=50)
Button(root, text='Decompress a file', width=20, font=button_font, bg=button_background, command=decompress_file).place(x=300, y=90)



Button(root, text='Open a folder', width=20, font=button_font, bg=button_background, command=open_folder).place(x=300, y=130)
Button(root, text='Create a folder', width=20, font=button_font, bg=button_background, command=create_folder).place(x=300, y=170)
Button(root, text='Delete a folder', width=20, font=button_font, bg=button_background, command=delete_folder).place(x=300, y=210)
Button(root, text='Copy a folder', width=20, font=button_font, bg=button_background, command=copy_folder).place(x=300, y=250)
Button(root, text='Rename a folder', width=20, font=button_font, bg=button_background, command=rename_folder).place(x=300, y=290)
Button(root, text='Move a folder', width=20, font=button_font, bg=button_background, command=move_folder).place(x=300, y=330)
Button(root, text='List all files in a folder', width=20, font=button_font, bg=button_background, command=list_files_in_folder).place(x=180, y=370)

# Finalize
root.update()
root.mainloop()
