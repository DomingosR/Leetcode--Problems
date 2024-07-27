def minNumSteps(initialPassword):
    nChars = len(initialPassword)
    if nChars == 0:
        return 6

    # *** First section: detecting problems in current password ***

    # Deciding whether characters must be added or removed to meet
    # length requirements
    charsToAdd = 0
    charsToDelete = 0

    if nChars < 6:
        charsToAdd = 6 - nChars
    if nChars > 20:
        charsToDelete = nChars - 20

    # Deciding whether specific type of character must be inserted
    hasNumber = any(c.isdigit() for c in initialPassword)
    hasLower = any(c.islower() for c in initialPassword)
    hasUpper = any(c.isupper() for c in initialPassword)

    numTypesToAdd = (0 if hasNumber else 1) + (0 if hasLower else 1) \
                    + (0 if hasUpper else 1)

    # Checking for sequences of repeated characters that must be broken up
    streakLen = []

    currentStreak = 1
    currentChar = initialPassword[0]
    currentOrder = 1

    while currentOrder < nChars:
        if initialPassword[currentOrder] == currentChar:
            currentStreak += 1
        else:
            if currentStreak >= 3:
                streakLen.append(currentStreak)
            currentChar = initialPassword[currentOrder]
            currentStreak = 1
        currentOrder += 1

    if currentStreak >= 3:
        streakLen.append(currentStreak)

    # *** Second section: processing short passwords (length < 6) ***

    # In this case, we don't need to worry about streaks, because only
    # one addition is sufficient to break it if its length is no more than
    # four, or two if it is five (in which case we need to add at least two
    # types anyway).

    if nChars < 6:
        return max(numTypesToAdd, charsToAdd)

    # *** Third section: processing medium passwords (6 <= length <= 20) ***

    # Since breaking streaks is done more efficiently by replacing characters
    # than deleting them, we need only consider types missing and character
    # replacements to break streaks.

    if 6 <= nChars <= 20:
        stepsNeeded = 0

        # Use types to add to break streaks
        while numTypesToAdd > 0 and len(streakLen) > 0:
            streakLen.sort()
            numStreaks = len(streakLen)
            streakLen[numStreaks - 1] -= 3
            if streakLen[numStreaks - 1] < 3:
                streakLen = streakLen[:numStreaks - 1]
            numTypesToAdd -= 1
            stepsNeeded += 1

        # If there are streaks left, break them up by replacing characters
        while len(streakLen) > 0:
            numStreaks = len(streakLen)
            stepsNeeded += int(streakLen[numStreaks - 1]/3)
            streakLen = streakLen[:numStreaks - 1]

        # Finally, return
        return stepsNeeded

    # *** Fourth section: processing long passwords (length > 20) ***

    # Here, each type to add can reduce the length of a streak by 3,
    # and each character to delete can reduce the length of a streak by
    # only 1, as opposed to 2 in the previous case.  If we have characters
    # to delete, we first use them to reduce the length of streaks that are
    # = 0 (mod 3) by 1, then to reduce the length of streaks that are = 1
    # (mod 3) by 2.

    if nChars > 20:
        stepsNeeded = 0

        # Use types to add
        while numTypesToAdd > 0 and len(streakLen) > 0:
            streakLen.sort()
            numStreaks = len(streakLen)
            streakLen[numStreaks - 1] -= 3
            if streakLen[numStreaks - 1] < 3:
                streakLen = streakLen[:numStreaks - 1]
            numTypesToAdd -= 1
            stepsNeeded += 1

        # Then use characters to delete
        # First, use them in streaks that are = 0 mod 3
        i = 0
        while charsToDelete >= 1 and i < len(streakLen):
            if streakLen[i] % 3 == 0:
                streakLen[i] -= 1
                if streakLen[i] < 3:
                    streakLen.pop(i)
                else:
                    i += 1
                charsToDelete -= 1
                stepsNeeded += 1
            else:
                i += 1

        # Then, use them in streaks that are = 1 (mod 3)
        i = 0
        while charsToDelete > 0 and i < len(streakLen):
            if streakLen[i] % 3 == 1:
                streakLen[i] -= min(charsToDelete, 2)
                if streakLen[i] < 3:
                    streakLen.pop(i)
                else:
                    i += 1
                stepsNeeded += min(charsToDelete, 2)
                charsToDelete -= min(charsToDelete, 2)

            else:
                i += 1

        # If there are characters left to delete and streaks, use them
        while charsToDelete > 0 and len(streakLen) > 0:
            streakLen[0] -= min(charsToDelete, 3)
            if streakLen[0] < 3:
                streakLen.pop(0)
            stepsNeeded += min(charsToDelete, 3)
            charsToDelete -= min(charsToDelete, 3)

        # Finally, if there are streaks left, break them up by replacing characters
        while len(streakLen) > 0:
            numStreaks = len(streakLen)
            stepsNeeded += int(streakLen[numStreaks - 1]/3)
            streakLen = streakLen[:numStreaks - 1]

        # Return final value with adjustments
        return stepsNeeded + charsToDelete + numTypesToAdd

class Solution(object):
    def strongPasswordChecker(self, password):
        return minNumSteps(password)