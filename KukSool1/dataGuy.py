import pickle
import os
import time
import Form

class dataGuy:
    def __init__(self, config_data, load_dir="", save_dir="", data_dir=""):
        self.config_data=config_data
        if self.config_data.has_key("load_dir"):
            self.load_dir = config_data["load_dir"]
        if self.config_data.has_key("save_dir"):
            self.save_dir = config_data["save_dir"]
        if self.config_data.has_key("data_dir"):
            self.data_dir = config_data["data_dir"]
        # user may choose to override the config_data at some point
        if load_dir:
            self.load_dir=load_dir
        if save_dir:
            self.save_dir=save_dir
        if data_dir:
            self.data_dir=data_dir
            
        self.loaded={}
    
    def save_data(self, data, filename="", path=""):
        full_path=""
        if not filename:
            filename="temp_"+time.mktime(time.localtime())
        if not path and self.data_dir:
            path=self.data_dir
        # if any path was set, join filename to it
        if path:
            full_path=os.path.join(path,filename)
        else:
            full_path=os.path.join(".",filename)
        if os.path.isfile(full_path):
            overwrite=raw_input("%s exists, overwrite? (y/n) " % full_path)
            if overwrite.upper()=="Y":
                write_file=open(full_path,"wb")
                pickle.dump(data, write_file)
                write_file.close()
                print "Data saved in %s" % full_path
                return True
            else:
                print "Quit without saving."
                return False
        elif not os.path.isdir(path):
            os.mkdir(path)
        write_file=open(full_path,"wb")
        pickle.dump(data, write_file)
        write_file.close()
        return True

    def load_all(self, load_dir=""):
        # TODO: This could be more general- generic load of whatever categories the user chooses
        #self.loaded={"Forms":[], "Techniques":[], "Weapons":[], "Exercises": [], "Meditations": []}
        if load_dir:
            self.load_dir=load_dir
        form_file=os.path.join(self.load_dir, "forms.txt")
        if os.path.isfile(form_file):
            print "Loading forms"
            self.loaded["Forms"]=self.read_loadingfile(form_file)
        # FIXME: Need to add other object loading
        tech_file=os.path.join(self.load_dir, "techniques.txt")
        if os.path.isfile(form_file):
            print "Loading techniques"
            self.loaded["Techniques"]=self.read_loadingfile(tech_file)
        
        '''weap_file=file(os.path.join(config_data["load_dir"], "weapons.csv"), "r")
        ex__file=file(os.path.join(config_data["load_dir"], "exercises.csv"), "r")
        med__file=file(os.path.join(config_data["load_dir"], "meditations.csv"), "r")'''
        return self.loaded
    
    def load_subset(self, file_contents, file_name, load_dir=""):
        if load_dir:
            self.load_dir=load_dir
        load_file=os.path.join(self.load_dir, file_name)
        if os.path.isfile(load_file):
            self.loaded[file_contents]=self.read_loadingfile(load_file)
     
    def read_loadingfile(self, filepath):
        f = file(filepath,"rb")
        file_data=pickle.load(f)
        return file_data
    
if __name__ == '__main__':
    test_form=Form.Form("Jung Gum Hyung", 1, "Straight Sword Form", 1, 70)
    data=dataGuy({})
    print test_form
    data.save_data(test_form, "forms.txt", "Data")
    data.load_all("Data")
    print data.loaded