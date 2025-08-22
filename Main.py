from pystray import Icon, Menu, MenuItem # type: ignore
from PIL import Image # type: ignore
import webbrowser,os

imageName: str = "file.ico"

URLs: dict[str,str] = {"Google": "https://www.google.com/",
                       "Youtube": "https://www.youtube.com/",
                       "Discord": "https://discord.com/channels/@me"}
subFolder: dict[str,str] = {"C": r"D:\Heet\CodingProjects\C",
                            "C#": r"D:\Heet\CodingProjects\C#",
                            "C++": r"D:\Heet\CodingProjects\C++",
                            "Java": r"D:\Heet\CodingProjects\Java",
                            "Python": r"D:\Heet\CodingProjects\Python"}

kritaFolder: dict[str,str] = {"Krita Test": r"D:\Heet\Krita\Project\test",
                              "Krita TileSprites": r"D:\Heet\Krita\Project\TileSprites"}

def loadIcon():
    return Image.open(imageName)

def openUrls(icon,item = None):
    if item and item.text in URLs:
        webbrowser.open(URLs[item.text])

def openFile(icon,item = None):
    if item and item.text in subFolder:
        os.startfile(subFolder[item.text])
        
def openKrita(icon,item = None):
    if item and item.text in kritaFolder:
        os.startfile(kritaFolder[item.text])

def onExit(icon):
    icon.stop()
    
def startFile(path):
    if os.path.exists(path):
       os.startfile(path)

def main():
    urlMenus = Menu(*(MenuItem(name, openUrls) for name in URLs))
    subFolderMenu = Menu(*(MenuItem(name, openFile) for name in subFolder))
    
    kritaMenu = Menu(*(MenuItem(name,openKrita) for name in kritaFolder))
    
    menu = Menu(
        MenuItem(" ",lambda: os.startfile(r"D:\Heet"),default=True,visible=False),
        Menu.SEPARATOR,
        MenuItem("Open Website",urlMenus),
        Menu.SEPARATOR,
        MenuItem("Open File",subFolderMenu),
        MenuItem("Krita",kritaMenu),
        Menu.SEPARATOR,
        MenuItem("Exit", onExit)
    )
    
    icon = Icon("Utility",loadIcon(),"Utilities",menu)
    icon.run()

if __name__ == "__main__":
    main()