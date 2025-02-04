from tkinter import *
from tkinter import messagebox
import random
import time

# Metallic/Chrome color palette
CYBER_COLORS = {
    'background': '#0A0A0F',    # Deep black
    'chrome1': '#E8E9EB',       # Light chrome
    'chrome2': '#A5A6A8',       # Mid chrome
    'chrome3': '#707174',       # Dark chrome
    'terminal_green': '#00FF00', # Matrix green
    'accent': '#2B2B2F',        
    'text': '#FFFFFF',          
}

MESSAGES = [
    "Keep pushing forward. Progress is progress.",
    "You've got this! One unit at a time.",
    "Small steps lead to big achievements.",
    "Stay focused. Stay strong.",
    "Your future self will thank you.",
    "Excellence is a habit. Keep at it!",
    "Every checkbox ticked is a step forward.",
    "You're doing better than you think.",
    "Progress > Perfection",
    "Trust the process. Keep going."
]

LOADING_MESSAGES = [
    "Initializing status check...",
    "Accessing database...",
    "Decrypting progress data...",
    "Analyzing completion rates...",
    "Compiling status report...",
    "Securing connection...",
    "Verifying checksums...",
    "Processing matrix data...",
    "Generating report..."
]

class HackerStatusWindow:
    def __init__(self, parent, checkbox_data):
        self.status_window = Toplevel(parent)
        self.status_window.configure(bg=CYBER_COLORS['background'])
        self.status_window.title('Terminal Status')
        self.status_window.geometry('600x400')
        
        # Create terminal-style text widget
        self.terminal = Text(
            self.status_window,
            bg=CYBER_COLORS['background'],
            fg=CYBER_COLORS['terminal_green'],
            font=('Courier', 10),
            relief='solid',
            borderwidth=1
        )
        self.terminal.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        self.checkbox_data = checkbox_data
        self.current_message = 0
        self.matrix_active = True
        self.simulate_hacking()
        self.matrix_background()

    def matrix_background(self):
        if self.matrix_active:
            matrix_chars = "01"
            self.terminal.insert(END, f"{random.choice(matrix_chars)}" * random.randint(1, 3))
            self.terminal.see(END)
            self.status_window.after(100, self.matrix_background)

    def glitch_effect(self, text):
        glitch_chars = "!@#$%^&*()_+"
        return ''.join(random.choice(glitch_chars) if random.random() < 0.1 else c for c in text)

    def simulate_hacking(self):
        if self.current_message < len(LOADING_MESSAGES):
            message = self.glitch_effect(LOADING_MESSAGES[self.current_message])
            self.type_text(f"\n> {message}")
            self.current_message += 1
            self.status_window.after(800, self.simulate_hacking)
        else:
            self.matrix_active = False
            self.show_final_status()

    def type_text(self, text):
        for char in text:
            self.terminal.insert(END, char)
            self.terminal.see(END)
            self.terminal.update()
            time.sleep(0.02)

    def show_final_status(self):
        self.type_text("\n\n===============================")
        self.type_text("\n=       STATUS REPORT        =")
        self.type_text("\n===============================\n")
        
        for sub in self.checkbox_data:
            self.type_text(f"\n> {sub}:")
            for u, var in self.checkbox_data[sub].items():
                status = "COMPLETED" if var.get() else "PENDING"
                self.type_text(f"\n  {u}: [{status}]")
        
        self.type_text("\n\n===============================")
        self.type_text("\n=       END OF REPORT        =")
        self.type_text("\n===============================\n")

win = Tk()
win.geometry('800x600')
win.title('ESA TRACKER')
win.configure(bg=CYBER_COLORS['background'])

title_font = ('Courier', 24, 'bold')
header_font = ('Courier', 12, 'bold')
text_font = ('Courier', 10)

subj = ["Math", "Python", "Phy", "EEE", "Mech", "EVS"]
unit = ["U1", "U2", "U3", "U4"]

def show_motivation():
    message = random.choice(MESSAGES)
    messagebox.showinfo("System Message", message)

def get_status():
    HackerStatusWindow(win, checkbox_var)

main_frame = Frame(
    win,
    bg=CYBER_COLORS['background'],
    padx=30,
    pady=30,
    highlightbackground=CYBER_COLORS['chrome2'],
    highlightthickness=2
)
main_frame.pack(expand=True, pady=50)

title_label = Label(
    win,
    text="SYSTEM TRACKER",
    font=title_font,
    bg=CYBER_COLORS['background'],
    fg=CYBER_COLORS['chrome1'],
    pady=20
)
title_label.pack(before=main_frame)

checkbox_var = {}

Label(
    main_frame,
    text="SUBJECTS",
    width=12,
    font=header_font,
    bg=CYBER_COLORS['background'],
    fg=CYBER_COLORS['chrome2']
).grid(row=0, column=0, padx=5, pady=10)

for j, u in enumerate(unit):
    Label(
        main_frame,
        text=u,
        width=10,
        font=header_font,
        bg=CYBER_COLORS['background'],
        fg=CYBER_COLORS['chrome2']
    ).grid(row=0, column=j+1, padx=5, pady=10)

for i, sub in enumerate(subj):
    Label(
        main_frame,
        text=sub,
        width=12,
        font=text_font,
        bg=CYBER_COLORS['background'],
        fg=CYBER_COLORS['chrome1'],
        anchor='w'
    ).grid(row=i+1, column=0, padx=5, pady=5)
    
    checkbox_var[sub] = {}
    for j, u in enumerate(unit):
        var = IntVar()
        checkbox_var[sub][u] = var
        cb = Checkbutton(
            main_frame,
            variable=var,
            bg=CYBER_COLORS['background'],
            activebackground=CYBER_COLORS['accent'],
            selectcolor=CYBER_COLORS['accent'],
            fg=CYBER_COLORS['chrome1']
        )
        cb.grid(row=i+1, column=j+1, padx=5, pady=5)

button_frame = Frame(win, bg=CYBER_COLORS['background'])
button_frame.pack(pady=20)

check_button = Button(
    button_frame,
    text="<CHECK_STATUS/>",
    command=get_status,
    font=('Courier', 12, 'bold'),
    bg=CYBER_COLORS['background'],
    fg=CYBER_COLORS['terminal_green'],
    activebackground=CYBER_COLORS['accent'],
    activeforeground=CYBER_COLORS['terminal_green'],
    relief='ridge',
    borderwidth=3,
    padx=20,
    pady=10
)
check_button.pack(side=LEFT, padx=10)

motivation_button = Button(
    button_frame,
    text="<MOTIVATION/>",
    command=show_motivation,
    font=('Courier', 12, 'bold'),
    bg=CYBER_COLORS['background'],
    fg=CYBER_COLORS['terminal_green'],
    activebackground=CYBER_COLORS['accent'],
    activeforeground=CYBER_COLORS['terminal_green'],
    relief='ridge',
    borderwidth=3,
    padx=20,
    pady=10
)
motivation_button.pack(side=LEFT, padx=10)

status_label = Label(
    win,
    text="[ SYSTEM ACTIVE ]",
    font=header_font,
    bg=CYBER_COLORS['background'],
    fg=CYBER_COLORS['chrome3']
)
status_label.pack(side=BOTTOM, pady=10)

def pulse_effect():
    current_color = status_label.cget("fg")
    if current_color == CYBER_COLORS['chrome3']:
        status_label.configure(fg=CYBER_COLORS['chrome1'])
    else:
        status_label.configure(fg=CYBER_COLORS['chrome3'])
    win.after(1000, pulse_effect)

pulse_effect()

win.mainloop()