import wx
import requests
import json
from views.user_profile_view import UserProfilePanel


class LoginForm(wx.Dialog):
    def __init__(self, parent, main_frame, *args, **kw):
        super(LoginForm, self).__init__(parent, *args, **kw)
        self.main_frame = main_frame

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
        if username and password:
            data = {'username': username, 'password': password}
            url = 'https://hirematch.xce.pl/api_login'
            response = requests.post(url, json=data)
            print(response.status_code)
            if response.status_code == 200:
                response_data = response.content.decode('utf-8')
                response_json = json.loads(response_data)
                if 'status' in response_json:
                    status = response_json['status']
                    wx.MessageBox(status, "Success", wx.OK | wx.ICON_INFORMATION)
                    email = response_json.get('email', '')  # Przypisanie adresu e-mail
                    self.main_frame.email = email  # Przypisanie adresu e-mail do atrybutu instancji głównego okna
                    self.EndModal(wx.ID_OK)
            else:
                wx.MessageBox("Error connecting to server", "Error", wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox("Please enter both username and password", "Error", wx.OK | wx.ICON_AUTH_NEEDED)


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.email = None
        self.user_data = None
        self.SetSize((400, 300))
        self.SetTitle("Main Window")

        panel = wx.Panel(self)
        self.text = wx.StaticText(panel, label="", pos=(100, 100))

        self.create_menu_bar()

    def create_menu_bar(self):
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        profile_item = file_menu.Append(wx.ID_ANY, "Profile", "Przejdź do profilu")
        logout_item = file_menu.Append(wx.ID_ANY, "Logout", "Wyloguj się z aplikacji")
        self.Bind(wx.EVT_MENU, self.profile_view, profile_item)
        self.Bind(wx.EVT_MENU, self.on_logout, logout_item)
        menubar.Append(file_menu, "&Menu")
        self.SetMenuBar(menubar)

    def on_logout(self, event):
        self.Close()
        login_form = LoginForm(None, self)
        if login_form.ShowModal() == wx.ID_OK:
            self.update_welcome_message()

    def update_welcome_message(self):
        if self.email:
            self.text.SetLabel("Welcome " + self.email)
        else:
            self.text.SetLabel("Welcome to the main window")

    def profile_view(self, event):
        self.user_data = {
            'email': self.email
        }
        profile_frame = wx.Frame(None, title="User Profile", size=(400, 300))
        user_profile_panel = UserProfilePanel(profile_frame, self.user_data)
        profile_frame.Show()


if __name__ == '__main__':
    app = wx.App()
    main_frame = MainFrame(None)
    login_form = LoginForm(None, main_frame)  # Przekazujemy referencję do głównego okna
    if login_form.ShowModal() == wx.ID_OK:
        main_frame.update_welcome_message()
        main_frame.Show()
    app.MainLoop()
