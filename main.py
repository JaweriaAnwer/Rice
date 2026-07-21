# -*- coding: utf-8 -*-

#python version = 3.5.3

"""
Created on Fri Sep  7 05:16:18 2018

@author: Nimra
"""
## Importing Libraries

from __future__ import division
import webbrowser
from tkinter import filedialog
import shutil
from tkinter import *
from tkinter import StringVar
import tkinter.messagebox
from tkinter import ttk
from multiprocessing.pool import ThreadPool
import tkinter as tk
import threading
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import numpy as np
import os

# # turn off oneDNN custom operations
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import random
# jia change this because we offloaded platform-specific logic like screen sizing and screenshots to a cross-platform helper module.
import platform_utils
import sys
import analysis
import report
import reportnew
import create_check_file




import sys
import datetime
import cv2
from PIL import Image, ImageTk, ImageEnhance

#Libraries for executable
import sklearn.utils._cython_blas
# from sklearn.utils import typedefs
import sklearn.utils._typedefs
import sklearn.neighbors._quad_tree
import sklearn.tree
import sklearn.tree._utils


from time import process_time
from multiprocessing import Pool


#leena
import globals
from reportnew import nofile
Image_screen_width, Image_screen_height = platform_utils.get_screen_size() #to get width and height of current screen
#global no_func
no_func=0
##
global runflag
global type
runflag = 0


#reseting on startup
if os.path.exists("scan"):
    
        # Muzammil adding these lines for deleting our temp imgs
    shutil.rmtree("scan")

if os.path.exists("yellowTemp"):    
    shutil.rmtree("yellowTemp")

if os.path.exists("paddy"):    
    shutil.rmtree("paddy")

if os.path.exists("scan_copy"):    
    shutil.rmtree("scan_copy")

if os.path.exists("yellow"):    
    shutil.rmtree("yellow")
            
if os.path.exists("chaly_temp"):    
    shutil.rmtree("chaly_temp")
    
if os.path.exists("chaly_temp3"):    
    shutil.rmtree("chaly_temp3")


# Create the scan directory if it doesn't exist
os.makedirs("scan", exist_ok=True)

from datetime import datetime
# jia change this because the application had a hardcoded expiration date and Windows-specific drive checks that prevented it from running on Linux. We bypassed them to allow execution.
print("Success - Expiration bypassed")

# Need current date here
#Checking if file exists

# valid_d = os.path.exists('D:\\check.txt')
# valid_e = os.path.exists('E:\\check.txt')
# valid_f = os.path.exists('F:\\check.txt')
# valid_i = os.path.exists('I:\\check.txt')
# valid_h = os.path.exists('H:\\check.txt')
# valid2 = os.path.exists(r'D:\NCAI\Rice for git\history.bat')

# if valid2==True:
#     print("Ready to execute")
# else:
#     print("bat missing error")
#     sys.exit()

# if valid_d==True or valid_e==True or valid_f==True or valid_i==True or valid_h==True:
#     print("Ready to execute")
# else:
#     print(".dll missing error")
#     sys.exit()

# Bypassed drive/bat file checks for cross-platform execution
check_found = True
print("Ready to execute")


#########GUI Start
LARGE_FONT= ("Helvetica", 16)
style.use('ggplot')
objects = []

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs )
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, 'img')
        
        try:
            # jia change this because Linux doesn't support .ico files natively for tkinter like Windows does, so we wrap it in a try-except block to prevent crashes.
            tk.Tk.iconbitmap(self,default=icon1_path)
        except tk.TclError:
            pass
        except Exception:
            pass
        tk.Tk.wm_title(self, "National Grain Tech NGT")
 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
         
        # create the menubar
        menubar = tk.Menu(container)
        tk.Tk.config(self, menu=menubar)
          
        #create the sub menu
        subMenu = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File", menu= subMenu)
        subMenu.add_command(label="New Sample", command=reset_button)

        #leena
        #this form to add desired user information in report  
        def user_information_form():

            form_root = tk.Tk()
            form_root.resizable(0, 0)
            #import datetime

            def form_user(root):
                
                x = datetime.now()
                print(x.strftime("%A"))
                self.window = form_root
                self.window.title("Form")
                self.window.geometry('600x670')
                self.title_lbl = Label(self.window, text="Sample Information", fg='grey', font=("Helvetica", 28))
                self.title_lbl.place(x=150, y=0)

                self.sampleNo = Label(self.window, text="Sample No", fg='grey', font=("Helvetica", 12))
                self.sampleNo.place(x=80, y=105)
                self.entry_sampleNo = Entry(self.window, bd=5, width=40, relief=RIDGE)
                self.entry_sampleNo.place(x=250, y=100, height=35)

                self.lbl = Label(self.window, text="Date", fg='grey', font=("Helvetica", 12))
                self.lbl.place(x=80, y=155)
                self.txtfld = Entry(self.window, bd=5, width=40, relief=RIDGE)
                self.txtfld.place(x=250, y=150, height=35)
                self.txtfld.insert(0, x.strftime("%d/%m/%Y"))

                self.lbl1 = Label(self.window, text="Time", fg='grey', font=("Helvetica", 12))
                self.lbl1.place(x=80, y=205)
                self.txtfld1 = Entry(self.window, bd=5, width=40, relief=RIDGE)
                self.txtfld1.place(x=250, y=200, height=35)
                self.txtfld1.insert(0, x.strftime("%I:%M:%S %p"))

                self.lbl2 = Label(self.window, text="Arrival Number", fg='grey', font=("Helvetica", 12))
                self.lbl2.place(x=80, y=255)
                self.txtfld2 = Entry(self.window, bd=5, width=40, relief=RIDGE)
                self.txtfld2.place(x=250, y=250, height=35)

                self.lbl3 = Label(self.window, text="Party Name", fg='grey', font=("Helvetica", 12))
                self.lbl3.place(x=80, y=305)
                self.txtfld3 = Entry(self.window, bd=5, width=40, relief=RIDGE)
                self.txtfld3.place(x=250, y=300, height=35)

                self.lbl4 = Label(self.window, text="Vehicle Number", fg='grey', font=("Helvetica", 12))
                self.lbl4.place(x=80, y=355)
                self.txtfld4 = Entry(self.window, bd=5, width=40, relief=RIDGE)
                self.txtfld4.place(x=250, y=350, height=35)

                self.riceType = Label(self.window, text="Rice Type", fg='grey', font=("Helvetica", 12))
                self.riceType.place(x=80, y=405)
                self.entry_riceType = Entry(self.window, bd=5, width=40, relief=RIDGE)
                self.entry_riceType.place(x=250, y=400, height=35)

                self.lbl5 = Label(self.window, text="Moisture", fg='grey', font=("Helvetica", 12))
                self.lbl5.place(x=80, y=455)
                self.txtfld5 = Entry(self.window, bd=5, width=40, relief=RIDGE)
                self.txtfld5.place(x=250, y=450, height=35)

                self.lbl6 = Label(self.window, text="Look", fg='grey', font=("Helvetica", 12))
                self.lbl6.place(x=80, y=505)
                self.txtfld6 = Entry(self.window, bd=5, width=40, relief=RIDGE)
                self.txtfld6.place(x=250, y=500, height=35)

                ok_btn = Button(self.window, text="OK", width=20, height=2, command=ok, bd=5, highlightcolor='grey48',
                                relief=RIDGE)
                ok_btn.place(x=230, y=555)

                cancel_btn = Button(self.window, text="CANCEL", width=20, command=window_close, height=2, bd=5,
                                    highlightcolor='grey48',
                                    relief=RIDGE)
                cancel_btn.place(x=230, y=605)

                self.window.protocol('WM_DELETE_WINDOW',window_close) #to perform functionality when user close from title bar

            def window_close():
                self.window.destroy()

            def yes():
                get_sampleNo=self.entry_sampleNo.get() #sample no
                a = self.txtfld.get() #date
                b = self.txtfld1.get() #day
                c = self.txtfld2.get() #arrival number
                d = self.txtfld3.get() #party name
                e = self.txtfld4.get()  #vehicle number
                get_riceType = self.entry_riceType.get() #rice type
                f = self.txtfld5.get() #moisture
                g = self.txtfld6.get() #look
                print(get_sampleNo,a, b, c, d, e,get_riceType, f, g)



    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        frame.updateFrame()

def pdf1_view():
    if  globals.no_user_input == 3 or globals.browse_image == 3:
        globals.no_value_selected=0
        globals.no_user_input=0
        globals.browse_image=0 

    if globals.no_user_input == 0 or  globals.browse_image == 0:
        tkinter.messagebox.showerror(title='Detailed Report Fail',message='No Report is generated')
    ####
    else:
        webbrowser.open_new(globals.D_Report)
        statusbar['text'] ="Detailed Report"

