# Import rqeuired modules
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import time
import serial
import paho.mqtt.client as mqtt #import the client1
import re
##ser = serial.Serial("COM3",baudrate=9600,timeout= .01 )

def updateTextTimer(update_location,issue,flag,lineValue):
    if(flag ==True ):
        if (update_location == 0):
            ##  update_location = 1  ### row for the 3 layers
            print(update_location)
            timer_one.Start()
            print(issue)
            label_fault_0.config(text=issue, bg="red")
            label_fault_type_0.config(text="fault in line:"+str(lineValue))
        elif (update_location == 1):
            print(update_location)
            timer_two.Start()
            ##update_location = 2
            label_fault_1.config(text=issue, bg="red")
            label_fault_type_1.config(text="fault in line:"+str(lineValue))
        elif (update_location == 2):
            print(update_location)
            ##update_location = 3
            timer_three.Start()
            label_fault_2.config(text=issue, bg="red")
            label_fault_type_2.config(text="fault in line:"+str(lineValue))
        elif (update_location == 3):
            print(update_location)
            ## update_location = 0
            timer_four.Start()
            label_fault_3.config(text=issue, bg="red")
            label_fault_type_3.config(text="fault in line:"+str(lineValue))
    if(flag ==False):
        if (update_location == 0):
            ##  update_location = 1  ### row for the 3 layers
            print(update_location)
            timer_one.Stop()
            label_fault_0.config(text=issue, bg="green")
            label_fault_type_0.config(text="fault fixed line:"+str(lineValue))
        elif (update_location == 1):
            print(update_location)
            ##update_location = 2
            timer_two.Stop()
            label_fault_1.config(text=issue, bg="green")
            label_fault_type_1.config(text="fault fixed line:"+str(lineValue))
        elif (update_location == 2):
            print(update_location)
            ##update_location = 3
            timer_three.Stop()
            label_fault_2.config(text=issue, bg="green")
            label_fault_type_2.config(text="fault fixed line:"+str(lineValue))
        elif (update_location == 3):
            print(update_location)
            ## update_location = 0
            timer_four.Stop()
            label_fault_3.config(text=issue, bg="green")
            label_fault_type_3.config(text="fault fixed line:"+str(lineValue))




def send_message( topic,message, parameter_list=None):
    client.publish(topic, message)


def on_message(client, userdata, message):
    global update_location
    global  my_list
    global issue
    global flag
    msg = str(message.payload.decode("utf-8"))
    print("message received ", msg)
    topic = message.topic
    print("on the topic ", topic)
    lineValue = int(re.search(r'\d+', topic).group())

    lineValues = lineValue - 1
    row, column = divmod(lineValues, 10)
    print(row, column)
    status =int(re.search(r'\d+', msg).group())
    print(status)
    if(status ==0):  ## line active
        label_dict["lbl_" + str(key_matrix[row][column])].config(bg="red")
        ##status =2
    elif(status ==1):   ## line fixed
        label_dict["lbl_" + str(key_matrix[row][column])].config(bg="green")
        ##status = 2


    if (msg.startswith("IDMoulidng")):
        issue= "MOULDING"
        send_message(topic="inTopic", message="okits working ")


        if (status == 0):
            flag = True
            my_list[update_location] = [lineValue, issue]
            updateTextTimer(update_location, issue, flag,lineValue)
            update_location = update_location + 1
            if (update_location == 4): update_location = 0

        elif (status == 1):
            flag = False
            for i in range(len(my_list)):
                temp1=  my_list[i][0]
                if (temp1 == lineValue):
                    temp2 =my_list[i][1]
                    if (temp2== issue):
                        update_location = i
                        break
            updateTextTimer(update_location, issue, flag,lineValue)
    if (msg.startswith("IDINPUT")):
        issue= "SuperMarket"

        if (status == 0):
            flag = True
            my_list[update_location] = [lineValue, issue]
            updateTextTimer(update_location, issue, flag,lineValue)
            update_location = update_location + 1
            if (update_location == 4): update_location = 0

        elif (status == 1):
            flag = False
            for i in range(len(my_list)):
                temp1=  my_list[i][0]
                if (temp1 == lineValue):
                    temp2 =my_list[i][1]
                    if (temp2== issue):
                        update_location = i
                        break
            updateTextTimer(update_location, issue, flag,lineValue)
    if (msg.startswith("IDmechanic")):
        issue= "Mechanic"

        if (status == 0):
            flag = True
            my_list[update_location] = [lineValue, issue]
            updateTextTimer(update_location, issue, flag,lineValue)
            update_location = update_location + 1
            if (update_location == 4): update_location = 0

        elif (status == 1):
            flag = False
            for i in range(len(my_list)):
                temp1=  my_list[i][0]
                if (temp1 == lineValue):
                    temp2 =my_list[i][1]
                    if (temp2== issue):
                        update_location = i
                        break
            updateTextTimer(update_location, issue, flag,lineValue)

    if (msg.startswith("IDwarehouse")):
        issue= "WareHouse"

        if (status == 0):
            flag = True
            my_list[update_location] = [lineValue, issue]
            updateTextTimer(update_location, issue, flag,lineValue)
            update_location = update_location + 1
            if (update_location == 4): update_location = 0

        elif (status == 1):
            flag = False
            for i in range(len(my_list)):
                temp1=  my_list[i][0]
                if (temp1 == lineValue):
                    temp2 =my_list[i][1]
                    if (temp2== issue):
                        update_location = i
                        break
            updateTextTimer(update_location, issue, flag,lineValue)

    if (msg.startswith("IDcutting")):
        issue= "Cutting"

        if (status == 0):
            flag = True
            my_list[update_location] = [lineValue, issue]
            updateTextTimer(update_location, issue, flag,lineValue)
            update_location = update_location + 1
            if (update_location == 4): update_location = 0

        elif (status == 1):
            flag = False
            for i in range(len(my_list)):
                temp1=  my_list[i][0]
                if (temp1 == lineValue):
                    temp2 =my_list[i][1]
                    if (temp2== issue):
                        update_location = i
                        break
            updateTextTimer(update_location, issue, flag,lineValue)
 ##   root.after(100,update)

