import clr
import os

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import *
from System.Drawing import *

dialog = OpenFileDialog()
f = ""

class MainForm(Form):
    def __init__(self):
        self.Text = "PyWinForms"
        self.Width = 400
        self.Height = 200
        self.ReSizable = False
        self.MaximizeBox = False
        self.MinimizeBox = False
        self.ShowIcon = False
        
        label_filename = Label()
        label_filename.Text = "Filename"
        label_filename.Height = 13
        label_filename.Width = 393
        label_filename.Location = Point(10, 10)

        self.textbox_filename = TextBox()
        self.textbox_filename.Height = 20
        self.textbox_filename.Width = 350
        self.textbox_filename.Location = Point(10, 30)
        self.textbox_filename.ReadOnly = True
        self.textbox_filename.Enabled = True

        button_select_file = Button()
        button_select_file.Text = "Select file"
        button_select_file.Location = Point(10, 60)
        button_select_file.Height = 23
        button_select_file.Width = 75

        button_show_file = Button()
        button_show_file.Text = "Open file"
        button_show_file.Location = Point(90, 60)
        button_show_file.Height = 23
        button_show_file.Width = 75

        button_select_file.Click += self.buttonSelectFilePressed
        button_show_file.Click += self.buttonShowFilePressed

        self.Controls.Add(label_filename)
        self.Controls.Add(self.textbox_filename)
        self.Controls.Add(button_select_file)
        self.Controls.Add(button_show_file)

    def buttonSelectFilePressed(self, sender, args):
        if dialog.ShowDialog() == DialogResult.OK:
            f = dialog.FileName
            self.textbox_filename.Text = f

    def buttonShowFilePressed(self, sender, args):
        if self.textbox_filename.Text != "":
            os.startfile(self.textbox_filename.Text)
        else:
            MessageBox.Show("No file to open.", "PyWinForms", MessageBoxButtons.OK, MessageBoxIcon.Warning)
            
form = MainForm()
Application.Run(form)