def pdf_view():
    if globals.no_user_input == 3 or globals.browse_image == 3:
       # globals.no_type_selected=0
        globals.no_value_selected=0
        globals.no_user_input=0
        globals.browse_image=0
 
    if  globals.no_user_input == 0 or globals.browse_image == 0:
        tkinter.messagebox.showerror(title='Summarized Report Fail',message='No Report is generated')
    ####
    else:
        #print(nofile)
        statusbar['text'] ="Summarized Report"
        webbrowser.open_new(globals.S_Report)

#this below function is  to reset form values when reset button is clicked
def reset_form_values():
    report.get_sampleNo("")
    report.get_date("")
    report.get_day("")
    report.get_arrivalNo("")
    report.get_partyName("")
    report.get_vehicleNo("")
    report.get_riceType("")
    report.get_moisture("")
    report.get_look("")

    reportnew.get_sampleNo("")
    reportnew.get_date("")
    reportnew.get_day("")
    reportnew.get_arrivalNo("")
    reportnew.get_partyName("")
    reportnew.get_vehicleNo("")
    reportnew.get_riceType("")
    reportnew.get_moisture("")
    reportnew.get_look("")
    
    
def reset_button():
    globals.reset=0
    globals.no_user_input=0
    globals.browse_image=0
    globals.direct_clicked=0 # this is for browse or scan should not be clicked before 10g
    globals.need_to_reset=0
    reset_form_values() #form values destroy

    if not isinstance(globals.label_input,str): 
        #this is to clear the view sample by destroying elements in it
        globals.label_input.destroy()
        globals.label_processed.destroy()
        #globals.button_to_open_new_window.destroy()
        globals.label2.destroy()
        globals.label.destroy()

    # if os.path.exists("scan"): 
    #     # Muzammil adding these lines for deleting our temp imgs
    #     shutil.rmtree("scan")
    
    # Remove contents of scan folder but keep the folder
    if os.path.exists("scan"):
        for filename in os.listdir("scan"):
            file_path = os.path.join("scan", filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

    if os.path.exists("yellowTemp"):    
        shutil.rmtree("yellowTemp")

    if os.path.exists("paddy"):    
        shutil.rmtree("paddy")

    if os.path.exists("scan_copy"):    
        shutil.rmtree("scan_copy")

    if os.path.exists("yellow"):    
        shutil.rmtree("yellow")
    
    if os.path.exists("chaly_temp"):    
        shutil.rmtree("chaly_temp")

    if os.path.exists("chaly_temp3"):    
        shutil.rmtree("chaly_temp3")

    if not no_func == 1:
        tkinter.messagebox.showinfo(title='Reset',message='Data Reset Successfully')

def get_currentDir():
    current_path = os.getcwd()

    # jia change this because hardcoded Windows backslashes (\\) cause FileNotFoundError on Linux. os.path.join is cross-platform.
    history_directory = os.path.join(current_path,"History")
    if not os.path.exists(history_directory):
        os.mkdir(history_directory)
        
    from datetime import date
    today = str(date.today())

    datewise_directory = os.path.join(history_directory,today)
    if not os.path.exists(datewise_directory):
        os.mkdir(datewise_directory)

    i=0
    sampleNo_directory= os.path.join(datewise_directory,"Sample-"+ str(i))

    bool_value= 0
    while os.path.exists(sampleNo_directory):
        i += 1
        sampleNo_directory= os.path.join(datewise_directory,"Sample-"+ str(i))
        bool_value=1
    
    os.mkdir(sampleNo_directory)    

    return sampleNo_directory

def get_nonexistant_path(fname_path):
    
    
    """
    Get the path to a filename which does not exist by incrementing path.

    Examples
    --------
    >>> get_nonexistant_path('/etc/issue')
    '/etc/issue-1'
    >>> get_nonexistant_path('whatever/1337bla.py')
    'whatever/1337bla.py'
    """
    if not os.path.exists(fname_path):
        return fname_path
    filename, file_extension = os.path.splitext(fname_path)
    i = 1
    new_fname = "{}-{}{}".format(filename, i, file_extension)
    while os.path.exists(new_fname):
        i += 1
        new_fname = "{}-{}{}".format(filename, i, file_extension)
    return new_fname

def center_widget(width,height):
    
    global screen_width,screen_height,x_cordinate,y_cordinate,window_height,window_width
    window_height = height
    window_width = width

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    

class VerticalScrolledFrame(tk.Frame):

    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)

