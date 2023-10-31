import tkinter as tk
import tkinter.font as tkFont
import webview

webUrlDict = {
  "QLD": "https://www.des.qld.gov.au/",
  "ACT": "https://www.environment.qct.gov.au/",
  "NSW": "https://www.epa.nsw.gov.au/",
  "SA": "https://www.epa.sa.gov.au/",
  "NT": "https://depws.nt.gov.au/",
  "WA": "https://wa.gov.au/organisation/department-of-water-and-environmental-regulation",
  "VIC": "https://www.epa.vic.gov.au",
  "TAS": "https://nre.tas.gov.au"}

def confirmButtonCommand():
  key = userEntry.get()
  if key in webUrlDict:
    webview.create_window(key, webUrlDict[key])
    webview.start()
    entryPrompt.config(text="Please enter your state.")
  else:
    entryPrompt.config(text="Invalid State, try again")

root=tk.Tk()
root.title("Envirofy")
width=585
height=183
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root.configure(bg="#1e9fff")

titleLabel=tk.Label(root)
titleLabel["bg"] = "#1e9fff"
titleLabel["font"] = "Arial", 30, "bold"
titleLabel["fg"] = "#ffffff"
titleLabel["justify"] = "center"
titleLabel["text"] = "Envirofy"
titleLabel.place(x=38,y=20,width=180,height=45)

descriptionLabel=tk.Label(root)
descriptionLabel["bg"] = "#1e9fff"
ft = tkFont.Font(family='Arial',size=13)
descriptionLabel["font"] = ft
descriptionLabel["fg"] = "#ffffff"
descriptionLabel["justify"] = "center"
descriptionLabel["text"] = "Get up to date on the latest \nenvironmental policies."
descriptionLabel["anchor"] = "e"
descriptionLabel.place(x=20,y=100,width=212,height=56)

userEntry=tk.Entry(root)
userEntry["bg"] = "#ffffff"
userEntry["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
userEntry["font"] = ft
userEntry["fg"] = "#333333"
userEntry["justify"] = "center"
userEntry["text"] = "State"
userEntry.place(x=390,y=70,width=149,height=30)

entryPrompt=tk.Label(root)
entryPrompt["bg"] = "#1e9fff"
ft = tkFont.Font(family='Arial',size=12)
entryPrompt["font"] = ft
entryPrompt["fg"] = "#ffffff"
entryPrompt["justify"] = "center"
entryPrompt["text"] = "Please enter your state."
entryPrompt.place(x=380,y=30,width=169,height=30)

confirmButton=tk.Button(root)
confirmButton["bg"] = "#6c6c6c"
confirmButton["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10,weight="bold")
confirmButton["font"] = ft
confirmButton["fg"] = "#ffffff"
confirmButton["justify"] = "center"
confirmButton["text"] = "Confirm"
confirmButton.place(x=430,y=120,width=70,height=25)
confirmButton["command"] = confirmButtonCommand

root.mainloop()
