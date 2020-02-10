import tkinter as tk
import tkinter.ttk as ttk
import serial

LARGE_FONT = ("Verdana", 18)
small_FONT = ("Verdana", 12)



class first_program(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def qf(quickPrint):
    print(quickPrint)


class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="**Simple serial write app**", fg='blue', font=small_FONT)
        label.grid(row=0, column=0)

        # Create button1 for connect to serial
        label = tk.Label(self, text="Connect COM port:", font=small_FONT) \
                                                                 .grid(row=2, column=0)
        ttk.Button(self, text='Connect COM', command=self.button1_callback, width=20) \
                                                                .grid(row=2, column=2)

        # Create buttons for init
        ttk.Button(self, text='Full_reset', command=self.button7_callback, width=12) \
            .grid(row=3, column=3)

        # Create buttons for sending channels
        label = tk.Label(self, text="| WRITE to DAC channels |", font=small_FONT) \
                                                                 .grid(row=5, column=3)
        ttk.Button(self, text='Channel_A', command=self.button2_callback, width=12) \
                                                                .grid(row=6, column=1)
        ttk.Button(self, text='Channel_B', command=self.button3_callback, width=12) \
                                                                .grid(row=6, column=2)
        ttk.Button(self, text='Channel_C', command=self.button4_callback, width=12) \
                                                                .grid(row=6, column=3)
        ttk.Button(self, text='Channel_D', command=self.button5_callback, width=12) \
                                                                .grid(row=6, column=4)
        ttk.Button(self, text='BIAS', command=self.button6_callback, width=12) \
                                                                .grid(row=6, column=7)

        # Buttons for Filter clock and ENABLE
        self.button_fc = ttk.Button(self, text='Filter_cl_Disable', command=self.button8_callback, width=15)
        self.button_fc.grid(row=3, column=4)

        self.button_en = ttk.Button(self, text='Driver_Disable', command=self.button9_callback, width=15)
        self.button_en.grid(row=3, column=5)



        # Create User input box
        self.user_spinbox1 = ttk.Spinbox(self, from_=0, to=65536, width=10)
        self.user_spinbox1.grid(row=7, column=1)
        self.user_spinbox1.delete(0, 'end')
        self.user_spinbox1.insert(0, '1') #Set default 1#
        # Create User input box
        self.user_spinbox2 = ttk.Spinbox(self, from_=0, to=65536, width=10)
        self.user_spinbox2.grid(row=7, column=2)
        self.user_spinbox2.delete(0, 'end')
        self.user_spinbox2.insert(0, '1') #Set default 1#
        # Create User input box
        self.user_spinbox3 = ttk.Spinbox(self, from_=0, to=65536, width=10)
        self.user_spinbox3.grid(row=7, column=3)
        self.user_spinbox3.delete(0, 'end')
        self.user_spinbox3.insert(0, '1') #Set default 1#
        # Create User input box
        self.user_spinbox4 = ttk.Spinbox(self, from_=0, to=65536, width=10)
        self.user_spinbox4.grid(row=7, column=4)
        self.user_spinbox4.delete(0, 'end')
        self.user_spinbox4.insert(0, '1') #Set default 1#
        # Create User input box
        self.user_spinbox5 = ttk.Spinbox(self, from_=0, to=65536, width=10)
        self.user_spinbox5.grid(row=7, column=7)
        self.user_spinbox5.delete(0, 'end')
        self.user_spinbox5.insert(0, '32000') #Set default 1#
        #
        # New buttons for X and Y
        ttk.Button(self, text='X_diff mV', command=self.X_callback, width=12) \
            .grid(row=9, column=3)
        ttk.Button(self, text='Y_diff mV', command=self.Y_callback, width=12) \
            .grid(row=9, column=4)
        # Create User input box
        self.user_spinbox6 = ttk.Spinbox(self, from_=0, to=65536, width=10)
        self.user_spinbox6.grid(row=10, column=3)
        self.user_spinbox6.delete(0, 'end')
        self.user_spinbox6.insert(0, '1') #Set default 1#
        # Create User input box
        self.user_spinbox7 = ttk.Spinbox(self, from_=0, to=65536, width=10)
        self.user_spinbox7.grid(row=10, column=4)
        self.user_spinbox7.delete(0, 'end')
        self.user_spinbox7.insert(0, '1') #Set default 1#

        # #Create label
        label2 = tk.Label(self, text="Output_window:", font=small_FONT)\
                                                                .grid(row=8, column=0)
        #
        #Create program output label
        self.label3 = tk.Label(self, text="", bg="White", font=small_FONT,width=22)
        self.label3.grid(row=9, column=0)


    #Method to connect to COM port
    def button1_callback(self):
        self._serial_port = serial.Serial('COM9', 9600, parity=serial.PARITY_NONE,
                                          stopbits=serial.STOPBITS_ONE, timeout=3.5, write_timeout=3.5)


    #Methods for sending commands
    def button2_callback(self):
        value = int(self.user_spinbox1.get())
        value = 'M30' + str(value) + '\n'
        self.label3['text'] = value
        self._serial_port.write(value.encode('ASCII'))

    def button3_callback(self):
        value = int(self.user_spinbox2.get())
        value = 'M31' + str(value) + '\n'
        self.label3['text'] = value
        self._serial_port.write(value.encode('ASCII'))

    def button4_callback(self):
        value = int(self.user_spinbox3.get())
        value = 'M32' + str(value) + '\n'
        self.label3['text'] = value
        self._serial_port.write(value.encode('ASCII'))

    def button5_callback(self):
        value = int(self.user_spinbox4.get())
        value = 'M33' + str(value) + '\n'
        self.label3['text'] = value
        self._serial_port.write(value.encode('ASCII'))

    def button6_callback(self):
        value = int(self.user_spinbox5.get())
        value = 'M27' + str(value) + '\n'
        self.label3['text'] = value
        self._serial_port.write(value.encode('ASCII'))

    def button7_callback(self):
        ###  [0x280001, 0x380001, 0x20000F, 0x300000] # # #
        value = ['M500001', 'M700001', 'M400015', 'M600000']
        for var in value:
            self.label3['text'] = var
            self._serial_port.write((var + '\n').encode('ASCII'))

    def button8_callback(self):
        filter_ON = 'C001'
        filter_OFF = 'S001'
        if self.button_fc.cget('text') == 'Filter_cl_Disable':
            self.button_fc.configure(text='Filter_cl_Enable')
            self._serial_port.write((filter_ON + '\n').encode('ASCII'))
            self.label3['text'] = filter_ON
        else:
            self.button_fc.configure(text='Filter_cl_Disable')
            self._serial_port.write((filter_OFF + '\n').encode('ASCII'))
            self.label3['text'] = filter_OFF

    def button9_callback(self):
        ON = 'E001'
        OFF = 'D001'
        if self.button_en.cget('text') == 'Driver_Disable':
            self.button_en.configure(text='Driver_Enable')
            self._serial_port.write((ON + '\n').encode('ASCII'))
            self.label3['text'] = ON
        else:
            self.button_en.configure(text='Driver_Disable')
            self._serial_port.write((OFF + '\n').encode('ASCII'))
            self.label3['text'] = OFF

    def X_callback(self):
        Vdiff_mV = int(self.user_spinbox6.get())
        # Vdiff convertion to decimal values
        value_X_dec = Vdiff_mV+10
        value_nX_dec = Vdiff_mV-10
        # send X positive channel
        value_X_dec = 'M30' + str(value_X_dec) + '\n'
        self.label3['text'] = value_X_dec
        self._serial_port.write(value_X_dec.encode('ASCII'))
        # send Xminus channel
        value_nX_dec = 'M31' + str(value_nX_dec) + '\n'
        self.label3['text'] = value_nX_dec
        self._serial_port.write(value_nX_dec.encode('ASCII'))

    def Y_callback(self):
        Vdiff_mV = int(self.user_spinbox7.get())
        # Vdiff convertion to decimal values
        value_Y_dec = Vdiff_mV+10
        value_nY_dec = Vdiff_mV-10
        # send X positive channel
        value_Y_dec = 'M32' + str(value_Y_dec) + '\n'
        self.label3['text'] = value_Y_dec
        self._serial_port.write(value_Y_dec.encode('ASCII'))
        # send Xminus channel
        value_nY_dec = 'M33' + str(value_nY_dec) + '\n'
        self.label3['text'] = value_nY_dec
        self._serial_port.write(value_nY_dec.encode('ASCII'))



app = first_program()
app.mainloop()