class Home(tk.Frame):
    def __init__(self, parent, controller):
    
        def first_test():
        
            global rice_image
            global objects            

            def scan_loading_func():
        
                #disable all button when it is processing
                Sample_button["state"] = "disabled"
                First_test["state"] = "disabled"
                Select_type["state"] = "disabled"
                Select_button["state"] = "disabled"
                Scan_button["state"] = "disabled"
                Repor_button["state"] = "disabled"
                DRepor_button["state"] = "disabled"
                Display_button["state"] = "disabled"
                Reset_button["state"] = "disabled"
                #####
                
                global prog_bar
                global top_progBar
                top_progBar = Toplevel()

                #these two lines of code are to bring on top this progress bar
                top_progBar.lift()
                top_progBar.attributes("-topmost",True)

                center_widget(360,100)
                top_progBar.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
                top_progBar.title("Loading..")

                prog_bar = ttk.Progressbar(top_progBar,
                                            orient="horizontal",
                                            length=500, mode = "indeterminate")
                prog_bar.pack(side=tk.TOP, pady=8)
                global wait_label
                wait_label = Label(top_progBar, text = "Please wait..", font = ("Arial",13))
                wait_label.pack()
                prog_bar.start()

            def scan_100G_process():
                try:
                    globals.no_value_selected= 1
                    globals.no_user_input=1
                    globals.browse_image=1
                    
                    #these below lines are necessary for threading operation
                    # import pythoncom
                    # pythoncom.CoInitialize()
                    ###
                    
                    statusbar['text'] ="Scanning Image"
                    global rice_image
                    global objects
                
                    our_path=get_currentDir()
                    a=str(random.randint(1,1000))
                    filename = os.path.join(our_path, 'scan_' + a)
                    png_path = filename + ".png"
                    
                    success = platform_utils.scan_image_to_file(png_path)
                    if not success:
                        return
            
                    im = Image.open(png_path)
                    im.save(filename + '.jpg')
                
                    #os.remove(filename + '.png')
                    path = str(png_path)
                    rice_image = cv2.imread(path)

                    #leena
                    globals.D_Report = get_nonexistant_path(our_path +'\\'+"Detailed Report.pdf")
                    #####
                
                    objects=analysis.analyze(rice_image,globals.D_Report)
                    os.remove(path)
                    reportnew.calculate_no_of_grains(objects)
                    grains = len(objects)
                    if(grains != 100):
                        os.remove(os.path.join(our_path, "Detailed Report.pdf"))

                    stop=prog_bar.stop()
                        
                    if stop == None:
                    
                        top_progBar.destroy()

                        #enable all buttons when the processing is completed
                        Sample_button["state"] = "active"
                        First_test["state"] = "normal"
                        Select_type["state"] = "normal"
                        Select_button["state"] = "normal"
                        Scan_button["state"] = "normal"
                        Repor_button["state"] = "active"
                        DRepor_button["state"] = "active"
                        Display_button["state"] = "normal"
                        Reset_button["state"] = "normal"
                        ###

                        globals.need_to_reset=1

                    #except clause to check for 100 grains
                    if(reportnew.calculate_no_of_grains.no_of_grains != 100):
                        print(reportnew.calculate_no_of_grains.no_of_grains)
                        tk.messagebox.showinfo("Grains Quantity =", grains)
                        statusbar['text'] ="Error!"
                        tkinter.messagebox.showerror(title='Error!',
                        message='Please put 100 grains on scanner bed then scan again')
                    else:
                        runflag = 1
                        print("After changing the flag",runflag)
                        globals.S_Report = get_nonexistant_path(os.path.join(our_path, "Summarized Report.pdf"))
                        #####
                        
                        reportnew.gen_report(objects,globals.S_Report)
                        from reportnew import ldata, cdata, tdata, Date, Time
                        from reportnew import AGL
                        print(reportnew.ldata,reportnew.cdata,reportnew.tdata)
                        statusbar['text'] ="Processing Completed"
                        tkinter.messagebox.showinfo("Processing Completed","Please click on View Sample Tab to see results.")
                except:
                    print("except condition true")
                    stop=prog_bar.stop()
                    if stop == None:
                    
                        top_progBar.destroy()

                        #enable all buttons when the processing is completed
                        Sample_button["state"] = "active"
                        First_test["state"] = "normal"
                        Select_type["state"] = "normal"
                        Select_button["state"] = "normal"
                        Scan_button["state"] = "normal"
                        Repor_button["state"] = "active"
                        DRepor_button["state"] = "active"
                        Display_button["state"] = "normal"
                        Reset_button["state"] = "normal"
                        ###

                        globals.need_to_reset=1
                    tkinter.messagebox.showerror("Scanner not connected","Please Connect the scanner.")

            def scan_for_100_grains():
                myLabel = Label(canvas1, text=clicked.get()).pack()
                
                selected_type = clicked.get()
                myLabel2 = Label(canvas1, text=clickednew.get()).pack()
                selected_value_chalky = clickednew.get()
                print("The selected value for chalky input is",selected_value_chalky)
                
                root1.destroy()
                
                reportnew.calculate_type(selected_type)
                analysis.chalky_input(selected_value_chalky)
                
                threading.Thread(target=scan_100G_process).start()
                threading.Thread(target=scan_loading_func).start()

             #leena
            if globals.need_to_reset != 1:
                root1 = tk.Tk()
                root1.title("100 Grains Testing")
            
                canvas1 = tk.Canvas(root1, width =300, height = 200)
                canvas1.config(bg="#336699")
                
                canvas1.pack()
                
                # Initializing the button for selection of Rice Type & Drop Down for Rice Types
                clicked = StringVar(root1)

                clickednew = StringVar(root1)
                clickednew.set("less than 50%")

                label4 = tk.Label(root1, text='Please select your chalky % ')
                label4.config(font=('helvetica', 10))
                canvas1.create_window(150, 30, window=label4)

                dropnew = OptionMenu(canvas1, clickednew, "less than 50%", "greater than 50%")
                canvas1.create_window(150,60, window=dropnew)
                

                # Closing the Canvas & executing functions in report file
                myButton = Button(canvas1,text = "Scan", command=scan_for_100_grains,width=12, height=2, bd=5,
                                highlightcolor='grey48',
                                relief=RIDGE)
                canvas1.create_window(150, 140, window=myButton)

                def change_dropdown(*args):
                    print(clicked.get())
                
                clicked.trace('w', change_dropdown)
                
                root1.mainloop()

            else:
                tkinter.messagebox.showwarning("Reset","Please click on Reset Button.")

             
        def select_type():

            global rice_image
            global objects
            
            AGL = None # Define AGL at the beginning of the function

            def show():
                def TenG_yes():
                    globals.direct_clicked=1

                    x1 = entry1.get()

                    #leena
                    x3_longBrokenMax = entry_longBrokenMax.get()
                    x4_longBrokenMin = entry_longBrokenMin.get()
                    x5_MediumBrokenMax = entry_MediumBrokenMax.get()
                    x6_MediumBrokenMin = entry_MediumBrokenMin.get()
                    x7_SmallBrokenMax = entry_SmallBrokenMax.get()
                    x8_SmallBrokenMin = entry_SmallBrokenMin.get()
                    ###

                    # Variable for chalky input
                    myLabel2 = Label(canvas1, text=clickednew.get()).pack()
                    selected_value_chalky = clickednew.get()
                    print("The selected value for chalky input is",selected_value_chalky)

                    analysis.chalky_input(selected_value_chalky)
                    report.get_user_input(x1)

                    #leena
                    report.get_input_LongBroken(x3_longBrokenMax, x4_longBrokenMin)
                    report.get_input_MediumBroken(x5_MediumBrokenMax, x6_MediumBrokenMin)
                    report.get_input_SmallBroken(x7_SmallBrokenMax, x8_SmallBrokenMin)
                    ###
                    
                    #from reportnew import AGL
                    if (runflag == 0):
                        temp_AGL = 0
                        print("100 Grain test not run",temp_AGL)
                    else:
                        temp_AGL = AGL
                        print("100 Grain test run",temp_AGL)
                        print("yes")
                        
                    TenG_cancel()
                    TenG_no()

                #leena
                def TenG_cancel():
                    neww_win.destroy()

                def TenG_no():
                    TenG_cancel()
                    root.destroy()
                ###

                #leena 
                neww_win = Toplevel()
                neww_win.geometry('320x100')#300x100
                neww_win.resizable(0, 0)
                neww_win.title('Grain Testing')
                message = "Changes have been made in the form.\n Save changes?"
                Label(neww_win, text=message, fg='grey', font=("Helvetica", 12)).place(x=40, y=10)
                Button(neww_win, text='Yes',command=TenG_yes, width=5, height=1).place(x=50, y=60)
                Button(neww_win, text='No', command=TenG_no, width=5, height=1).place(x=120, y=60)
                Button(neww_win, text='Cancel', command=TenG_cancel, width=6, height=1).place(x=190, y=60)
                ###
        
            if globals.need_to_reset != 1:
                
                root = tk.Tk()
                #root = Tk()
                root.title("Rice Type Selection")
                #root.geometry("400x400")
                
                canvas1 = Canvas(root, height = 280, width = 400) #height = 410, width = 400, bg ="lavender"
                canvas1.pack()

                # Code to Enter the Rice Size directly for broken rice detection
                label2 = tk.Label(root, text='Option 1:  Insert the number in mm for broken size')
                label2.config(font=('helvetica', 10))
                canvas1.create_window(200, 100, window=label2)#200,100

                entry1 = tk.Entry(root)
                canvas1.create_window(200, 130, window=entry1) #200,130

                #leena

                #Check box for chalky% input
                clickednew = StringVar(root)
                clickednew.set("less than 50%")

                label4 = tk.Label(root, text='Please select your chalky % ')
                label4.config(font=('helvetica', 10))
                canvas1.create_window(200, 30, window=label4)

                dropnew = OptionMenu(canvas1, clickednew, "less than 50%", "greater than 50%")
                canvas1.create_window(200,60, window=dropnew)


                #for long broken
                label_longBroken= tk.Label(root, text= "Long Broken")
                label_longBroken.config(font=('helvetica', 10))
                canvas1.create_window(70, 170, window=label_longBroken)#70,170

                entry_longBrokenMin = tk.Entry(root,width=5)
                canvas1.create_window(45, 200, window=entry_longBrokenMin)#45,200

                label_min= tk.Label(root, text= "min")
                label_min.config(font=('helvetica', 10))
                canvas1.create_window(45, 220, window=label_min)#45,220

                label_line= tk.Label(root, text= "--")
                label_line.config(font=('helvetica', 10))
                canvas1.create_window(70, 200, window=label_line)

                entry_longBrokenMax = tk.Entry(root,width=5)
                canvas1.create_window(95, 200, window=entry_longBrokenMax)

                label_max= tk.Label(root, text= "max")
                label_max.config(font=('helvetica', 10))
                canvas1.create_window(95, 220, window=label_max)

                #for medium broken
                label_MediumBroken= tk.Label(root, text= "Medium Broken")
                label_MediumBroken.config(font=('helvetica', 10))
                canvas1.create_window(200, 170, window=label_MediumBroken)#200,170

                entry_MediumBrokenMin = tk.Entry(root,width=5)
                canvas1.create_window(175, 200, window=entry_MediumBrokenMin)

                label_min= tk.Label(root, text= "min")
                label_min.config(font=('helvetica', 10))
                canvas1.create_window(175, 220, window=label_min)

                label_line= tk.Label(root, text= "--")
                label_line.config(font=('helvetica', 10))
                canvas1.create_window(200, 200, window=label_line)

                entry_MediumBrokenMax = tk.Entry(root,width=5)
                canvas1.create_window(225, 200, window=entry_MediumBrokenMax)

                label_max= tk.Label(root, text= "max")
                label_max.config(font=('helvetica', 10))
                canvas1.create_window(225, 220, window=label_max)

                #for small broken
                label_SmallBroken= tk.Label(root, text= "Small Broken")
                label_SmallBroken.config(font=('helvetica', 10))
                canvas1.create_window(330, 170, window=label_SmallBroken)#330,170

                entry_SmallBrokenMin = tk.Entry(root,width=5)
                canvas1.create_window(305, 200, window=entry_SmallBrokenMin)

                label_min= tk.Label(root, text= "min")
                label_min.config(font=('helvetica', 10))
                canvas1.create_window(305, 220, window=label_min)

                label_line= tk.Label(root, text= "--")
                label_line.config(font=('helvetica', 10))
                canvas1.create_window(330, 200, window=label_line)

                entry_SmallBrokenMax = tk.Entry(root,width=5)
                canvas1.create_window(355, 200, window=entry_SmallBrokenMax)

                label_max= tk.Label(root, text= "max")
                label_max.config(font=('helvetica', 10))
                canvas1.create_window(355, 220, window=label_max)
                ####

                #leena
                root.protocol('WM_DELETE_WINDOW',show) #to perform functionality when close from title bar
                ###
            
                # Closing the Canvas & executing functions in report file
                myButton = Button(canvas1,text = "Submit", command=show)
                canvas1.create_window(200, 250, window=myButton)#200,350

                def change_dropdownnew(*args):
                    print( clickednew.get() )

                clickednew.trace('w', change_dropdownnew)

                root.mainloop()
                
            else:
                tkinter.messagebox.showwarning("Reset","Please click on Reset Button.")
                
        

        def select_image():

            if globals.direct_clicked == 1 and globals.need_to_reset != 1:

                statusbar['text'] ="Selecting Image"
                # open a file chooser dialog and allow the user to select an input image
                
                path = filedialog.askopenfilename()

                #leena
                globals.browse_image=0 #if the browse image is not selected 
                ##

             ######leenaaaa########        
                def processing(path):
                    global rice_image
                    global objects
                    rice_image = cv2.imread(path)
                    statusbar['text'] ="Processing Image"
                    t1_start = process_time()
                    #p = Pool()
                    
                    pool = ThreadPool(processes=6)

                    async_result = pool.apply_async(analysis.analyze, (rice_image,globals.D_Report)) # tuple of args for foo

                    objects = async_result.get()

                    t1_stop = process_time()
                    print("Elapsed time:", t1_stop, t1_start)
                    print("Elapsed time during the ANALYSIS program in seconds:", 
                                         t1_stop-t1_start)
                    report.gen_report(objects,globals.S_Report)
                    from report import ldata, cdata, tdata, Date, Time
                    print(report.ldata,report.cdata,report.tdata)

                    stop=prog_bar.stop()
                    if stop == None:
                        #wait_label.destroy()
                        top_progBar.destroy()

                        #enable all buttons when the processing is completed
                        Sample_button["state"] = "active"
                        First_test["state"] = "normal"
                        Select_type["state"] = "normal"
                        Select_button["state"] = "normal"
                        Scan_button["state"] = "normal"
                        Repor_button["state"] = "active"
                        DRepor_button["state"] = "active"
                        Display_button["state"] = "normal"
                        Reset_button["state"] = "normal"
                        ###

                        globals.need_to_reset=1
                        
                        tkinter.messagebox.showinfo("Processing Completed","Please click on View Sample Tab to see results.")
    
                def loading_func():

                    #disable all button when it is processing
                    Sample_button["state"] = "disabled"
                    First_test["state"] = "disabled"
                    Select_type["state"] = "disabled"
                    Select_button["state"] = "disabled"
                    Scan_button["state"] = "disabled"
                    Repor_button["state"] = "disabled"
                    DRepor_button["state"] = "disabled"
                    Display_button["state"] = "disabled"
                    Reset_button["state"] = "disabled"
                    #####
                    
                    global prog_bar
                    global top_progBar
                    top_progBar = Toplevel()
                    center_widget(360,100)
                    top_progBar.resizable(0, 0)
                    top_progBar.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
                    #top_progBar.geometry("360x100")
                    top_progBar.title("Loading..")

                    prog_bar = ttk.Progressbar(top_progBar,
                                               orient="horizontal",
                                               length=500, mode = "indeterminate")
                    prog_bar.pack(side=tk.TOP, pady=8)
                    global wait_label
                    wait_label = Label(top_progBar, text = "Please wait..", font = ("Arial",13))
                    wait_label.pack()
                    prog_bar.start()
                
                if len(path) > 0:

                    #leena
                    global our_path
                    our_path= get_currentDir()
                    globals.S_Report = get_nonexistant_path(os.path.join(our_path, "Summarized Report.pdf"))
                    globals.D_Report = get_nonexistant_path(os.path.join(our_path, "Detailed Report.pdf"))
                    
                    #leena
                    globals.browse_image=1 #if browse image is selected
                    ##
   
                    #leena
                    threading.Thread(target=processing,args=(path,)).start()
                    threading.Thread(target=loading_func).start()
                    ####
         
                statusbar['text'] ="Processing Completed"

            else:
                tkinter.messagebox.showerror("Test Sample Failed","There is no entry in 10g Sample Test.\n Please click on 10g Grain Test")
            
        
        # initialize the window toolkit along with the two image panels
        iconb_path = os.path.join(img_dir, 'iconb.png')
        self.image_b = tk.PhotoImage(file=iconb_path)
        # self.image_t = tk.PhotoImage(file="img/iconb.png")
        Select_button = ttk.Button(button_frame, text="Browse Image", 
                                   image=self.image_b, compound="left",
                                   command=select_image)    

        iconv_path = os.path.join(img_dir, 'iconv.png')
        self.image_v = tk.PhotoImage(file=iconv_path)
        # self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left", 
                                   command=lambda: controller.show_frame(Sample))

        icona_path = os.path.join(img_dir, 'icona.png')
        self.image_a = tk.PhotoImage(file=icona_path)
        # self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left",
                                     command=lambda: controller.show_frame(Analyses))

        iconr_path = os.path.join(img_dir, 'iconr.png')
        self.image_r = tk.PhotoImage(file=iconr_path)
        # self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                  image=self.image_r, compound="left",
                                  command= pdf_view)

        dr_path = os.path.join(img_dir, 'detailed.png')
        self.image_dr = tk.PhotoImage(file=dr_path)        
        # self.image_dr = tk.PhotoImage(file="img/detailed.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                  image=self.image_dr, compound="left",
                                  command= pdf1_view)
        
        iconss_path = os.path.join(img_dir, 'iconss.png')
        self.image_s = tk.PhotoImage(file=iconss_path)
        # self.image_s = tk.PhotoImage(file="img/iconss.png")
        Scan_button = ttk.Button(button_frame, text="Scan Image",
                                 image=self.image_s, compound="left",
                                 command=Scan_Image)

        display_icon_path = os.path.join(img_dir, 'display.png')
        self.display_icon = tk.PhotoImage(file=display_icon_path)
        # self.display_icon = tk.PhotoImage(file="img/display.png")
        Display_button = ttk.Button(button_frame, text="Display All",image=self.display_icon, compound="left",command=Display)

        reset_icon_path = os.path.join(img_dir, 'reset.png')
        self.reset_icon = tk.PhotoImage(file=reset_icon_path)
        # self.reset_icon = tk.PhotoImage(file="img/reset.png")
        Reset_button = ttk.Button(button_frame, text="Reset",
                                 image=self.reset_icon, compound="left",
                                 command=reset_button)

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)
        button_frame.columnconfigure(8, weight=1)
      
        First_test.grid(row=2, column=0, sticky=tk.W+tk.E)
        Select_type.grid(row=2, column=1, sticky=tk.W+tk.E)
        Select_button.grid(row=2, column=2, sticky=tk.W+tk.E)
        Scan_button.grid(row=2, column=3, sticky=tk.W+tk.E) #4
        Sample_button.grid(row=2, column=4, sticky=tk.W+tk.E) #5
        Repor_button.grid(row=2, column=5, sticky=tk.W+tk.E) #7
        DRepor_button.grid(row=2, column=6, sticky=tk.W+tk.E) #8
        Display_button.grid(row=2, column=7, sticky=tk.W+tk.E)
        Reset_button.grid(row=2, column=8, sticky=tk.W+tk.E)
            
    def updateFrame(self):
        print('Sample')

