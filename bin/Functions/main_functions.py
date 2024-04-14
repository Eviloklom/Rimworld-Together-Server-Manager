import csv
import json
import tkinter

from tkinter import ttk, messagebox
from bin.Variables import main_vars as mv


# =====================================
#               READERS
# =====================================
def read_csv(file):

    file_path = f"ServerManager/csv/{file}.csv"
    data = []

    with open(file_path, newline='', encoding="UTF-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    return data


def read_json(file):

    with open(file) as f:
        data = json.load(f)

    return data

# =====================================
#              GETTERS
# =====================================


def get_widget(tab, widget, library):

    # library = [2 = WIDGET VAR DATA, 3 = WIDGET VAR OBJECT]

    if widget == "Scale":
        library[3] = tkinter.DoubleVar(master=tab, value=library[2]["value"])
        return tkinter.Scale(tab, from_=library[2]["min_value"], to=library[2]["max_value"], orient="horizontal", variable=library[3], resolution=0.1)

    if widget == "Checkbutton":
        library[3] = tkinter.BooleanVar(master=tab, value=library[2])
        return ttk.Checkbutton(tab, variable=library[3])

    if widget == "Entry":
        library[3] = tkinter.StringVar(master=tab, value=library[2])
        return tkinter.Entry(master=tab, textvariable=library[3])

    return ttk.Label(tab, text="WIDGET ERROR")


def get_label_info(mode, label, popup):

    if mode == "show":
        # Mouse coordinates
        x = label.winfo_pointerx() + 10  # x offset
        y = label.winfo_pointery() + 10  # y offset

        popup.geometry(f"+{x}+{y}")
        popup.configure(background="light blue")
        popup.deiconify()

    if mode == "hide":
        popup.withdraw()


def get_csv_data(data, var_name, item, item2):

    var_name = f"{var_name}.json"

    for opt in data:

        if opt[var_name] == item:
            return opt[item2]


# =====================================
#           DATA MANAGEMENT
# =====================================
def save_data(file, folder, library):

    file_path = f"{folder}/{file.replace(' ', '')}.json"

    data_json = read_json(file_path)

    for key in library:
        if key != "BUTTONS":
            data_json[key.replace(" ", "")] = library[key][3].get()
            # print(f"{key} -> Value {library[key][3].get()}")

    with open(file_path, "w") as f:
        json.dump(data_json, f, indent=2)

    messagebox.showinfo(title="DATA SAVED", message=f"Data changes to {file.replace(' ', '')}.json saved successfully!")


def load_data():

    for folder in mv.folders:
        for file in mv.folders[folder]:
            if folder == "Core":

                file_path = f"{folder}/{file}.json"

                csv_data = read_csv(file)
                json_data = read_json(file_path)

                library = mv.folders[folder][file]

                for key in library:
                    if key != "BUTTONS":
                        var_name = key.replace(" ", "")
                        if library[key][1] in ["Checkbutton", "Entry"]:
                            library[key][2] = json_data[var_name]  # Gets the json current value

                        if library[key][1] == "Scale":
                            library[key][2]["value"] = json_data[var_name] # Gets the json current value
                            library[key][2]["max_value"] = get_csv_data(csv_data, file, key.replace(" ", ""), "Max Range")
                            library[key][2]["min_value"] = get_csv_data(csv_data, file, key.replace(" ", ""), "Min Range")

                        library[key][5] = get_csv_data(csv_data, file, key.replace(" ", ""), "Description") # Gets the label description
