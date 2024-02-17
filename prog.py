import clr
import time

from time import sleep

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("RvtProgressBar")

from System.Windows.Forms import *
from System.Drawing import *
from RvtProgressBar import *

dialog = OpenFileDialog()
f = ""

class MainForm(Form):
    def __init__(self):
        self.Text = "Data Import"
        self.Height = 176
        self.Width = 393
        self.Sizable = False
        self.MaximizeBox = False
        self.MinimizeBox = False
        self.ShowIcon = False
        
        label_filename = Label()
        label_filename.Text = "Select the csv file containing the data to import"
        label_filename.Height = 13
        label_filename.Width = 393
        label_filename.Location = Point(13, 14)

        self.textbox_filename = TextBox()
        self.textbox_filename.Height = 20
        self.textbox_filename.Width = 266
        self.textbox_filename.Location = Point(16, 35)
        self.textbox_filename.ReadOnly = True
        self.textbox_filename.Enabled = False

        button_select_file = Button()
        button_select_file.Text = "Select file"
        button_select_file.Location = Point(288, 32)
        button_select_file.Height = 23
        button_select_file.Width = 75

        button_import = Button()
        button_import.Text = "Import"
        button_import.Location = Point(207, 102)
        button_import.Height = 23
        button_import.Width = 75

        button_close = Button()
        button_close.Text = "Close"
        button_close.Location = Point(288, 102)
        button_close.Height = 23
        button_close.Width = 75

        button_select_file.Click += self.buttonSelectFilePressed
        button_import.Click += self.buttonImportPressed
        button_close.Click += self.buttonClosePressed

        self.Controls.Add(label_filename)
        self.Controls.Add(self.textbox_filename)
        self.Controls.Add(button_select_file)
        self.Controls.Add(button_import)
        self.Controls.Add(button_close)

    def buttonSelectFilePressed(self, sender, args):
        if dialog.ShowDialog() == DialogResult.OK:
            f = dialog.FileName
            self.textbox_filename.Text = f

    def buttonImportPressed(self, sender, args):
        if self.textbox_filename.Text != "":
            if MessageBox.Show(f'Import data from?\n{self.textbox_filename.Text}', "Import data", MessageBoxButtons.YesNo, MessageBoxIcon.Question):
                total = 10
                pf = ProgressForm("Updating parameters", total)
                for i in range(total):
                    time.sleep(1)
                    pf.Increment(total)
                MessageBox.Show("Data import complete", "Import data", MessageBoxButtons.OK, MessageBoxIcon.Information)
                pf.Close()
        else:
            MessageBox.Show("Select a file containing the data to import", "Import data", MessageBoxButtons.OK, MessageBoxIcon.Error)

    def buttonClosePressed(self, sender, args):
        self.Close()

form = MainForm()
Application.Run(form)