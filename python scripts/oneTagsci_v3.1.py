import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk,Image
from tkinter import messagebox
import serial
import time
import sqlite3
import sys
import os
from datetime import datetime


# create database
conn = sqlite3.connect('studentDatabase4.db')
curs = conn.cursor()
curs.execute("create table if not exists students(RFIDcode, Name, GradeNSec, LRN, Sex, Birthday, Contact, imgFile, timeInt, login,  logout)")
conn.commit()


def dailyLoggerFunc():
    mainWindow.destroy()
    
    loggerWindow = tk.Tk()
    loggerWindow.geometry("950x620+300+50")
    loggerWindow.configure(bg = '#2d2d2d')
    
    def restartProgram():
        #exit()
        os.execl(sys.executable, sys.executable, *sys.argv)
    
    def login():
        #Scan first!
        if __name__ == '__main__':
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            ser.flush()

            line = ""
           
            while line == "":    # While no received key from arduino, keep on trying to read
                ser.write(b"scanNOW\n")
                line = ser.readline().decode('utf-8').rstrip()
                #time.sleep(1)
                print("Key: ", line)
            
            #return str(line)
            line = str(line)
            
            loggerEntry1.delete(first = 0, last = 100)
            loggerEntry1.configure(show = "*")
            loggerEntry1.insert(0, line)
        
        keyFromEntry = str(loggerEntry1.get())
        
        # Update pic and nameSec
        querySelect = "SELECT * FROM students"
        curs.execute(querySelect)
        dataFromDataBase = curs.fetchall()
        
        goodRFID = 1 #not recognized
        
        for row in dataFromDataBase:
            if row[0] == keyFromEntry:
                goodRFID = 0 #good
                imageFile = row[7]
                nameDisplay = row[1]
                sectionDisplay = row[2]
                
                global imageDisplay5 #PAAAKSHEEEET
                imageDisplay5 = ImageTk.PhotoImage((Image.open(imageFile)).resize((250,250), Image.ANTIALIAS))
                loggerCanvas.itemconfigure(myimg3, image = imageDisplay5) #update image

                loggerLabelName.configure(text = nameDisplay)
                loggerLabelSection.configure(text = sectionDisplay)
                
                if row[9] == "" or row[9] == None or row[9] == " ":
                    goodRFID = 0
                else:
                    goodRFID = 2
        
        
            
        
        #error code
        if goodRFID == 1:
            messagebox.showwarning("Login Info", "RFID NOT REGISTERED!")
        elif goodRFID == 2:
            messagebox.showwarning("Login Info", "ALREADY LOGGED IN FOR THE DAY!")
        else:
            # Update Database!

            loggerEntry1.configure(show = "*")
                
            currentTime = datetime.now().strftime("%H:%M")
            #keyFromEntry = str(loggerEntry1.get())
            currentTimeInt = int(datetime.now().strftime("%H%M%S"))
            #print(keyFromEntry)

            queryUpdate = """Update students set login = ? where RFIDcode = ?"""    #updates time in str format
            curs.execute(queryUpdate,(currentTime,keyFromEntry))
            queryUpdate = """Update students set timeInt = ? where RFIDcode = ?"""  #updates time in int format
            curs.execute(queryUpdate,(currentTimeInt,keyFromEntry))
            conn.commit()
            messagebox.showinfo("Login Info", "Logged Successfully! Now, go to ur room!")
        
        
        # update gui!
        querySelect = "SELECT * FROM students ORDER BY timeInt DESC"
        curs.execute(querySelect)
        dataFromDataBase = curs.fetchall()
        
        i = 1
        for row in dataFromDataBase:
            if i == 1:
                time = row[9]
                name = row[1]
                
                if time != "":
                    loggerLabelTime1.configure(text = time)
                    loggerLabelLog1.configure(text = name)
                i = 2
            elif i == 2:
                time = row[9]
                name = row[1]
                if time != "":
                    loggerLabelTime2.configure(text = time)
                    loggerLabelLog2.configure(text = name)
                i = 3
            elif i == 3:
                time = row[9]
                name = row[1]
                if time != "":
                    loggerLabelTime3.configure(text = time)
                    loggerLabelLog3.configure(text = name)
                i = 4
            elif i == 4:
                time = row[9]
                name = row[1]
                if time != "":
                    loggerLabelTime4.configure(text = time)
                    loggerLabelLog4.configure(text = name)
                i = 5
            elif i == 5:
                time = row[9]
                name = row[1]
                if time != "":
                    loggerLabelTime5.configure(text = time)
                    loggerLabelLog5.configure(text = name)
                i = 6
            else:
                print("lol")
  
        
        #reset
        global imageDisplay6 #PAAAKSHEEEET
        imageDisplay6 = ImageTk.PhotoImage((Image.open("images/imgDefault.jpg")).resize((250,250), Image.ANTIALIAS))
        loggerCanvas.itemconfigure(myimg3, image = imageDisplay6) #update image

        loggerLabelName.configure(text = "")
        loggerLabelSection.configure(text = "")
        loggerEntry1.configure(show = "")
        loggerEntry1.delete(0, 100)
        loggerEntry1.insert(0, "    RFID CODE")
        
        
        
        #end of login
        

    def logout():
        #Scan first!
        if __name__ == '__main__':
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            ser.flush()

            line = ""
           
            while line == "":    # While no received key from arduino, keep on trying to read
                ser.write(b"scanNOW\n")
                line = ser.readline().decode('utf-8').rstrip()
                #time.sleep(1)
                print("Key: ", line)
            
            #return str(line)
            line = str(line)
            
            loggerEntry1.delete(first = 0, last = 100)
            loggerEntry1.configure(show = "*")
            loggerEntry1.insert(0, line)
        
        
        keyFromEntry = str(loggerEntry1.get())
        goodRFID = 1
        
        # Update pic and nameSec
        querySelect = "SELECT * FROM students"
        curs.execute(querySelect)
        dataFromDataBase = curs.fetchall()
        
        for row in dataFromDataBase:
            if row[0] == keyFromEntry:
                goodRFID = 0
                imageFile = row[7]
                nameDisplay = row[1]
                sectionDisplay = row[2]
                
                global imageDisplay7 #PAAAKSHEEEET
                imageDisplay7 = ImageTk.PhotoImage((Image.open(imageFile)).resize((250,250), Image.ANTIALIAS))
                loggerCanvas.itemconfigure(myimg3, image = imageDisplay7) #update image

                loggerLabelName.configure(text = nameDisplay)
                loggerLabelSection.configure(text = sectionDisplay)
                
                if row[10] == "" or row[10] == None or row[10] == " ":
                    goodRFID = 0
                else:
                    goodRFID = 2
            
        
        
        
        if goodRFID == 1:
            messagebox.showwarning("Login Info", "RFID NOT REGISTERED!")
        elif goodRFID == 2:
            messagebox.showwarning("Login Info", "ALREADY LOGGED OUT FOR THE DAY!")
        else:
            # Update database!
            loggerEntry1.configure(show = "*")
            #currentDate = datetime.now().strftime("%m/%d/%y")
            currentTime = datetime.now().strftime("%H:%M")

            queryUpdate = """Update students set logout = ? where RFIDcode = ?"""
            curs.execute(queryUpdate,(currentTime,keyFromEntry))
            conn.commit()
            messagebox.showinfo("Logout Info", "Logged Out Successfully! Adios!")       
        
        #reset
        global imageDisplay8 #PAAAKSHEEEET
        imageDisplay8 = ImageTk.PhotoImage((Image.open("images/imgDefault.jpg")).resize((250,250), Image.ANTIALIAS))
        loggerCanvas.itemconfigure(myimg3, image = imageDisplay8) #update image

        loggerLabelName.configure(text = "")
        loggerLabelSection.configure(text = "")
        loggerEntry1.configure(show = "")
        loggerEntry1.delete(0, 100)
        loggerEntry1.insert(0, "    RFID CODE")
    
    
        #end of logout
    
    
    def printLog():
        username = loggerEntryUsername.get()
        password = loggerEntryPassword.get()
        
        if username == "admin" and password == "1234":
            currentDate = datetime.now().strftime("%m-%d-%Y")
            currentTime = datetime.now().strftime("%H:%M")
            
            #For STEM - 21
            querySelect = ("SELECT * FROM students where GradeNSec = 'STEM - 21' ORDER BY timeInt ASC")     # Sample select query, may vary depending on purpose
            curs.execute(querySelect)
            dataFromDatabase = curs.fetchall()  
            conn.commit() #test
            
            filename = currentDate + " - STEM 21" + ".txt"
            filename = str(filename)
            fh = open(filename, 'w')
            fh.write("\n\n========================================================================")
            fh.write("\n\n   DAILY REPORT")
            fh.write("\n\n   Date:      ")
            fh.write(currentDate)
            fh.write('\n   Section:   STEM 21')
            fh.write("\n\n========================================================================")
            fh.write('\n\n')
            fh.write("    ")
            fh.write("  NAME                       LOGIN               LOGOUT")
            fh.write("\n\n")
            
            for row in dataFromDatabase:
                if row[9] == None or row[9] == "":
                    loginData = "none"
                else:
                    loginData = row[9]
                if row[10] == None or row[10] == "":
                    logoutData = "none"
                else:
                    logoutData = row[10]
                fh.write("    ")
                fh.write(row[1])
                
                numOfCharac = len(row[1])
                numToSpace = 29 - numOfCharac
                i = 1
                toSpace = ""
                while i <= numToSpace:
                    toSpace = str(toSpace + " ")
                    i += 1
                
                fh.write(toSpace)
                fh.write(loginData)
                
                numOfCharac2 = len(loginData)
                numToSpace2 = 20 - numOfCharac2
                i = 1
                toSpace2 = ""
                while i <= numToSpace2:
                    toSpace2 = str(toSpace2 + " ")
                    i += 1
                    
                fh.write(toSpace2)
                fh.write(logoutData)
                fh.write("\n\n")
            
            fh.write("\n========================================================================")
            fh.close()
            
            #For ABM - 21
            querySelect = ("SELECT * FROM students where GradeNSec = 'ABM - 21' ORDER BY timeInt ASC") 
            curs.execute(querySelect)
            dataFromDatabase = curs.fetchall()  
            conn.commit() #test
            
            filename = currentDate + " - ABM 21" + ".txt"
            filename = str(filename)
            fh = open(filename, 'w')
            fh.write("\n\n========================================================================")
            fh.write("\n\n   DAILY REPORT")
            fh.write("\n\n   Date:      ")
            fh.write(currentDate)
            fh.write('\n   Section:   ABM 21')
            fh.write("\n\n========================================================================")
            fh.write('\n\n')
            fh.write("    ")
            fh.write("  NAME                       LOGIN               LOGOUT")
            fh.write("\n\n")
            
            for row in dataFromDatabase:
                if row[9] == None or row[9] == "":
                    loginData = "none"
                else:
                    loginData = row[9]
                if row[10] == None or row[10] == "":
                    logoutData = "none"
                else:
                    logoutData = row[10]
                fh.write("    ")
                fh.write(row[1])
                
                numOfCharac = len(row[1])
                numToSpace = 29 - numOfCharac
                i = 1
                toSpace = ""
                while i <= numToSpace:
                    toSpace = str(toSpace + " ")
                    i += 1
                
                fh.write(toSpace)
                fh.write(loginData)
                
                numOfCharac2 = len(loginData)
                numToSpace2 = 20 - numOfCharac2
                i = 1
                toSpace2 = ""
                while i <= numToSpace2:
                    toSpace2 = str(toSpace2 + " ")
                    i += 1
                    
                fh.write(toSpace2)
                fh.write(logoutData)
                fh.write("\n\n")
            
            fh.write("\n========================================================================")
            fh.close()
        
            #NOTE: REPEAT ABOVE FOR EVERY SECTION!
        
            # Flush login and logout records after print
            queryUpdate1 = """Update students set login = "" """
            curs.execute(queryUpdate1)
            queryUpdate2 = """Update students set logout = "" """
            curs.execute(queryUpdate2)
            queryUpdate3 = """Update students set timeInt = "" """
            curs.execute(queryUpdate3)
            conn.commit()
            
            messagebox.showinfo("Print Info", "Records Printed Successfully!")
            
            loggerLabelTime1.configure(text = "")
            loggerLabelLog1.configure(text = "")
            loggerLabelTime2.configure(text = "")
            loggerLabelLog2.configure(text = "")
            loggerLabelTime3.configure(text = "")
            loggerLabelLog3.configure(text = "")
            loggerLabelTime4.configure(text = "")
            loggerLabelLog4.configure(text = "")
            loggerLabelTime5.configure(text = "")
            loggerLabelLog5.configure(text = "")
            
        else:
            messagebox.showwarning("Print Log Error", "Username or Password is Wrong!")

            
        

    
    
    # fonts
    fontStyle1 = tkFont.Font(family="Lucida Grande", size = 30, weight = "bold")
    fontStyle2 = tkFont.Font(family="Lucida Grande", size = 15, slant = "italic")
    fontStyle3 = tkFont.Font(family="Lucida Grande", size = 13)
    fontStyle4 = tkFont.Font(family="Lucida Grande", size = 15, weight = "bold")
    fontStyle5 = tkFont.Font(family="Lucida Grande", size = 15)
    
    # widget start
    
    #labelx
    loggerLabelx1 = tk.Label(text = " ", 
                      font=fontStyle5, 
                      bg = '#2d2d2d',
                      fg = 'white', 
                      width = 20)
    loggerLabelx2 = tk.Label(text = " ", 
                      font=fontStyle5, 
                      bg = '#2d2d2d',
                      fg = 'white', 
                      width = 20)
    loggerLabelx3 = tk.Label(text = " ", 
                      font=fontStyle5, 
                      bg = '#2d2d2d',
                      fg = 'white', 
                      width = 20)
    
    # Label
    loggerLabel1 = tk.Label( 
                      text = "      DAILY LOGGER", 
                      font=fontStyle1, 
                      bg = '#2d2d2d',
                      fg = 'white')
    
    loggerLabelName = tk.Label(text = "name here ", 
                      font=fontStyle5, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 20)
    loggerLabelSection = tk.Label(text = "sec here ", 
                      font=fontStyle5, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 20)
    loggerLabel2 = tk.Label(text = "RECENT LOGINS", 
                      font=fontStyle5, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 38)
    loggerLabelTime1 = tk.Label(text = "",   #log start
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 15)
    loggerLabelTime2 = tk.Label(text = "",   
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 15)
    loggerLabelTime3 = tk.Label(text = "",   
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 15)
    loggerLabelTime4 = tk.Label(text = "",   
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 15)
    loggerLabelTime5 = tk.Label(text = "",   
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 15)
    
    loggerLabelLog1 = tk.Label(text = "",   #log2 start
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 21)
    loggerLabelLog2 = tk.Label(text = "",   
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 21)
    loggerLabelLog3 = tk.Label(text = "",   
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 21)
    loggerLabelLog4 = tk.Label(text = "",   
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 21)
    loggerLabelLog5 = tk.Label(text = "",   
                      font=fontStyle3, 
                      bg = 'white',
                      fg = '#2d2d2d', 
                      width = 21)
    
    loggerLabelUsername = tk.Label(text = "Username: ",   
                      font=fontStyle3, 
                      bg = '#2d2d2d',
                      fg = 'white', 
                      width = 15, anchor = "e")
    loggerLabelPassword = tk.Label(text = "Password: ",   
                      font=fontStyle3, 
                      bg = '#2d2d2d',
                      fg = 'white', 
                      width = 15, anchor = "e")
    
    
    
    # Entry
    loggerEntry1 = tk.Entry(
                      font=fontStyle3, 
                      bg = '#bebebe', fg = "#2d2d2d", 
                      width = 14)
    loggerEntryUsername = tk.Entry(
                      font=fontStyle3, 
                      bg = 'white', fg = "#2d2d2d", 
                      width = 21)
    loggerEntryPassword = tk.Entry(
                      font=fontStyle3, 
                      bg = 'white', fg = "#2d2d2d", 
                      width = 21, show = "*")
    
    # Button
    loggerButtonScan = tk.Button(text = "scan-login", 
                              height = 1, width = 10,
                              relief = "groove", 
                              bg = '#bebebe', fg = "#2d2d2d",
                              font = fontStyle4, command = login)
    loggerButtonScan2 = tk.Button(text = "scan-logout", 
                              height = 1, width = 10,
                              relief = "groove", 
                              bg = '#bebebe', fg = "#2d2d2d",
                              font = fontStyle4, command = logout)
    loggerButtonBack = tk.Button(text = "back", 
                              height = 1, width = 10,
                              relief = "groove", 
                              bg = '#bebebe', fg = "#2d2d2d",
                              font = fontStyle4, command = restartProgram)
    loggerButtonPrint = tk.Button(text = "print log", 
                              height = 1, width = 10,
                              relief = "groove", 
                              bg = '#bebebe', fg = "#2d2d2d",
                              font = fontStyle4, command = printLog)
    
    # Canvas
    loggerCanvas = tk.Canvas(width = 200, height = 200)
    img3 = ImageTk.PhotoImage((Image.open("images/imgDefault.jpg")).resize((250,250) , Image.ANTIALIAS)) # open image
    
    
    
    #LAYOUT
    #column 0
    loggerLabel1.grid(row = 0, column = 0, columnspan = 3, pady = 20)
    
    loggerCanvas.grid(row = 1, rowspan = 7, column = 0)
    myimg3 = loggerCanvas.create_image(100,120, image = img3) #set image
    
    loggerLabelName.grid(row = 9, column = 0, pady = 5, padx = 70)
    loggerLabelSection.grid(row = 10, column = 0)
    
    
    loggerEntry1.grid(row = 11, column = 0, pady = 5)
    loggerEntry1.insert(0, "    RFID CODE")
    
    loggerButtonScan.grid(row = 12, column = 0)
    loggerButtonScan2.grid(row = 13, column = 0)
    
    #loggerLabelx2.grid(row = 13, column = 0, pady = 6)
    #loggerLabelx3.grid(row = 14, column = 0)
    loggerButtonBack.grid(row = 14, column = 0)
    
    #column 1
    loggerLabelx1.grid(row = 1, column = 1, pady = 30)
    loggerLabel2.grid(row = 3, column = 1, pady = 5, columnspan = 2)
    
    
    loggerLabelTime1.grid(row = 4, column = 1, sticky = "w")
    loggerLabelTime2.grid(row = 5, column = 1, sticky = "w")
    loggerLabelTime3.grid(row = 6, column = 1, sticky = "w")
    loggerLabelTime4.grid(row = 7, column = 1, sticky = "w")
    loggerLabelTime5.grid(row = 8, column = 1, sticky = "w")
    
    loggerLabelUsername.grid(row = 12, column = 1, sticky = "e")
    loggerLabelPassword.grid(row = 13, column = 1, sticky = "e")
    
    #column 2
    loggerLabelLog1.grid(row = 4, column = 2, sticky = "w")
    loggerLabelLog2.grid(row = 5, column = 2, sticky = "w")
    loggerLabelLog3.grid(row = 6, column = 2, sticky = "w")
    loggerLabelLog4.grid(row = 7, column = 2, sticky = "w")
    loggerLabelLog5.grid(row = 8, column = 2, sticky = "w")
    
    loggerEntryUsername.grid(row = 12, column = 2, sticky = "w")
    loggerEntryPassword.grid(row = 13, column = 2, sticky = "w")
    loggerButtonPrint.grid(row = 14, column = 2)
    
    #end of gui
    loggerWindow.mainloop()
    #END OF LOGGER FUNC






