import tkinter as tk
import yfinance as yf

window = tk.Tk()
window.title("Stock info")

topWidget = tk.Frame(window)
label = tk.Label(topWidget,text="Write stock ticker: ")
label.pack(side=tk.LEFT)
entry=tk.Entry(topWidget)
entry.pack(side= tk.RIGHT)
topWidget.pack()

scrollbar = tk.Scrollbar(window)
textBox = tk.Text(window, height= 15, width= 90, padx=5, pady=5, 
                  font="Helvetica 12")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textBox.pack(expand=True, fill=tk.BOTH)
scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand= scrollbar.set)

def downloadData(e):
    textBox.delete("1.0", tk.END)
    stock = str(e.widget.get())

    if not stock:
        print("No stock tiker")
        return
    
    stock = stock.upper().strip()
    print("Download stock data: ", stock)

    stockData = yf.Ticker(stock)
    print(stockData.info)

    textBox.insert(tk.END, "Ticker: " + stock + " \n\n")
    
    for key in stockData.info.keys():
        try:
            v = str(key) + ": " + stockData.info[str(key)] + " \n\n "
            textBox.insert(tk.END, v)
        except:
            pass
    
    history = stockData.history(period="1mo", interval = "1d")
    textBox.insert(tk.END, history)

entry.bind("<Return>", downloadData)



window.mainloop()