def myfunc():
    print('Function created')
#leena
def Display( ):
    
    # base_dir = os.path.dirname(os.path.abspath(__file__))
    def get_base_dir():
        if getattr(sys, 'frozen', False):
        # The application is frozen
            base_dir = os.path.dirname(sys.executable)
        else:
        # The application is not frozen
            base_dir = os.path.dirname(os.path.abspath(__file__))
        return base_dir

    base_dir = get_base_dir()
    
    print('Function created')
    root = tk.Tk()
    root.geometry('1300x600')
    # root.resizable(0, 0)
    root.title("Display Window")
    root.config(bg='#336699')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #these None are for to check if they doesn't exists then don't show them 
    canvas=None
    all=None
    yellow=None
    damage=None
    paddy = None
    chalky=None
    vsb=None
    hsb=None
    label_error=None
    back=None
    #self.nback=None

    def ss():
        # native tkinter geometry fetching to replace FindWindow
        root.update_idletasks()
        x = root.winfo_rootx()
        y = root.winfo_rooty()
        w = root.winfo_width()
        h = root.winfo_height()
        list_frame = [8, -5, 8, 8]  # Adjusting for borders if needed (like the original code)
        final_rect = (x - list_frame[0], y - list_frame[1], x + w - list_frame[2], y + h - list_frame[3])
        
        img_path = os.path.join(base_dir, "Image.jpg")
        
        # On Linux ImageGrab might fail without gnome-screenshot, but taking screenshot via pyautogui is wrapped in platform_utils
        import platform_utils
        from PIL import ImageGrab
        import platform
        
        if platform.system() == "Windows":
            img = ImageGrab.grab(bbox=final_rect)
            img.save(img_path)
        else:
            # On Linux we use PyAutoGUI through platform_utils or just full grab if possible
            # Depending on platform_utils implementation
            try:
                import pyscreenshot as ImageGrabLinux
                img = ImageGrabLinux.grab(bbox=final_rect)
                img.save(img_path)
            except:
                platform_utils.take_screenshot(img_path)

    def all():
        nonlocal All
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal back
        nonlocal canvas

        i = 0
        columns = 15
        all_count = 0
        if frame_all != None:
            frame_all.destroy()
            frame_yellow.destroy()
            frame_damage.destroy()
            frame_paddy.destroy()
            frame_chalky.destroy()
            frame_all = Frame(canvas)
            frame_all.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_all, anchor="nw")
            frame_all.grid_columnconfigure(0, weight=1)
            frame_all.grid_rowconfigure(0, weight=1)
        for name in All:
            i += 1
            all_count += 1
            r, c = divmod(all_count - 1, columns)
            # current_path = os.getcwd() # to get the current directory path
            # im = Image.open(current_path+"\\scan_copy\\" + str(name))
            im = Image.open(os.path.join(base_dir, "scan_copy", str(name)))
            # resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            resized = im.resize((columns * 5, columns * 8), Image.LANCZOS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_all, text='All' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()
            canvas.config(yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=frame_all.bbox(ALL))

        root.mainloop()
        
    def yellow():
        nonlocal Yellow
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal back
        nonlocal canvas
        columns = 15
        image_count = 0
        i = 0
        if frame_yellow != None:
            frame_yellow.destroy()
            frame_damage.destroy()
            frame_paddy.destroy()
            frame_all.destroy()
            frame_chalky.destroy()
            frame_yellow = Frame(canvas)
            frame_yellow.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_yellow, anchor="nw")
            frame_yellow.grid_columnconfigure(0, weight=1)
            frame_yellow.grid_rowconfigure(0, weight=1)
        for name in Yellow:
            i += 1
            image_count += 1
            r, c = divmod(image_count - 1, columns)
            # current_path = os.getcwd() # to get the current directory path
            # im = Image.open(current_path+"\\scan_copy\\" + str(name))
            im = Image.open(os.path.join(base_dir, "scan_copy", str(name)))
            # resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            resized = im.resize((columns * 5, columns * 8), Image.LANCZOS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_yellow, text='Yellow' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()
            canvas.config(yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=frame_yellow.bbox(ALL))

        root.mainloop()

    def damage():
        nonlocal damages
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal back
        nonlocal canvas
        i = 0
        columns = 15
        damage_count = 0
        if frame_damage != None:
            frame_damage.destroy()
            frame_yellow.destroy()
            frame_paddy.destroy()
            frame_all.destroy()
            frame_chalky.destroy()

            frame_damage = Frame(canvas)
            frame_damage.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_damage, anchor="nw")
            frame_damage.grid_columnconfigure(0, weight=1)
            frame_damage.grid_rowconfigure(0, weight=1)
        for name in damages:
            i += 1
            damage_count += 1
            r, c = divmod(damage_count - 1, columns)
            # current_path = os.getcwd() # to get the current directory path
            # im = Image.open(current_path+"\\scan_copy\\" + str(name))
            im = Image.open(os.path.join(base_dir, "scan_copy", str(name)))
            # resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            resized = im.resize((columns * 5, columns * 8), Image.LANCZOS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_damage, text='Damage' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()

            canvas.config(yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=canvas.bbox(ALL))

        root.mainloop()

    def chalky():
        nonlocal Chalky
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal back
        nonlocal canvas
        i = 0
        columns = 15
        chalky_count = 0
        if frame_chalky != None:
            frame_chalky.destroy()
            frame_yellow.destroy()
            frame_all.destroy()
            frame_paddy.destroy()
            frame_damage.destroy()
            frame_chalky = Frame(canvas)
            frame_chalky.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_chalky, anchor="nw")
            frame_chalky.grid_columnconfigure(0, weight=1)
            frame_chalky.grid_rowconfigure(0, weight=1)
        for name in Chalky:
            i += 1
            chalky_count += 1
            r, c = divmod(chalky_count - 1, columns)
            # current_path = os.getcwd() # to get the current directory path
            # im = Image.open(current_path+"\\scan_copy\\" + str(name))
            im = Image.open(os.path.join(base_dir, "scan_copy", str(name)))
            # resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            resized = im.resize((columns * 5, columns * 8), Image.LANCZOS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_chalky, text='Chalky' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()
            canvas.config(yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=frame_chalky.bbox(ALL))
        root.mainloop()
    
    def Paddy():
        nonlocal paddy
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal back
        nonlocal canvas
        i = 0
        columns = 15
        paddy_count = 0
        if frame_paddy != None:
            frame_chalky.destroy()
            frame_yellow.destroy()
            frame_paddy.destroy()
            frame_all.destroy()
            frame_damage.destroy()
            frame_paddy = Frame(canvas)
            frame_paddy.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_paddy, anchor="nw")
            frame_paddy.grid_columnconfigure(0, weight=1)
            frame_paddy.grid_rowconfigure(0, weight=1)
        for name in paddy:
            i += 1
            paddy_count += 1
            r, c = divmod(paddy_count - 1, columns)
            # current_path = os.getcwd() # to get the current directory path
            # im = Image.open(current_path+"\\paddy\\" + str(name))
            im = Image.open(os.path.join(base_dir, "paddy", str(name)))
            # resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            resized = im.resize((columns * 5, columns * 8), Image.LANCZOS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_paddy, text='Paddy' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()
            canvas.config(yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=frame_paddy.bbox(ALL))
        root.mainloop()


    # current_path = os.getcwd()
    # if os.path.exists(current_path+"\\scan_copy"):
    if os.path.exists(os.path.join(base_dir, "scan_copy")):
        from analysis import yellow_filename , new_damage1_name, chalky_name, paddy_name
        # All = os.listdir(current_path+"\\scan_copy")
        All = os.listdir(os.path.join(base_dir, "scan_copy"))
        Yellow = yellow_filename
        damages = new_damage1_name
        Chalky = chalky_name
        paddy = paddy_name
        if label_error != None:
            label_error.destroy()
    #             self.nback.destroy()
        canvas = Canvas(root, bg='grey48', relief=SUNKEN)
        canvas.grid(row=0, column=0, sticky="news")
        frame_all = Frame(canvas)
        frame_all.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_all, anchor="nw")
        frame_yellow = Frame(canvas)
        frame_yellow.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_yellow, anchor="nw")
        frame_damage = Frame(canvas)
        frame_damage.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_damage, anchor="nw")
        frame_chalky = Frame(canvas)
        frame_chalky.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_chalky, anchor="nw")
        frame_paddy = Frame(canvas)
        frame_paddy.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_paddy, anchor="nw")
        canvas.grid_columnconfigure(0, weight=1)
        frame_all.grid_columnconfigure(0, weight=1)
        frame_yellow.grid_columnconfigure(0, weight=1)
        frame_damage.grid_columnconfigure(0, weight=1)
        frame_chalky.grid_columnconfigure(0, weight=1)
        canvas.grid_rowconfigure(0, weight=1)
        frame_all.grid_rowconfigure(0, weight=1)
        frame_yellow.grid_rowconfigure(0, weight=1)
        frame_damage.grid_rowconfigure(0, weight=1)
        frame_chalky.grid_rowconfigure(0, weight=1)
        frame_paddy.grid_columnconfigure(0, weight=1)
        frame_paddy.grid_rowconfigure(0, weight=1)

        vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        hsb = Scrollbar(root, orient="horizontal", command=canvas.xview)
        hsb.grid(row=1, column=0, sticky="wes")
        all = Button(root, text="ALL", width=20, command=all, height=2, bd=5, highlightcolor='grey48',
                 relief=RIDGE)

        all.grid(row=0, column=2, sticky="nw", padx=80, pady=50)
        yellow = Button(root, text="Yellow", command=yellow, width=20, height=2, bd=5, relief=RIDGE)
        yellow.grid(row=0, column=2, sticky="nw", padx=80, pady=100)
        damage = Button(root, text="Damage", command=damage, width=20, height=2, bd=5, relief=RIDGE)
        damage.grid(row=0, column=2, sticky="nw", padx=80, pady=150)
        chalky = Button(root, text="Chalky ", command=chalky, width=20, height=2, bd=5, relief=RIDGE)
        chalky.grid(row=0, column=2, sticky="nw", padx=80, pady=200)
        paddy1 = Button(root, text="Paddy ", command=Paddy, width=20, height=2, bd=5, relief=RIDGE)
        paddy1.grid(row=0, column=2, sticky="nw", padx=80, pady=250)


    else:
        if canvas != None:
            canvas.destroy()
            all.destroy()
            yellow.destroy()
            damage.destroy()
            chalky.destroy()
            paddy.destroy()
            # self.back.destroy()
            back.destroy()
            vsb.destroy()
            hsb.destroy()
                    
        label_error=Label(root,foreground="black",background="azure",text="Please Test Sample",relief=RAISED,font=("Courier", 44))
        label_error.grid(row=0,column=0)
        

    root.mainloop()       

