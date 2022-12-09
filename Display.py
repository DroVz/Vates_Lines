
from tkinter.messagebox import NO
from algo_password import *
import tkinter



class screen_app :

    def __init__(self,i):

        self.title_w = "Vates Lines"
        self.logo = None
        self.screen_min_x = 200
        self.screen_min_y = 100
        self.screen_background_color = 'white'
        self.screen = self.choice_screen(i)
    
    def choice_screen(self,i) : 
        screen = None
        if i == 0:
            screen = self.launch_first_screen()
        elif i == 1:
            screen = self.register()
        elif i == 2:
            screen = self.gen_password_w()
        elif i == 3:
            screen = self.chest_password()
        return screen


    def launch_first_screen (self):
        def valid_log(login_user,password_user):
            fichier = open('log.txt','r')
            contenu = fichier.readlines()
            if contenu[0] == login_user+"\n" and contenu[1] == password_user+"\n":
                swipe_windows_chest()
            else :
                error_l = self.new_label(windows,"password ou login incorecte",'red','white',None,None,None,None,None)
                error_l.pack()

        def swipe_windows_chest():
            windows.destroy()
            new_screen = screen_app(3)
            return new_screen
        def swipe_windows_reg():
            windows.destroy()
            new_screen = screen_app(1)
            return new_screen

        windows = tkinter.Tk()
        windows.geometry('300x480')
        windows.minsize(self.screen_min_x,self.screen_min_y)
        windows.title(self.title_w)
        windows.iconbitmap(self.logo)
        title_app = self.new_label(windows,"Vates Lines","#358714","white",tkinter.CENTER,1000,5,30,None)
        title_app.pack(pady=(0,40))
        l_login = self.new_label(windows,"Login :",None,"#358714",tkinter.LEFT,14,2,20,tkinter.W)
        l_login.pack()
        in_login = self.new_entry(windows)
        in_login.pack()
        l_password = self.new_label(windows,"Password :",None,"#358714",tkinter.LEFT,14,2,20,tkinter.W)
        l_password.pack()
        in_password = self.new_entry(windows)
        in_password.pack()
        confirm_button = self.new_button(windows,"Confirm","#358714","white","white","#358714",lambda:valid_log(in_login.get(),in_password.get())) #TODO lastnone
        confirm_button.pack(pady=10)
        register_button = self.new_button(windows,"Register",None,"black",None,None,lambda: swipe_windows_reg()) #TODO lastnone 
        register_button.pack(pady=0)

        windows.mainloop()
        return windows

    def register (self):#end
        def swipe_windows_log():
            windows.destroy()
            new_screen = screen_app(0)
            return new_screen
        
        def comp_password(login_user,first_pass,conf_pass):
            if first_pass == conf_pass :
                fichier = open('log.txt','w')
                fichier.writelines([login_user+"\n",first_pass+"\n",conf_pass])
                fichier.close()
                swipe_windows_log()
            return None


        def new_account(login_user,first_pass,conf_pass):
            with open('log.txt','r') as fichier:
                contenu = fichier.readlines()
                fichier.close()
                print(contenu)
            if login_user +'\n' == contenu[0]:#compte existe deja
                if contenu[0] != "login\n":
                    swipe_windows_log()  # vrai compte existant 
                else: #pas de compte cree
                    comp_password(login_user,first_pass,conf_pass)

            else : #compte existe pas
                if contenu[0] != "login\n":  #compte créé
                    swipe_windows_log() 
                else : # pas de compte cree
                    comp_password(login_user,first_pass,conf_pass)        
            return None
                       
        windows = tkinter.Tk()
        windows.geometry('300x480')
        windows.minsize(self.screen_min_x,self.screen_min_y)
        windows.title(self.title_w)
        windows.iconbitmap(self.logo)
        title_app = self.new_label(windows,"Vates Lines","#358714","white",tkinter.CENTER,1000,5,30,None)
        title_app.pack(pady=(0,40))
        l_login = self.new_label(windows,"Login :",None,"#358714",tkinter.LEFT,14,2,20,tkinter.W)
        l_login.pack()
        in_login = self.new_entry(windows)
        in_login.pack()
        l_password = self.new_label(windows,"Password :",None,"#358714",tkinter.LEFT,14,2,20,tkinter.W)
        l_password.pack()
        in_password1 = self.new_entry(windows)
        in_password1.pack()
        l_confpassword = self.new_label(windows,"Confirm password :",None,"#358714",tkinter.LEFT,18,2,20,tkinter.W)
        l_confpassword.pack()
        in_password = self.new_entry(windows)
        in_password.pack()
        confirm_button = self.new_button(windows,"Confirm","#358714","white","white","#358714",lambda: new_account(in_login.get(),in_password1.get(),in_password.get())) #TODO lastnone
        confirm_button.pack(pady=10)

        windows.mainloop()
        return windows

    def gen_password_w(self): #END

        def get_password(n):
            
            result = password.password_gen(self,n)
            in_password.delete(0,"end")
            return in_password.insert(1,result)
        
        def txt_insert(app,password_app):
            #Read Part 
            read_file = open("chest.txt",'r')
            j = 0  #Condition 
            k = 0  #Compteur 
            for i in (read_file) :
                char = read_file.readlines()
                word_rec = char[k]
                find_word = word_rec.find(app)
                k = k + 1
                if find_word != -1 :  #Condition app identique
                    j = 1
            read_file.close()
            if app == "" or password_app == "" or j == 1:
                in_login.delete(0,"end")
                in_password.delete(0,"end")
                in_login.insert(0,"ERROR")
                in_password.insert(0,"ERROR")
            else :
                f = open('chest.txt','a')
                f.write("\n"+ app +" = "+ password_app)
                in_login.delete(0,"end")
                in_password.delete(0,"end")
                f.close()
        
        def swipe_windows_gen():
            windows.destroy()
            new_screen = screen_app(3)
            return new_screen
        
            
        windows = tkinter.Tk()
        windows.geometry('300x480')
        windows.minsize(self.screen_min_x,self.screen_min_y)
        windows.title(self.title_w)
        windows.iconbitmap(self.logo)
        title_app = self.new_label(windows,"Vates Lines","#358714","white",tkinter.CENTER,1000,5,30,None)
        title_app.pack(pady= (0,40))
        l_login = self.new_label(windows,"User App :",None,"#358714",tkinter.LEFT,14,2,20,tkinter.W)
        l_login.pack()
        in_login = self.new_entry(windows)
        in_login.pack()
        l_password = self.new_label(windows,"Password :",None,"#358714",tkinter.LEFT,14,2,20,tkinter.W)
        l_password.pack()
        in_password = self.new_entry(windows)
        in_password.pack()
        nb_character =["8","9","10","11","12"]
        var_char = tkinter.StringVar(windows)
        var_char.set("8")
        menu_char = tkinter.OptionMenu(windows,var_char, *nb_character)
        menu_char.pack()
        confirm_button = self.new_button(windows,"Confirm","#358714","white","white","#358714",lambda:txt_insert(in_login.get(),in_password.get())) #TODO lastnone
        confirm_button.pack(pady=(10,5))
        register_button = self.new_button(windows,"Random",None,"black",None,None,lambda:get_password(int(var_char.get())))  
        register_button.pack(pady=(0,10))
        chest_button = self.new_button(windows,"Chest",None,"black",None,None,lambda:swipe_windows_gen())  
        chest_button.pack()
        windows.mainloop()
        return windows
    
    def chest_password (self):

        def swipe_windows_chest():
            windows.destroy()
            new_screen = screen_app(2)
            return new_screen
    
        windows = tkinter.Tk()
        windows.geometry('300x480')
        windows.minsize(self.screen_min_x,self.screen_min_y)
        windows.title(self.title_w)
        windows.iconbitmap(self.logo)
        title_app = self.new_label(windows,"Vates Lines","#358714","white",tkinter.CENTER,1000,5,30,None)
        title_app.pack(pady= (0,40))
        l_login = self.new_label(windows,"Chest :",None,"#358714",tkinter.LEFT,14,2,20,tkinter.W)
        l_login.pack()

        with open('chest.txt','r') as fichier:
            app_reg = fichier.readlines()
        var_char = tkinter.StringVar(windows)
        var_char.set("App and Password")
        menu_char = tkinter.OptionMenu(windows,var_char, *app_reg)
        menu_char.pack(pady=(0,10))
        generation_button = self.new_button(windows,"New Password","#358714","white","white","#358714",lambda:swipe_windows_chest())  
        generation_button.pack()

        windows.mainloop()
        return windows

    def new_label (self,screen,l_text,bg_color,fg_color,position,l_width,l_height,l_font,l_pos):
        label_w = tkinter.Label(screen,text= l_text, bg= bg_color,fg= fg_color,justify= position,width= l_width,height= l_height, font= l_font,anchor= l_pos)
        return label_w
    def new_entry (self,screen):
        entry_w = tkinter.Entry(screen)
        return entry_w
    def new_button (self,screen,b_text,bg_color,fg_color,abg_color,afg_color,w_command):
        button_w = tkinter.Button(screen,text= b_text, bg=bg_color, fg=fg_color,activebackground=abg_color,activeforeground=afg_color,command=w_command)
        return button_w



screen1 = screen_app(0)
