from tkinter import ttk

# =====================================
#       RIMWORLD TOGETHER VARS
# =====================================

'''
These dictionaries are intended to serve as a storage place for quickly and efficiently managing all tkinter objects 
related to each item and merging them with all the data related to the same item. Similarly, each dictionary represents
a JSON file, and each key represents every variable listed in each JSON.

This is meant to be quite modular, as in the event a new variable is added to a JSON, you would only need to add it 
as a new key following this index structure:

    0 = Tkinter Label
    1 = Widget type associated with the label. This string is used in mf.get_widget to create the specific widget for each variable.
    2 = Value variable to store the json original value
        - Note that in "Scale" widgets, this variable is a dictionary, as more data is needed.
    3 = Variable that stores the tkinter widget itself, and can be called with a var.get() method to read its current value
    4 = Variable that stores the tkinter popup window showing description info
    5 = Variable that stores the text that will be shown in the popup window

The "BUTTONS" key is intended to store as many buttons are needed per tab, so they remain bound to their respective tabs. 
'''

# CORE

action_values = {
    "Spy Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "BUTTONS": ["SAVE BUTTON"]
}

difficulty_values = {
    "Use Custom Difficulty": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Threat Scale": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Allow Big Threats": [ttk.Label, "Checkbutton", False, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Allow Violent Quests": [ttk.Label, "Checkbutton", False, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Allow Intro Threats": [ttk.Label, "Checkbutton", False, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Predators Hunt Humanlikes": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Allow Extreme Weather Incidents": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Crop Yield Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Mine Yield Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Butcher Yield Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Research Speed Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Quest Reward Value Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Raid Loot Points Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Trade Price Factor Loss": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Maintenance Cost Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Scaria Rot Chance": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Enemy Death On Downed Chance Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Colonist Mood Offset": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Food Poison Chance Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Man hunter Chance On Damage Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Player Pawn Infection Chance Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Disease Interval Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Enemy Reproduction Rate Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Deep Drill Infestation Chance Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Friendly Fire Chance Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Allow Instant Kill Chance": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Peaceful Temples": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Allow Cave Hives": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Unwavering Prisoners": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Allow Traps": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Allow Turrets": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Allow Mortars": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Classic Mortars": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Adaptation Effect Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Adaptation Growth Rate Factor Over Zero": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Fixed Wealth Mode": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Low Pop Conversion Boost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "No Babies Or Children": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Babies Are Healthy": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Child Raiders Allowed": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Child Aging Rate": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Adult Aging Rate": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Wastepack Infestation Chance Factor": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "BUTTONS": ["SAVE BUTTON"]
}

event_values = {
    "Raid Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Infestation Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "MechCluster Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Toxic Fallout Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Manhunter Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Wanderer Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Farm Animals Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Ship Chunk Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Trader Caravan Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "BUTTONS": ["SAVE BUTTON"]
}

server_config = {
    "IP": [ttk.Label, "Entry", "192.168.1.134", "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Port": [ttk.Label, "Entry", "25555", "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Max Players": [ttk.Label, "Entry", "100", "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Max Timeout In MS": [ttk.Label, "Entry", "5000", "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Verbose Logs": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Display Chat In Console": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "BUTTONS": ["SAVE BUTTON"]
}

server_values = {
    "Allow Custom Scenarios": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "BUTTONS": ["SAVE BUTTON"]
}

site_values = {
    "Personal Farmland Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Faction Farmland Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Farmland Reward Count": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Personal Quarry Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Faction Quarry Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Quarry Reward Count": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Personal Sawmill Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Faction Sawmill Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Sawmill Reward Count": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Personal Bank Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Faction Bank Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Bank Reward Count": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Personal Laboratory Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Faction Laboratory Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Laboratory Reward Count": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Personal Refinery Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Faction Refinery Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Refinery Reward Count": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Personal Herbal Workshop Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Faction Herbal Workshop Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Herbal Workshop Reward Count": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Personal Textile Factory Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Faction Textile Factory Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Textile Factory Reward Count": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Personal Food Processor Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Faction Food Processor Cost": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Food Processor Reward Count": [ttk.Label, "Scale", {"value": 50.0, "max_value": 100.0, "min_value": 0.0}, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "BUTTONS": ["SAVE BUTTON"]
}

whitelist = {
    "Use Whitelist": [ttk.Label, "Checkbutton", True, "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "Whitelisted Users": [ttk.Label, "Entry", "LIST HERE", "TK OBJECT", "TK POPUP", "TK POPUP TEXT"],
    "BUTTONS": ["SAVE BUTTON"]
}

# =====================================
#           MANAGER VARS
# =====================================

folders = {
    "Core": {
        "ActionValues": action_values,
        "DifficultyValues": difficulty_values,
        "EventValues": event_values,
        "ServerConfig": server_config,
        "ServerValues": server_values,
        "SiteValues": site_values,
        "Whitelist": whitelist
    },
    "Factions": {

    },
    "Logs": {
        "CHAT": "",
        "SYSTEM": ""
    },
    "Maps": {

    },
    "Mods": {
        "FORBIDDEN": "",
        "OPTIONAL": "",
        "REQUIRED": ""
    },
    "Saves": {

    },
    "Settlements": {

    },
    "Sites": {

    },
    "Users": {

    }
}
