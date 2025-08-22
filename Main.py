from pystray import Icon, Menu, MenuItem
from PIL import Image
import webbrowser,os,json,threading
import tkinter as tk
from tkinter import ttk,filedialog,messagebox

#File Variables
jsonFile = "directory.json"
imageFile = "file.ico"

#UI control variable
inAction = False

#defaults
defaultJsonVal = '[{"URLs": {}},{"Files": {}},{"Other": {}}]'


def loadImage():
    return Image.open(imageFile)

def loadJson():
    if os.path.exists(jsonFile):
        with open(jsonFile,"r") as file:
            return json.load(file)
    with open(jsonFile,"x") as file:
        file.write(defaultJsonVal)
        return json.load(file)
    
def saveJson(data):
    with open(jsonFile,"w") as file:
        json.dump(data, file,indent=4)
        
#Variable for doing json stuff
jsonData = loadJson()
URLs = jsonData[0]["URLs"]
Files = jsonData[1]["Files"]
Other = jsonData[2]["Other"]
Default = jsonData[3]["Default"]

def openURL(icon,item):
    if item and item.text in URLs:
        webbrowser.open(URLs[item.text])

def openFiles(icon,item):
    if item and item.text in Files:
        os.startfile(Files[item.text])
        
def openOther(icon,item):
    if item and item.text in Other:
        try:
            os.startfile(Other[item.text])
        except:
            try:
                webbrowser.open(Other[item.text])
            except:
                pass

def onExit(icon):
    icon.stop()
    
def changeDefault():
    def wrapper():
    
        jsonData[3]["Default"] = filedialog.askdirectory()
        
        saveJson(jsonData)
    threading.Thread(target=wrapper).start()

def showAddUI(icon):
    def runUI():
        global inAction
        
        def onClose():
            global inAction
            root.destroy()
            inAction = False
        
        root = tk.Tk()
        root.geometry("300x150")
        inAction = True

        nameLabel = tk.Label(root, text="Enter Name: ")
        nameLabel.grid(row=0, column=0)
        nameEntry = tk.Entry(root)
        nameEntry.grid(row=0, column=1)

        directoryLabel = tk.Label(root, text="Enter directory: ")
        directoryLabel.grid(row=1, column=0)
        directoryEntry = tk.Entry(root)
        directoryEntry.grid(row=1, column=1)

        def browseFolder():
            selectedFile = filedialog.askdirectory(title="Select Folder")
            if selectedFile:
                directoryEntry.delete(0, tk.END)
                directoryEntry.insert(0, selectedFile)

        def submit():
            if nameEntry.get() == "" or directoryEntry == "":
                messagebox.showerror("Empty field", " A Field is left Empty")
            
            if dropdown.get() == "URLs":
                URLs.update({nameEntry.get(): directoryEntry.get()})
            elif dropdown.get() == "Files":
                Files.update({nameEntry.get(): directoryEntry.get()})
            elif dropdown.get() == "Other":
                Other.update({nameEntry.get(): directoryEntry.get()})
                
            newJson = [{"URLs": URLs}, {"Files": Files}, {"Other": Other},{"Default": Default}]
            saveJson(newJson)
            icon.menu = updateMenu(icon)

            onClose()
            
        

        browseBtn = tk.Button(root, text="Browse", command=browseFolder)
        browseBtn.grid(row=1, column=2)

        dropdownList = ["URLs", "Files", "Other"]
        dropdown = ttk.Combobox(root, values=dropdownList, state="readonly")
        dropdown.grid(row=2, column=1)
        dropdown.current(0)

        submitBtn = tk.Button(root, text="Add", command=submit)
        submitBtn.grid(row=4, column=1)

        cancelBtn = tk.Button(root, text="Cancel", command=onClose)
        cancelBtn.grid(row=4, column=2)
        
        root.protocol("WM_DELETE_WINDOW",onClose)

        root.mainloop()
        
    if not inAction:
        threading.Thread(target=runUI).start()
    else:
        messagebox.showerror("Something in Action", "A UI is already running pls close it to open a new one")
    
