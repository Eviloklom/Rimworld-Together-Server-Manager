import tkinter
from tkinter import ttk

from bin.Variables import main_vars as mv
from bin.Functions import main_functions as mf

# =====================================
#              MAIN DATA
# =====================================

resolution = "1024x720"
title = "Rimworld Together Server Manager"

root = tkinter.Tk()

root.geometry(resolution)
root.resizable(0, 0)
root.title(title)
root.iconbitmap("ServerManager/img/app.ico")

# =====================================
#                TABS
# =====================================

# TAB CONTROL

tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill="both")

tabs = {
    "CORE": {
        "Action Values": ttk.Frame,
        "Difficulty Values": ttk.Frame,
        "Event Values": ttk.Frame,
        "Server Config": ttk.Frame,
        "Server Values": ttk.Frame,
        "Site Values": ttk.Frame,
        "Whitelist": ttk.Frame
    }

}

# TAB CREATION

for tab_name, subtabs in tabs.items():

    tab_frame = ttk.Frame(tab_control)
    tab_control.add(tab_frame, text=tab_name)

    subtabs_instances = {}  # Stores actual subtabs instances

    subtab_control = ttk.Notebook(tab_frame)
    subtab_control.pack(expand=1, fill="both")

    for subtab_name, subtab_frame_type in subtabs.items():

        subtab_frame = ttk.Frame(subtab_control)
        subtab_control.add(subtab_frame, text=subtab_name)

        # In-frame canvas for scrollbar
        canvas = tkinter.Canvas(subtab_frame)
        canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(subtab_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Inner frame for canvas to store widgets
        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        inner_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        subtabs_instances[subtab_name] = inner_frame

    tabs[tab_name] = subtabs_instances


# LOAD INFO TABS

core_tabs_data = {
    "Action Values": [tabs["CORE"]["Action Values"], mv.action_values],
    "Difficulty Values": [tabs["CORE"]["Difficulty Values"], mv.difficulty_values],
    "Event Values": [tabs["CORE"]["Event Values"], mv.event_values],
    "Server Config": [tabs["CORE"]["Server Config"], mv.server_config],
    "Server Values": [tabs["CORE"]["Server Values"], mv.server_values],
    "Site Values": [tabs["CORE"]["Site Values"], mv.site_values],
    "Whitelist": [tabs["CORE"]["Whitelist"], mv.whitelist],
}


def load_json_info_tabs():

    for tab in core_tabs_data:

        column_count = 0
        row_count = 0

        root_master = core_tabs_data[tab][0]
        library = core_tabs_data[tab][1]

        for key in library:
            if key != "BUTTONS":

                # Create label and widget linked
                label = library[key][0](root_master, text=key)
                widget = mf.get_widget(root_master, library[key][1], library[key])

                # Store label and widget linked on the proper dict
                library[key][0] = label
                library[key][2] = widget
                label = library[key][0]
                widget = library[key][2]

                # Create popup info window
                popup = tkinter.Toplevel(root)
                popup.overrideredirect(True)
                popup.withdraw()

                # Link text info with popup
                popup_label = ttk.Label(popup, text=library[key][5].replace("\\n", "\n"), wraplength=300, justify="left", background="light blue")
                popup_label.pack(padx=5, pady=2)

                # Store popup info window
                library[key][4] = popup

                label.bind("<Enter>", lambda event, popup=popup: mf.get_label_info("show", label, popup))
                label.bind("<Leave>", lambda event, popup=popup: mf.get_label_info("hide", label, popup))

                # Creates a grid
                label.grid(column=column_count, row=row_count, padx=10, pady=5, sticky="w")
                widget.grid(column=column_count+1, row=row_count, padx=10, pady=5, sticky="w")

                row_count += 1

                # Set max row count per column
                if row_count >= len(library)/2:
                    row_count = 0
                    column_count += 2

        library["BUTTONS"][0] = tkinter.Button(root_master, text="SAVE DATA", width=15, height=2, bg="black", fg="white", command=lambda tab=tab, library=library: mf.save_data(tab, "Core", library))
        library["BUTTONS"][0].grid(column=column_count+3, row=0, sticky="ew")


mf.load_data()  # Loads data from files (json and csv)
load_json_info_tabs()  # Loads data in root

root.mainloop()
