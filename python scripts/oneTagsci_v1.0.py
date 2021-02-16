import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk,Image
from tkinter import messagebox
import serial
import time
import sqlite3
import sys
import os


# create database
conn = sqlite3.connect('studentDatabase.db')
curs = conn.cursor()

# create table
#curs.execute("create table STEM21(RFIDcode, Name, GradeNSec, LRN, Sex, Birthday, Contact, imgFile)")

conn.commit()







def accessDBwindowFunc():
    mainWindow.destroy()
    
    def writeDetails():
        query1 = ("SELECT * FROM STEM21")     # Sample select query, may vary depending on purpose
        curs.execute(query1)
        
        dataFromDatabase = curs.fetchall()
        
        keyFromEntry = str(accessEntry1.get())
        #print(keyFromEntry)
        
        for row in dataFromDatabase:
            if row[0] == keyFromEntry:
                name = row[1]
                grade = row[2]
                lrn = row[3]
                sex = row[4]
                bday = row[5]
                contact = row[6]
                imageFile = str(row[7])
                
                accessLabelName2.configure(text = name)
                accessLabelGradeSec2.configure(text = grade)
                accessLabelLRN2.configure(text = lrn)
                accessLabelSex2.configure(text = sex)
                accessLabelBday2.configure(text = bday)
                accessLabelContact2.configure(text = contact)
                
                global imageDisplay #PAAAKSHEEEET
                imageDisplay = ImageTk.PhotoImage((Image.open(imageFile)).resize((250,250), Image.ANTIALIAS))
                
                #accessCanvas1.grid_forget()
                accessCanvas1.itemconfigure(myimg, image = imageDisplay)
                
                
                
        
    
    
    def readRFID1():   # Read RFID from arduino
        # Establishing connection with arduino
        # the '/dev/ttyACM0' parameter depends on the arduino name in rpi
        if __name__ == '__main__':
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            ser.flush()

            line = ""
           
            while line == "":    # While no received key from arduino, keep on trying to read
                ser.write(b"scanNOW\n")
                line = ser.readline().decode('utf-8').rstrip()
                time.sleep(1)
                print("Key: ", line)
            
            #return str(line)
            line = str(line)
            
            accessEntry1.delete(first = 0, last = 100)
            accessEntry1.configure(show = "*")
            accessEntry1.insert(0, line)
            
            writeDetails()
    
    def restartProgram():
        #exit()
        os.execl(sys.executable, sys.executable, *sys.argv)
        
    
      
    #ACCESS START
    accessDBwindow = tk.Tk()
    accessDBwindow.geometry("920x620+300+50")
    accessDBwindow.configure(bg = '#2d2d2d')
    
    
    #register Start
    def registerWindowFunc():
        accessDBwindow.destroy()
        
        #rfid2 start
        def readRFID2():   # Read RFID from arduino
            if __name__ == '__main__':
                ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
                ser.flush()

                line = ""
               
                while line == "":    # While no received key from arduino, keep on trying to read
                    ser.write(b"scanNOW\n")
                    line = ser.readline().decode('utf-8').rstrip()
                    time.sleep(1)
                    print("Key: ", line)
                
                #return str(line)
                line = str(line)
                
                query1 = ("SELECT * FROM STEM21")     # Sample select query, may vary depending on purpose
                curs.execute(query1)
                
                dataFromDatabase = curs.fetchall()
                
                validRFID = True
                for row in dataFromDatabase:
                    if row[0] == line:
                        validRFID = False
                
                if validRFID == True:
                    registerEntry1.delete(first = 0, last = 100)
                    registerEntry1.configure(show = "*")
                    registerEntry1.insert(0, line)
                else:
                    messagebox.showwarning("RFID Code Error", "RFID Code Already in Use!")
                #end of rfid2
        
        def checkImage():
            imageFile2 = str(registerEntryImagePath.get())
            print(imageFile2) #test
            
            global imageDisplay2 #PAAAKSHEEEET
            imageDisplay2 = ImageTk.PhotoImage((Image.open(imageFile2)).resize((250,250), Image.ANTIALIAS))
            #imageDisplay2 = imageDisplay2.resize((200,200), Image.ANTIALIAS)
            registerCanvas.itemconfigure(myimg2, image = imageDisplay2)
        
        def confirm():
            rfidCode = registerEntry1.get()
            name = registerEntryName.get()
            grade = registerEntryGrade.get()
            lrn = registerEntryLRN.get()
            sex = registerEntrySex.get()
            bday = registerEntryBday.get()
            contact = registerEntryContact.get()
            imagePath = registerEntryImagePath.get()
            
            if (rfidCode == "    RFID CODE") or (name == "") or (grade == "") or (lrn == "") or (sex == "") or (bday == "") or (contact == "") or (imagePath == "images/"):
                messagebox.showwarning("Registration Error", "Please Fill Up Everything!")
            else:
                dataTuple = rfidCode, name, grade, lrn, sex, bday, contact, imagePath
                query2 = "INSERT INTO STEM21 (RFIDcode, Name, GradeNSec, LRN, Sex, Birthday, Contact, imgFile) VALUES (?,?,?,?,?,?,?,?)"
                curs.execute(query2, dataTuple)
                conn.commit()
                
                messagebox.showinfo("Registration Info", "Registered Successfully")
                os.execl(sys.executable, sys.executable, *sys.argv)
                
        
        registerWindow = tk.Tk()
        registerWindow.geometry("920x620+300+50")
        registerWindow.configure(bg = '#2d2d2d')
            
        fontStyle1 = tkFont.Font(registerWindow, family="Lucida Grande", size = 30, weight = "bold")
        fontStyle2 = tkFont.Font(registerWindow, family="Lucida Grande", size = 15, slant = "italic")
        fontStyle3 = tkFont.Font(registerWindow, family="Lucida Grande", size = 13)
        fontStyle4 = tkFont.Font(registerWindow, family="Lucida Grande", size = 15, weight = "bold")
        fontStyle5 = tkFont.Font(registerWindow, family="Lucida Grande", size = 15)    
            
            
            
        #labelx
        registerLabelx1 = tk.Label(registerWindow, text = " ", 
                              bg = '#2d2d2d',
                              )
        registerLabelx2 = tk.Label(registerWindow, text = " ", 
                              bg = '#2d2d2d',
                              )
        registerLabelx3 = tk.Label(registerWindow, text = " ", 
                              bg = '#2d2d2d',
                              )
        registerLabelx4 = tk.Label(registerWindow, text = " ", 
                              bg = '#2d2d2d',
                              )
        registerLabelx5 = tk.Label(registerWindow, text = " ", 
                              bg = '#2d2d2d',
                              )

        #label
        registerLabel1 = tk.Label(registerWindow,  
                              text = "    REGISTER", 
                              font=fontStyle1, 
                              bg = '#2d2d2d',
                              fg = 'white')

        registerLabelName1 = tk.Label(registerWindow, text = "NAME:", 
                              font=fontStyle5, 
                              bg = '#2d2d2d',
                              fg = 'white', width = 15, anchor = "w")
            
        registerLabelGradeSec1 = tk.Label(registerWindow, text = "Grade & Sec:", 
                              font=fontStyle5, 
                              bg = '#2d2d2d',
                              fg = 'white')

        registerLabelLRN1 = tk.Label(registerWindow, text = "LRN:", 
                              font=fontStyle5, 
                              bg = '#2d2d2d',
                              fg = 'white')

        registerLabelSex1 = tk.Label(registerWindow, text = "Sex:", 
                              font=fontStyle5, 
                              bg = '#2d2d2d',
                              fg = 'white')

        registerLabelBday1 = tk.Label(registerWindow, text = "Date of Birth:", 
                              font=fontStyle5, 
                              bg = '#2d2d2d',
                              fg = 'white')

        registerLabelContact1 = tk.Label(registerWindow, text = "Contact No:", 
                              font=fontStyle5, 
                              bg = '#2d2d2d',
                              fg = 'white')
        registerLabelImagePath = tk.Label(registerWindow, text = "Image Path:", 
                              font=fontStyle5, 
                              bg = '#2d2d2d',
                              fg = 'white')


        #entry
        registerEntry1 = tk.Entry(registerWindow, 
                              font=fontStyle3, 
                              bg = '#bebebe', fg = "#2d2d2d", 
                              width = 14)
        registerEntryName = tk.Entry(registerWindow,  
                              font=fontStyle5, 
                              bg = 'white',
                              fg = '#2d2d2d', 
                              width = 25)
        registerEntryGrade = tk.Entry( registerWindow, 
                              font=fontStyle5, 
                              bg = 'white',
                              fg = '#2d2d2d', 
                              width = 25)
        registerEntryLRN = tk.Entry( registerWindow, 
                              font=fontStyle5, 
                              bg = 'white',
                              fg = '#2d2d2d', 
                              width = 25)
        registerEntrySex = tk.Entry( registerWindow, 
                              font=fontStyle5, 
                              bg = 'white',
                              fg = '#2d2d2d', 
                              width = 25)
        registerEntryBday = tk.Entry( registerWindow, 
                              font=fontStyle5, 
                              bg = 'white',
                              fg = '#2d2d2d', 
                              width = 25)
        registerEntryContact = tk.Entry( registerWindow, 
                              font=fontStyle5, 
                              bg = 'white',
                              fg = '#2d2d2d', 
                              width = 25)
        registerEntryImagePath = tk.Entry( registerWindow, 
                              font=fontStyle5, 
                              bg = 'white',
                              fg = '#2d2d2d', 
                              width = 25)
            
            

        #button
        registerButtonScan = tk.Button(registerWindow, text = "Scan", 
                                      height = 1, width = 10,
                                      relief = "groove", 
                                      bg = '#bebebe', fg = "#2d2d2d",
                                      font = fontStyle4, command = readRFID2)
        registerButtonConfirm = tk.Button(registerWindow, text = "Confirm", 
                                      width = 10,
                                      relief = "groove", 
                                      bg = '#bebebe', fg = "#2d2d2d",
                                      font = fontStyle4, command = confirm)
        registerButtonCheckImage = tk.Button(registerWindow, text = "Check Img", 
                                      width = 10,
                                      relief = "groove", 
                                      bg = '#bebebe', fg = "#2d2d2d",
                                      font = fontStyle4, command = checkImage)

        #canvas
        registerCanvas = tk.Canvas(registerWindow, width = 200, height = 200)
        
            
            
        #LAYOUT
        
            
            
        registerLabel1.grid(column = 0, columnspan = 4, pady = 10)
        
        #accessLabelx1.grid(row = 2, column = 0, pady = 10)
        registerLabelx4.grid(row = 3, column = 0, pady = 20) #orig 45
        registerEntry1.grid(row = 4, column = 0, pady = 5, padx = 80)

        registerEntry1.insert(0, "    RFID CODE")

        registerButtonScan.grid(row = 5, column = 0, padx = 80)
        registerLabelx2.grid(row = 6, column = 0, padx = 80, pady = 45)
        registerLabelx3.grid(row = 7, column = 0, padx = 80)
        registerLabelx5.grid(row = 8, column = 0, padx = 80)
        registerButtonCheckImage.grid(row = 10, column = 0, padx = 80)
        registerButtonConfirm.grid(row = 12, column = 0, padx = 80)

        
        registerCanvas.grid(row = 3, column = 3, rowspan = 4)
        img2 = ImageTk.PhotoImage((Image.open("images/imgDefault.jpg").resize((250,250), Image.ANTIALIAS)))
        myimg2 = registerCanvas.create_image(100,120, image = img2)
        

        registerLabelName1.grid(row = 8, column = 2, sticky = "w", pady = 7)
        registerLabelGradeSec1.grid(row = 9, column = 2, sticky = "w")
        registerLabelLRN1.grid(row = 10, column = 2, sticky = "w", pady = 7)
        registerLabelSex1.grid(row = 11, column = 2, sticky = "w")
        registerLabelBday1.grid(row = 12, column = 2, sticky = "w", pady = 7)
        registerLabelContact1.grid(row = 13, column = 2, sticky = "w")
        registerLabelImagePath.grid(row = 14, column = 2, sticky = "w", pady = 7)
        

        registerEntryName.grid(row = 8, column = 3, sticky = "w")
        registerEntryGrade.grid(row = 9, column = 3, sticky = "w")
        registerEntryLRN.grid(row = 10, column = 3, sticky = "w")
        registerEntrySex.grid(row = 11, column = 3, sticky = "w")
        registerEntryBday.grid(row = 12, column = 3, sticky = "w")
        registerEntryContact.grid(row = 13, column = 3, sticky = "w")
        
        registerEntryImagePath.grid(row = 14, column = 3, sticky = "w")
        registerEntryImagePath.insert(0, "images/")
            
        
        
            
        #end
        registerWindow.mainloop()
        
    
    
    
    
    
    

    # widgets
    fontStyle1 = tkFont.Font(family="Lucida Grande", size = 30, weight = "bold")
    fontStyle2 = tkFont.Font(family="Lucida Grande", size = 15, slant = "italic")
    fontStyle3 = tkFont.Font(family="Lucida Grande", size = 13)
    fontStyle4 = tkFont.Font(family="Lucida Grande", size = 15, weight = "bold")
    fontStyle5 = tkFont.Font(family="Lucida Grande", size = 15)
    
    img = ImageTk.PhotoImage((Image.open("images/imgDefault.jpg")).resize((250,250), Image.ANTIALIAS)) # OPEN IMAGE
    
    
    #labelx
    accessLabelx1 = tk.Label(text = " ", 
                      bg = '#2d2d2d',
                      )
    accessLabelx2 = tk.Label(text = " ", 
                      bg = '#2d2d2d',
                      )
    accessLabelx3 = tk.Label(text = " ", 
                      bg = '#2d2d2d',
                      )
    accessLabelx4 = tk.Label(text = " ", 
                      bg = '#2d2d2d',
                      )
    accessLabelx5 = tk.Label(text = " ", 
                      bg = '#2d2d2d',
                      )
    
    #label
    accessLabel1 = tk.Label( 
                      text = "      STUDENT DATABASE", 
                      font=fontStyle1, 
                      bg = '#2d2d2d',
                      fg = 'white')
    accessLabel2 = tk.Label(text = "New Student?", 
                      font=fontStyle2, 
                      bg = '#2d2d2d',
                      fg = 'white')
    
    accessLabelName1 = tk.Label(text = "NAME:", 
                      font=fontStyle5, 
                      bg = '#2d2d2d',
                      fg = 'white', width = 15, anchor = "w")
    accessLabelName2 = tk.Label(text = "", 
                      font=fontStyle5, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 25, anchor = "w")
    
    accessLabelGradeSec1 = tk.Label(text = "Grade & Sec:", 
                      font=fontStyle5, 
                      bg = '#2d2d2d',
                      fg = 'white')
    
    accessLabelGradeSec2 = tk.Label(text = "", 
                      font=fontStyle5, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 25, anchor = "w")
    
    accessLabelLRN1 = tk.Label(text = "LRN:", 
                      font=fontStyle5, 
                      bg = '#2d2d2d',
                      fg = 'white')
    
    accessLabelLRN2 = tk.Label(text = "", 
                      font=fontStyle5, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 25, anchor = "w")
    
    accessLabelSex1 = tk.Label(text = "Sex:", 
                      font=fontStyle5, 
                      bg = '#2d2d2d',
                      fg = 'white')
    
    accessLabelSex2 = tk.Label(text = "", 
                      font=fontStyle5, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 25, anchor = "w")
    accessLabelBday1 = tk.Label(text = "Date of Birth:", 
                      font=fontStyle5, 
                      bg = '#2d2d2d',
                      fg = 'white')
    accessLabelBday2 = tk.Label(text = "", 
                      font=fontStyle5, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 25, anchor = "w")
    
    accessLabelContact1 = tk.Label(text = "Contact No:", 
                      font=fontStyle5, 
                      bg = '#2d2d2d',
                      fg = 'white')
    
    accessLabelContact2 = tk.Label(text = "", 
                      font=fontStyle5, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 25, anchor = "w")
    
    #entry
    accessEntry1 = tk.Entry(
                      font=fontStyle3, 
                      bg = '#bebebe', fg = "#2d2d2d", 
                      width = 14)
    
    #button
    accessButtonScan = tk.Button(text = "Scan", 
                              height = 1, width = 10,
                              relief = "groove", 
                              bg = '#bebebe', fg = "#2d2d2d",
                              font = fontStyle4,
                              command = readRFID1)
    accessButtonRegister = tk.Button(text = "Register", 
                              width = 10,
                              relief = "groove", 
                              bg = '#bebebe', fg = "#2d2d2d",
                              font = fontStyle4, command = registerWindowFunc)
    accessButtonBack = tk.Button(text = "Back", 
                              width = 10,
                              relief = "groove", 
                              bg = '#bebebe', fg = "#2d2d2d",
                              font = fontStyle4, command = restartProgram)
    
    #canvas
    accessCanvas1 = tk.Canvas(accessDBwindow, width = 200, height = 200)
    
    
    
    # LAYOUT
    accessLabel1.grid(column = 0, columnspan = 4, pady = 10)
    
    #accessLabelx1.grid(row = 2, column = 0, pady = 10)
    accessLabelx4.grid(row = 3, column = 0, pady = 20) #orig 45
    accessEntry1.grid(row = 4, column = 0, pady = 5, padx = 80)
    
    accessEntry1.insert(0, "    RFID CODE")
    
    accessButtonScan.grid(row = 5, column = 0, padx = 80)
    accessLabelx2.grid(row = 6, column = 0, padx = 80, pady = 45)
    accessLabelx3.grid(row = 7, column = 0, padx = 80)
    accessLabelx5.grid(row = 8, column = 0, padx = 80)
    accessButtonBack.grid(row = 13, column = 0)
    accessLabel2.grid(row = 10, column = 0, padx = 80)
    accessButtonRegister.grid(row = 11, column = 0, padx = 80)
    
    accessCanvas1.grid(row = 3, column = 3, rowspan = 4)
    myimg = accessCanvas1.create_image(100,120, image = img)    #SET IMAGE 
    
    accessLabelName1.grid(row = 8, column = 2, sticky = "w")
    accessLabelGradeSec1.grid(row = 9, column = 2, sticky = "w", pady = 5)
    accessLabelLRN1.grid(row = 10, column = 2, sticky = "w")
    accessLabelSex1.grid(row = 11, column = 2, sticky = "w")
    accessLabelBday1.grid(row = 12, column = 2, sticky = "w")
    accessLabelContact1.grid(row = 13, column = 2, sticky = "w")
    
    accessLabelName2.grid(row = 8, column = 3, sticky = "w")
    accessLabelGradeSec2.grid(row = 9, column = 3, sticky = "w")
    accessLabelLRN2.grid(row = 10, column = 3, sticky = "w")
    accessLabelSex2.grid(row = 11, column = 3, sticky = "w")
    accessLabelBday2.grid(row = 12, column = 3, sticky = "w")
    accessLabelContact2.grid(row = 13, column = 3, sticky = "w")
    
    # end
    accessDBwindow.mainloop()
    
    











    # MAIN START