class StopWatch(Frame):
    """ Implements a stop watch frame widget. """

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.update()

    def _update(self):
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)


    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02dm:%02ds:%02dms' % (minutes, seconds, hseconds))
        self.minute =hseconds
        return self.timestr

    def Start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1
    def Stop(self):
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

# Creating the main window
root = Tk()
theta = ""
update_location =0
my_list =[[100,"All is GOOD"],[100,"All is GOOD"],[100,"All is GOOD"],[100,"All is GOOD"]]
flag =True
issue ="All is GOOD"
timer_one = StopWatch(root)
timer_two = StopWatch(root)
timer_three = StopWatch(root)
timer_four = StopWatch(root)
timer_one.pack()


##
##timer_one.Start()
# Assigning it the desired geometry
width  = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}+0+0')
root.config(bg="black")
# Assigning the name of our window
root.title("SHI Line Monitoring System ")
myFont = font.Font(size=12)
top_Frame = Frame(root, bg = "white" ,height = 75,width = width,relief = 'solid')
image1 = Image.open("sumbri_logo.png")
image2 = Image.open("hela _ogo.jpg")
sumbrilogo = ImageTk.PhotoImage(image1)
helalogo = ImageTk.PhotoImage(image2)
logo_label_sum = Label(top_Frame,image=sumbrilogo,height = 75,width = 100,bd = 15)

logo_label_sum.pack(side = "left")
title_lable = Label(top_Frame,bg = "white",
                    text = "SUMBIRI HELA INTIMATE APPAREL PLC \n  Line Monitoring System ",
                    font = ("timesnewroman",30, "bold"),height = 2,width = 50)
title_lable.pack(side = "left")
logo_label_hela = Label(top_Frame,image=helalogo,height = 75,width = 100,bd = 15)
logo_label_hela.pack(side = "left")
top_Frame.pack( fill = "x",)

line_Frame = Frame(root,bg = "darkblue")
line_Frame.pack(pady = 5,padx = 5)
fault_line_Frame = Frame(root,bg = "black",height = 40,bd=15,relief = "raised",)
label_fault_type_0 = Label(fault_line_Frame,text = " fault in line",
                           bg = "powderblue",height = 1,width = 22, font = ("timesnewroman",22, "bold"))
label_fault_type_0.pack(side = "left",padx = 5, pady = 0)
label_fault_type_1 = Label(fault_line_Frame,text = "fault in line",
                           bg = "powderblue",height = 1,width = 22, font = font.Font(size=22))
label_fault_type_1.pack(side = "left", after = label_fault_type_0,padx = 5, pady = 0)
label_fault_type_2 = Label(fault_line_Frame,text = "fault in line",
                           bg = "powderblue",height = 1,width = 22, font = font.Font(size=22))
label_fault_type_2.pack(side = "left",after = label_fault_type_1,padx = 5, pady = 0)
label_fault_type_3 = Label(fault_line_Frame,text = "fault in line",
                           bg = "powderblue",height = 1,width = 22, font = font.Font(size=22))
