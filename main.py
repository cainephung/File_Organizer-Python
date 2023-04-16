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

    