def accessDBwindowFunc():
    mainWindow.destroy()
    
    def writeDetails():
        query1 = ("SELECT * FROM students")     # Sample select query, may vary depending on purpose
        curs.execute(query1)
        
        dataFromDatabase = curs.fetchall()
        
        keyFromEntry = str(accessEntry1.get())
        #print(keyFromEntry)
        goodRFID = False
        for row in dataFromDatabase:
            if row[0] == keyFromEntry:
                goodRFID = True
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
                
        if goodRFID == False:
            messagebox.showwarning("Access Error", "RFID NOT RECOGNIZED")
                
        
    
    
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
                #time.sleep(1)
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
                    #time.sleep(1)
                    print("Key: ", line)
                
                #return str(line)
                line = str(line)
                
                query1 = ("SELECT * FROM students")     # Sample select query, may vary depending on purpose
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
            try:
                imageFile2 = str(registerEntryImagePath.get())
                #print(imageFile2) #test
                global imageDisplay2 #PAAAKSHEEEET
                imageDisplay2 = ImageTk.PhotoImage((Image.open(imageFile2)).resize((250,250), Image.ANTIALIAS))
                #imageDisplay2 = imageDisplay2.resize((200,200), Image.ANTIALIAS)
                registerCanvas.itemconfigure(myimg2, image = imageDisplay2)
            except:
                messagebox.showwarning("Check Image Error", "Image Not Found! Recheck File Name!")
                #print("image not found!")

            
        
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
                query2 = "INSERT INTO students (RFIDcode, Name, GradeNSec, LRN, Sex, Birthday, Contact, imgFile) VALUES (?,?,?,?,?,?,?,?)"
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
                                  font = fontStyle4, command = dailyLoggerFunc)

mainLabel1.grid(row = 1, column = 1, columnspan = 2, pady = 100, padx = 130)
mainLabel2.grid(row = 2, column = 1, columnspan = 2, pady = 0, padx = 50)
mainLabel3.grid(row = 3, column = 1, columnspan = 2, pady = 0, padx = 50)
mainButton_access.grid(row = 4, column = 1, pady = 100, padx = 50 )
mainButton_logger.grid(row = 4, column = 2, pady = 100, padx = 50)


    # end
mainWindow.mainloop()