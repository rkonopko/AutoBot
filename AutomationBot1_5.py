####################################
# AutomationBot 1.5                #
# Created by: Robert Konopko       #
# Last Updated 1/21/25             #
####################################


import time
import pyautogui
import customtkinter
import tkinter as tk
from tkinter import ttk


# Sets theme and size of Main GUI WIndow ########################

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title('AutomationBot')
root.geometry('380x180')

##########################################################################################################################################################################################
######## Functions #######################################################################################################################################################################
##########################################################################################################################################################################################

# Check for Image onscreen ################################################################################################
def CheckForImage(image,conf,count):
   
    loop = 0
    counter = 0
    
    while loop == 0:
        
        counter +=1

        if pyautogui.locateOnScreen(image, confidence=conf) != None: 

            print('Image found returning 1')
            loop = 1
            return(1)
        
        elif counter >= count:
            print('Image not found. exiting, return 2')
            loop = 1
            return(2)

        else:
            print('loop count:')
            print(counter)
            time.sleep(1)

#################################################################################################################################################################

#### Updates text in conosle text box and can add a delay or 0 for none

def UpdateConsoleText(ConsoleName,TextToInsert,Delay):

    ConsoleName.insert(tk.END,TextToInsert)
    time.sleep(Delay)
    ConsoleName.update()



#### Check for image then move to image center than click ########################################
## Image: file location of the image.
## Confidence: how accurate the image reading is in prectantage based on pixels.
## Counter: how many tries before it exits.

# MoveToImageCenter Single Click ################################################################################################
def MoveToImageCenter_1clk(image,conf,count):
   
    loop = 0
    counter = 0
    
    while loop == 0:
        
        try:
            pic_pos = pyautogui.locateOnScreen(image, confidence=conf)
            pic_cent = pyautogui.center(pic_pos)
            time.sleep(.5)
            pyautogui.moveTo(pic_cent)
            time.sleep(1)
            pyautogui.click()
            time.sleep(.2)
            
            loop = 1
            return(1)
        
        except pyautogui.ImageNotFoundException:
            time.sleep(.8)
            print('Image not found, loop: ', counter)

        except:
            print("Other error")

        if counter == count:
            print("image not found exiting")
            loop = 1
            return(2)

        counter +=1


# MoveToImageCenter Double Click ################################################################################################
def MoveToImageCenter_2clk(image,conf,count):
   
    loop = 0
    counter = 0
    
    while loop == 0:
        
        try:
            pic_pos = pyautogui.locateOnScreen(image, confidence=conf)
            pic_cent = pyautogui.center(pic_pos)
            time.sleep(.5)
            pyautogui.moveTo(pic_cent)
            time.sleep(1)
            pyautogui.doubleClick()
            time.sleep(.2)
            
            loop = 1
            return(1)
        
        except pyautogui.ImageNotFoundException:
            time.sleep(.8)
            print('Image not found, loop: ', counter)

        except:
            print("Other error")

        if counter == count:
            print("image not found exiting")
            loop = 1
            return(2)

        counter +=1


#### Pin App to Taskbar default is D4 aka down 4 #########################################

def Pin2TaskbarD5(app_name):
    time.sleep(.5)
    pyautogui.press('win')
    time.sleep(.5)
    pyautogui.write(app_name, interval=.1)
    time.sleep(.5)
    pyautogui.press('right')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('enter')
    time.sleep(.5)

def Pin2TaskbarD4(app_name):
    time.sleep(.5)
    pyautogui.press('win')
    time.sleep(.5)
    pyautogui.write(app_name, interval=.1)
    time.sleep(.5)
    pyautogui.press('right')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('enter')
    time.sleep(.5)

def Pin2TaskbarD3(app_name):
    time.sleep(.5)
    pyautogui.press('win')
    time.sleep(.5)
    pyautogui.write(app_name, interval=.1)
    time.sleep(.5)
    pyautogui.press('right')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('enter')
    time.sleep(.5)

