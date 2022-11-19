from msilib.schema import CheckBox
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


import sqlite3

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Login(Screen):
    def ButtonLogin(self):
        login = self.ids.login.text
        password = self.ids.password.text

        if len(password) >= 6 and len(login) >=6:
            print("login com sucesso")
            conn = sqlite3.connect('clientes.db')

            c = conn.cursor()
            d = conn.cursor()
            #selectTRIM
            c.execute("Select login from UserClientesLogin ")

            registro = c.fetchall()
            numeros = []
            nome = ''
            variavelBoolean = True

            for reg in registro:
                # nome = f'{nome}{reg[0]}'
                # print(nome)
                # print(login)
                # print(nome,'a')
                if login == reg[0]:
                    test = d.execute("Select password from UserClientesLogin")
                    for i in test:
                        if i[0]==password:
                            print("login feito com sucessoaaaaaaaaaaaaa")
                            variavelBoolean = True
            conn.commit()
            conn.close()
            if variavelBoolean == True:
                self.manager.current = "MenuJogar"
                
            

        else:
            print("Porfavor tente novamente")

class Register(Screen):
    checkbox = False
    def ButtonLogin(self):
        conn = sqlite3.connect('clientes.db')
        d = conn.cursor()

        email = self.ids.email.text
        login = self.ids.login.text
        password = self.ids.password.text
        confere = False
        if self.checkbox == True :
            if "@" in email and ".com" in email :
                if len(password) >= 6:
                    if len(login) >=6:
                        d.execute("Select login from UserClientesLogin ")
                        registro = d.fetchall()
                        conn.commit()
                        conn.close()
                        for reg in registro:
                            print(reg[0])
                            if login == reg[0]:
                                
                               
                                print("Login ja existente")
                                confere = False
                                return

                            else:
                                confere = True
                                
                    else:
                        print("login invalido")
                else:
                    print("password invalido")
            else:
                print("email Invalido")
        else:
            print("Voce precisa ir de acordo com os termos")
        
        if confere == True :
            conn = sqlite3.connect('clientes.db')
            c = conn.cursor()
            
            # c.execute("Insert into UserClientesLogin (login,email,password) values","('",login,"',","'",email,"',","'",password,"')")
            c.execute("Insert into UserClientesLogin (login,email,password) values (?, ? ,?)", (login, email,password))
            registroc = c.fetchall()
            print(registroc)
            # print("Insert into UserClientesLogin (login,email,password)values" , '(',{'login': login,'email':email,'password':password},')' )
            # 
            # ('otavio','otaviofaria30@gmail.com','otavio')
            conn.commit()
            conn.close()


    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.checkbox = True
        else:
            self.checkbox = False

class MenuJogar(Screen):
   pass
    
class SkinAviao(Screen):
   pass

class SkinMapa(Screen):
   pass

class Jogar(Screen):

    def controlTheProgress(self, *args):
        value = args[1]
        
        # control angle end value via progress attribute
        self.ids.circular_progress.progress = value
        # control text progress value
        self.ids.circular_progress.text = f'{int(value/3.6)}%'

class main(MDApp):
    def build(self):

        conn = sqlite3.connect('clientes.db')

        c = conn.cursor()

        c.execute("Create table if not exists user(id int primary key not null,login char(50) not null, email char(50) not null,password char(50) not null,score int)")
        conn.commit()

        conn.close()

        return Gerenciador()

if __name__ =="__main__":
        LabelBase.register(name="MPoppins",fn_regular="./Poppins-Medium.ttf")
        LabelBase.register(name="BPoppins",fn_regular="./Poppins-SemiBold.ttf")
        main().run()