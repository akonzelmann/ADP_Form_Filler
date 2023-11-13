import io
import os
import math
import PyPDF2
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader

from reportlab.pdfbase.ttfonts import TTFont

# Import other scripts in project
import itemList

# Register custom fonts
pdfmetrics.registerFont(TTFont('AdamsFont-Regular', 'AdamsFont-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SFSans', 'SFScribbledSans.ttf'))
pdfmetrics.registerFont(TTFont('DavysCrappy', 'DavysCrappyWrit.ttf'))
pdfmetrics.registerFont(TTFont('Hoffman', 'hoffm___.ttf'))
pdfmetrics.registerFont(TTFont('MessySketch', 'MessySketch-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Nothing', 'NothingYouCouldDo.ttf'))

# Register custom checkmark font
pdfmetrics.registerFont(TTFont('Checkmarks', 'Checkmarks-Regular.ttf'))

# Dictionary of fonts
fonts = {
    "AdamsFont-Regular": 19,
    "DavysCrappy": 23,
    "Hoffman": 20,
    "MessySketch": 20,
    "Nothing": 20
}

# Variable keeps track of the current page number
currentPage = 0


class CustomCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.styles = getSampleStyleSheet()

    def lastName(self, x, y):
        r = random.randint(0, len(itemList.lastName) - 1)
        self.drawString(x, fontY - y, itemList.lastName[r])

    def firstName(self, x, y):
        r = random.randint(0, len(itemList.firstName) - 1)
        self.drawString(x, fontY - y, itemList.firstName[r])

    def middleInitial(self, x, y):
        r = random.randint(0, len(itemList.middleInitial) - 1)
        self.drawString(x, fontY - y, itemList.middleInitial[r])

    def healthNumber(self, x, y):
        s = ''
        for i in range(0, 10):
            r = random.randint(0, 9)
            s = s + str(r)
        return self.drawString(x, fontY - y, s)

    def healthVersion(self, x, y):
        v0 = random.randint(0, len(itemList.middleInitial) - 1)
        v1 = random.randint(0, len(itemList.middleInitial) - 1)
        self.drawString(x, fontY - y, itemList.middleInitial[v0] + itemList.middleInitial[v1])

    def date(self, x, y, minYear=1900, maxYear=2023):
        year = random.randint(minYear, maxYear)
        month = random.randint(1, 12)
        day = 0
        if month == 2:
            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                day = random.randint(1, 29)
            else:
                day = random.randint(1, 28)
        elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            day = random.randint(1, 31)
        elif month == 4 or 6 or 9 or 11:
            day = random.randint(1, 30)

        if month < 10:
            month = "0" + str(month)
        if day < 10:
            day = "0" + str(day)

        if fontName == "Nothing":
            self.drawString(x, fontY - y, str(year) + "-" + str(month) + "-" + str(day))
        else:
            self.drawString(x, fontY - y, str(year) + "/" + str(month) + "/" + str(day))

    def checkboxLR(self, x1, x2, y):
        yesNo = random.randint(0, 1)
        rngCheckbox = random.randint(0, 10)
        self.setFont("Checkmarks", 20)
        if yesNo == 0:
            self.drawString(x1, 792 - y, itemList.checkmarks[rngCheckbox])
        else:
            self.drawString(x2, 792 - y, itemList.checkmarks[rngCheckbox])
        self.setFont(fontName, fontSize)
        return yesNo

    def checkboxTF(self, x, y, chance=1):
        drawChance = random.randint(0, chance)
        self.setFont("Checkmarks", 20)
        rngCheckbox = random.randint(0, 10)
        if drawChance == 0:
            self.drawString(x, 792 - y, itemList.checkmarks[rngCheckbox])
        self.setFont(fontName, fontSize)

    def checkbox(self, x, y):
        self.setFont("Checkmarks", 20)
        rngCheckbox = random.randint(0, 10)
        self.drawString(x, 792 - y, itemList.checkmarks[rngCheckbox])
        self.setFont(fontName, fontSize)

    def longTermCareHome(self, x, y):
        r = random.randint(0, len(itemList.longTermCareHomes) - 1)
        self.drawString(x, fontY - y, itemList.longTermCareHomes[r])

    def randomNumber(self, x, y, min=1, max=1000):
        r = random.randint(min, max)
        self.drawString(x, fontY - y, str(r))

    def streetName(self, x, y):
        r = random.randint(0, len(itemList.streetName) - 1)
        self.drawString(x, fontY - y, itemList.streetName[r])

    def lotConcRR(self, x, y):
        r = random.randint(0, len(itemList.streetName) - 1)
        rdNumber = random.randint(1, 5000)
        self.drawString(x, fontY - y, str(rdNumber) + " " + itemList.streetName[r])

    def city(self, x, y):
        r = random.randint(0, len(itemList.city) - 1)
        self.drawString(x, fontY - y, itemList.city[r])

    def postalCode(self, x, y):
        r = random.randint(0, len(itemList.postalCode) - 1)
        self.drawString(x, fontY - y, itemList.postalCode[r])

    def phoneNumber(self, x, y):
        r = random.randint(0, len(itemList.areaCode) - 1)
        middleNum = str(random.randint(0, 999))
        if len(middleNum) == 2:
            middleNum = "0" + str(middleNum)
        elif len(middleNum) == 1:
            middleNum = "00" + str(middleNum)

        endNum = str(random.randint(0, 9999))
        if len(endNum) == 3:
            endNum = "0" + str(endNum)
        elif len(endNum) == 2:
            endNum = "00" + str(endNum)
        elif len(endNum) == 1:
            endNum = "000" + str(endNum)

        phoneNum = itemList.areaCode[r] + "-" + str(middleNum) + "-" + str(endNum)
        self.drawString(x, fontY - y, phoneNum)

    def surgicalProcedure(self, x, y):
        r = random.randint(0, len(itemList.surgicalProcedures) - 1)
        self.drawString(x, fontY - y, itemList.surgicalProcedures[r])

    def clinicName(self, x, y):
        r = random.randint(0, len(itemList.clinicNames) - 1)
        self.drawString(x, fontY - y, itemList.clinicNames[r])

    def vendorName(self, x, y):
        r = random.randint(0, len(itemList.vendorNames) - 1)
        self.drawString(x, fontY - y, itemList.vendorNames[r])

    def positionTitle(self, x, y):
        r = random.randint(0, len(itemList.positionTitles) - 1)
        self.drawString(x, fontY - y, itemList.positionTitles[r])

    def confirmations(self, x, y):
        for i in range(len(y)):
            r = random.randint(0, 2)
            self.checkbox(x[r], y[i])

    def medicalDevices(self, x, y):
        if fontName == "DavysCrappy" or fontName == "AdamsFont-Regular" or fontName == "Nothing":
            r = random.randint(0, len(itemList.medicalDevicesForBadFont) - 1)
            self.drawString(x, fontY - y, itemList.medicalDevicesForBadFont[r])
        else:
            r = random.randint(0, len(itemList.medicalDevices) - 1)
            self.drawString(x, fontY - y, itemList.medicalDevices[r])

    # Draw text to page
    def drawPage(self, pageNum):
        # Draw Page 1
        if pageNum == 1:

            global color
            global fontName, fontSize, fontY
            fontY = 792

            # Set Font
            # Wacky random chance to get a really bad custom font
            wackyRandomFont = random.randint(0, 1000)
            if wackyRandomFont == 1000:
                fontName, fontSize = "SFSans", 21
            else:
                fontName, fontSize = random.choice(list(fonts.items()))
                print("AFRES Font: " + fontName + "\n" + "Font Size: " + str(fontSize))

            # Adjust Y value depending on Font
            match fontName:
                case "AdamsFont-Regular":
                    fontY = 792
                case "DavysCrappy":
                    fontY = 791
                case "Hoffman":
                    fontY = 791
                case "MessySketch":
                    fontY = 789
                case "Nothing":
                    fontY = 790

            # Set Font
            self.setFont(fontName, fontSize)

            # Set Color
            randomCol = random.randint(0, 100)
            if 90 <= randomCol < 98:
                self.setFillColor('red')

                color = 'red'
                print("Color: Red")
            elif randomCol >= 98:
                self.setFillColor('blue')

                color = 'blue'
                print("Color: Blue")
            else:
                color = 'black'

            adjustY = 9

            # Last name
            self.lastName(20, 205 - adjustY)

            # First name
            self.firstName(20, 232 - adjustY)

            # Middle initial
            self.middleInitial(313, 232 - adjustY)

            # Health number
            self.healthNumber(20, 261 - adjustY)

            # Version
            self.healthVersion(263, 261 - adjustY)

            # Date of birth
            self.date(312, 261 - adjustY)

            # Sex
            self.checkboxLR(474, 532, 262 - adjustY)

            # Long term care homes
            self.longTermCareHome(22, 291 - adjustY)

            # Unit number
            self.randomNumber(22, 335 - adjustY, 1, 5000)

            # Street number
            self.randomNumber(312, 335 - adjustY, 1, 1500)

            # Street name
            self.streetName(22, 363 - adjustY)

            # Lot/Concession/Rural Route
            self.lotConcRR(22, 392 - adjustY)

            # City
            self.city(22, 420 - adjustY)

            # Postal Code
            self.postalCode(512, 420 - adjustY)

            # Phone number and Business Phone
            self.phoneNumber(22, 449 - adjustY)
            self.phoneNumber(312, 449 - adjustY)

            # Business Extension
            self.randomNumber(555, 449 - adjustY, 0, 999)

            # Confirmation of Benefits Yes or No
            yesNo = self.checkboxLR(218, 258, 480 - adjustY)

            # If yes, please select one
            if yesNo == 0:
                opThree = random.randint(0, 2)

                if opThree == 0:
                    self.checkbox(218, 499 - adjustY)
                elif opThree == 1:
                    self.checkbox(218, 517 - adjustY)
                else:
                    self.checkbox(218, 535 - adjustY)

            # WSIB Yes or No
            self.checkboxLR(273, 313, 573 - adjustY)

            # VAC Yes or No
            self.checkboxLR(273, 313, 589 - adjustY)

            # LTCH Yes or No
            self.checkboxLR(273, 313, 599)

            # Chornic care hospital
            self.checkboxLR(273, 313, 615)

            # Section 2 Stuff
            for i in range(3):
                self.checkboxTF(22, 695 + (i * 17))

        # Draw Page 2
        if pageNum == 2:

            # Reset color
            self.setFillColor(color)

            # Hypertrophic Scarring
            for i in range(6):
                self.checkboxTF(21, 63 + (i * 18))

            # Section 2a - the hellscape of checkboxes
            increments = [206, 224, 241]
            r = random.randint(0, 2)
            self.checkbox(22, increments[r])

            # Reason for application
            increments = [275, 294]
            r = random.randint(0, 1)
            self.checkbox(22, increments[r])

            # Replacement
            for i in range(2):
                self.checkboxTF(22, 328 + (i * 28))

            # Confirmation of Applicant
            confirmationX = [413, 475, 536]
            confirmationY = [435, 476, 542, 606, 653]
            for i in range(5):
                r = random.randint(0, 2)
                self.checkbox(confirmationX[r], confirmationY[i])

        # Draw Page 3
        if pageNum == 3:

            # Reset color
            self.setFillColor(color)

            # Device
            for i in range(3):
                self.checkboxTF(22, 95 + (i * 18))

            # Reason
            increments = [165, 182]
            r = random.randint(0, 1)
            self.checkbox(22, increments[r])

            # Replacement
            for i in range(2):
                self.checkboxTF(22, 218 + (i * 30))

            # Confirmations
            confirmationX = [414, 475, 536]
            confirmationY = [315, 340, 366, 395, 424, 450, 727, 753]
            for i in range(8):
                r = random.randint(0, 2)
                self.checkbox(confirmationX[r], confirmationY[i])

            # Section 2c
            # Device
            for i in range(3):
                self.checkboxTF(22, 506 + (i * 18))

            # Reason
            increments = [575, 593]
            r = random.randint(0, 1)
            self.checkbox(22, increments[r])

            # Replacement
            for i in range(2):
                self.checkboxTF(22, 629 + (i * 30))

        # Draw Page 4
        if pageNum == 4:

            # Reset color
            self.setFillColor(color)

            # Device
            increments = [95, 113]
            r = random.randint(0, 1)
            self.checkbox(22, increments[r])

            # Confirmations
            confirmationX = [414, 474, 536]
            confirmationY = [156, 190, 225, 259, 501, 633]
            self.confirmations(confirmationX, confirmationY)

            # Device
            for i in range(3):
                self.checkboxTF(22, 319 + (i * 18))

            # Reason
            increments = [370, 387]
            r = random.randint(0, 1)
            self.checkbox(22, increments[r])

            # Replacement
            for i in range(2):
                self.checkboxTF(22, 421 + (i * 30))

            # Tracheostomy Equipment
            for i in range(3):
                self.checkboxTF(22, 556 + (i * 18))

        # Draw Page 5
        if pageNum == 5:

            # Reset color
            self.setFillColor(color)

            adjustY = 15

            ############ Applicant / Agent ############
            self.checkboxLR(325, 398, 385)

            ############ Date ############
            self.date(470, 403 - adjustY, 2000, 2023)

            ############ Relationship ############

            increments = [21, 92, 162, 261, 358]
            yesNo = random.randint(0, 4)
            self.checkbox(increments[yesNo], 442 - adjustY)

            # Last name
            self.lastName(22, 453)

            # First name
            self.firstName(22, 482)

            # Middle initial
            self.middleInitial(313, 482)

            # Unit Number
            self.randomNumber(22, 528, 1, 5000)

            # Street number
            self.randomNumber(312, 528, 1, 1500)

            # Street name
            self.streetName(22, 555)

            # Lot/Concession/Rural Route
            self.lotConcRR(22, 586)

            # City
            self.city(22, 613)

            # Postal Code
            self.postalCode(496, 642)

            # Phone number
            self.phoneNumber(22, 671)
            self.phoneNumber(312, 671)

            # Business Extension
            self.randomNumber(555, 671, 0, 999)

        # Draw Page 6
        if pageNum == 6:

            # Reset color
            self.setFillColor(color)

            ############ Physician / Nurse ############
            self.checkboxLR(21, 130, 128)

            # Last name
            self.lastName(21, 155)

            # First name
            self.firstName(312, 155)

            # Business Phone Number
            self.phoneNumber(22, 185)

            # Business Extension
            self.randomNumber(270, 185, 0, 999)

            # Ontario Health Billing No.
            self.randomNumber(313, 185, 10000, 999999)

            # Date
            self.date(455, 221, 2018, 2023)

            ############ Clininc ############

            # Clinic Name
            self.clinicName(22, 268)

            # ADP Clinic Number
            self.randomNumber(22, 297, 10000, 999999)

            # Fit Business Phone Number
            self.phoneNumber(313, 297)

            # Clinic Business Extension
            self.randomNumber(559, 297, 0, 999)

            ############ Vendor ############

            # Vendor Name
            self.vendorName(22, 370)

            # ADP Vendor Reg Number
            self.randomNumber(436, 370, 10000, 999999)

            # Vendor Last name
            self.lastName(21, 398)

            # Vendor First name
            self.firstName(312, 398)

            # Position Title
            self.positionTitle(22, 428)

            # Vendor Business Phone Number
            self.phoneNumber(311, 428)

            # Vendor Business Extension
            self.randomNumber(558, 428, 0, 999)

            # Vendor Location
            streetNo = str(random.randint(0, 999))
            r = random.randint(0, len(itemList.streetName) - 1)
            self.drawString(22, fontY - 456, streetNo + " " + itemList.streetName[r])

            ############ Vendor Date ############
            self.date(343, 493, 2000, 2023)

            # Vendor Invoice
            self.randomNumber(497, 493)

            # Equipment Specifications
            objX = [26, 121, 303, 408, 512]
            objY = [562, 592, 622, 652, 682, 712, 742]
            for i in range(7):
                self.randomNumber(objX[0], objY[i], 10000, 99999)

                self.medicalDevices(objX[1], objY[i])

                self.randomNumber(objX[2], objY[i], 10000, 99999)

                r = round(random.uniform(1.00, 999.99), 2)
                self.drawString(objX[3], fontY - objY[i], str(r))
                r = round(random.uniform(1.00, 999.99), 2)
                self.drawString(objX[4], fontY - objY[i], str(r))


        # Draw Page 7
        if pageNum == 7:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)
            # Date
            self.date(457, 136, 2018, 2023)