#### run CMD as user #########################################

def RunCMDasUser(user_cmd):
    time.sleep(.5)
    pyautogui.press('win')
    time.sleep(.3)
    pyautogui.write('cmd', interval=.1)
    time.sleep(.2)
    pyautogui.press('enter')
    time.sleep(3)
    print('running CMD as user')
    pyautogui.write(user_cmd, interval=.2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('exit', interval=.2)
    time.sleep(.5)
    pyautogui.press('enter')
    time.sleep(1)

#### run CMD as admin ############################################

def RunCMDasAdmin(adm_cmd):
    time.sleep(.5)
    pyautogui.press('win')
    pyautogui.write('cmd', interval=.1)
    pyautogui.press('right')
    time.sleep(.1)
    pyautogui.press('down')
    time.sleep(.1)
    pyautogui.press('enter')
    time.sleep(.1)
    pyautogui.press('left')
    time.sleep(.1)
    pyautogui.press('enter')
    print('running as admin')
    pyautogui.write(adm_cmd, interval=.05)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write('exit', interval=.2)
    time.sleep(.5)
    pyautogui.press('enter')

#### Get Resoloution #########################################

def GetRes():
    res = pyautogui.size()
    print("The current resolution is:")
    print(res)
    print(' ')

    if res[0] == 1920 and res[1] == 1080:
        print("Correct RES")
    else:
        print("Wrong RES")


##########################################################################################################################################################################################
#### End Global Functions #######################################################################################################################################################################
##########################################################################################################################################################################################


# UI Window ##############################################################################################################################################################

def UIwindow():
    
    def UIstart():
        print('UI Start')

        UIusername = UIusername1.get()
        UIpassword = UIpassword1.get()
        
        UIconsole_text.insert(tk.END,' ' + '\n')
        UIconsole_text.update()
        UIconsole_text.insert(tk.END,'Running UI Prep in:' + '\n')
        UIconsole_text.update()
        time.sleep(1)
        UIconsole_text.insert(tk.END,'5....' + '\n')
        UIconsole_text.update()
        time.sleep(1)
        UIconsole_text.insert(tk.END,'4...' + '\n')
        UIconsole_text.update()
        time.sleep(1)
        UIconsole_text.insert(tk.END,'3..' + '\n')
        UIconsole_text.update()
        time.sleep(1)
        UIconsole_text.insert(tk.END,'2.' + '\n')
        UIconsole_text.update()
        time.sleep(1)
        UIconsole_text.insert(tk.END,'1' + '\n')
        UIconsole_text.update()
        time.sleep(1)

        UIconsole_text.insert(tk.END,'Gathering Creds'+ '\n')
        UIconsole_text.insert(tk.END,UIusername + '\n')
        UIconsole_text.insert(tk.END,UIpassword + '\n')
        


    #####################################################################
    
    UIwindow = customtkinter.CTkToplevel(root)
    UIwindow .title('UI')
    UIwindow.geometry('620x360')


    # UI Frame 1&2 ##################################################################################################################
    UIframe12 = customtkinter.CTkFrame(master=UIwindow)
    UIframe12.pack(pady=10, padx=10, side='left', fill='both', expand=True)

    # UI Frame 1 ##################################################################################################################
    UIframe1 = customtkinter.CTkFrame(master=UIframe12)
    UIframe1.pack(pady=10, padx=10, side='bottom', fill='both', expand=True)
    
    chk_lst_clr = 'DarkOrange2'
    chk_lst_fnt = 'Georgia'

    UIchk1= customtkinter.CTkCheckBox(master=UIframe1, text='Ui Connect', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    UIchk1.pack(pady=5, padx=5, fill='both', expand=True)

    UIchk2 = customtkinter.CTkCheckBox(master=UIframe1, text='Email', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    UIchk2.pack(pady=5, padx=5, fill='both', expand=True)

    UIchk3= customtkinter.CTkCheckBox(master=UIframe1, text='Pin to Taskbar', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    UIchk3.pack(pady=5, padx=5, fill='both', expand=True)

    UIchk4 = customtkinter.CTkCheckBox(master=UIframe1, text='Run CMD', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    UIchk4.pack(pady=5, padx=5, fill='both', expand=True)

    UIchk5 = customtkinter.CTkCheckBox(master=UIframe1, text='CleanUp', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    UIchk5.pack(pady=5, padx=5, fill='both', expand=True)


    # UI Frame 2 ##################################################################################################################
    UIframe2 = customtkinter.CTkFrame(master=UIframe12)
    UIframe2.pack(pady=5, padx=5, side='top', fill='both', expand=True)

    UIusername1 = customtkinter.CTkEntry(master=UIframe2, placeholder_text='Username')
    UIusername1.pack(pady=5, padx=5, fill='both')

    UIpassword1 = customtkinter.CTkEntry(master=UIframe2, placeholder_text='Password')
    UIpassword1.pack(pady=5, padx=5, fill='both')

    UIbutton1 = customtkinter.CTkButton(master=UIframe2, text='Start', command=UIstart)
    UIbutton1.pack(pady=5, padx=5)

    # UI Frame 3 ##################################################################################################################
    UIframe3 = customtkinter.CTkFrame(master=UIwindow)
    UIframe3.pack(pady=5, padx=5, side='right', fill='both', expand=True)

    UIconsole_text = customtkinter.CTkTextbox(master=UIframe3, fg_color='black', text_color='deep sky blue', font=('Terminal',14))
    UIconsole_text.pack(pady=5, padx=5, fill='both', expand=True)
    UIconsole_text.insert('0.0','########## UI Bot ##########' + '\n')

##########################################################################################################################################################################################


####### SQ ##################################################################################################################################################################

######## SQ Global Variables ##########################################################################
###### folder path: r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\*********.png

#### GPedit Variables #########################################
global sq_gpedit_1
sq_gpedit_1 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\sq_gpedit_1.png'
global sq_gpedit_2
sq_gpedit_2 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\sq_gpedit_2.png'
global sq_gpedit_3
sq_gpedit_3 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\sq_gpedit_3.png'
global sq_gpedit_4
sq_gpedit_4 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\sq_gpedit_4.png'
global sq_gpedit_5
sq_gpedit_5 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\sq_gpedit_5.png'
global sq_gpedit_6
sq_gpedit_6 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\sq_gpedit_6.png'
global sq_gpedit_7
sq_gpedit_7 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\sq_gpedit_7.png'
global sq_gpedit_e
sq_gpedit_e = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\sq_gpedit_e.png'

#### Installs Folder Vars ############################################
global Ifolder
Ifolder = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\installs_folder.png'
global infolder
infolder = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\in_installs_folder.png'
global NetxFolder
NetxFolder = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\NetxFolder.png'
global VIPaFolder
VIPaFolder = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\VIPaFolder.png'

#### Installs Clicks Vars ###########################################
global netX_nxt
netX_nxt = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX_nxt.png'
global netX_accept
netX_accept = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX_accept.png'
global netX_any
netX_any = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX_any.png'
global netX_fin
netX_fin = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX_fin.png'
global netX_nxtv
netX_nxtv = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX_nxtv.png'

#### Installs Windows Vars ###########################################
global netX1
netX1 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX1.png'
global netX2
netX2 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX2.png'
global netX3
netX3 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX3.png'
global netX4
netX4 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX4.png'
global netX5
netX5 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX5.png'
global netX6
netX6 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX6.png'
global netX9
netX9 = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\netX9.png'

#### Outlook Vars ###########################################
global outlookIcon
outlookIcon = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\outlookIcon.png'
global outlook_username
outlook_username = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\outlook_username.png'
global outlook_sign_in_btn
outlook_sign_in_btn = r'C:\Users\Public\Desktop\BobbyBot_SQ\Images\outlook_sign_in_btn.png'

# Test Vars ###############################################################


# can be deleted:

global CMD
CMD = r'C:\Users\Rob\Desktop\Python\BobbyBot\Images\CMD.png'
#############################################################



########################################################################################################################################################

# SQ Window #####################################################################################################

def SQwindow():
    
    ### SQ Functions ########################################################################################
    
    ### Installs ####

    def installs():
        
        console_text.insert(tk.END,'Running Installs' + '\n')
        console_text.update()

        # check for installs folder on desktop and loops until found or 15 times
        MoveToImageCenter_2clk(Ifolder,.80,20)
        
        # check for NetX360 exe in folder and loops until found or 15 times
        MoveToImageCenter_2clk(NetxFolder,.80,15)

        MoveToImageCenter_1clk(netX1,.80,20)
        
        # waiting for 2nd installer window to show
        MoveToImageCenter_1clk(netX2,.80,10)
        
        MoveToImageCenter_1clk(netX_accept,.80,10)
    
        MoveToImageCenter_1clk(netX_nxt,.80,10)

        MoveToImageCenter_1clk(netX_any,.80,10)

        MoveToImageCenter_1clk(netX_nxt,.80,10)

        MoveToImageCenter_1clk(netX5,.80,10)

        MoveToImageCenter_1clk(netX_any,.80,10)

        MoveToImageCenter_1clk(netX_nxt,.80,10)

        MoveToImageCenter_1clk(netX_nxtv,.80,10)

        MoveToImageCenter_1clk(netX9,.80,99)

        console_text.insert(tk.END,'Installs complete' + '\n')
        console_text.update()
        print('Installs complete')

###### Gpedit settings Function #################################################

    def Gpedit():
    
        time.sleep(1)
        pyautogui.press('win')
        time.sleep(.3)
        pyautogui.write('gpedit.msc', interval=.1)
        time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(2)

        MoveToImageCenter_1clk(sq_gpedit_1,.80,10)

        MoveToImageCenter_2clk(sq_gpedit_2,.80,10)
        
        MoveToImageCenter_1clk(sq_gpedit_3,.80,10)

        time.sleep(1)
        pyautogui.write('win', interval=.1)
        time.sleep(1)

        MoveToImageCenter_2clk(sq_gpedit_4,.80,10)

        MoveToImageCenter_2clk(sq_gpedit_5,.80,10)
        time.sleep(1)

        MoveToImageCenter_1clk(sq_gpedit_e,.80,10)

        MoveToImageCenter_1clk(sq_gpedit_6,.80,10)

        MoveToImageCenter_1clk(sq_gpedit_7,.80,10)

        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.hotkey('alt', 'f4')
        
        console_text.insert(tk.END,'gpedit complete' + '\n')
        console_text.update()
        print('gpedit complete')


######### SQ Functions End #####################################################################

######### SQ Window ############################################################################

    def SQstart():
        
        ## Check off check box and update the UI

        SQchk1.select()
        SQchk1.update()
        time.sleep(1)
        SQchk1.deselect()
        SQchk1.update()

        ##############################################

        print('SQ Start')

        SQusername1 = SQusername.get()
        SQpassword1 = SQpassword.get()
        
        console_text.insert(tk.END,' ' + '\n')
        console_text.update()
        console_text.insert(tk.END,'Running SQ Prep in:' + '\n')
        console_text.update()
        time.sleep(1)
        console_text.insert(tk.END,'5....' + '\n')
        console_text.update()
        time.sleep(1)
        console_text.insert(tk.END,'4...' + '\n')
        console_text.update()
        time.sleep(1)
        console_text.insert(tk.END,'3..' + '\n')
        console_text.update()
        time.sleep(1)
        console_text.insert(tk.END,'2.' + '\n')
        console_text.update()
        time.sleep(1)
        console_text.insert(tk.END,'1' + '\n')
        console_text.update()
        time.sleep(1)

        console_text.insert(tk.END,'Gathering Creds'+ '\n')
        console_text.insert(tk.END,SQusername1 + '\n')
        console_text.insert(tk.END,SQpassword1 + '\n')

        # Main Funtions ###########

        GetRes()
        time.sleep(1)

        installs()
        time.sleep(2)

        RunCMDasUser(r'Powershell.exe -executionpolicy unrestricted -File "C:\Users\Public\Desktop\RunMe\SQ_PS.ps1"')
        time.sleep(1)
        print('Run Command step done')
        


        ##  Pin2Task()
        ## print('Pin to Taskbar complete')
        ## time.sleep(2)


        Gpedit()
        time.sleep(2)



        ## Outlook()



        print('SQ Prep Done *****')

### Main SQ Window ############################################################################################################################################
    
    SQwindow = customtkinter.CTkToplevel(root)
    SQwindow.title('SQ')
    SQwindow.geometry('620x360')


    # SQ Frame 1&2 ##################################################################################################################
    SQframe12 = customtkinter.CTkFrame(master=SQwindow)
    SQframe12.pack(pady=10, padx=10, side='left', fill='both', expand=True)

    # SQ Frame 1 ##################################################################################################################
    SQframe1 = customtkinter.CTkFrame(master=SQframe12)
    SQframe1.pack(pady=10, padx=10, side='bottom', fill='both', expand=True)
    
    chk_lst_clr = 'deep sky blue'
    chk_lst_fnt = 'Georgia'

    SQchk1= customtkinter.CTkCheckBox(master=SQframe1, text='Symantec', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    SQchk1.pack(pady=5, padx=5, fill='both', expand=True)

    SQchk2 = customtkinter.CTkCheckBox(master=SQframe1, text='Vip Access', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    SQchk2.pack(pady=5, padx=5, fill='both', expand=True)

    SQchk3= customtkinter.CTkCheckBox(master=SQframe1, text='Pin to Taskbar', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    SQchk3.pack(pady=5, padx=5, fill='both', expand=True)

    SQchk4 = customtkinter.CTkCheckBox(master=SQframe1, text='Outlook', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    SQchk4.pack(pady=5, padx=5, fill='both', expand=True)

    SQchk5 = customtkinter.CTkCheckBox(master=SQframe1, text='Gpedit', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    SQchk5.pack(pady=5, padx=5, fill='both', expand=True)

    # SQ Frame 2 ##################################################################################################################
    SQframe2 = customtkinter.CTkFrame(master=SQframe12)
    SQframe2.pack(pady=5, padx=5, side='top', fill='both', expand=True)

    SQusername = customtkinter.CTkEntry(master=SQframe2, placeholder_text='Username')
    SQusername.pack(pady=5, padx=5, fill='both')

    SQpassword = customtkinter.CTkEntry(master=SQframe2, placeholder_text='Password')
    SQpassword.pack(pady=5, padx=5, fill='both')

    SQbutton1 = customtkinter.CTkButton(master=SQframe2, text='Start', command=SQstart)
    SQbutton1.pack(pady=5, padx=5)

    # SQ Frame 3 ##################################################################################################################
    SQframe3 = customtkinter.CTkFrame(master=SQwindow)
    SQframe3.pack(pady=5, padx=5, side='right', fill='both', expand=True)

    console_text = customtkinter.CTkTextbox(master=SQframe3, fg_color='black', text_color='SpringGreen3', font=('Terminal',14))
    console_text.pack(pady=5, padx=5, fill='both', expand=True)
    console_text.insert('0.0','############## SQ Bot ##############' + '\n')


#####################################################################################################################################################################################

#####  EX Window    ####################################################################################################################################################################################

######## EX Global Variables ##########################################################################
###### folder path: r'C:\Temp\AutoBot\*********.png


#### Installer Bot #########################################
global iBot1
iBot1 = r'C:\Temp\iBot\iBot1.png'
global AutoBot2
iBot2 = r'C:\Temp\iBot\iBot2.png'
global iBot3
iBot3 = r'C:\Temp\iBot\iBot3.png'
global iBot4
iBot4 = r'C:\Temp\iBot\iBot4.png'
global iBot5
iBot5 = r'C:\Temp\iBot\iBot5.png'
global iBot6
iBot6 = r'C:\Temp\iBot\iBot6.png'
global iBot7
iBot7 = r'C:\Temp\iBot\iBot7.png'



def EXwindow():
    
    def InstallApp(LicenseKey):
        
        MoveToImageCenter_2clk(iBot1,.80,10)
        MoveToImageCenter_1clk(iBot7,.80,10)
        
        time.sleep(.5)
        pyautogui.write(LicenseKey, interval=.1)
        
        MoveToImageCenter_1clk(iBot2,.80,10)
        MoveToImageCenter_1clk(iBot3,.80,10)
        MoveToImageCenter_1clk(iBot4,.80,10)
        MoveToImageCenter_1clk(iBot5,.80,10)
        MoveToImageCenter_1clk(iBot6,.80,60)

        EXchk1.select()
        EXchk1.update()

    def EXstart():

        print("EX start")
        
        # Correct License key = AF7GB-HN8R6-DD9DS-DS8P0
        LicenseKey = EXkey.get()

        GetRes()

        UpdateConsoleText(EXconsole_text,' \n',0)
        UpdateConsoleText(EXconsole_text,'Starting in: \n',0)
        UpdateConsoleText(EXconsole_text,'5....\n',1)
        UpdateConsoleText(EXconsole_text,'4...\n',1)
        UpdateConsoleText(EXconsole_text,'3..\n',1)
        UpdateConsoleText(EXconsole_text,'2.\n',1)
        UpdateConsoleText(EXconsole_text,'1\n',1)
        UpdateConsoleText(EXconsole_text,'\n',0)

        UpdateConsoleText(EXconsole_text,'Running Install Exmaple \n',1)
        UpdateConsoleText(EXconsole_text,'\n',0)

        if EXchk1.get() == 1:
            UpdateConsoleText(EXconsole_text,'Checked off, skipping task\n',1)
            UpdateConsoleText(EXconsole_text,'\n',0)
        else:
            InstallApp(LicenseKey)

        time.sleep(2)

        UpdateConsoleText(EXconsole_text,'Running Pin to Taskbar \n',1)
        UpdateConsoleText(EXconsole_text,'\n',0)

        if EXchk2.get() == 1:
            UpdateConsoleText(EXconsole_text,'Checked off, skipping task\n',1)
            UpdateConsoleText(EXconsole_text,'\n',0)
        else:
            Pin2TaskbarD4('CMD')
            
            EXchk2.select()
            EXchk2.update()
        
        UpdateConsoleText(EXconsole_text,'Running unpin from Taskbar \n',1)
        UpdateConsoleText(EXconsole_text,'\n',0)

        if EXchk3.get() == 1:
            UpdateConsoleText(EXconsole_text,'Checked off, skipping task\n',1)
            UpdateConsoleText(EXconsole_text,'\n',0)
        else:
            Pin2TaskbarD4('CMD')

            EXchk3.select()
            EXchk3.update()

        pyautogui.press('esc') 

        UpdateConsoleText(EXconsole_text,'EX Prep done\n',0.2)
        UpdateConsoleText(EXconsole_text,'\n',0)

### EX Window ############################################################################################################################
   
    EXwindow = customtkinter.CTkToplevel(root)
    EXwindow .title('EX')
    EXwindow.geometry('620x270')



    # EX Frame 1&2 ##################################################################################################################
    EXframe12 = customtkinter.CTkFrame(master=EXwindow)
    EXframe12.pack(pady=10, padx=10, side='left', fill='both', expand=True)

    # EX Frame 1 ##################################################################################################################
    EXframe1 = customtkinter.CTkFrame(master=EXframe12)
    EXframe1.pack(pady=10, padx=10, side='bottom', fill='both', expand=True)


    chk_lst_clr = 'SkyBlue2'
    chk_lst_fnt = 'Georgia'

    EXchk1= customtkinter.CTkCheckBox(master=EXframe1, text='Install App', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    EXchk1.pack(pady=5, padx=5, fill='both', expand=True)

    EXchk2 = customtkinter.CTkCheckBox(master=EXframe1, text='Pin Icon', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    EXchk2.pack(pady=5, padx=5, fill='both', expand=True)

    EXchk3= customtkinter.CTkCheckBox(master=EXframe1, text='UnPin Icon', text_color=chk_lst_clr, font=(chk_lst_fnt,16))
    EXchk3.pack(pady=5, padx=5, fill='both', expand=True)


    # EX Frame 2 ##################################################################################################################
    EXframe2 = customtkinter.CTkFrame(master=EXframe12)
    EXframe2.pack(pady=5, padx=5, side='top', fill='both', expand=True)

    EXkey = customtkinter.CTkEntry(master=EXframe2, placeholder_text='License Key')
    EXkey.pack(pady=5, padx=5, fill='both')

    EXbutton1 = customtkinter.CTkButton(master=EXframe2, text='Start', command=EXstart)
    EXbutton1.pack(pady=5, padx=5)

    # EX Frame 3 ##################################################################################################################
    EXframe3 = customtkinter.CTkFrame(master=EXwindow)
    EXframe3.pack(pady=5, padx=5, side='right', fill='both', expand=True)

    EXconsole_text = customtkinter.CTkTextbox(master=EXframe3, fg_color='black', text_color='SeaGreen2', font=('Terminal',14))
    EXconsole_text.pack(pady=5, padx=5, fill='both', expand=True)
    EXconsole_text.insert('0.0','############## EX Bot #############' + '\n')






#####################################################################################################################################################################################


###########################
####### Main Window #################################################################################################################################################################
###########################

# Start Button text box ######################################################################

def start_type():

    print(EntryClientName.get())
    clientName = EntryClientName.get()

    match clientName:
        case 'SQ'|'sq':
            print('SQ choosen')
            SQwindow()
        
        case 'ex'|'EX'|'Example'|'example'|'eg.':
            EXwindow()

        case 'UI'|'ui':
            print('UI chosen')
            UIwindow()
        
        case _:
            print('No Valid option chosen')


# Start Button list ##########################################

def start_list():
    print(ClientDropDown.get())
    clientNameDP = ClientDropDown.get()
    
    match clientNameDP:
        case 'SQ':
            print('SQ choosen')
            SQwindow()
            #SQ
        
        case 'EX':
            print('EX choosen')
            EXwindow()
            #EX

        case 'UI':
            print('UI choosen')
            UIwindow()
            #UI

        case _:
            print('No Valid option chosen')

def optionmenu_callback(choice):
    print("option menu dropdown clicked:", choice)

# Frame 1 #########################
frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(pady=10, padx=10, side='top', fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame1, text='AutoBot', text_color='light sea green', font=('Terminal',26,'bold'))
label.pack(pady=5, padx=5, fill='both', expand=True)


# Frame 2 #########################

frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(pady=5, padx=5, side='left', fill='both', expand=True)

EntryClientName = customtkinter.CTkEntry(master=frame2, placeholder_text='Client Name')
EntryClientName.pack(pady=5, padx=5, fill='both', expand=True)

button1 = customtkinter.CTkButton(master=frame2, text='Start', command=start_type)
button1.pack(pady=5, padx=5)


# Frame 3 #########################

frame3 = customtkinter.CTkFrame(master=root)
frame3.pack(pady=5, padx=5, side='right', fill='both', expand=True)

ClientDropDown = customtkinter.CTkOptionMenu(master=frame3, values=['SQ', 'EX', 'UI'], command=optionmenu_callback)
ClientDropDown.pack(pady=5, padx=5, fill='both', expand=True)
ClientDropDown.set('Choose a Client')  # set initial value

button2 = customtkinter.CTkButton(master=frame3, text='Start', command=start_list)
button2.pack(pady=5, padx=5)

root.mainloop()
