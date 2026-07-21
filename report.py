# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:27:31 2018

@author: Ahsan, Muzammil, Leena
"""

######### This file is for 10g test ##############


# import the necessary packages

from __future__ import division
from reportlab.pdfgen import canvas
from reportlab.platypus import *
from reportlab.rl_config import defaultPageSize
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from bidi.algorithm import get_display
from rtl import reshaper
from reportlab.platypus import SimpleDocTemplate, Paragraph
from textwrap3 import wrap
from reportlab.graphics.charts.legends import Legend
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.colors import black, white
from reportlab.graphics.charts.textlabels import Label
from PIL import Image, ImageTk, ImageEnhance
import os
import numpy as np
import tensorflow as tf
from keras._tf_keras.keras.models import load_model
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import platform_utils

#leena
screen_width, screen_height = platform_utils.get_screen_size()
import globals
###


# ---------------------------------------------------------------------------
# Report Writing
# Report Writing
# ---------------------------------------------------------------------------

# Checking if 100 grains are there or not on the scanner

def calculate_no_of_grains(objects):
    print("Checking number of grains")
    print("The number of grains are:", len(objects))
    calculate_no_of_grains.no_of_grains = len(objects)
    return(calculate_no_of_grains.no_of_grains)

    
# Getting user input (in mm) for broken size calculation
def get_user_input(x1):
    if x1 == "":
        #global no_user_input
        globals.no_user_input=0
        print("The user input is: empty")
    else:
        #global no_user_input
        globals.no_user_input=1
        print("The user input is:",x1 ,"mm")
        get_user_input.result1 = x1
        

#leena
#these functions to get user input
#for long broken maximum and minimum
def get_input_LongBroken(x3_longBrokenMax, x4_longBrokenMin):
    get_input_LongBroken.Max = x3_longBrokenMax
    get_input_LongBroken.Min = x4_longBrokenMin
    #print("long broken")

#for medium broken max and min
def get_input_MediumBroken(x5_MediumBrokenMax, x6_MediumBrokenMin):
    get_input_MediumBroken.Max = x5_MediumBrokenMax
    get_input_MediumBroken.Min = x6_MediumBrokenMin
    #print("Medium broken")

#for small broken max and min
def get_input_SmallBroken(x7_SmallBrokenMax, x8_SmallBrokenMin):
    get_input_SmallBroken.Max = x7_SmallBrokenMax
    get_input_SmallBroken.Min = x8_SmallBrokenMin
    #print("Small broken")

#######


#leena
#to get user desired data to be add on report
def get_sampleNo(sampleNo):
    globals.called=1
    if sampleNo == "":
        get_sampleNo.input="-"
    else:
        get_sampleNo.input = sampleNo

def get_date(date):
    globals.called=1
    if date == "":
        get_date.input="-"
    else:
        get_date.input = date

def get_day(day):
    globals.called=1
    if day == "":
        get_day.input="-"
    else:
        get_day.input = day

def get_arrivalNo(arrivalNo):
    globals.called=1
    if arrivalNo == "":
        get_arrivalNo.input="-"
    else:
        get_arrivalNo.input = arrivalNo

def get_partyName(partyName):
    globals.called=1
    if partyName == "":
        get_partyName.input="-"
    else:
        get_partyName.input = partyName

def get_vehicleNo(vehicleNo):
    globals.called=1
    if vehicleNo == "":
        get_vehicleNo.input="-"
    else:
        get_vehicleNo.input = vehicleNo

def get_riceType(riceType):
    globals.called=1
    if riceType == "":
        get_riceType.input="-"
    else:
        get_riceType.input = riceType

def get_moisture(moisture):
    globals.called=1
    if moisture == "":
        get_moisture.input="-"
    else:
        get_moisture.input = moisture

def get_look(look):
    globals.called=1
    if look == "":
        get_look.input="-"
    else:
        get_look.input = look

####
    
### Getting user input (in %) for broken size calculation
##def get_user_input2(x2):
##    print("The user input is:",x2 ,"%")
##    get_user_input2.result2 = x2


def gen_report(objects,S_Report):
    import time

    gtype = [0,0,0,0]
    global ldata, cdata, tdata, Date, Time
    head = 0
    long = 0
    med = 0
    small = 0

    ## Making the logic of weighted average for head rice & broken rice ##
    ## Initializing variables ##
    #global broken_weight, final_weight
    
    head_weight = []
    broken_rice_weight = []
    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []
    head_rice = []
    broken_rice = []

    #leena
    long_broken=[]
    med_broken = []
    small_broken = []
    

    long_broken_list=[]
    medium_broken_list=[]
    small_broken_list = []
    
    long_broken_weight = []
    medium_broken_weight = []
    small_broken_weight = []
    
    total_long_broken_weight=0
    total_medium_broken_weight=0
    total_small_broken_weight=0
    

    if globals.called != 1:
        #if values are empty in that case
        get_sampleNo.input="-"
        get_date.input="-"
        get_day.input="-"
        get_arrivalNo.input="-"
        get_partyName.input="-"
        get_vehicleNo.input="-"
        get_riceType.input="-"
        get_moisture.input="-"
        get_look.input="-"
        ##

    
    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c=canvas.Canvas(S_Report,DefaultPageSize)

    #leena
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(base_dir, 'img')
    
    img = os.path.join(img_dir, 'header.jpg')
    # img="img/header.jpg"
    
    #path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img,1,640,width=650,height=150) 
    ##
    
    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    now.strftime("%A")
    date= now.strftime("%d-%m-%Y")
    time= now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" %time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" %date
    
    total_grains=len(objects)
    
    avg_length = float(round(sum(x['Length'] for x in objects)/len(objects),3))
    avg_width = float(round(sum(x['Width'] for x in objects)/len(objects),2))
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)
    

    for i in objects:
       
        
        # Calculations for whole/broken ratio

         #(calculate_value.result3 == 'No-AGL') and   
        if ( len(get_user_input.result1) != 0):
            
            #print("The user input for mm field exists. Not taking AGL as reference")
            #print("The input variable is: ",get_user_input.result1)
            #print("The length of variable is: ",len(get_user_input.result1))
            global x
            x = get_user_input.result1
            #print("\n\n\n")
            if (float(i['Length']) >= float((x))):
                #print( "{} >= {}".format(float(i['Length']), float((x))) )
                head_rice.append(i)
            elif(float(i['Length']) < float((x))):
                #print( "{} < {}".format(float(i['Length']), float((x))) )
                broken_rice.append(i)
            #print("\n\n\n")
                  
##                             
##         #(calculate_value.result3 == 'AGL') and len(get_user_input2.result2) != 0
##        elif ( (get_user_input.result1) == "" ):
##        
##            #print("The user input for % field exists. Taking AGL as reference")
##            
##            from reportnew import AGL
##            
##            temp_AGL = AGL
##            #print("100 Grain test ran",temp_AGL)
##        
##            
##            x = float(get_user_input2.result2)/float(100)
##            #print("The percentage is:", x)
##            #j = (float(avg_length)*float(x))
##            j = (float(temp_AGL)*float(x))
##            
##            if (float((i['Length'])) >= (j)):
##                head_rice.append(i)
##            elif(float((i['Length'])) < (j)):
##                broken_rice.append(i)
           
            #and (get_user_input2.result2) == ""
        elif ((get_user_input.result1) == "" ):
        
            #print("The user inputs for both fields do not exist. By defaul input is 75%")
            
            x = 3/4
            y = 1/2
            z = 1/4
        
            #print(x,y,z)

            if (i['Length'] >= avg_length*(x)):
                head_rice.append(i)
            elif((i['Length'] < avg_length*(x)) and (i['Length'] > avg_length*(y))):
                broken_rice.append(i)
            elif((i['Length'] <= avg_length*(y)) and (i['Length'] > avg_length*(z))):
                broken_rice.append(i)
            elif(i['Length'] <= (z)):
                broken_rice.append(i) 
    
        
    ## Making the logic of weighted average for head rice & broken rice ##
                          ##   Start  ##
        
    #final_weight = 0
    
    #print("This is head rice array items",head_rice)
    #print("This is broken rice array items",broken_rice)


    ####leena
    if broken_rice:
        #print("broken rice list here")
        #print(broken_rice)
        for brokenRice_element in broken_rice:
            if not get_input_LongBroken.Max == "" or not get_input_LongBroken.Min == "":
                if(float(get_input_LongBroken.Max) >= brokenRice_element["Length"] >= float(get_input_LongBroken.Min) ):
                    #print( "{} >= {} >= {}".format(float(get_input_LongBroken.Max), brokenRice_element["Length"] ,float(get_input_LongBroken.Min)))
                    #print("long broken rice detected")
                    long_broken_list.append(brokenRice_element)
                    
            if not get_input_MediumBroken.Max == "" or not get_input_MediumBroken.Min == "":
                if( float(get_input_MediumBroken.Max) >= brokenRice_element["Length"] >= float(get_input_MediumBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_MediumBroken.Max), brokenRice_element["Length"] ,float(get_input_MediumBroken.Min)))
                    #print(" Medium broken rice detected")
                    medium_broken_list.append(brokenRice_element) #if particular item need to be added then brokenRice_element["Length"]
                    
            if not get_input_SmallBroken.Max == "" or not get_input_SmallBroken.Min == "":
                if( float(get_input_SmallBroken.Max) >= brokenRice_element["Length"] >= float(get_input_SmallBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_SmallBroken.Max), brokenRice_element["Length"] ,float(get_input_SmallBroken.Min)))
                    #print(" Small broken rice detected")
                    small_broken_list.append(brokenRice_element)
    ##############
    
    # Ahsan adding head_rice AGL in report
    
    head_rice_AGL = float(round(sum(x['Length'] for x in head_rice)/len(head_rice),3))
    head_rice_AGL = head_rice_AGL
    print("This is head_rice AGL", head_rice_AGL)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    w_model_dir = os.path.join(base_dir, 'w.h5')
    
    model = load_model(w_model_dir)
    # model = load_model('D:\\NCAI\\Rice for git\\w.h5')
    
    for i in range(0,len(head_rice)-1):
       #print("\n\n\nThis is first element's Length & Width of head_rice",head_rice[i]["Length"],head_rice[i]["Width"])
       #global head_weight
       data = np.array([[float(head_rice[i]["Length"]),float(head_rice[i]["Width"])]])
    #  nm = model.predict([[float(head_rice[i]["Length"]),float(head_rice[i]["Width"])]])
       nm = model.predict(data)
       head_weight.append(nm)
       #head_weight.append(round((((-0.00860)+(0.00167*head_rice[i]["Length"]))+(0.00663*head_rice[i]["Width"])),5)) Muzammil commented
       #head_weight.append(round((((-0.00860)+(0.00188*head_rice[i]["Length"]))+(0.00680*head_rice[i]["Width"])),5))old
       
    #total_head_weight = float(round(sum(head_weight),3))
    total_head_weight = float(sum(head_weight))
    #print("\n\nThis is total weight of head_rice",total_head_weight)

    for i in range(0,len(broken_rice)-1):
        data_1 = np.array([[float(broken_rice[i]["Length"]),float(broken_rice[i]["Width"])]])
        # nm1 = model.predict([[float(broken_rice[i]["Length"]),float(broken_rice[i]["Width"])]])
        nm1 = model.predict(data_1)
        broken_rice_weight.append(nm1)
        #broken_rice_weight.append(round((((-0.00860)+(0.00167*broken_rice[i]["Length"]))+(0.00663*broken_rice[i]["Width"])),5))

    total_brokenRice_weight = float(sum(broken_rice_weight))
    #print("\n\nThis is total weight of long_broken_rice",total_brokenRice_weight)
    
    Total_new_weight = float(total_head_weight + total_brokenRice_weight)
    #print("This is total_new_weight",Total_new_weight)
    

    #leena
    if long_broken_list:    #if the list is not empty then do following
        for i in range(0,len(long_broken_list)-1):
            data_2 = np.array([[float(long_broken_list[i]["Length"]),float(long_broken_list[i]["Width"])]])
            long_broken_weight.append(model.predict(data_2))
            #long_broken_weight.append(round((((-0.00994)+(0.00167*long_broken_list[i]["Length"]))+(0.00663*long_broken_list[i]["Width"])),5))
            
        total_long_broken_weight = float(sum(long_broken_weight))
        #print("This is total_new_weight of long broken ",total_long_broken_weight)

    if medium_broken_list:   
        for i in range(0,len(medium_broken_list)-1):
            data_3 = np.array([[float(medium_broken_list[i]["Length"]),float(medium_broken_list[i]["Width"])]])
            medium_broken_weight.append(model.predict(data_3))
            # medium_broken_weight.append(model.predict([[float(medium_broken_list[i]["Length"]),float(medium_broken_list[i]["Width"])]]))
            #medium_broken_weight.append(round((((-0.00994)+(0.00167*medium_broken_list[i]["Length"]))+(0.00663*medium_broken_list[i]["Width"])),5))

        total_medium_broken_weight = float(sum(medium_broken_weight))
        #print("This is total_new_weight of medium broken",total_medium_broken_weight)

    if small_broken_list:   
        for i in range(0,len(small_broken_list)-1):
            data_4 = np.array([[float(small_broken_list[i]["Length"]),float(small_broken_list[i]["Width"])]])
            small_broken_weight.append(model.predict(data_4))
            # small_broken_weight.append(model.predict([[float(small_broken_list[i]["Length"]),float(small_broken_list[i]["Width"])]]))
            #small_broken_weight.append(round((((-0.00994)+(0.00167*small_broken_list[i]["Length"]))+(0.00663*small_broken_list[i]["Width"])),5))

        total_small_broken_weight = float(sum(small_broken_weight))
        #print("This is total_new_weight of small broken",total_small_broken_weight)    
   #####
            
       
       
    #print("\n\n\nEnd of for loop")
    
    ## Making the logic of weighted average for head rice & broken rice ##
                          ##   End  ##
                          
                          
    
    ## Making the logic of weighted average for yellow rice ##
                          ##   Start  ##
                          
    from analysis import yellow_length, yellow_width
    for i,j in zip(yellow_length, yellow_width):
        yw = np.array([[float(i),float(j)]])
        yellow_weight.append(model.predict(yw))
        # yellow_weight.append(model.predict([[float(i),float(j)]]))
            #yellow_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))
            
    #total_yellow_weight = round(sum(yellow_weight),3)
    total_yellow_weight = round(float(sum(yellow_weight)),3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)   


    ## Making the logic of weighted average for yellow rice ##
                          ##   End  ##
                          
    
    ## Making the logic of weighted average for damage rice ##
                          ##   Start  ##
                          
    from analysis import damage_length, damage_width
    for i,j in zip(damage_length, damage_width):
            dw = np.array ([[float(i),float(j)]])
            damage_weight.append(model.predict(dw))
            # damage_weight.append(model.predict([[float(i),float(j)]]))
            #damage_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))
            
    total_damage_weight = round(float(sum(damage_weight)),3)
    #print("\n\nThis is total weight of damage",total_damage_weight)
    
        ## Making the logic of weighted average for damage rice ##
                          ##   End  ##
                          
        ## Making the logic of weighted average for chalky rice ##
                          ##   Start  ##
                          
    from analysis import chalky_length, chalky_width
    for i,j in zip(chalky_length, chalky_width):
            cw = np.array([[float(i),float(j)]])
            chalky_weight.append(model.predict(cw))
            # chalky_weight.append(model.predict([[float(i),float(j)]]))
            #chalky_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))
            
    total_chalky_weight = round(float(sum(chalky_weight)),3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)
    
        ## Making the logic of weighted average for chalky rice ##
                          ##   End  ##  
    
        ## Making the logic of weighted average for yellow rice ##
                          ##   Start  ##
                          
    from analysis import paddy_length, paddy_width
    for i,j in zip(paddy_length, paddy_width):
            pw = np.array([[float(i),float(j)]])
            paddy_weight.append(model.predict(pw))
            # paddy_weight.append(model.predict([[float(i),float(j)]]))
            #paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))
            
    total_paddy_weight = round(float(sum(paddy_weight)),3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)   


    ## Making the logic of weighted average for yellow rice ##
                          ##   End  ##
    
    head=round(len(head_rice))
    
    long=round(len(broken_rice))
    
               
    #Report generation with mm Reference

    #(calculate_value.result3 == 'No-AGL') and 
    if (len(get_user_input.result1) != 0):

        
        from analysis import yellow_count,chalky_count, new_damage1_count, paddy_count
        yellow_percentage = round(float(total_yellow_weight/Total_new_weight),2)
        chalky_percentage = round(float(total_chalky_weight/Total_new_weight),2)
        damage_percentage = round(float(total_damage_weight/Total_new_weight),2)
        paddy_percentage = round(float(total_paddy_weight/Total_new_weight),2)
        

        #leena
        data3=[['Sample No',get_sampleNo.input],
               ['Date', get_date.input],
               ['Time',get_day.input],
               ['Arrival No',get_arrivalNo.input],
               ['Party Name',get_partyName.input],
               ['Vehicle No',get_vehicleNo.input],
               ['Rice Type',get_riceType.input],
               ['Moisture',get_moisture.input],
               ['Look', get_look.input]
              ]
        ###
        #removing 0.14 in agl
        data2=[[Time , Date],[' Variables        ',' Values  '], ['Average Length (10g) (mm)      ',round(avg_length,3)],
               ['Average Width (10g) (mm)        ' ,round(avg_width,3)],
               ['Head Rice AGL       ' ,round(head_rice_AGL,3)],
               ['Whole Grain (qty)      ',head],
               ['Whole Grain Weight (gm)     ',round(total_head_weight,3)],
               ['Broken Grain   (qty)      ',long],
               ['Broken Grain Weight (gm)     ',round(total_brokenRice_weight,3)],
               ['Total Grains (qty)    ', total_grains],
               ['Reference Value (100g) (mm)',    x],
               ['Yellow Grains (qty)    ', yellow_count],
               ['Yellow Grains Weight (gm)    ', total_yellow_weight],
               ['Yellow Percengate (%)    ', round((yellow_percentage*100),3)],
               ['Chalky Grains (qty)    ', chalky_count],
               ['Chalky Grains Weight (gm)    ', total_chalky_weight],
               ['Chalky Percengate (%)    ', round((chalky_percentage*100),3)],
               ['Damage Grains (qty)    ', new_damage1_count],
               ['Damage Grains Weight (gm)    ', total_damage_weight],
               ['Damage Percengate (%)    ', (damage_percentage*100)],
               ['Paddy Grains (qty)    ', paddy_count],
               ['Paddy Grains Weight (gm)    ', total_paddy_weight],
               ['Paddy Percengate (%)    ', (paddy_percentage*100)],
               ['Total Weight (gm)',    round(Total_new_weight,3)],
               ['Broken Rice Percengate',    round(((total_brokenRice_weight/Total_new_weight)*100),3)],
               ['Long Broken Weight', round(total_long_broken_weight,3)],
               ['Medium Broken Weight', round(total_medium_broken_weight,3)],
               ['Small Broken Weight', round(total_small_broken_weight,3)]
               ]
               
               
    table2 = Table(data2, colWidths=[170,150], rowHeights=22.1)#rowHeights=24.2
    table2.setStyle(TableStyle([
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ('FONTSIZE',(0,0),(-1,-1),12)
                               ]))

    
    #leena
    ldata=(len(head_rice), len(broken_rice), len(med_broken), len(small_broken))
    ####

    cdata=(0, 1, 2, 3)
    tdata=(gtype[0], gtype[1], gtype[2], gtype[3])

    
    table2.wrapOn(c, 20, 400)#20,400, to set 
    table2.drawOn(c,20,15)  #c,20,25,,, to set report alignment increase or decrease the last value
 

    #leena
    #for user defined values
    table3 = Table(data3, colWidths=[100,130], rowHeights=30)
    table3.setStyle(TableStyle([
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ('FONTSIZE',(0,0),(-1,-1),12)
                               ]))

    
    table3.wrapOn(c, 20, 400)#20,400
    table3.drawOn(c,360,360)  #c,160,260  
    ##
 
    c.save()
   
