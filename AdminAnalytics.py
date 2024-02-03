import tkinter as tk

from pandas import DataFrame #to store the data
import matplotlib.pyplot as plt #to create a graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #to plot the graph in the GUI
from DatabaseHelper import *

class Analytics:
    def __init__(self):
        self.temp_root = tk.Toplevel()
        self.add_bar_graph("Total earnings per day")
        self.add_line_graph("Total orders per day")

    def get_food_total_data(self):
        query = """ Select OrderDate, FoodTotal 
                    from world.foodorder
                    where IsComplete=1
                    order by OrderDate
                """
        result = DatabaseHelper.get_all_data(query)

        df1 = DataFrame(result[1:], columns=result[0]).groupby("OrderDate").sum()
        return df1

    def get_total_orders_data(self):
        query = """ Select OrderDate, FoodOrderId 
                    from world.foodorder
                    order by OrderDate
                """
        result = DatabaseHelper.get_all_data(query)

        df = DataFrame(result[1:], columns=result[0]).groupby("OrderDate").count()
        return df

    def add_bar_graph(self, title):
        #1. get the data from db and create the dataframe
        #2. create the figure
        #2. create a subplot in the figure
        #3. create the GUI graph and link figure(2)
        # Plot the dataframe(1) in the subplot (2)



        # put the data in the data frame and give it back
        df1 = self.get_food_total_data()

        #create the graph
        figure1 = plt.Figure(figsize=(7, 5), dpi=100)
        #create the subplot to store it in the figure
        ax1 = figure1.subplots()

        bar1 = FigureCanvasTkAgg(figure1, self.temp_root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        #bar, barh, line,area,pie
        df1.plot(kind='bar', legend=True, ax=ax1, fontsize=10)
        ax1.set_title(title)

    def add_line_graph(self, title):
        df2 = self.get_total_orders_data()

        figure2 = plt.Figure(figsize=(7, 4), dpi=100)
        ax2 = figure2.subplots()

        line2 = FigureCanvasTkAgg(figure2, self.temp_root)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2.plot(kind='line', legend=True, ax=ax2, color='red', marker='o', fontsize=10)
        ax2.set_title(title)


r=tk.Tk()
a=Analytics()
r.mainloop()