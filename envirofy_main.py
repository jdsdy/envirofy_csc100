import tkinter as tk
import webview #py -m pip install pywebview

webUrlDict = {
  "QLD": "https://www.des.qld.gov.au/",
  "ACT": "https://www.environment.qct.gov.au/",
  "NSW": "https://www.epa.nsw.gov.au/",
  "SA": "https://www.epa.sa.gov.au/",
  "NT": "https://depws.nt.gov.au/",
  "WA": "https://wa.gov.au/organisation/department-of-water-and-environmental-regulation",
  "VIC": "https://www.epa.vic.gov.au",
  "TAS": "https://nre.tas.gov.au"}

def returnUrl():
  key = entry.get()
  if key in webUrlDict:
    resultLabel.config(text=webUrlDict[key])
    webview.create_window(key, webUrlDict[key])
    webview.start()
  else:
    resultLabel.config(text="Invalid State, try again")

root=tk.Tk()
root.title("Envirofy")

label = tk.Label(root, text="Envirofy notifications app")
label.pack()

resultLabel = tk.Label(root, text="")
resultLabel.pack()

entry = tk.Entry(root)
entry.pack()

entryButton = tk.Button(root, text="Select", command = returnUrl)
entryButton.pack()

root.mainloop()
