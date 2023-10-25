from tkinter import *
from PIL import Image,ImageTk
import gui3

class MainWindow():

    def __init__(self) -> None:
        #Set the geometry
        self.root = Tk()
        self.root.title("Cryptocurrency Price Predictor")
        self.root.geometry("1300x680")

        frame = Canvas(self.root, width=1300, height = 680)
        frame.place(x = 0, y = 0)
        #Load the image
        img= Image.open("img.png").resize((1300, 680))


        #Convert To photoimage
        tkimage= ImageTk.PhotoImage(img)

        #Display the Image
        # label=Label(frame,image=tkimage)
        # label.pack()

        #Heading with transparent background
        frame.create_image(0, 0, anchor=NW, image = tkimage)
        frame.create_text(650, 100, text = 'Cryptocurrency Price Predictor', fill='white', font=('Rubik', 48, 'bold'))

        frame.create_text(900,300,text = "You can predict the future prices of two popular \n cryptocurrencies i.e Litecoin and Binance Coin. \nTo get started, simply click on the button of\n the cryptocurrency you are interested in",fill='white', font=('Rubik', 18,"bold"))
        # frame.create_text(650,150,text = "(Predict the future prices of Litecoin and Binance Coin)",fill='white', font=('Rubik', 18,"bold"))


        #Binance coin Window
        def Button1_clicked():
            print("Button1 clicked")
            
            self.root.destroy()
            obj = gui3.CryptoPlot('binance')

        #litecoin Window
        def Button2_clicked():
            print("Button1 clicked")
            
            self.root.destroy()
            obj = gui3.CryptoPlot('lite')


        predict_button = Button(self.root, text="Binance coin (BNB)",bg = "white",fg ="black",font = ("Arial", 20),command = Button1_clicked)
        # predict_button.pack(pady=20)
        predict_button.place(x=600,y=470)
        

        predict_button = Button(self.root, text="Litecoin (LTC)", bg = "white",fg ="black",font = ("Arial", 20),command = Button2_clicked,)
        # predict_button.pack(pady=20)
        predict_button.place(x=980,y=470)

        frame.create_text(900,600,text = "This model may generate inaccurate predictions",fill='white', font=('Rubik', 18))

        self.root.mainloop()


if __name__ == '__main__':
    MainWindow()


