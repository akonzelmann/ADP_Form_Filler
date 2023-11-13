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
                print("AFMPD Font: " + fontName + "\n" + "Font Size: " + str(fontSize))

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

            # Last name
            self.lastName(20, 205)

            # First name
            self.firstName(20, 232)

            # Middle initial
            self.middleInitial(313, 232)

            # Health number
            self.healthNumber(20, 261)

            # Version
            self.healthVersion(263, 261)

            # Date of birth
            self.date(312, 261)

            # Sex
            self.checkboxLR(458, 532, 262)

            # Long term care homes
            self.longTermCareHome(22, 291)

            # Unit number
            self.randomNumber(22, 335, 1, 5000)

            # Street number
            self.randomNumber(312, 335, 1, 1500)

            # Street name
            self.streetName(22, 363)

            # Lot/Concession/Rural Route
            self.lotConcRR(22, 392)

            # City
            self.city(22, 420)

            # Postal Code
            self.postalCode(512, 420)

            # Phone number and Business Phone
            self.phoneNumber(22, 449)
            self.phoneNumber(312, 449)

            # Business Extension
            self.randomNumber(555, 449, 0, 999)

            # Confirmation of Benefits Yes or No
            yesNo = self.checkboxLR(209, 250, 487)

            # If yes, please select one
            if yesNo == 0:
                opThree = random.randint(0, 2)

                if opThree == 0:
                    self.checkbox(210, 506)
                elif opThree == 1:
                    self.checkbox(210, 520)
                else:
                    self.checkbox(210, 536)

            # WSIB Yes or No
            self.checkboxLR(248, 288, 573)

            # VAC Yes or No
            self.checkboxLR(249, 288, 589)

        # Draw Page 2
        if pageNum == 2:
            self.setFillColor(color)

            # Hypertrophic Scarring
            self.checkboxTF(21, 94)

            # Chornic Lymphedema
            self.checkboxTF(21, 125)
            self.checkboxTF(100, 125)

            # Surgical Procedures
            self.surgicalProcedure(21, 151)

            # Date of Surgery
            self.date(460, 151, 2017, 2025)

            # Section 2a - the hellscape of checkboxes
            chanceChance = 1
            # Devices:
            #############Face Mask#############
            self.checkboxTF(21, 225, chanceChance)

            #############Chin Strap#############
            self.checkboxTF(123, 225, chanceChance)

            #############Accessories#############
            self.checkboxTF(290, 225, chanceChance)

            #############Vest Sleeveless#############
            self.checkboxTF(21, 260, chanceChance)

            #############Vest Short Sleeves#############
            self.checkboxTF(151, 260, chanceChance)

            #############Vest - Two Sleeves#############
            self.checkboxTF(292, 260, chanceChance)

            #############Chest Brace############
            self.checkboxTF(425, 260, chanceChance)

            #############Body Brief Sleeves############
            self.checkboxTF(22, 280, chanceChance)

            #############Body Brief Sleeveless############
            self.checkboxTF(152, 280, chanceChance)

            #############Body Brief Legs############
            self.checkboxTF(293, 280, chanceChance)

            #############Body Brief Legs and Sleeves############
            self.checkboxTF(425, 280, chanceChance)

            #############Options############
            self.checkboxTF(21, 303, chanceChance)

            #############Interim Care Garments############
            self.checkboxTF(22, 322, chanceChance)

            #########################################################
            ####################LOWER EXTREMITY######################
            #########################################################

            #############Foot Gloves to Thigh Length############
            for i in range(5):
                self.checkboxLR(173, 213, 361 + (i * 22))

            #############Waist High to Chaps############
            for i in range(2):
                self.checkboxLR(173, 213, 465 + (i * 21))

            #############Stockings to Stockings Chaps Two Legs############
            for i in range(3):
                self.checkbox(290, 361 + (i * 22))

            #############Stockings Chest to Penile############
            for i in range(2):
                self.checkbox(466, 361 + (i * 22))

            #########################################################
            ####################UPPER EXTREMITY######################
            #########################################################

            #############Mittens to Sleeve with Shoulder############
            for i in range(7):
                self.checkboxLR(173, 213, 530 + (i * 20))

        # Draw Page 3
        if pageNum == 3:

            self.setFillColor(color)

            ############Wrist to Ankle-Foot-Bi############
            for i in range(6):
                self.checkboxLR(173, 213, 80 + (i * 20))

            ############Face to Neck############
            for i in range(2):
                self.checkboxTF(290, 80 + (i * 24))

            ############Reason for Application############
            increments = [223, 241, 259]
            yesNo = random.randint(0, 2)
            self.checkbox(21, increments[yesNo])

            ############Reason Replacment############
            for i in range(3):
                self.checkboxTF(21, 293 + (i * 20))

            ############Confirmation############
            increments = [414, 474, 536]
            yesNo = random.randint(0, 2)
            self.checkbox(increments[yesNo], 383)

            #########################################################
            #######################SECTION 2B########################
            #########################################################
            chanceChance = 1

            ############Mask############
            checkbox_positions = [21, 123, 291]  # X-coordinate values for each checkbox
            for x in checkbox_positions:
                self.checkboxTF(x, 462)

            ############Trunk############
            checkbox_positions = [21, 151, 291, 449]  # X-coordinate values for each checkbox
            for x in checkbox_positions:
                self.checkboxTF(x, 500)

            ############Options - Garments############
            self.checkboxTF(21, 527)

            ############Lower Extremity############
            for i in range(5):
                self.checkboxLR(173, 213, 572 + (i * 21.5))

            for i in range(2):
                self.checkboxLR(173, 213, 688 + (i * 21.5))

            for i in range(3):
                self.checkboxTF(291, 573 + (i * 21.5))

        # Draw Page 4
        if pageNum == 4:

            self.setFillColor(color)

            ############ Upper Extremity ############
            for i in range(7):
                self.checkboxLR(173, 213, 80 + (i * 20))

            ############ Arm Sleeve Shoulder Flap Glove ############
            self.checkboxLR(173, 213, 231)

            ############ Compression Sleeves ############
            for i in range(4):
                self.checkboxLR(173, 213, 285 + (i * 20))

            ############ Gauge ##################
            self.checkboxTF(290, 283)

            ############ Sequential Extremity Pumps and Accessories ############
            increments = [24, 204, 404]
            for i in range(3):
                self.checkboxTF(increments[i], 386)

            ############ Reason For Application ############
            increments = [428, 447, 465]
            yesNo = random.randint(0, 2)
            self.checkbox(21, increments[yesNo])

            ############ Replacement Required ############
            for i in range(3):
                self.checkboxTF(21, 501 + (i * 18))

            ############ Confirmation of Applicant's Eligibility ############
            increments = [415, 476, 537]
            for j in range(2):
                for i in range(2):
                    yesNo = random.randint(0, 2)
                    self.checkbox(increments[yesNo], 589 + (i * 45) + (j * 120) - (j * 4 * i))

        # Draw Page 5
        if pageNum == 5:
            self.setFillColor(color)

            ############ Applicant / Agent ############
            self.checkboxLR(326, 404, 400)

            ############ Date ############
            self.date(470, 403, 2000, 2023)

            ############ Relationship ############

            increments = [21, 129, 236, 356, 475]
            yesNo = random.randint(0, 4)
            self.checkbox(increments[yesNo], 442)

            # Last name
            self.lastName(22, 474)

            # First name
            self.firstName(22, 503)

            # Middle initial
            self.middleInitial(313, 503)

            # Unit Number
            self.randomNumber(22, 547, 1, 5000)

            # Street number
            self.randomNumber(312, 547, 1, 1500)

            # Street name
            self.streetName(22, 575)

            # Lot/Concession/Rural Route
            self.lotConcRR(22, 603)

            # City
            self.city(22, 632)

            # Postal Code
            self.postalCode(496, 660)

            # Phone number
            self.phoneNumber(22, 690)
            self.phoneNumber(312, 690)

            # Business Extension
            self.randomNumber(555, 690, 0, 999)

        # Draw Page 6
        if pageNum == 6:
            self.setFillColor(color)

            ############ Physician / Nurse ############
            self.checkboxLR(21, 130, 128)

            # Last name
            self.lastName(21, 157)

            # First name
            self.firstName(312, 157)

            # Business Phone Number
            self.phoneNumber(22, 187)

            # Business Extension
            self.randomNumber(270, 187, 0, 999)

            # Ontario Health Billing No.
            self.randomNumber(313, 187, 10000, 999999)

            ############ Date ############
            self.date(449, 223, 2000, 2023)

            # Auth Last name
            self.lastName(21, 320)

            # Auth First name
            self.firstName(312, 320)

            # Auth Business Phone Number
            self.phoneNumber(22, 349)

            # Auth Business Extension
            self.randomNumber(270, 349, 0, 999)

            # Auth Ontario Health Billing No.
            self.randomNumber(313, 349, 10000, 999999)

            ############ Auth Date ############
            self.date(449, 384, 2000, 2023)

            # Fit Last name
            self.lastName(21, 469)

            # Fit First name
            self.firstName(312, 469)

            # Fit Business Phone Number
            self.phoneNumber(22, 498)

            # Fit Business Extension
            self.randomNumber(270, 498, 0, 999)

            # Fit Ontario Health Billing No.
            self.randomNumber(313, 498, 10000, 999999)

            ############ Fit Date ############
            self.date(449, 534, 2000, 2023)

            # Clinic Name
            self.clinicName(22, 580)

            # ADP Clinic Number
            self.randomNumber(22, 610, 10000, 999999)

            # Fit Business Phone Number
            self.phoneNumber(311, 610)

            # Clinic Business Extension
            self.randomNumber(558, 610, 0, 999)

        # Draw Page 7
        if pageNum == 7:
            self.setFillColor(color)

            self.setFont(fontName, fontSize)

            # Vendor Name
            self.vendorName(22, 116)

            # ADP Vendor Reg Number
            self.randomNumber(445, 116, 10000, 999999)

            # Vendor Last name
            self.lastName(21, 145)

            # Vendor First name
            self.firstName(312, 145)

            # Position Title
            self.positionTitle(22, 173)

            # Vendor Business Phone Number
            self.phoneNumber(311, 173)

            # Vendor Business Extension
            self.randomNumber(556, 173, 0, 999)

            # Vendor Location
            streetNo = str(random.randint(0, 999))
            r = random.randint(0, len(itemList.streetName) - 1)
            self.drawString(22, fontY - 201, streetNo + " " + itemList.streetName[r])

            ############ Fit Date ############
            self.date(446, 238, 2000, 2023)


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
inputDir = r"ADP Form Filler/Input Documents"
inputDirectory = os.fsencode(inputDir)
inputFiles = []

