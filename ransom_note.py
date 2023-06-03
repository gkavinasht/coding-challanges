# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

def canConstruct(ransomNote, magazine):
	magazineDict = {}

	for i in range(len(magazine)):
	    if magazine[i] in magazineDict:
	        magazineDict[magazine[i]] += 1
	    else:
	        magazineDict[magazine[i]] = 1

	for i in range(len(ransomNote)):
	    if ransomNote[i] not in magazineDict:
	        return False
	    if magazineDict[ransomNote[i]] == 0:
	        return False
	    magazineDict[ransomNote[i]] -= 1
	return True

    # ransomNoteDict = {}
    # magazineDict = {}

    # for i in range(len(magazine)):
    #     if magazine[i] in magazineDict:
    #         magazineDict[magazine[i]] += 1
    #     else:
    #         magazineDict[magazine[i]] = 1

    # for i in range(len(ransomNote)):
    #     if ransomNote[i] in ransomNoteDict:
    #         ransomNoteDict[ransomNote[i]] += 1
    #     else:
    #         ransomNoteDict[ransomNote[i]] = 1

    # for key in ransomNoteDict.keys():
    #     if key not in magazineDict:
    #         return False
    #     if magazineDict[key] < ransomNoteDict[key]:
    #         return False
    # return True


ransomNote = "a"
magazine = "ab"
print(canConstruct(ransomNote, magazine))
# Output: true

# Time Complexity : O(n)
# Space Complexity : O(k) Space to store unique elements in the Dictionary 