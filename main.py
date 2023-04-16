import os
import shutil
import PIL

from tkinter import *
from threading import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog

# You can add more extensions to this dictionary
Extensions={
   'Documents' : ('.log','.LOG', '.rar','.RAR','.PDF','.DOC','.XLS','TXT','.CSV',\
    '.XML','.ZIP', '.DOCX', '.DOCX', '.ODT','.pdf','.doc','.xls','txt','.csv','.zip',\
    '.xml', '.docx', '.DOCX', '.odt', '.pptx', '.PPTX','.epub','.EPUB', '.tar.gz', 'TAR.GZ', '.iso.gz', 'ISO.GZ', '.7z', '.7Z','.ppt', '.PPT'),
   'Pictures' : ('.webp','.WEBP','.jfif','.JFIF','.jpg','.jpeg','.png', '.PNG','.JPG', '.JPEG', '.ico', '.ICO'),
   'Videos' : ('.mp4','.mkv','.3gp','.flv','.mpeg','.MP4','.MKV','.3GP','.FLV','.MPEG'),
   'Music' : ('.mp3','.wav','.m4a','.webm', '.MP3','.WAV','.M4A','.WEBM'),
   'Programs' : ('.srec','.SREC','.bin','.BIN', '.py','.cpp','.c','.cs','.CS','.sh','.js','.jsx', '.PY','.CPP','.C','.SH','.JS','.JSX','.s', '.asm','.ASM', '.S', '.tar', '.TAR', '.h', '.H'),
   'Apps' : ('.exe','.apk', '.EXE', '.APK','.iso', '.ISO', '.msi', '.MSI', '.ova', '.OVA'),

}