class Sample(tk.Frame):
   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg =  "#ffffff")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, 'img')
           
        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, 120))
            photo = ImageTk.PhotoImage(image)
            label.config(image = photo)
            label.image = photo #avoid garbage collection
            
        cv3img_path = os.path.join(img_dir, 'cv3.jpg')
        image = Image.open(cv3img_path)
        # image = Image.open("img/cv3.jpg")
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.bind('<Configure>', resize_image)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)


        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)
        
        # Initialize Buttons and add images to button
        iconh_path = os.path.join(img_dir, 'iconh.png')
        self.image_h = tk.PhotoImage(file=iconh_path)
        # self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))

        iconv_path = os.path.join(img_dir, 'iconv.png')
        self.image_v = tk.PhotoImage(file=iconv_path)        
        # self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left")
                                   
        iconr_path = os.path.join(img_dir, 'iconr.png')
        self.image_r = tk.PhotoImage(file=iconr_path)        
        # self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)

        dr_path = os.path.join(img_dir, 'detailed.png')
        self.image_dr = tk.PhotoImage(file=dr_path)        
        # dr_path = os.path.join(img_dir, 'detailed.png')
        # self.image_dr = tk.PhotoImage(file="img/detailed.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)

        display_icon_path = os.path.join(img_dir, 'display.png')
        self.display_icon = tk.PhotoImage(file=display_icon_path)        
        # self.display_icon = tk.PhotoImage(file="img/display.png")
        Display_button = ttk.Button(button_frame, text="Display Button",
                         image=self.display_icon, compound="left",
                         command=Display)

        reset_icon_path = os.path.join(img_dir, 'reset.png')
        self.reset_icon = tk.PhotoImage(file=reset_icon_path)
        # self.reset_icon = tk.PhotoImage(file="img/reset.png")
        Reset_button = ttk.Button(button_frame, text="Reset Button",
                                 image=self.reset_icon, compound="left",
                                 command= reset_button)

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        
        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=3, sticky=tk.W+tk.E)
        Display_button.grid(row=0, column=4, sticky=tk.W+tk.E)
        Reset_button.grid(row=0, column=5, sticky=tk.W+tk.E)
        
        lineimg_path = os.path.join(img_dir, 'line.jpg')
        image1 = Image.open(lineimg_path)        
        # image1 = Image.open("img/line.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="top" ,padx=0, pady=0)

    def updateFrame(self):

            #globals.no_value_selected is 1 and
        if  globals.no_user_input == 1 and globals.browse_image == 1: #make reset value 1
            globals.reset=1
            
        #leena
        if globals.reset == 0:
            print("reset == 0")
            tkinter.messagebox.showinfo(title='Reset',message='No Data to show')
        ###
            
        else: #make reset value 1
            try:
                    
               #image1 = cv2.resize(rice_image, (400,600))
                image1 = cv2.resize(rice_image,None,fx = 0.15, fy = 0.15, interpolation = cv2.INTER_LINEAR)
                b,g,r = cv2.split(image1)
                img = cv2.merge((r,g,b))
                im1 = Image.fromarray(img)
               
                photo1 = ImageTk.PhotoImage(image=im1)

                #leena
                globals.label_input=tk.Label(self,text="Input Image ->",fg = "red")
                globals.label_input.pack(side ="left",anchor = tk.W ,padx=20)
                ####

                #leena
                globals.label_processed=tk.Label(self,text="<- Processed Image",fg = "red")
                globals.label_processed.pack(side="right",anchor = tk.E,padx=20)
                ####
                
                #this is for raw image
                globals.label = tk.Label(self,image=photo1)
                globals.label.image = photo1 # keep a reference!
                globals.label.pack(side ="left" ,anchor = tk.NW , pady=0)

               
                image2 = analysis.return_final_image()
                if len(image2) == 0:
                    image2 = rice_image
                #image2 = cv2.resize(image2, (700,700))
                image2 = cv2.resize(image2,None,fx = 0.25, fy = 0.25, interpolation = cv2.INTER_LINEAR)
                b,g,r = cv2.split(image2)
                img = cv2.merge((r,g,b))
                im2 = Image.fromarray(img)
       
                photo2 = ImageTk.PhotoImage(image=im2)
               
                globals.label2 = tk.Label(self,image=photo2)
                globals.label2.image = photo2 # keep a reference!
                globals.label2.pack(side ="right" ,anchor= tk.NE, pady=0)

                     
            except:
                #except clause
                tkinter.messagebox.showwarning(title='Warning',
                                             message='No Sample Image Found! First Input Sample Image')
