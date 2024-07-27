class Solution(object):
    def intToRoman(self, num):
        strNum = str(num)
        numDigits = len(strNum)
        roman = ""

        onesDigit = strNum[-1]

        if onesDigit == "1": roman = "I"
        if onesDigit == "2": roman = "II"
        if onesDigit == "3": roman = "III"
        if onesDigit == "4": roman = "IV"
        if onesDigit == "5": roman = "V"
        if onesDigit == "6": roman = "VI"
        if onesDigit == "7": roman = "VII"
        if onesDigit == "8": roman = "VIII"
        if onesDigit == "9": roman = "IX"

        if numDigits >= 2:
            tensDigit = strNum[-2:-1]

            if tensDigit == "1": roman = "X" + roman
            if tensDigit == "2": roman = "XX" + roman
            if tensDigit == "3": roman = "XXX" + roman
            if tensDigit == "4": roman = "XL" + roman
            if tensDigit == "5": roman = "L" + roman
            if tensDigit == "6": roman = "LX" + roman
            if tensDigit == "7": roman = "LXX" + roman
            if tensDigit == "8": roman = "LXXX" + roman
            if tensDigit == "9": roman = "XC" + roman

        if numDigits >= 3:
            hundredsDigit = strNum[-3:-2]

            if hundredsDigit == "1": roman = "C" + roman
            if hundredsDigit == "2": roman = "CC" + roman
            if hundredsDigit == "3": roman = "CCC" + roman
            if hundredsDigit == "4": roman = "CD" + roman
            if hundredsDigit == "5": roman = "D" + roman
            if hundredsDigit == "6": roman = "DC" + roman
            if hundredsDigit == "7": roman = "DCC" + roman
            if hundredsDigit == "8": roman = "DCCC" + roman
            if hundredsDigit == "9": roman = "CM" + roman

        if numDigits >= 4:
            thousandsDigit = strNum[-4:-3]

            if thousandsDigit == "1": roman = "M" + roman
            if thousandsDigit == "2": roman = "MM" + roman
            if thousandsDigit == "3": roman = "MMM" + roman

        return roman