mainWindow = tk.Tk()
mainWindow.geometry("920x620+300+50")
mainWindow.configure(bg = '#2d2d2d')


    # widgets
fontStyle1 = tkFont.Font(family="Lucida Grande", size = 70, weight = "bold")
fontStyle2 = tkFont.Font(family="Lucida Grande", size = 15, slant = "italic")
fontStyle3 = tkFont.Font(family="Lucida Grande", size = 10)
fontStyle4 = tkFont.Font(family="Lucida Grande", size = 15, weight = "bold")

mainLabel1 = tk.Label(text = "ONE TAGSCI", 
                          font=fontStyle1, 
                          bg = '#2d2d2d',
                          fg = 'white')
mainLabel2 = tk.Label(text = "Student database system with RFID-based daily logger", 
                          font = fontStyle2, 
                          bg = '#2d2d2d',
                          fg = '#bebebe')
mainLabel3 = tk.Label(text = "Created by Arthur E. Betez Jr",
                          bg = '#2d2d2d',
                          fg = '#bebebe', 
                          font = fontStyle3)
mainButton_access = tk.Button(text = "ACCESS DATABASE", 
                                  height = 2, width = 20,
                                  relief = "groove", 
                                  bg = '#bebebe', fg = "#2d2d2d",
                                  font = fontStyle4,
                                  command = accessDBwindowFunc)
mainButton_logger = tk.Button(text = "DAILY LOGGER", 
                                  height = 2, width = 20,
                                  relief = "groove",
                                  bg = '#bebebe', fg = "#2d2d2d",
                                  font = fontStyle4)

mainLabel1.grid(row = 1, column = 1, columnspan = 2, pady = 100, padx = 130)
mainLabel2.grid(row = 2, column = 1, columnspan = 2, pady = 0, padx = 50)
mainLabel3.grid(row = 3, column = 1, columnspan = 2, pady = 0, padx = 50)
mainButton_access.grid(row = 4, column = 1, pady = 100, padx = 50 )
mainButton_logger.grid(row = 4, column = 2, pady = 100, padx = 50)


    # end
mainWindow.mainloop()