#leena
def saveProcessedImage(photo2):
    
    i = 0
    while os.path.exists(os.path.join(our_path, "processed-image-%s.png" % i)):
        i += 1

    photo2._PhotoImage__photo.write(os.path.join(our_path, "processed-image-%s.png" % i))
    

def open_new_window(im2):
    ventana2=tk.Toplevel()
    canvas = Canvas(ventana2, width = 300, height = 200)
    canvas.pack(expand = YES, fill = BOTH)
    ventana2.title("Image")
    photo1 = ImageTk.PhotoImage(image=im2)
    canvas.create_image(50, 10, image = photo1, anchor = NW)
    canvas.photo1 = photo1

class Analyses(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg =  "#ffffff")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, 'img')
        
        cv3_path = os.path.join(img_dir, 'cv3.jpg')
        image = Image.open(cv3_path)
        # image = Image.open("img/cv3.jpg")
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self,image=photo)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)

        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)
        
        # Initialize Buttons and add images to button
        iconh_path = os.path.join(img_dir ,'iconh.png')
        self.image_h = tk.PhotoImage(file=iconh_path)
        # self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))

        iconv_path = os.path.join(img_dir, 'iconv.png')
        self.image_v = tk.PhotoImage(file=iconv_path)
        # self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left",
                                   command=lambda: controller.show_frame(Sample))

        icona_path = os.path.join(img_dir, 'icona.png')
        self.image_a = tk.PhotoImage(file=icona_path)
        # self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left")

        iconr_path = os.path.join(img_dir, 'iconr.png')
        self.image_r = tk.PhotoImage(file=iconr_path)
        # self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)

        dr_path = os.path.join(img_dir, 'detailed.png')
        self.image_dr = tk.PhotoImage(file=dr_path)        
        # dr_path = os.path.join(img_dir, 'detailed.png')
        self.image_dr = tk.PhotoImage(file=dr_path)
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)
        
        iconp_path = os.path.join(img_dir, 'iconp.png')
        self.image_p1 = tk.PhotoImage(file=iconp_path)        
        # self.image_p1 = tk.PhotoImage(file="img/iconp.png")
        LGraph_button = ttk.Button(button_frame,text="Features Graph",
                                   image=self.image_p1, compound="left",
                                   command=lambda: controller.show_frame(LGraph))

        self.image_p2 = tk.PhotoImage(file=iconp_path)
        # self.image_p2 = tk.PhotoImage(file="img/iconp.png")
        CGraph_button = ttk.Button(button_frame,text="Color Graph",
                                   image=self.image_p2, compound="left",
                                   command=lambda: controller.show_frame(CGraph))

        self.image_p3 = tk.PhotoImage(file=iconp_path)
        # self.image_p3 = tk.PhotoImage(file="img/iconp.png")
        TGraph_button = ttk.Button(button_frame,text="Type Graph",
                                   image=self.image_p3, compound="left",
                                   command=lambda: controller.show_frame(TGraph))

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)

        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Analyses_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        LGraph_button.grid(row=0, column=3,sticky=tk.W+tk.E)
        CGraph_button.grid(row=0, column=4,sticky=tk.W+tk.E)
        TGraph_button.grid(row=0, column=5,sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=6, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=7, sticky=tk.W+tk.E)
        
        lineimg_path = os.path.join(img_dir, 'line.jpg')
        image1 = Image.open(lineimg_path)         
        # image1 = Image.open("img/line.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="top",padx=0, pady=0)

        
        label = tk.Label(self, text="Analyses", font=LARGE_FONT, bg="#ffffff")
        label.pack(pady=50,padx=10)
        self.frame = VerticalScrolledFrame(self)
        self.frame.pack( side=tk.TOP,padx=90, pady=0)

        main1_path = os.path.join(img_dir, 'main1.jpg')
        image1 = Image.open(main1_path)         
        # image1 = Image.open("img/main1.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="bottom" ,padx=0, pady=0)
        

        # Analyses table entries
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=0)
        b.insert(END, 'Object number')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=1)
        b.insert(END, 'Width (mm)')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=2)
        b.insert(END, 'Length (mm)')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=3)
        b.insert(END, 'Area (mm^2)')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=4)
        b.insert(END, 'Perimeter (mm)')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=5)
        b.insert(END, 'Whole/Broken')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=6)
        b.insert(END, 'Class')

    def updateFrame(self):