class File_Organizer:
    def __init__(self, root):
        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("750x500")
        self.window.title('File Organizer - Caine Phung')
        self.window.resizable(width = False, height = False)
        self.window.configure(bg='lime green')

        self.Selected_Dir = ''
        self.Browsed = False

        Heading_Label = Label(self.window, text="File Organizer", justify=CENTER  , font=("Kokila", 45, 'bold'), bg='lime green', fg= "white")
        Heading_Label.place(x=170, y=20)
       

        # Frame 2: For the Main Page Widgets
        self.frame_2 = Frame(self.window, bg="lime green",\
        width=750,height=500)
        self.frame_2.place(x=0, y=110)

        # Calling the function to display main pageF
        # widgets
        self.Main_Page()

    
    # This function displays all the widgets in the 'self.frame_2'
    # related to File Organizing Operation
    def Main_Page(self):
        # Heading Label
    

        # The directory path selected from the Tkinter file dialog 
        # that opens by the 'Folder_Button' is displayed here.
        # self.Folder_Entry = Entry(self.frame_2, \
        # font=("Helvetica", 12), width=32)
        # self.Folder_Entry.place(x=256, y=85)

        self.Folder_Button = Button(self.frame_2, text="Select Folder", \
        font=("Kozuka Gothic Pro R", 16, 'bold'), bg="gold", width=20, \
        command=self.Select_Directory)
        self.Folder_Button .place(relx= 0.5, rely=0.125, anchor= CENTER)

        self.choosen = Label(self.frame_2, text="... ", \
        font=("Kokila", 14, 'bold'), bg='lime green', wraplength=720)
        self.choosen.place(relx= 0.5, rely=0.25, anchor= CENTER)

        self.Status = Label(self.frame_2, text="Status: ", \
        font=("Kokila", 16, 'bold'), bg='lime green')
        self.Status.place(relx= 0.25, rely=0.60, anchor= CENTER)

        # Status Label:
        # Options: 'Not Started Yet(By Default), or 'Processing...',
        # or 'Complete!''
        self.Status_Label = Label(self.frame_2, text="Not Started Yet ...", \
        font=("Kokila", 16), bg='lime green', fg="red")
        self.Status_Label.place(relx= 0.5, rely=0.6, anchor= CENTER)

        # Start Button: Users have to press this button
        # to start the operation
        self.Start_Button = Button(self.frame_2, text="Start", \
        font=("Kokila", 16, 'bold'), bg="dodger blue", fg="white", \
        width=20, command=self.Organizer)
        self.Start_Button.place(relx= 0.5, rely=0.5, anchor= CENTER)

            # Exit Button
        self.Exit_Btn = Button(self.frame_2, text="Exit", \
        font=("Kokila", 16, 'bold'), bg="dodger blue", \
        fg="white", width=20, command=self.Exit_Window)
        self.Exit_Btn.place(relx= 0.5, rely=0.7, anchor= CENTER)

        

    # This function opens the Tkinter file dialog to
    # let users select the directory where the files are presented
    def Select_Directory(self):
        self.Selected_Dir = filedialog.askdirectory(title = \
        "Select a location")
        
        self.Selected_Dir = str(self.Selected_Dir)
        self.choosen.config(text= self.Selected_Dir)

        # Checks if the folder path is exists or not
        if os.path.exists(self.Selected_Dir):
            self.Browsed = True

    # Creating a different thread to run the 'self.Organizer' function
    def Threading(self):
        # Killing a thread through "daemon=True" isn't a good idea
        self.x = Thread(target=self.Organizer, daemon=True)
        self.x.start()
    
    # The Organizer function 
    def Organizer(self):
        # If no directory is chosen
        if not self.Browsed:
            messagebox.showwarning('No folders are choosen', \
            'Please Select a Folder First')
            return
        try:
            # Showing the current status of the operation
            self.Status_Label.config(text='Processing...')

            self.Current_Path = self.Selected_Dir
 
            if os.path.exists(self.Current_Path):
            # self.Folder_List1: stores all the folders that 
            # are already presented in the selected directory
                self.Folder_List1 = []
                # self.Folder_List2 stores newly created folders
                self.Folder_List2 = []
                self.Flag = False
 
                for folder, extensions in Extensions.items():
                    self.folder_name = folder
                    self.folder_path = os.path.join(self.Current_Path, self.folder_name)
 
                    # Change the directory to the current 
                    # folder path that we've selected
                    os.chdir(self.Current_Path)
 
                    # If the folder is already present in that directory
                    if os.path.exists(self.folder_name):
                        self.Folder_List1.append(self.folder_name)
                   # If the folder is not present in that directory,
                   # then create a new folder
                    else:
                        self.Folder_List2.append(self.folder_name)
                        os.mkdir(self.folder_path)
                    
                    # Calling the 'File_Finder()' function to
                    # find a specific type of file(extension)
                    # and change their old path to new path(for separation)
                    for item in self.File_Finder(self.Current_Path, extensions):
                        self.Old_File_Path = os.path.join(self.Current_Path,item)
                        self.New_File_Path = os.path.join(self.folder_path,item)
 
                        # Moving each file to their new location(folder)
                        shutil.move(self.Old_File_Path, self.New_File_Path)
                        # Making the 'self.Frag' variable True
                        self.Flag = True
            else:
                messagebox.showerror('Error!','Please Enter a Valid Path!')
 
            # Checking files are separated or not
            # If Flag is True: It means the program had found
            # some matching files and those have been organized
            if self.Flag:
                self.Status_Label.config(text='Complete!',fg='green')
                messagebox.showinfo('Done!', 'Complete!')
                self.Clear()
            # If Flag is False: It means the program didn't find
            # any matching files there; only folders are created
            if not self.Flag:
                self.Status_Label.config(text='Complete!', fg='green')
                messagebox.showinfo('Done!', \
                'Folders have been created\nNo Files were there to move')
                self.Clear()
        # If any error occurs
        except Exception as es:
            messagebox.showerror("Failed")

    # This function finds a specific file-type in
    # the selected directory, appends the matched file path
    # to a list, and returns that list
    def File_Finder(self,folder_path, file_extensions):
        self.files = []
        for file in os.listdir(folder_path):
            for extension in file_extensions:
                if file.endswith(extension):
                    self.files.append(file)
        return self.files

    def Clear(self):
        self.Status_Label.config(text='Not Started Yet ...', fg='red')
        self.Selected_Dir = '...'
        self.choosen.config(text= '...')

   
    
    # This function closes the main window
    def Exit_Window(self):
        self.window.destroy()

# The main function
if __name__ == "__main__":
    root = Tk()
    # Creating a 'File_Renamer' class object
    obj = File_Organizer(root)
    root.mainloop()