def showRemoveUI(icon):
    def runUI():
        global inAction
        def onClose():
            global inAction
            root.destroy()
            inAction = False

        root = tk.Tk()
        root.geometry("500x300")
        inAction = True
                
        dropdownList = ["URLs", "Files", "Other"]
        dropdown = ttk.Combobox(root,values= dropdownList,state= "readonly")
        dropdown.grid(row=0,column=0)
        dropdown.current(0)
        def clearList(listBox):
            listBox.delete(0,tk.END)
            
        def insertList(insertionType,listBox):
            clearList(listBox)
            if insertionType == "URLs":
                for item in URLs:
                    listBox.insert(tk.END,item)
            elif insertionType == "Files":
                for item in Files:
                    listBox.insert(tk.END,item)
            elif insertionType == "Other":
                for item in Other:
                    listBox.insert(tk.END,item)
                    
        def getCurrentType():
            return dropdown.get()
        
        def showList():
            currentType = getCurrentType()
            
            insertList(currentType,myListBox)
        
        def removeItem():
            try:
                selectedItem = myListBox.selection_get()
                try:
                    if getCurrentType() == "URLs":
                        URLs.pop(selectedItem)
                        # print(f"{selectedItem} = {type(selectedItem)}")
                        
                    elif getCurrentType() == "Files":
                        Files.pop(selectedItem)
                        
                    elif getCurrentType() == "Other":
                        Other.pop(selectedItem)
                        
                except:
                    messagebox.showerror("Types don's match","Selected Item type and Dropdown item type is not same")
                   
                
                newJson = [{"URLs": URLs}, {"Files": Files}, {"Other": Other},{"Default": Default}]
                saveJson(newJson)
                showList()
                icon.menu = updateMenu(icon)
                
                
            except:
                messagebox.showerror("Item not Selected","Select an Item to delete")
            
        
        myListBox = tk.Listbox(root)
        myListBox.grid(row=1,column=0)
        
        showList()
        
        updateBtn = tk.Button(root,text="Update List",command=showList)
        updateBtn.grid(row=0,column=1)
        
        cancleBtn = tk.Button(root,text="Cancle",command=onClose)
        cancleBtn.grid(row=2,column=1)
        
        deleteBtn = tk.Button(root,text="Delete",command=removeItem)
        deleteBtn.grid(row=2,column=2)
        
        root.protocol("WM_DELETE_WINDOW",onClose)
        
        root.mainloop()
    if not inAction:
        threading.Thread(target=runUI).start()
    else:
        messagebox.showerror("Something in Action", "A UI is already running pls close it to open a new one")

def updateMenu(icon):
    jsonData = loadJson()
    URLs = jsonData[0]["URLs"]
    Files = jsonData[1]["Files"]
    Other = jsonData[2]["Other"]
    
    urlMenu = Menu(*(MenuItem(name,openURL) for name in URLs),)
    fileMenu = Menu(*(MenuItem(name,openFiles) for name in Files))
    otherMenu = Menu(*(MenuItem(name,openOther) for name in Other))
    
    if jsonData[3]["Default"] != "":
        return Menu(
            MenuItem("",lambda: os.startfile(jsonData[3]["Default"]), visible=False,default=True),
            Menu.SEPARATOR,
            MenuItem("Open URLs",urlMenu),
            Menu.SEPARATOR,
            MenuItem("Open File",fileMenu),
            Menu.SEPARATOR,
            MenuItem("Other",otherMenu),
            Menu.SEPARATOR,
            MenuItem("Add More Options", showAddUI),
            MenuItem("Remove Options",showRemoveUI),
            Menu.SEPARATOR,
            MenuItem("Change Default",changeDefault),
            Menu.SEPARATOR,
            MenuItem("Exit", onExit)
        )
    return Menu(
        Menu.SEPARATOR,
        MenuItem("Open URLs",urlMenu),
        Menu.SEPARATOR,
        MenuItem("Open File",fileMenu),
        Menu.SEPARATOR,
        MenuItem("Other",otherMenu),
        Menu.SEPARATOR,
        MenuItem("Add More Options", showAddUI),
        MenuItem("Remove Options",showRemoveUI),
        Menu.SEPARATOR,
        MenuItem("Change Default",changeDefault),
        Menu.SEPARATOR,
        MenuItem("Exit", onExit)
    )
    

def main():
    loadJson()
    icon = Icon("Utility",loadImage(),"Utilities")
    icon.menu = updateMenu(icon)
    icon.run()

if __name__ == "__main__":
    main()