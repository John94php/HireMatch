import wx


class LoginForm(wx.Dialog):
    def __init__(self, parent, *args, **kw):
        super(LoginForm, self).__init__(parent, *args, **kw)

        self.SetSize((300, 200))
        self.SetTitle("Login Form")

        self.panel = wx.Panel(self)

        self.username_label = wx.StaticText(self.panel, label="Username:")
        self.username_text = wx.TextCtrl(self.panel)
        self.password_label = wx.StaticText(self.panel, label="Password:")
        self.password_text = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)
        self.login_button = wx.Button(self.panel, label="Login")

        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.username_label, 0, wx.ALL, 5)
        sizer.Add(self.username_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.password_label, 0, wx.ALL, 5)
        sizer.Add(self.password_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.login_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.panel.SetSizer(sizer)

    def on_login(self, event):
        username = self.username_text.GetValue()
        password = self.password_text.GetValue()
        if username == "admin" and password == "admin":
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox("Invalid username or password", "Error", wx.OK | wx.ICON_ERROR)


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.SetSize((400, 300))
        self.SetTitle("Main Window")

        panel = wx.Panel(self)
        self.text = wx.StaticText(panel, label="Welcome to the main window!", pos=(100, 100))

        self.create_menu_bar()

    def create_menu_bar(self):
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        logout_item = file_menu.Append(wx.ID_ANY, "Logout", "Wyloguj się z aplikacji")
        self.Bind(wx.EVT_MENU, self.on_logout, logout_item)
        menubar.Append(file_menu, "&Menu")
        self.SetMenuBar(menubar)

    def on_logout(self, event):
        self.Close()
        login_form = LoginForm(None)
        if login_form.ShowModal() == wx.ID_OK:
            main_frame = MainFrame(None)
            main_frame.Show()


if __name__ == '__main__':
    app = wx.App()
    login_form = LoginForm(None)
    if login_form.ShowModal() == wx.ID_OK:
        main_frame = MainFrame(None)
        main_frame.Show()
    app.MainLoop()
