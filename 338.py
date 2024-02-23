# 383. Ransom Note
# ----------------
# Given two strings `ransomNote` and `magazine`, return true if ransomNote can be constructed by using the letters
# from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
# Example:
#   Input: ransomNote = "aa", magazine = "aab"
#   Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        control = dict.fromkeys(magazine, 0)
        for letter in magazine:
            control[letter] += 1

        for letter in ransomNote:
            try:
                control[letter] -= 1
                if control[letter] == -1:
                    return False
            except KeyError:
                return False

        return True

if __name__ == '__main__':
    s = Solution()
    response = s.canConstruct(
        ransomNote="aa",
        magazine="aab"
    )
    print(response)