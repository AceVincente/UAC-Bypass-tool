import customtkinter as ctk
from tkinter import filedialog
from customtkinter import *
import subprocess

selected_executable_file = None

def credits():
    app = CTk()
    app.title('Credits')
    app.geometry('200x200')
    label = CTkLabel(app, text='Developed By Dexter')
    label.place(relx=0.5, rely=0.5, anchor='center')
    app.mainloop()

def select_executable():
    global selected_executable_file
    selected_executable_file = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
    if selected_executable_file:
        print("Selected executable file:", selected_executable_file)
    else:
        print("No executable file selected.")

def run_selected_executable():
    if selected_executable_file:
        command = f'cmd /min /C "set __COMPAT_LAYER=RUNASINVOKER && start "" "{selected_executable_file}"'
        subprocess.Popen(command, shell=True)
    else:
        print("No executable file selected. Please select an executable file first.")

def instructions():
    app2 = CTk()

    app2.title('Instructions')

    app2.geometry('400x200')  # Adjusted the width and height of the window

    # Adjusted the text to fit within the window and added newline characters
    text = ('Open any executable file with the Open button.\n'
            'Then go ahead and click on the Bypass UAC button.\n'
            'This will bypass the UAC prompt on the .exe file!')

    label = CTkLabel(app2, text=text, justify='center', wraplength=380)  # Adjusted wrap length
    label.place(relx=0.5, rely=0.5, anchor='center')

    app2.mainloop()

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry('300x300')
    app.title('UAC bypassing tool')

    label = ctk.CTkLabel(app, text='UAC Bypassing Tool')
    label.place(relx=0.5, rely=0.20, anchor='center')

    button_select = ctk.CTkButton(app, text='Open', command=select_executable)
    button_select.place(relx=0.5, rely=0.35, anchor='center')

    button_bypass = ctk.CTkButton(app, text='Bypass UAC', command=run_selected_executable)
    button_bypass.place(relx=0.5, rely=0.5, anchor='center')

    button_credits = ctk.CTkButton(app, text='Credits', command=credits)
    button_credits.place(relx=0.5, rely=0.65, anchor='center')

    button_instructions = ctk.CTkButton(app, text='instructions',
                                        command=instructions)
    button_instructions.place(relx=0.5, rely=0.8, anchor='center')

    app.mainloop()