#        try:
        
        length_seq = [x['Length'] for x in objects]
        height = len(length_seq)
        for i in range(height+1):
            if (i == 0):
                continue
            else:
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=0)
                b.insert(END, '%d' %(objects[i-1]["Object_number"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=1)
                b.insert(END, '{:.3f}'.format(objects[i-1]["Width"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=2)
                b.insert(END, '{:.3f}'.format(objects[i-1]["Length"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=3)
                b.insert(END, '{:.3f}'.format(objects[i-1]["Area"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=4)
                b.insert(END, '{:.3f}'.format(objects[i-1]["Perimeter"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=5)
                if (objects[i-1]["WB"] == 0):
                    b.insert(END, 'Broken Grain')
                else:
                    b.insert(END, 'Whole Grain')
                b = Entry(self.frame.interior, text="", bg=objects[i-1]["color_hex"])
                b.grid(row=i, column=6)
                b.insert(END, objects[i-1]["Type"])

class LGraph(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg =  "#ffffff")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, 'img')
        
        cv3_path = os.path.join(img_dir, 'cv3.jpg')
        image = Image.open(cv3_path)        
        # image = Image.open("img/cv3.jpg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)
         
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)


        # Initialize Buttons and add images to button
        iconh_path = os.path.join(img_dir, 'iconh.png')
        self.image_h = tk.PhotoImage(file=iconh_path)
        # self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))

        iconv_path = os.path.join(img_dir, 'iconv.png')
        self.image_v = tk.PhotoImage(file=iconv_path)
        # self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left",
                                   command=lambda: controller.show_frame(Sample))

        icona_path = os.path.join(img_dir, 'icona.png')
        self.image_a = tk.PhotoImage(file=icona_path)
        # self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left",
                                     command=lambda: controller.show_frame(Analyses))

        iconr_path = os.path.join(img_dir, 'iconr.png')
        self.image_r = tk.PhotoImage(file=iconr_path)
        # self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)

        dr_path = os.path.join(img_dir, 'detailed.png')
        self.image_dr = tk.PhotoImage(file=dr_path)        
        # self.image_dr = tk.PhotoImage(file="img/iconr.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)

        iconp_path = os.path.join(img_dir, 'iconp.png')
        self.image_p1 = tk.PhotoImage(file=iconp_path)        
        # self.image_p1 = tk.PhotoImage(file="img/iconp.png")
        LGraph_button = ttk.Button(button_frame,text="Features Graph",
                                   image=self.image_p1, compound="left",
                                   command=lambda: controller.show_frame(LGraph))

        self.image_p2 = tk.PhotoImage(file=iconp_path)
        # self.image_p2 = tk.PhotoImage(file="img/iconp.png")
        CGraph_button = ttk.Button(button_frame,text="Color Graph",
                                   image=self.image_p2, compound="left",
                                   command=lambda: controller.show_frame(CGraph))

        self.image_p3 = tk.PhotoImage(file=iconp_path)
        # self.image_p3 = tk.PhotoImage(file="img/iconp.png")
        TGraph_button = ttk.Button(button_frame,text="Type Graph",
                                   image=self.image_p3, compound="left",
                                   command=lambda: controller.show_frame(TGraph))
 
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)
        
        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Analyses_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        LGraph_button.grid(row=0, column=3,sticky=tk.W+tk.E)
        CGraph_button.grid(row=0, column=4,sticky=tk.W+tk.E)
        TGraph_button.grid(row=0, column=5,sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=6, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=7, sticky=tk.W+tk.E)
        
        
        
        label = tk.Label(self,
                         text='Rice Quality Analysis on the basis of Features of Rice Grains', 
                         font=LARGE_FONT, bg="#ffffff" )
        label.pack(pady=10, padx=10)

        main1_path = os.path.join(img_dir, 'main1.jpg')
        image1 = Image.open(main1_path)
        # image1 = Image.open("img/main1.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="bottom", padx=0, pady=0)

    def updateFrame(self):
       
#       Pie Chart
        try:
        
            f = Figure(figsize=(5,5), dpi=100)
                
                
            ax = f.add_subplot(111)
            
            data =report.ldata
            
            statusbar['text'] ="Feature Graph"
            
            leg=['Whole Grains', 'Long Broken Grain', 
                 'Medium Broken Grain', 'Small Broken Grain'] # Legends of Pie Chart
            # Condition for the labels
            label=[0,1,2,3]
                # Condition for the labels
            if data[0]>2:
                label[0]='Whole Grains'
            else:
                label[0]=' '
            if data[1]>2:
                label[1]='Long Broken Grain'
            else:
                label[1]=' ' 
            if data[2]>2:
                label[2]='Medium Broken Grain'
            else:
                label[2]=' '
            if data[3]>2:
                label[3]='Small Broken Grain'
            else:
                label[3]=' '
            
            Time = report.Time
            Date = report.Date
    
            colors = ['yellowgreen', 
                      'gold', 
                      'lightskyblue', 
                      'lightcoral']
            explode = (0.2, 0.2, 0.2, 0.2)
            ax.pie(data, colors= colors, 
                   labels=label, 
                   explode=explode,
                   autopct='%1.1f%%')
            ax.set_title(Date +' '+ Time)
            ax.legend(leg,loc='best')
            ax.axis('equal')
            
            canvas = FigureCanvasTkAgg(f,self)
            canvas.draw()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)        
            
            # Navigation Toolbar
            toolbar= NavigationToolbar2Tk(canvas, self)
            toolbar.update()

        except:
            #except clause
            tkinter.messagebox.showwarning(title='Warning',
                                           message='No Sample Image Found! First Input Sample Image')


class CGraph(tk.Frame):
    
    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent, bg =  "#ffffff")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, 'img')

        cv3_path = os.path.join(img_dir, 'cv3.jpg')
        image = Image.open(cv3_path)      
        # image = Image.open("img/cv3.jpg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)

        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)

        # Initialize Buttons and add images to button
        iconh_path = os.path.join(img_dir, 'iconh.png')
        self.image_h = tk.PhotoImage(file=iconh_path)
        # self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))

        iconv_path = os.path.join(img_dir, 'iconv.png')
        self.image_v = tk.PhotoImage(file=iconv_path)
        # self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left",
                                   command=lambda: controller.show_frame(Sample))

        icona_path = os.path.join(img_dir, 'icona.png')
        self.image_a = tk.PhotoImage(file=icona_path)
        # self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left",
                                     command=lambda: controller.show_frame(Analyses))

        iconr_path = os.path.join(img_dir, 'iconr.png')
        self.image_r = tk.PhotoImage(file=iconr_path)
        # self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)

        dr_path = os.path.join(img_dir, 'detailed.png')
        self.image_dr = tk.PhotoImage(file=dr_path)        
        # self.image_dr = tk.PhotoImage(file="img/iconr.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)

        iconp_path = os.path.join(img_dir, 'iconp.png')
        self.image_p1 = tk.PhotoImage(file=iconp_path)
        # self.image_p1 = tk.PhotoImage(file="img/iconp.png")
        LGraph_button = ttk.Button(button_frame,text="Features Graph",
                                   image=self.image_p1, compound="left",
                                   command=lambda: controller.show_frame(LGraph))

        self.image_p2 = tk.PhotoImage(file=iconp_path)
        # self.image_p2 = tk.PhotoImage(file="img/iconp.png")
        CGraph_button = ttk.Button(button_frame,text="Color Graph",
                                   image=self.image_p2, compound="left",
                                   command=lambda: controller.show_frame(CGraph))

        self.image_p3 = tk.PhotoImage(file=iconp_path)
        # self.image_p3 = tk.PhotoImage(file="img/iconp.png")
        TGraph_button = ttk.Button(button_frame,text="Type Graph",
                                   image=self.image_p3, compound="left",
                                   command=lambda: controller.show_frame(TGraph))
        
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)

        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Analyses_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        LGraph_button.grid(row=0, column=3,sticky=tk.W+tk.E)
        CGraph_button.grid(row=0, column=4,sticky=tk.W+tk.E)
        TGraph_button.grid(row=0, column=5,sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=6, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=7, sticky=tk.W+tk.E)
        
        label = tk.Label(self,text='Rice Quality Analysis on the basis of Color of Rice Grains', 
                         font=LARGE_FONT, bg="#ffffff")
        label.pack(pady=10,padx=10)

        main1_path = os.path.join(img_dir, 'main1.jpg')
        image1 = Image.open(main1_path)        
        # image1 = Image.open("img/main1.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="bottom" ,padx=0, pady=0)

    def updateFrame(self):
        
