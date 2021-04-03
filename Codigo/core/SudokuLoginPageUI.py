from tkinter import *
from core.SudokuMainWindowUI import SudokuMainWindowUI
from core.SudokuAdministratorUI import SudokuAdministratorUI
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.ScreenCenter import ScreenCenter

class SudokuLoginPageUI(Frame):

    def __init__(self):
        
        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.config = ConfigConnection()
        self.db = MySQLEngine(self.config.getConfig())
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):

        self.width = 400
        self.height = 600
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.backgroundImage = PhotoImage(file="core/images/LoginScreen.png", master=self.parent)
        self.parent.title("Inicio de Sesión")
        self.parent.resizable(False, False)
        self.parent.geometry("%dx%d"%(self.width, self.height))
        self.parent.iconphoto(True, self.logo)
        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)
        canvas = Canvas(self, width=self.backgroundImage.width(), height=self.backgroundImage.height())
        labelLogo = Label(self,image=self.backgroundImage)
        labelLogo.place(x=0, y=0, relwidth=1, relheight=1)
        canvas.grid(row=0, column=0)
        usernameText = StringVar()
        usernameEntry = Entry(self, textvariable = usernameText, font=("Lato",15),  justify=CENTER)
        passwordText = StringVar()
        passwordEntry = Entry(self, textvariable = passwordText, show = "*", font=("Lato",15),  justify=CENTER)
        canvas.create_window(200, 120, window=usernameEntry)
        canvas.create_window(200, 210, window=passwordEntry)
        loginButton = Button(self, text="Iniciar Sesión", bg="#6ea8d9",width=10, height=2,font=("Lato",15), command = lambda: self.__loginFn(usernameText, passwordText))
        canvas.create_window(200, 280, window=loginButton)

    def __loginFn(self, username, password):

        # Variable de texto donde se almacenará el texto de error que corresponda
        # para después mostrarlo en un messagebox
        error = ""
        
        # Comprobando la longitud del texto correspondiente al nombre de usuario
        if (len(username.get()) == 0):
            error += "El campo usuario está vacio.\n"
        
        # Comprobando la longitud del texto correspondiente a la contraseña
        if(len(password.get()) == 0):
            error += "El campo contraseña está vacio.\n"

        """ 
        PROBLEMAS AQUÍ, me toca solucionar
        statusLogin = self.db.select("SELECT fn_compareData( %s, %s);"%(username.get(), password.get()))
        print(statusLogin[0][0])
        if (statusLogin[0][0] == 0):
            error += "Usuario o contraseña no válidos.\n" 
        """

        # Comprobando si ocurrio algún error
        if (len(error) == 0):
            # Se destruye la ventana
            self.parent.destroy()
            # Se instancia una ventana nueva del tipo MainWindow
            SudokuMainWindowUI()

        # En caso contrario de que se haya presentado un error
        else:
            messagebox.showerror(title="Error", message=error)
            return

        """ 
        Si es admin
        if()
            self.parent.destroy()
            SudokuAdministratorUI() """