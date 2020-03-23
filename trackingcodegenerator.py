#!/usr/bin/python3

import string
import easypost
easypost.api_key = "[REPLACE ME]"

# can use string digits + string.uppercase if you need alphanumerics
listOfPossibleValues = string.digits


def howManyDigitsToGenerate(partialTrackingNumber):
    # UPS Tracking Numbers are 18 digits long
    return 18 - len(partialTrackingNumber)


def generateOneDigitPlaceWorthOfValues(tempList):
    # generate some digits ok
    listToReturn = []
    for item in tempList:
        for digit in listOfPossibleValues:
            listToReturn.append(item + digit)

    return listToReturn


if __name__ == "__main__":
    partialTrackingNumber = "[REPLACE ME]"
    possibleTrackingNumbers = [partialTrackingNumber]
    i = howManyDigitsToGenerate(partialTrackingNumber)

    postTrackingResults = {}

    while i != 0:
        possibleTrackingNumbers = generateOneDigitPlaceWorthOfValues(
            possibleTrackingNumbers)
        i = i - 1

        j = 0
        while j < len(possibleTrackingNumbers):

            # UPS's website had a limit of 25 tracking numbers per lookup,
            # however it turned out that if any of them failed the parity check
            # then none of the IDs would look up. I'm leaving it in because
            # I don't want break the script but it can be removed any time.

            if j % 25 != 0:
                pass
                if len(possibleTrackingNumbers[j]) == 18:
                    print(possibleTrackingNumbers[j])
                j = j + 1
            elif j != 0:
                print("\n\n")
                j = j + 1
            else:
                j = j + 1

    # create an EasyPost Tracker for each ID,
    # and only print a list if the tracking numbers with valid results.
    for trackingnumber in possibleTrackingNumbers:
        tracker = easypost.Tracker.create(
            tracking_code=trackingnumber,
            carrier="UPS"
        )
        if tracker.status_detail != 'unknown':
            postTrackingResults[trackingnumber] = tracker.status_detail

    print(postTrackingResults)
