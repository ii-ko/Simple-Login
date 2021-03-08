# Python Ver 3.9.2

from tkinter import *
from tkinter import ttk, messagebox as ps

data = ['admin', '123']

class login:
    def __init__(self, par):
        self.par = par
        self.par.resizable(0, 0)
        self.par.title('Simple Login')

        lebar = 220
        tinggi = 180

        # posisi aplikasi ketika muncul di layar (pos=tengah)
        setTengahX = (self.par.winfo_screenwidth() - lebar) // 2
        setTengahY = (self.par.winfo_screenheight() - tinggi) // 2
        self.par.geometry("%ix%i+%i+%i" % (lebar, tinggi, setTengahX, setTengahY))
        self.build()

    def do_login(self):
        username = self.en_id.get()
        password = self.en_pasw.get()
        if username == data[0] and password == data[1]:
            ps.showinfo('INFO', 'Login Success')
        else:
            ps.showwarning('INFO', 'Invalid Username or Password')

    def build(self):
        frame_1 = ttk.Frame(self.par); frame_1.grid(row=0, column=0)
        frame_2 = ttk.Frame(self.par); frame_2.grid(row=1, column=0, pady=10)
        frame_3 = ttk.Frame(self.par); frame_3.grid(row=2, column=0)

# Title
        ttk.Label(frame_1, text='Login Here', font=('Tahoma', 14)).pack(padx=3, pady=3)
# Labels
        ttk.Label(frame_2, text='Username', font=('Tahoma', 12)).grid(row=0, column=0, sticky=W, padx=3, pady=3)
        ttk.Label(frame_2, text='Pasword', font=('Tahoma', 12)).grid(row=1, column=0, sticky=W, padx=3, pady=3)
# Text Input
        self.en_id = ttk.Entry(frame_2); self.en_id.grid(row=0, column=1, padx=5, pady=3)
        self.en_id.focus()
        self.en_pasw = ttk.Entry(frame_2, show='*'); self.en_pasw.grid(row=1, column=1, padx=5, pady=3)
# Button
        self.login = ttk.Button(frame_3, text='Login', command=self.do_login)
        self.login.grid(row=1, column=0, padx=5, pady=3)
        self.cancel = ttk.Button(frame_3, text='Cancel', command=self.par.destroy)
        self.cancel.grid(row=2, column=0, padx=5, pady=3)

if __name__ == '__main__':
    root = Tk()
    login(root)
    root.mainloop()