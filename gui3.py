from tkinter import *
import numpy as np
import pandas as pd
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date, timedelta
from tkinter import ttk
from PIL import Image,ImageTk
import pickle
import yfinance as yf
import plotly.graph_objs as go
import gui3


class CryptoPlot:
    def __init__(self, frm) -> None:
        self.window2 = Tk()
        self.frm = frm
        #Set the geometry
        self.window2.geometry("1300x650")
        frame = Canvas(self.window2, width=1300, height = 680)
        frame.place(x = 0, y = 0)

        self.frame1 = Frame(self.window2, width=400, height=680,bg = "#000080")
        self.frame1.place(x = 0, y = 0)

        self.frame2 = Frame(self.window2, width=900, height=680,bg = "white")
        self.frame2.place(x = 400, y = 0)
        # Load the image
        # img= Image.open("img1.png").resize((1200, 650))


        #Convert To photoimage
        # tkimage= ImageTk.PhotoImage(img)


        #Heading with transparent background
        # frame.create_image(0, 0, anchor=NW, image = tkimage)


        self.backBtn = Button(self.window2, text = 'Back',bg = "Black",fg ="white",font = ("Arial", 16), command=self.back)
        self.backBtn.place(x=160,y=600)
        # Define the GUI elements for the custom plot window
        tk.Label(self.window2, text="Select the time period:",font = ("Arial", 16),bg = "white",fg = "black").place(x = 450, y = 20)
        time_periods = ["1 month", "3 months","15 days"]
        self.time_period_box = ttk.Combobox(self.window2, values=time_periods)
        self.time_period_box.place(x = 700, y = 20) 

        tk.Button(self.window2, text="Plot", command=self.plot_custom_data,bg = "Black",fg= "white").place(x=920,y = 20)
        self.predictBtn = tk.Button(self.frame1, text = 'Predict',font = ("Arial", 15), bg = "Black",fg= "white",command = self.predictions)
        self.predictBtn.place(x = 150, y = 300)

        if (frm == 'binance'):
            self.window2.title("Binance Coin")
            self.tickerSymbol = 'BNB-USD'
            open_label = tk.Label(self.frame1, text=f"Today's Price of Binance Coin",font=("Rubik",19,"bold"),bg = "#000080",fg= "white")
            open_label.place(x=10,y=20)

        
        if (frm == 'lite'):
            self.window2.title("Lite Coin")
            # Define the ticker symbol
            self.tickerSymbol = 'LTC-USD'
            open_label = tk.Label(self.frame1, text=f"Today's Price of Lite Coin",font=("Rubik",19,"bold"),bg = "#000080",fg= "white")
            open_label.place(x=10,y=20)
           
        self.today_data()
        # Define the function to plot the data
        self.plot_data(15)
        
    
    def today_data(self):
            df = yf.download(self.tickerSymbol, period = "1d")      
            print(df.head())

            self.today = df.copy()
            today = date.today()
            delta = timedelta(days=0)
            start_date = today - delta
            # print(start_date)
            date_label = tk.Label(self.frame1, text=f" Date : {start_date}",font=("Rubik",16),bg = "#000080",fg= "white")
            date_label.place(x=30,y=60)
            # Get today's open and close prices
            today_open = round(df.iloc[0]["Open"], 2)
            today_high = round(df.iloc[0]["High"], 2)
            today_low = round(df.iloc[0]["Low"], 2)
            today_volume = round(df.iloc[0]["Volume"], 2)
           

            open_label = tk.Label(self.frame1, text=f" Open : ${today_open}",font=("Rubik",13),bg = "#000080",fg= "white")
            open_label.place(x=50,y=130)
            High_label = tk.Label(self.frame1, text=f" High : ${today_high}",font=("Rubik",13),bg = "#000080",fg= "white")
            High_label.place(x=50,y=160)
            Low_label = tk.Label(self.frame1, text=f" Low : ${today_low}",font=("Rubik",13),bg = "#000080",fg= "white")
            Low_label.place(x=50,y=190)
            Volume_label = tk.Label(self.frame1, text=f" Volume : ${today_volume}",font=("Rubik",13),bg = "#000080",fg= "white")
            Volume_label.place(x=50,y=220)
   

    def plot_data(self, days):
            # Get the data for the specified time 
            today = date.today()
            delta = timedelta(days=days)
            start_date = today - delta
            df = yf.download(self.tickerSymbol, start=start_date, end=today)
            # print('data is ')
            # print(df)

            self.fig = Figure(figsize=(9,6.5), dpi=100)

            plot = self.fig.add_subplot(111)
            left, bottom, width, height = 0.15, 0.2, 0.8, 0.6
            plot.set_position([left, bottom, width, height])
            # plot.title(f'Open And Close price data of ')
            a = self.time_period_box.get() if self.time_period_box.get() else '15 days'
            plot.set_title(f'Open and Close Values for last {a}')
            df['Open'].plot(ax = plot,linewidth=1.5, color='green',label="Open Price")
            df['Close'].plot(ax = plot, linewidth=1.5, color='red', label='Close Price')
            plot.legend(loc='upper right')
            # plot.set_xlabel('Date')
            plot.set_ylabel('Price ($)')
            # plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8)
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame2)
            self.canvas.draw()

    
            self.canvas.get_tk_widget().pack()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            self.window2.mainloop()

        
    def plot_custom_data(self):
            try:
                # Get the user input for the time period
                time_period = self.time_period_box.get()
                if self.canvas:
                    self.canvas.get_tk_widget().destroy()
            
                # Validate the user input and plot the data for the specified time period
                if time_period == "1 month":
                    self.plot_data(30)
                elif time_period == "3 months":
                    self.plot_data(90)
                elif time_period == "15 days":
                     self.plot_data(15)
                else:
                    raise ValueError("Invalid input")
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))
                

    def predictions(self):
        if self.frm == 'binance':
            with open('Binance.pkl' , 'rb') as f:
                lr = pickle.load(f)
                print('today data is ', self.today)
                self.todayPrediction = lr.predict(self.today[["High","Low","Open", "Volume"]])
                print('today close is ', self.todayPrediction[0])

                p_label = tk.Label(self.frame1, text=f"Predicted Close Price",font=("Rubik",19,"bold"), bg = "#000080", fg = "white",)
                p_label.place(x=10,y=380)

                closep_label = tk.Label(self.frame1, text=f"Close Price: ${round(self.todayPrediction[0],2)}",font=("Rubik",15), bg = "white", fg = "black",borderwidth=1, relief="solid")
                closep_label.place(x=50,y=450)
            

        else:
            with open('Litecoin.pkl' , 'rb') as f:
                lr = pickle.load(f)
                print('today data is ', self.today)
                self.todayPrediction = lr.predict(self.today[["High","Low","Open", "Volume"]])
                print('today close is ', self.todayPrediction[0])
                p_label = tk.Label(self.frame1, text=f"Predicted Close Price",font = ("Rubik",19,"bold"), bg = "#000080", fg = "white")
                p_label.place(x=10,y=380)
                closep_label = tk.Label(self.frame1, text=f"Close Price: ${round(self.todayPrediction[0],2)}",font=("Rubik",15), bg = "white", fg = "black",borderwidth=1, relief="solid")
                closep_label.place(x=50,y=450)
    
    def back(self):
        self.window2.destroy()
        obj = gui3.MainWindow()

if __name__ == '__main__':
    CryptoPlot('binance')



