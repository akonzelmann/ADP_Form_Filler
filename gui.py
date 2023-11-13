import PySimpleGUI as sg
import afpmd
import afres
import afmd

# Change to your python project folder
folderPath = r"C:\Users\Adam\Desktop\pythonProject"

sg.theme('DarkAmber')

names = ["Application for Funding Pressure Modification Devices", "Application for Funding Respiratory Equipment Services", "Application for Funding Mobility Devices"]
lst = sg.Combo(names, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-COMBO-')

layout = [[sg.Text("ADP Form Generator", font=('Arial Bold', 14))],
          [lst],
          [sg.Text("Choose output folder: ", font=('Arial Bold', 14)), sg.Input(key="-IN2-", change_submits=True, font=('Arial Bold', 14)), sg.FolderBrowse(key="-IN-")],
          [sg.Text("Enter number of documents:", font=('Arial Bold', 14)), sg.InputText(1, font=('Arial Bold', 14))],
          [sg.Button('Ok', font=('Arial Bold', 14)), sg.Button('Cancel', font=('Arial Bold', 14))]
        ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(values["-IN2-"])

    if event == "Ok" and values['-COMBO-'] == "Application for Funding Pressure Modification Devices":
        afpmd.mergePdfs(0, 0, 0, values["-IN2-"], True)
        print("Generating AFPMD...")
        afpmd.generatePDF(int(values[0]))
        window.refresh()
        break

    if event == "Ok" and values['-COMBO-'] == "Application for Funding Respiratory Equipment Services":
        afres.mergePdfs(0, 0, 0, values["-IN2-"], True)
        print("Generating AFRES...")
        afres.generatePDF(int(values[0]))
        window.refresh()
        break

    if event == "Ok" and values['-COMBO-'] == "Application for Funding Mobility Devices":
        afmd.mergePdfs(0, 0, 0, values["-IN2-"], True)
        print("Generating AFMD...")
        afmd.generatePDF(int(values[0]))
        window.refresh()
        break

    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break
window.close()