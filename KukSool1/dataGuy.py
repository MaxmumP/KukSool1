import json
import os

class data_guy:
    def __init__(self, load_dir="", save_dir="", data_dir=""):
        global config_data
        if config_data.haskey("load_dir"):
            self.load_dir = config_data["load_dir"]
        if config_data.haskey("save_dir"):
            self.save_dir = config_data["save_dir"]
        if config_data.haskey("data_dir"):
            self.data_dir = config_data["data_dir"]
        # user may choose to override the config_data at some point
        if load_dir:
            self.load_dir=load_dir
        if save_dir:
            self.save_dir=save_dir
        if data_dir:
            self.data_dir=data_dir
        
    def load_all(self):
        # TODO: This could be more general- generic load of whatever categories the user chooses
        self.returndata={"Forms":[], "Techniques":[], "Weapons":[], "Exercises": [], "Meditations": []}
    
        form_file=os.path.join(config_data["load_dir"], "forms.txt")
        form_data=self.load_form(self.read_loadingfile(form_file))
        
        tech_file=file(os.path.join(config_data["load_dir"], "techniques.csv"), "r")
        weap_file=file(os.path.join(config_data["load_dir"], "weapons.csv"), "r")
        ex__file=file(os.path.join(config_data["load_dir"], "exercises.csv"), "r")
        med__file=file(os.path.join(config_data["load_dir"], "meditations.csv"), "r")
    
    def load_form(self, columns):
        form_data=[]
        for column in columns:
            print column
        
    def read_loadingfile(self, filepath):
        f = file(filepath,"r")
        title_line=""
        for line in f.readlines():
            if line.strip()[0]=="#":
                continue
            if title_line=="":
                title_line=line.strip()
                continue
            
        return title_line