# This function adds text to the pdf
# and is called each time the generatePDF()
# function iterates to a different input file path
def add_text_to_pdf(input_path, output_path):
    # Open the existing PDF file
    with open(input_path, 'rb') as file:
        pdf = PdfReader(file)
        total_pages = len(pdf.pages)

        # Create a new PDF file for writing
        with open(output_path, 'wb') as output_file:
            writer = PyPDF2.PdfWriter()

            # Iterate over each page of the existing PDF
            for page_number in range(total_pages):
                page = pdf.pages[page_number]

                # Create a custom canvas to draw the text on the page
                packet = io.BytesIO()
                can = CustomCanvas(packet, pagesize=letter)
                can.setPageSize((page.mediabox.width, page.mediabox.height))

                # Draw current page, increment by 1 to next page
                global currentPage
                currentPage = currentPage + 1
                can.drawPage(currentPage)
                can.save()

                # Create a PdfReader object from the modified canvas
                packet.seek(0)
                overlay = PdfReader(packet)

                # Merge the modified canvas with the original page
                page.merge_page(overlay.pages[0])

                # Add the modified page to the new PDF file
                writer.add_page(page)

            # Write the modified PDF to the output file
            writer.write(output_file)


# Set input file paths into inputFiles list
inputDir = r"AFRES/Input Documents/"
inputDirectory = os.fsencode(inputDir)
inputFiles = []

