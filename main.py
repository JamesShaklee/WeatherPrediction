# -------------------------- IMPORTANT ---------------------------------
# Before you can run this code, you need to run two commands in your CMD
# 1. pip install customtkinter
# 2. pip install tkcalendar
# ----------------------------------------------------------------------

# Table of Contents
#   1. Setting up the Primary Containers of the UI
#   2. Populating the tabs with User Interface Elements
#   3. Methods for Creating basic UI Elements
#   4. Methods that are called as commands by UI elements

import customtkinter
from tkcalendar import Calendar
from datetime import datetime

class App(customtkinter.CTk):
    # ----------------------------------------------------------------------------------------------------------------
    # 1. Setting up the Primary Containers of the UI
    # ----------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()

        # Set the color scheme for the UI
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        self.title("AI GUI")
        self.geometry("1000x700")

        # Create a container to put a label in for the right side of the UI
        self.right_frame = customtkinter.CTkFrame(master=self, width=500, height=400)


        # Create a label to be used to display the results on the right hand side of the UI
        self.results_text_area = customtkinter.CTkLabel(master=self.right_frame, width=590, height=650,
                                                        fg_color='silver', text_color='black', font=('Arial', 20), text='',
                                                        justify='left', anchor='nw')

        # Create a tab view that will be added to the left side of the UI
        self.tabs = self.create_tab_view()

        # Note: in CTK grids do not have to be established before adding item to them, but only one method of adding
        # elements to an area can be used, so no Grid and Pack in the same area. To change methods, you have to
        # create a frame to use the new method within.

        # Add the Tab View and Frame to the grid and add the results_text_area to the Frame.
        self.tabs.grid(row=0, column=0, padx=5, pady=5)
        self.right_frame.grid(row=0, column=1, padx=1, pady=1)
        self.results_text_area.pack(pady=5, padx=5)


        # Create the tab view that will hold the UI elements for each use case.
    def create_tab_view(self):
        self.tab_view_builder = customtkinter.CTkTabview(self, width=380, height=650, fg_color='silver')

        # Create the individual tabs
        self.tab_1 = self.tab_view_builder.add('Tab 1')
        self.tab_2 = self.tab_view_builder.add('tab 2')

        # Add UI elements to the tabs
        self.populate_tab_1()
        #self.populate_tab_2()

        return self.tab_view_builder

    # ----------------------------------------------------------------------------------------------------------------
    # 2. Populating the tabs with User Interface Elements
    # ----------------------------------------------------------------------------------------------------------------
        # Adds UI elements to Tab 1 of the Tab View
    def populate_tab_1(self):
        # Call methods to create each UI element
        self.tab_1_header_label = self.create_label(self.tab_1,'Enter the day\'s information you want\n to predict the chance of rain for.',20)
        self.tab_1_location_label = self.create_label(self.tab_1, 'Select a Location', 15)
        self.tab_1_location_combobox = self.create_combo_box(self.tab_1)
        self.tab_1_calender_label = self.create_label(self.tab_1,'Select a Day', 15)
        self.tab_1_calender = self.create_calendar(self.tab_1)
        self.tab_1_humidity_label = self.create_label(self.tab_1,'Humidity Level (%)', 15)
        self.tab_1_humidity_slider = self.create_slider(self.tab_1,0,100, self.get_tab_1_humidity_slider_number, 0)
        self.tab_1_humidity_slider_value_label = self.create_label(self.tab_1,self.tab_1_humidity_slider.get(), 15)
        self.tab_1_temperature_label = self.create_label(self.tab_1,'Temperature (F)', 15)
        self.tab_1_temperature_slider = self.create_slider(self.tab_1,32, 95, self.get_tab_1_temperature_slider_number, 32)
        self.tab_1_temperature_slider_value_label = self.create_label(self.tab_1,self.tab_1_temperature_slider.get(), 15)
        self.tab_1_submit_button = self.create_button(self.tab_1, self.tab1_submit)


        # Add the UI elements to the tab with padding
        self.tab_1_header_label.pack(pady=5, padx=5)
        self.tab_1_location_label.pack(pady=5, padx=5)
        self.tab_1_location_combobox.pack(pady=5, padx=5)
        self.tab_1_calender_label.pack(pady=5, padx=5)
        self.tab_1_calender.pack(fill='both', expand=True, padx=20)
        self.tab_1_humidity_label.pack(pady=5, padx=5)
        self.tab_1_humidity_slider.pack(pady=5, padx=5)
        self.tab_1_humidity_slider_value_label.pack(pady=5, padx=5)
        self.tab_1_temperature_label.pack(pady=5, padx=5)
        self.tab_1_temperature_slider.pack(pady=5, padx=5)
        self.tab_1_temperature_slider_value_label.pack(pady=5, padx=5)
        self.tab_1_submit_button.pack(pady=5, padx=5)


    #----------------------------------------------------------------------------------------------------------------
    # 3. Methods for Creating basic UI Elements
    #----------------------------------------------------------------------------------------------------------------
    def create_label(self, master, text, font_size):
        return customtkinter.CTkLabel(master=master, text=text, text_color='black', font=('Arial', font_size))

    def create_slider(self,master, starting_value, ending_value, command, default_value):
        slider_builder = customtkinter.CTkSlider(master=master, from_=starting_value, to=ending_value, command=command)
        # Starting position of the slider
        slider_builder.set(default_value)
        return slider_builder

    def create_combo_box(self, master):
        locations = ['Chicago','Dallas','Houston','Los Angeles','New York','Philadelphia','Phoenix','San Antonio','San Diego','San Jose']
        return customtkinter.CTkComboBox(master=master, values=locations, font=('Arial', 15), dropdown_font=('Arial', 15), corner_radius=25, width=200, justify='center' )

    def create_calendar(self, master):
        return Calendar(master=master, selectmode='day', font=('Arial', 12),
                        mindate=datetime(2024,1,1), maxdate=datetime(2024,5,18),
                        showweeknumbers=False, showothermonthdays=False, date_pattern='m/d/yyyy')

    def create_button(self, master, command):
        return  customtkinter.CTkButton(master=master, text="Submit", font=('Arial', 20), command=command)



    # ----------------------------------------------------------------------------------------------------------------
    # 4. Methods that are called as commands by UI elements
    # ----------------------------------------------------------------------------------------------------------------
        # Updates the humidity slider value label each time the slider is moved on tab 1
    def get_tab_1_humidity_slider_number(self, value):
        self.tab_1_humidity_slider_value_label.configure(text=int(value))

        # Updates the temperature slider value label each time the slider is moved on tab 1
    def get_tab_1_temperature_slider_number(self, value):
        self.tab_1_temperature_slider_value_label.configure(text=int(value))

        # Prints the current values of the elements in tab 1 to the textbox on the right side of the UI
    def tab1_submit(self):
        # Clears any old text from the textbox before adding the new text
        self.clear_textbox()

        text =  (f'Location: {self.tab_1_location_combobox.get()}'
                 f'\nDate: {self.tab_1_calender.get_date()} '
                 f'\nHumidity: {int(self.tab_1_humidity_slider.get())}%'
                 f'\nTemperature: {int(self.tab_1_temperature_slider.get())}F')

        #self.textbox.insert("0.0", text)
        self.results_text_area.configure(text=text)

        # Clears the text from the textbox if text is found in the textbox
    def clear_textbox(self):
        self.text = self.results_text_area.cget('text')
        if self.text != "":
            self.results_text_area.configure(text='')



app = App()
app.mainloop()
