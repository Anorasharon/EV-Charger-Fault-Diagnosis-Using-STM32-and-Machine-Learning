import serial
import pandas as pd
import numpy as np
import joblib
import tkinter as tk
from PIL import Image, ImageTk

# Load Model
model = joblib.load('charger_fault_model.pkl')
ser = serial.Serial('COM20', 115200, timeout=1)

root = tk.Tk()
root.title("EV Charger Health Dashboard")
root.geometry("800x500")

# 1. Background Image Setup
bg_image = Image.open("bgf.png").resize((800, 500)) # Change to your preferred BG image
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 2. Status Box (Frame)
status_frame = tk.Frame(root, bg="white", bd=5, relief="ridge")
status_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=150)

status_label = tk.Label(status_frame, text="ANALYZING...", font=("Helvetica", 20, "bold"), bg="white")
status_label.pack(expand=True)

COL_NAMES = [
    'ADC0_RMS', 'ADC0_Mean', 'ADC0_Std', 'ADC0_Max', 
    'ADC1_RMS', 'ADC1_Mean', 'ADC1_Std', 'ADC1_Max', 
    'ADC2_RMS', 'ADC2_Mean', 'ADC2_Std', 'ADC2_Max',
    'CONN_VOLT_RMS', 'CONN_VOLT_Mean', 'CONN_VOLT_Std', 'CONN_VOLT_Max', 
    'CAP_VOLT_RMS', 'CAP_VOLT_Mean', 'CAP_VOLT_Std', 'CAP_VOLT_Max',
    'MOS_CURR_RMS', 'MOS_CURR_Mean', 'MOS_CURR_Std', 'MOS_CURR_Max'
]

buffer = []

def update_gui():
    global buffer
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            try:
                data = [float(x) for x in line.split(',')]
                if len(data) == 6: buffer.append(data)
            except: pass

        if len(buffer) == 30:
            df = pd.DataFrame(buffer, columns=['ADC0', 'ADC1', 'ADC2', 'CONN_VOLT', 'CAP_VOLT', 'MOS_CURR'])
            features = []
            for col in df.columns:
                features.extend([np.sqrt(np.mean(df[col]**2)), df[col].mean(), df[col].std(ddof=0), df[col].max()])
            
            pred = model.predict(pd.DataFrame([features], columns=COL_NAMES))[0]
            if str(pred).lower() == 'capacitor_mild': 
                pred = 'normal'
            # Text update inside box
            status_label.config(text=str(pred).upper(), fg="black")
            
            buffer = []

    root.after(10, update_gui)

root.after(100, update_gui)
root.mainloop()