'''
File Handling
    ->Normally, when a python programs runs, data created during execution is
      stored in memory (RAM). When the program terminates, that temporary data
      is lost.

    ->If we want to store data persistently we can store it in a file on secondary
      storage such as an SSD, hard disk, or pendrive. The data remains available even
      after the program terminates.
      
    ->File-a file is a named location on a storage device where data is stores
      permanently so that we can is it later.


FileHandling is the process of creating , opening, reading, writing, and managing
files using a program.

1.1)text files -> Stores data as characters/text
Ex: Student.txt
1.2)Binary files-> Stores data in binary form, generally not intended to be read
                   directly as human-readable text.
Ex:audio(.mp3), images(.jpg,.png), video(.mp4)

2)Database: used when data becomes structured and needs searching, relationships,
            transactions and multiple users.

Important functions which are used wrt file handling
----------------------------------------------------
1)open()
-------
Syntax:
    f=open("filepath", "operationmode")

-open() is a built-in python function that opens a file and establishes a connection
 between the python program and the file. it returns a file object through which
 we can perform operations on the file.

We have different modes in which file can be opened:

Imp attributes in file object:
------------------------------

1)f.name-->displays the name of the file
2)f.mode-->gives the mode in which file is open
3)f.closed-->used to check whether the file is closed or not and it gives boolean
  value.

We have different modes in which a file can be opened:

1)'r'-> read only
    -if the file exists, it opens the file in read mode.
    -if file DOES NOT exit it raise FileNotFoundError

i)readable()
    Syntax:
        f.readable()

    -Checks whether the file is opened in a mode that allows reading and return
     a boolean value.
     
ii)writable()
    Syntax:
        f.writable()
    -Checks whether the file is opened in a mode that allows writing and return
     a boolen value.

iii)read(n)
    Syntax:
        data=f.read(n)
    -method of file object, if n is given reads Exactly upto n characters from
     the current position and returns it as a string.
    -If n is not given, reads the entire file and returns it as a string.
    
iv)readline(n)
    Syntax:
        data=f.readline(n)

    -readline(n) reads up to n characters, but only within the current line.
    -if n is not given, it reads the complete line.

v)readlines()
    Syntax:
        data= f.readlines()
    -reads all remaining lines and returns them as a list of strings, with each
     element representing one line.

2)'w'->write only
----------------
    -if file exists, it opens the file in write mode BUT all the existing data will
     be erased.
    -if file DOES NOT exist, a new file of that name will be created and opened in
     write mode.

i)write(string)
    Syntax:
        f.write(string)
    -method of file object used to send the string data from python into a file.
    -write() does not automatically add a newline.

ii)writelines(list)
    Syntax:
        f.writelines(listofstring)
    -method of file object which writes elements of an iterable to the file.It
     does not automatically add newline characters.

3)'a'->append mode
------------------
    -if file exists, it opens the file in write mode BUT it retains the existing
     data, all write operations happen at end only, even if seek() is used.
    -if file does not EXIST, a new file of that name will be created and opened
     in write mode.

4)'r+'->read and write mode
---------------------------
    -if file exists it opens the file in read+ write mode and cursor starts at
     begining.
    -if file is not present, FileNotFoundError

5)'w+'->write and read mode
---------------------------
    -if file exists, it opens the file in write+read mode, existing data erased
     & cursor starts at begining.
    -if file not present, it creates a file and opens in write mode.

i)tell()
    Syntax:
        position=f.tell()
    -it returns the current file cursor position in the form of int.

ii)seek(offset)
    Syntax:
        f.seek(offset)
    -method of file object is used to move the file cursor to a specified position
     by passing the positive int value.

iii)close()
    Syntax:
        f.close()
    -close() is a method of the file object used to close the file and release the
     resources associated with it in simple terms, it disconnects the program from
     the file.

6)'a+'->append and read mode
----------------------------
    -if file exists, it opens the file in append+read mode, &cursor is at the end
     of the file & all write operations happen at end only even if seek() is used

    -if file not present, it create a file and opens in write mode.

7)'x'->exclusive
----------------
    -if the file is already existing -> FileExistError
    -it creates a new file in write mode, ONLY if that file is NOT existing
    -it is used when you specifically want to create a new file and don't want
     to accidently overwrite an existing file.

with:
-----
    Syntax:
        with open("filename.txt","mode") as variable:
            -------------------------------------
        -->|#file operations in this indentation |
           |         block                       |
            -------------------------------------

    -with keyword opens the file, gives it a name, and closes the file when the
     block ends.
    -with statement/keyword "automatically" handles opening and closing of a file,
     even if an exception occurs.

'''