label_fault_type_3.pack(side = "left",after = label_fault_type_2,padx = 5, pady = 0)

fault_line_Frame.pack( after =line_Frame ,fill = X)

fault_type_Frame = Frame(root,bg = "black",height = 40,bd=15,relief = "raised",)
label_fault_0 = Label(fault_type_Frame,text = " All  is Good",  bg = "green",
                      height = 1,width = 22, font = ("timesnewroman",22, "bold"))
label_fault_0.pack(side = "left",padx = 5, pady = 0)
label_fault_1 = Label(fault_type_Frame,text = "All  is Good",  bg = "green",height = 1,width = 22,
                      font = font.Font(size=22))
label_fault_1.pack(side = "left", after = label_fault_0,padx = 5, pady = 0)
label_fault_2 = Label(fault_type_Frame,text = "All  is Good",  bg = "green",height = 1,width = 22,
                      font = font.Font(size=22))
label_fault_2.pack(side = "left",after = label_fault_1,padx = 5, pady = 0)
label_fault_3 = Label(fault_type_Frame,text = "All  is Good", bg = "green",height = 1,width = 22,
                      font = font.Font(size=22))
label_fault_3.pack(side = "left",after = label_fault_2,padx = 5, pady = 0)
fault_type_Frame.pack( after =fault_line_Frame ,fill = X)


down_time_Frame = Frame(root,bg = "black",height = 40,bd=15,relief = "raised",)
timer_fault_0 = Label(down_time_Frame,textvariable = timer_one.timestr,  bg = "blue",height = 1,width = 22,
                      font = ("timesnewroman",22, "bold"))
timer_fault_0.pack(side = "left",padx = 5, pady = 0)
timer_fault_1 = Label(down_time_Frame, textvariable = timer_two.timestr,  bg = "blue",height = 1,width = 22,
                      font = font.Font(size=22))
timer_fault_1.pack(side = "left", after = timer_fault_0,padx = 5, pady = 0)
timer_fault_2 = Label(down_time_Frame,textvariable = timer_three.timestr,  bg = "blue",height = 1,width = 22,
                      font = font.Font(size=22))
timer_fault_2.pack(side = "left",after = timer_fault_1,padx = 5, pady = 0)
timer_fault_3 = Label(down_time_Frame,textvariable = timer_four.timestr, bg = "blue",height = 1,width = 22,
                      font = font.Font(size=22))
timer_fault_3.pack(side = "left",after = timer_fault_2,padx = 5, pady = 0)

down_time_Frame.pack( after =fault_type_Frame ,fill = X)

# Key matrix contains all the required the keys
key_matrix = [["1", "2", "3", "4", "5","6","7","8","9",'10'],
              ["11", "12", "13", "14", "15","16","17","18","19",'20'],
              ["21", "22", "23", "24", "25", "26", "27", "28", "29", '30'],
              ["31", "32", "33", "34", "35", "36", "37", "38", "39", '40'],
              ["41", "42", "43", "44", "45", "46", "47", "48", "49", '50'],
              ["51", "52", "53", "54", "55", "56", "57", "58", "59", '60'],
              ["61", "62", "63", "64", "65", "66", "67", "68", "69", '70'],
              ]

# Creating a dictionary for the buttons
label_dict = {}

# Variable to store our results
ans_to_print = 0

##title = Frame(root,bg = "blue",height = 30,width = width)
##//title.grid(colmun);

# Number of rows containing buttons
for i in range(len(key_matrix)):
    # Number of columns
    for j in range(len(key_matrix[i])):
        # Creating and Adding the buttons to dictionary
        label_dict["lbl_" + str(key_matrix[i][j])] = Label(
            line_Frame, bd=15,relief = "raised", text="LINE "+str(key_matrix[i][j]), font=myFont)

        # Positioning buttons
        label_dict["lbl_" + str(key_matrix[i][j])].grid(
            row=i + 1, column=j, padx=5, pady=5, ipadx=5, ipady=5)

##label_dict["lbl_" + str(key_matrix[1][6])].config(bg="red")
##label_dict["lbl_" + str(key_matrix[2][9])].config(bg="green")
broker_address="192.168.43.190"

print("creating new instance")
client = mqtt.Client() #create new instance
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address, port = 1883) #connect to broker

print("Subscribing to topic","home")
client.subscribe("Line1")

send_message(topic="inTopic",message="okits working ")
 #Start the MQTT Mosquito process loop
client.loop_start()
# Running the main loop
##root.after(100,update)
root.mainloop()