for file in os.listdir(inputDirectory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        inputFiles.append(inputDir + filename)
        continue
    else:
        continue

# Set output files path to outputFiles list
outputDir = r"AFRES/Output Documents/"
outputDirectory = os.fsencode(outputDir)
outputFiles = []

for file in os.listdir(outputDirectory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        outputFiles.append(outputDir + filename)
        continue
    else:
        continue

# Create instances of the PDFMerger() class
# Cannot reuse merger objects when merging PDFs
# so this code creates 100 of them in a list that we can use
mergers = []
for i in range(200):
    merger = PyPDF2.PdfMerger()
    mergers.append(merger)
    merger_name = f"merger{i}"  # Set a unique name for each merger object
    locals()[merger_name] = merger  # Assign the merger object to the dynamically created variable

# mergerCounter is used to keep track of how many documents have been merged
mergerCounter = 0


# The great merge function
def mergePdfs(start, end, docRange, folderPath=r"C:\Users\Adam\Desktop\pythonProject", isGUI=False):
    global mergerCounter
    global userDocumentFolder
    if isGUI == True:
        userDocumentFolder = folderPath + "/"
    else:
        for root, dirs, outputFiles in os.walk(outputDir):
            # Iterate over the list of the file names
            for file_name in outputFiles[start:end]:
                # Append PDF files
                mergers[mergerCounter].append(outputDir + file_name)

        # This code ensures the merged documents are named with respect to the original doc they came from
        if mergerCounter == 0 or mergerCounter == 1:
            if not os.path.exists(userDocumentFolder + "AFRES/" + docRange):
                os.makedirs(userDocumentFolder + "AFRES/" + docRange)
            # mergers[mergerCounter].write(r"C:/Users/Adam/Desktop/" + "0-AFRES" + docRange + ".pdf")
            mergers[mergerCounter].write(userDocumentFolder + "AFRES/" + docRange + "/" + "0-AFRES" + docRange + ".pdf")
        else:
            if not os.path.exists(userDocumentFolder + "AFRES/" + docRange):
                os.makedirs(userDocumentFolder + "AFRES/" + docRange)
            documentNumber = math.floor(
                mergerCounter / 2)  # Using mergerCounter we can keep assign split docs the same name
            mergers[mergerCounter].write(userDocumentFolder + "AFRES/" + docRange + "/" + str(documentNumber) + "-AFRES" + docRange + ".pdf")
    if isGUI == False:
        mergerCounter += 1


# Set number of default iterations to 1
numDocs = 1


def generatePDF(inputNumberDocs):
    global numDocs
    numDocs = int(inputNumberDocs)

    for j in range(numDocs):
        global currentPage
        currentPage = 0
        for i in range(7):
            add_text_to_pdf(inputFiles[i], r"AFRES/Output Documents/AFRES_" + str(i + 1) + "_output.pdf")

            # When each file has been written, execute the great merger function
            if i == 3:
                mergePdfs(0, 4, "_1_4")

            if i == 6:
                mergePdfs(4, 7, "_5_end")

        print("Current Document: " + str(j + 1) + " of " + str(numDocs))