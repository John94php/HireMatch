import wx


class UserProfilePanel(wx.Panel):
    def __init__(self, parent, user_data):
        super(UserProfilePanel, self).__init__(parent)

        self.user_data = user_data

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.email_label = wx.StaticText(self, label="Email: " + self.user_data['email'])
        sizer.Add(self.email_label, 0, wx.ALL, 5)

        self.edit_button = wx.Button(self, label="Edit")
        self.edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        sizer.Add(self.edit_button, 0, wx.ALL, 5)

        self.SetSizer(sizer)

    def on_edit(self, event):
        # Tutaj możesz dodać logikę, która otwiera okno edycji danych użytkownika
        wx.MessageBox("Edit button clicked!", "Info", wx.OK | wx.ICON_INFORMATION)
