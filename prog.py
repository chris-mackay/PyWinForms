# Import common language runtime
import clr

# Add references to the .Net libraries to access forms and controls
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import *
from System.Drawing import *

class MainForm(Form):

    # Create the definition for the form
    def __init__(self):
        
        # Set properties of the form
        self.Text = "PyWinForms"
        self.Width = 300
        self.Height = 200
        self.Sizable = False
        self.MaximizeBox = False
        self.MinimizeBox = False
        self.ShowIcon = False

        # Create a new button and set properties
        button_show_message = Button()
        button_show_message.Text = "Click me"
        button_show_message.Location = Point(10, 10)
        button_show_message.Height = 30
        button_show_message.Width = 150

        # Create a click event for the show message button
        button_show_message.Click += self.buttonShowMessagePressed

        # Add the show message button to the forms list of controls
        self.Controls.Add(button_show_message)

    # Create a definition for the click event
    def buttonShowMessagePressed(self, sender, args):
        MessageBox.Show("Hello from WinForms!", "PyWinForms", MessageBoxButtons.OK, MessageBoxIcon.Information)
        
# Create a new form
form = MainForm()

# Run the form
Application.Run(form)
