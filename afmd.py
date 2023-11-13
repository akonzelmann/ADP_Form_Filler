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

    def randomFloat(self, x, y, max=99.99):
        if fontName == "AdamsFont-Regular":
            self.setFont("Nothing", 20)
            r = round(random.uniform(1.00, max), 2)
            self.drawString(x, fontY - y, str(r))
            self.setFont(fontName, fontSize)
        else:
            r = round(random.uniform(1.00, max), 2)
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

    def customModifications(self, x, y):
        if fontName == "AdamsFont-Regular":
            r = random.randint(0, len(itemList.customModificationsAdam) - 1)
            self.drawString(x, fontY - y, itemList.customModificationsAdam[r])
        else:
            r = random.randint(0, len(itemList.customModifications) - 1)
            self.drawString(x, fontY - y, itemList.customModifications[r])

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
                print("AFMD Font: " + fontName + "\n" + "Font Size: " + str(fontSize))

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

            adjustY = 3

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
            self.randomNumber(559, 449 - adjustY, 0, 999)

            # Confirmation of Benefits Yes or No
            yesNo = self.checkboxLR(209, 248, 482)

            # If yes, please select one
            if yesNo == 0:
                opThree = random.randint(0, 2)

                if opThree == 0:
                    self.checkbox(209, 498)
                elif opThree == 1:
                    self.checkbox(209, 512)
                else:
                    self.checkbox(209, 526)

            # WSIB Yes or No
            self.checkboxLR(248, 287, 563)

            # VAC Yes or No
            self.checkboxLR(248, 287, 580)


            # Section 2 Stuff
            # Iterate through the lines
            r = random.randint(0, len(itemList.medicalConditions) - 1)
            lineItem = itemList.medicalConditions[r]
            self.drawString(22, fontY - 643, lineItem)

            r = random.randint(0, len(itemList.functionalMobility) - 1)
            lineItem = itemList.functionalMobility[r]
            self.drawString(22, fontY - 706, lineItem)

        # Draw Page 2
        if pageNum == 2:

            # Reset color
            self.setFillColor(color)

            # Mobility Equipment
            yesNo = random.randint(0, 1)
            posX = [112, 255, 414]

            if yesNo == 0:
                self.checkbox(22, 79)

            else:
                for i in range(4):
                    self.checkboxTF(posX[0], 78 + (i * 19))
                    self.checkboxTF(posX[1], 78 + (i * 19))
                    self.checkboxTF(posX[2], 78 + (i * 19))

            # Devices currently required
            for i in range(6):
                self.checkboxTF(22, 213 + (i * 29.5))

            for i in range(6):
                self.checkboxTF(22, 385 + (i * 29.5))

            posY = [559, 598, 627, 689]
            for i in range(4):
                self.checkboxTF(22, posY[i])

        # Draw Page 3
        if pageNum == 3:

            # Reset color
            self.setFillColor(color)

            # Device
            xPos = [21, 172, 424]
            yPos = [93, 111, 128]

            for i in range(3):
                isChecked = random.randint(0,1)
                if isChecked == 0:
                    yesNo = random.randint(0,2)
                    self.checkbox(xPos[i], yPos[yesNo])

            yesNo = random.randint(0,1)
            if yesNo == 0:
                self.checkbox(21, 148)

            # Reason
            increments = [183, 199, 218, 237, 253]
            r = random.randint(0, 4)
            self.checkbox(22, increments[r])

            # Replacement
            increments = [288, 316, 337, 364]
            for i in range(4):
                self.checkboxTF(22, increments[i])

            # Confirmations
            confirmationX = [436, 490, 544]
            confirmationY = [410, 444, 478, 511, 546, 579]
            for i in range(len(confirmationY)):
                r = random.randint(0, 2)
                self.checkbox(confirmationX[r], confirmationY[i])

        # Draw Page 4
        if pageNum == 4:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)

            # Measurement values
            posX = [143, 144, 176, 143]
            posY = [77, 96, 150, 168]
            for i in range(4):
                self.randomFloat(posX[i], posY[i])

            # Measurement Checkboxes
            # 1
            posX = [207, 262, 321]
            r = random.randint(0, 2)
            self.checkbox(posX[r], 78)

            # 2
            self.checkboxLR(207, 262, 97)

            # 3
            posX = [137, 207, 296]
            r = random.randint(0, 2)
            self.checkbox(posX[r], 114)

            self.checkboxLR(137, 207, 132)

            # 4
            self.checkboxLR(237, 292, 150)

            # 5
            self.checkboxLR(207, 261, 168)

            # 6 to 9
            posX = [137, 206, 296]
            for i in range(4):
                r = random.randint(0, 2)
                self.checkbox(posX[r], 186 + (i * 18))

            # 10
            self.checkboxLR(137, 207, 259)

            # Additional ADP
            for i in range(3):
                self.checkboxTF(22, 293 + (i * 18))

            # Custom modifications
            r = random.randint(0, 90)
            self.checkbox(22, 582)
            self.customModifications(21, 646 + r)

        # Draw Page 5
        if pageNum == 5:

            # Reset color
            self.setFillColor(color)

            adjustY = 15

            # Device
            xPos = [22, 274]
            yPos = [95, 122, 130, 147, 167]
            positions = []
            for i in range(2):
                for j in range(5):
                    positions.append([xPos[i], yPos[j]])
            positions.append([545, 95])

            r = random.randint(0, len(positions) - 1)
            self.checkbox(positions[r][0], positions[r][1])

            # Power Add-On
            self.checkboxTF(22, 185)

            # Reason
            increments = [219, 237, 255, 273, 291]
            r = random.randint(0, 4)
            self.checkbox(22, increments[r])

            # Replacement
            increments = [326, 342, 370, 396]
            for i in range(4):
                self.checkboxTF(22, increments[i])

            # Confirmations
            confirmationX = [469, 512, 555]
            confirmationY = [435, 461, 486, 511, 536, 562, 583, 604, 630, 655, 680, 705, 733]
            for i in range(len(confirmationY)):
                r = random.randint(0, 2)
                self.checkbox(confirmationX[r], confirmationY[i])

        # Draw Page 6
        if pageNum == 6:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)

            # Measurement values
            posX = [131, 131, 168, 131, 131, 168, 131]
            for i in range(7):
                self.randomFloat(posX[i], 78 + (i * 18))

            # Measurement Checkboxes
            for i in range(5):
                skipY = 36
                if i % 2 == 0 and i != 0:
                    self.checkboxLR(199, 253, 78 + (i * 18 + skipY))
                else:
                    self.checkboxLR(199, 253, 78 + (i * 18))

            for i in range(2):
                self.checkboxLR(235, 289, 113 + (i * 55))

            # Additional ADP
            posX = [21, 226, 450]

            for i in range(3):
                for j in range(3):
                    if i == 2 and j == 1:
                        self.checkbox(226, 276)
                    else:
                        self.checkboxTF(posX[j], 241 + (i * 18))

            for i in range(2):
                self.checkboxTF(21, 300 + (i * 18))

            for i in range(4):
                self.checkboxTF(226, 304 + (i * 18))

            for i in range(5):
                if i == 0:
                    self.checkbox(449, 300)
                else:
                    self.checkboxTF(449, 300 + (i * 18))

            # Clinical Rationale
            randY = random.randint(0, 34)
            r = random.randint(0, len(itemList.medicalConditions) - 1)
            self.drawString(22, fontY - 410 - randY, itemList.medicalConditions[r])

            # Custom modifications
            r = random.randint(0, 33)
            self.checkbox(22, 677)
            self.customModifications(21, 731 + r)

        # Draw Page 7
        if pageNum == 7:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)

            # Device
            xPos = [22, 185, 358]
            yPos = [95, 113, 131]

            r = random.randint(0, 2)
            r1 = random.randint(0, 2)

            self.checkbox(xPos[r], yPos[r1])

            # Reason
            increments = [165, 183, 201, 219, 237]
            r = random.randint(0, 4)
            self.checkbox(22, increments[r])

            # Replacement
            increments = [272, 298, 316, 342]
            for i in range(4):
                self.checkboxTF(22, increments[i])

            # Confirmation
            confirmationX = [436, 490, 544]
            confirmationY = [384, 413, 460, 489, 518]
            for i in range(len(confirmationY)):
                r = random.randint(0, 2)
                self.checkbox(confirmationX[r], confirmationY[i])

            # Prescription Details
            xPos = [135, 135, 173, 136, 136, 136]
            yPos = [559, 577, 595, 613, 631, 650]

            for i in range(len(xPos)):
                self.randomFloat(xPos[i], yPos[i])

            xPos = [200, 254]
            yPos = [559, 577, 613, 631, 649]
            for i in range(len(yPos)):
                yesNo = random.randint(0, 1)
                self.checkbox(xPos[yesNo], yPos[i])

            xPos = [236, 290]
            yesNo = random.randint(0, 1)
            self.checkbox(xPos[yesNo], 595)

        # Draw Page 8
        if pageNum == 8:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)

            # Prescribed Power Base
            xPos = [22, 276]
            yPos = [80, 98, 116, 134, 152]
            yPos1 = [80, 98, 116, 143, 171, 189]

            for i in range(len(xPos)):
                if i == 0:
                    for j in range(len(yPos)):
                        self.checkboxTF(xPos[i], yPos[j])
                else:
                    for j in range(len(yPos1)):
                        self.checkboxTF(xPos[i], yPos1[j])

            # Clinical Rationale Checkboxes
            xPos = [22, 275]
            yPos = [224, 242, 260, 278]

            for i in range(len(xPos)):
                for j in range(len(yPos)):
                    if i == 1 and j == 3:
                        continue
                    else:
                        self.checkboxTF(xPos[i], yPos[j])

            # Clinical Rationale
            rY = random.randint(0, 34)
            r = random.randint(0, len(itemList.medicalConditions) - 1)
            self.drawString(22, fontY - 314 - rY, itemList.medicalConditions[r])

            # Power Positioning Devices
            xPos = [22, 276]
            yPos = [386, 404, 422]

            for i in range(len(xPos)):
                for j in range(len(yPos)):
                    if i == 1 and j == 2:
                        continue
                    else:
                        self.checkboxTF(xPos[i], yPos[j])

            # Custom Modifications
            r = random.randint(0, 50)
            self.checkbox(22, 655)
            self.customModifications(21, 710 + r)

        # Draw Page 9
        if pageNum == 9:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)

            # Modular
            for i in range(27):
                if i != 5 and i != 8 and i != 12 and i != 15 and i != 22 and i != 23:
                    self.checkboxTF(173, 94 + (i * 18))
                self.checkboxTF(234, 94 + (i * 18))

        # Draw Page 10
        if pageNum == 10:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)

            # Reason
            increments = [77, 95, 113, 131, 149]
            r = random.randint(0, 4)
            self.checkbox(22, increments[r])

            # Replacement
            increments = [184, 214, 236, 257]
            for i in range(4):
                self.checkboxTF(22, increments[i])

            # Confirmation
            confirmationX = [436, 490, 544]
            confirmationY = [299, 344]
            for i in range(len(confirmationY)):
                r = random.randint(0, 2)
                self.checkbox(confirmationX[r], confirmationY[i])

            # Custom modifications
            r = random.randint(0, 80)
            self.checkbox(22, 602)
            self.customModifications(21, 666 + r)

        # Draw Page 11
        if pageNum == 11:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)

            adjustY = 17

            ############ Applicant / Agent ############
            self.checkboxLR(325, 394, 370)

            ############ Date ############
            self.date(470, 375, 2000, 2023)

            ############ Relationship ############

            increments = [21, 92, 165, 272, 381]
            yesNo = random.randint(0, 4)
            self.checkbox(increments[yesNo], 407)

            # Last name
            self.lastName(22, 453 - adjustY)

            # First name
            self.firstName(22, 482 - adjustY)

            # Middle initial
            self.middleInitial(313, 482 - adjustY)

            # Unit Number
            self.randomNumber(22, 526 - adjustY, 1, 5000)

            # Street number
            self.randomNumber(312, 526 - adjustY, 1, 1500)

            # Street name
            self.streetName(22, 555 - adjustY)

            # Lot/Concession/Rural Route
            self.lotConcRR(22, 584 - adjustY)

            # City
            self.city(22, 613 - adjustY)

            # Postal Code
            self.postalCode(496, 640 - adjustY)

            # Phone number
            self.phoneNumber(22, 669 - adjustY)
            self.phoneNumber(312, 669 - adjustY)

            # Business Extension
            self.randomNumber(558, 669 - adjustY, 0, 999)

        # Draw Page 12
        if pageNum == 12:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)

            # Authorizer
            self.lastName(31, 193)
            self.firstName(321, 193)
            self.phoneNumber(31, 222)
            self.randomNumber(272, 222)
            self.randomNumber(321, 222, 10000, 999999)
            self.date(445, 254)

            # Vendor
            self.vendorName(45, 298)
            self.randomNumber(443, 298, 10000, 999999)

            if fontName == "AdamsFont-Regular":
                self.setFont("Hoffman", 20)
            r = random.randint(0, len(itemList.lastName) - 1)
            r1 = random.randint(0, len(itemList.firstName) - 1)
            self.drawString(41, fontY - 349, itemList.lastName[r] + ", " + itemList.firstName[r1])

            self.setFont(fontName, fontSize)

            self.positionTitle(327, 349)

            streetNo = str(random.randint(0, 999))
            r = random.randint(0, len(itemList.streetName) - 1)
            self.drawString(41, fontY - 378, streetNo + " " + itemList.streetName[r])

            self.phoneNumber(384, 378)
            self.randomNumber(559, 378)
            self.date(440, 407)

            # Vendor 2
            yAdjust = 138

            self.vendorName(45, 298 + yAdjust)
            self.randomNumber(443, 298 + yAdjust, 10000, 999999)

            if fontName == "AdamsFont-Regular":
                self.setFont("Hoffman", 20)
            r = random.randint(0, len(itemList.lastName) - 1)
            r1 = random.randint(0, len(itemList.firstName) - 1)
            self.drawString(41, fontY - (349 + yAdjust), itemList.lastName[r] + ", " + itemList.firstName[r1])

            self.setFont(fontName, fontSize)

            self.positionTitle(327, 349 + yAdjust)

            streetNo = str(random.randint(0, 999))
            r = random.randint(0, len(itemList.streetName) - 1)
            self.drawString(41, fontY - (378 + yAdjust), streetNo + " " + itemList.streetName[r])

            self.phoneNumber(384, 378 + yAdjust)
            self.randomNumber(559, 378 + yAdjust)
            self.date(457, 407 + yAdjust)

            # Equipment Specifications
            self.randomNumber(25, 588, 1, 10000)
            self.randomNumber(283, 588, 10000, 999999)
            self.randomNumber(25, 617, 10000, 999999)
            self.medicalDevices(170, 617)
            self.randomNumber(457, 617, 1, 100000)
            self.randomNumber(25, 646, 100000, 999999999)
            self.randomNumber(457, 646, 1, 100000)
            self.checkboxLR(329, 390, 718)
            self.date(443, 722)

        # Draw Page 13
        if pageNum == 13:

            # Reset color
            self.setFillColor(color)
            self.setFont(fontName, fontSize)

            self.checkbox(30, 173)

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
inputDir = r"AFMD/Input Documents/"
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
outputDir = r"AFMD/Output Documents/"
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
            if not os.path.exists(userDocumentFolder + "AFMD/" + docRange):
                os.makedirs(userDocumentFolder + "AFMD/" + docRange)
            mergers[mergerCounter].write(userDocumentFolder + "AFMD/" + docRange + "/" + "0-AFMD" + docRange + ".pdf")
        else:
            if not os.path.exists(userDocumentFolder + "AFMD/" + docRange):
                os.makedirs(userDocumentFolder + "AFMD/" + docRange)
            documentNumber = math.floor(
                mergerCounter / 3)  # Using mergerCounter we can keep assign split docs the same name
            mergers[mergerCounter].write(userDocumentFolder + "AFMD/" + docRange + "/" + str(documentNumber) + "-AFMD" + docRange + ".pdf")

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
        for i in range(13):
            if i >= 9:
                add_text_to_pdf(inputFiles[i], r"AFMD/Output Documents/bAFMD_" + str(i + 1) + "_output.pdf")
            else:
                add_text_to_pdf(inputFiles[i], r"AFMD/Output Documents/AFMD_" + str(i + 1) + "_output.pdf")

            # When each file has been written, execute the great merger function
            if i == 3:
                mergePdfs(0, 4, "_1_4")

            if i == 7:
                mergePdfs(4, 8, "_5_8")

            if i == 12:
                mergePdfs(8, 13, "_9_13")

        print("Current Document: " + str(j + 1) + " of " + str(numDocs))