for file in os.listdir(inputDirectory):
    filename = os.fsdecode(file)
    if (filename.endswith(".pdf")):
        inputFiles.append(inputDir + "/" + filename)
        continue
    else:
        continue

# Set output files path to outputFiles list
outputDir = r"ADP Form Filler/Output Documents/"
outputDirectory = os.fsencode(outputDir)
outputFiles = []

for file in os.listdir(outputDirectory):
    filename = os.fsdecode(file)
    if (filename.endswith(".pdf")):
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
            if not os.path.exists(userDocumentFolder + "AFPMD/" + docRange):
                os.makedirs(userDocumentFolder + "AFPMD/" + docRange)
            mergers[mergerCounter].write(userDocumentFolder + "AFPMD/" + docRange + "/" + "0-AFPMD" + docRange + ".pdf")
        else:
            if not os.path.exists(userDocumentFolder + "AFPMD/" + docRange):
                os.makedirs(userDocumentFolder + "AFPMD/" + docRange)
            documentNumber = math.floor(
                mergerCounter / 2)  # Using mergerCounter we can keep assign split docs the same name
            mergers[mergerCounter].write(
                userDocumentFolder + "AFPMD/" + docRange + "/" + str(documentNumber) + "-AFPMD" + docRange + ".pdf")
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
            add_text_to_pdf(inputFiles[i], r"ADP Form Filler/Output Documents/AFPMD_" + str(i + 1) + "_output.pdf")

            # When each file has been written, execute the great merger function
            if i == 2:
                mergePdfs(0, 3, "_1_3")

            if i == 6:
                mergePdfs(3, 7, "_4_end")

        print("Current Document: " + str(j + 1) + " of " + str(numDocs))