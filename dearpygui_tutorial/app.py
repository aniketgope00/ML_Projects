from dearpygui import dearpygui as dpg


dpg.create_context()

'''with dpg.window(label="Main Window", width = 600, height = 400):
    dpg.add_text("Hello, Dear PyGui!")
    
    def on_button_click(sender, app_data):
        entered_text = dpg.get_value(input_field)
        dpg.set_value(input_field, f"Hello, {entered_text}!")
    
    input_field = dpg.add_input_text(label="Input Text", default_value="Type here")
    dpg.add_button(label="Submit", callback=on_button_click)



with dpg.window(label="Secondary Window", width=300, height=200):
    dpg.add_text("This is a secondary window")
    with dpg.group(horizontal=True):
        dpg.add_button(label="Button 1")
        dpg.add_button(label="Button 2")
        dpg.add_button(label="Button 3")

with dpg.window(label="main window"):
    with dpg.group(horizontal=True):
        dpg.add_button(label="Button A")
        dpg.add_button(label="Button B")
        dpg.add_button(label="Button C")


'''

with dpg.window(label = "Data Viz"):
    dpg.add_text("Hello, Dear PyGui!")
    x_data = [1, 2, 3, 4, 5]
    y_data = [10, 20, 30, 40, 50]
    with dpg.plot(label = "line plot"):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label = "X Axis")
        dpg.add_plot_axis(dpg.mvYAxis, label = "Y Axis")
        line_series = dpg.add_line_series(x_data, y_data, label = "Line Series", parent = y_axis)


dpg.create_viewport(title="Main Window", width=600, height=400)




dpg.create_viewport(title='Custom Title', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()