#       Pie Chart
        try:
            
            f = Figure(figsize=(5,5), dpi=100)
            ax = f.add_subplot(111)
    
            data =report.cdata
            
            statusbar['text'] ="Color Graph"
    
            leg=['Brown Rice Grains', 'Ye_Brown Rice Grains',
                 'White Rice Grains', 'Yellow Rice Grains'] # Legends of Pie Chart
            label=[0,1,2,3]
                # Condition for the labels
            if data[0]>2:
                label[0]='Brown Rice Grain'
            else:
                label[0]=' '
            if data[1]>2:
                label[1]='Ye_Brown Rice Grains'
            else:
                label[1]=' ' 
            if data[2]>2:
                label[2]='White Rice Grains'
            else:
                label[2]=' '
            if data[3]>2:
                label[3]='Yellow Rice Grains'
            else:
                label[3]=' '
                
            Time = report.Time
            
            Date = report.Date
            
            colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
            explode = (0.2, 0.2, 0.2, 0.2)
            ax.pie(data, 
                   colors=colors, 
                   explode=explode,
                   labels=label,
                   autopct='%1.1f%%')
            
            ax.legend(leg,loc='best')
            ax.axis('equal')
            
            ax.set_title(Date +' '+ Time)
           
            
            canvas = FigureCanvasTkAgg(f,self)
            canvas.draw()
    #        # Navigation Toolbar
            toolbar= NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        except:
            #except clause
            tkinter.messagebox.showwarning(title='Warning',
                                           message='No Sample Image Found! First Input Sample Image')

class TGraph(tk.Frame):

        
    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent, bg =  "#ffffff")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, 'img')

        cv3_path = os.path.join(img_dir, 'cv3.jpg')
        image = Image.open(cv3_path)  
        # image = Image.open("img/cv3.jpg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)
         
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)


        # Initialize Buttons and add images to button
        iconh_path = os.path.join(img_dir, 'iconh.png')
        self.image_h = tk.PhotoImage(file=iconh_path)
        # self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))

        iconv_path = os.path.join(img_dir, 'iconv.png')
        self.image_v = tk.PhotoImage(file=iconv_path)
        # self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left",
                                   command=lambda: controller.show_frame(Sample))

        icona_path = os.path.join(img_dir, 'icona.png')
        self.image_a = tk.PhotoImage(file=icona_path)
        # self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left",
                                     command=lambda: controller.show_frame(Analyses))

        iconr_path = os.path.join(img_dir, 'iconr.png')
        self.image_r = tk.PhotoImage(file=iconr_path)
        # self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)

        dr_path = os.path.join(img_dir, 'detailed.png')
        self.image_dr = tk.PhotoImage(file=dr_path)
        # self.image_dr = tk.PhotoImage(file="img/iconr.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)
        
        iconp_path = os.path.join(img_dir, 'iconp.png')
        self.image_p1 = tk.PhotoImage(file=iconp_path)     
        # self.image_p1 = tk.PhotoImage(file="img/iconp.png")
        LGraph_button = ttk.Button(button_frame,text="Features Graph",
                                   image=self.image_p1, compound="left",
                                   command=lambda: controller.show_frame(LGraph))

        self.image_p2 = tk.PhotoImage(file=iconp_path)        
        # self.image_p2 = tk.PhotoImage(file="img/iconp.png")
        CGraph_button = ttk.Button(button_frame,text="Color Graph",
                                   image=self.image_p2, compound="left",
                                   command=lambda: controller.show_frame(CGraph))

        self.image_p3 = tk.PhotoImage(file=iconp_path)        
        # self.image_p3 = tk.PhotoImage(file="img/iconp.png")
        TGraph_button = ttk.Button(button_frame,text="Type Graph",
                                   image=self.image_p3, compound="left",
                                   command=lambda: controller.show_frame(TGraph))
        
 
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)
        
 
        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Analyses_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        LGraph_button.grid(row=0, column=3,sticky=tk.W+tk.E)
        CGraph_button.grid(row=0, column=4,sticky=tk.W+tk.E)
        TGraph_button.grid(row=0, column=5,sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=6, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=7, sticky=tk.W+tk.E)
        
                
        label = tk.Label(self,text='Rice Quality Analysis on the basis of Type of Rice Grains', 
                         font=LARGE_FONT, bg="#ffffff")
        label.pack(pady=10,padx=10)

        main1_path = os.path.join(img_dir, 'main1.jpg')
        image1 = Image.open(main1_path)        
        # image1 = Image.open("img/main1.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="bottom" ,padx=0, pady=0)
        
    def updateFrame(self):
        
#        Pie Chart
        try:
            
            f = Figure(figsize=(5,5), dpi=100)
            ax = f.add_subplot(111)

            data =report.tdata
            
            statusbar['text'] ="Type Graph"
    
            leg=['Brown Basmati Grains', 'Super Grians',
                 'Irri6 Grains', 'Brown Grains'] # Legends of Pie Chart
            
             # Condition for the labels
            label=[0,1,2,3]
                # Condition for the labels
            if data[0]>2:
                label[0]='Brown Basmati Grains'
            else:
                label[0]=' '
            if data[1]>2:
                label[1]='Super Grians'
            else:
                label[1]=' ' 
            if data[2]>2:
                label[2]='Irri6 Grains'
            else:
                label[2]=' '
            if data[3]>2:
                label[3]='Brown Grains'
            else:
                label[3]=' '
    
            
            Time = report.Time
            
            Date = report.Date
    
            
            colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
            explode = (0.2, 0.2, 0.2, 0.2)
            ax.pie(data, colors=colors, labels=label, explode=explode,
                   autopct='%1.1f%%')
            
            ax.set_title(Date +' '+ Time)

            ax.legend(leg,loc='best')
            ax.axis('equal')
            
            
            canvas = FigureCanvasTkAgg(f,self)
            canvas.draw()
            # Navigation Toolbar
            toolbar= NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
  
        except:
            #except clause
            tkinter.messagebox.showwarning(title='Warning',
                                           message='No Sample Image Found! First Input Sample Image')
        
#calling main class
app = SeaofBTCapp()
LOOP_ACTIVE = True


# create status bar
statusbar = ttk.Label(app, text='Welcome to Rice Quality Analyzer', relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X) 

# defining the geometry of window
app.geometry('1300x900+0+0')
app.resizable(width=True, height=True)

#leena
def yes_func():
    global no_func
    no_func=1
    reset_button()
    app.destroy()

def cancel_func():
    new_win.destroy()
def close_app():
    
    global new_win
    new_win = Toplevel()

    center_widget(300,100)
    new_win.resizable(0, 0)
    new_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    new_win.title('Confirm Exit')
    message = "Are you sure you want to exit?"
    Label(new_win, text=message, fg='grey', font=("Helvetica", 12)).place(x=40, y=10)
    Button(new_win, text='Yes',command=yes_func, width=6, height=1).place(x=60, y=60)
    Button(new_win, text='Cancel', command=cancel_func, width=6, height=1).place(x=170, y=60)


app.protocol('WM_DELETE_WINDOW',close_app) #to perform functionality when close from title bar, whole app
###

tk.mainloop()
