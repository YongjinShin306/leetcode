class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        dic_str2num = {
            "a":"0", 
            "b":"1", 
            "c":"2", 
            "d":"3", 
            "e":"4", 
            "f":"5", 
            "g":"6", 
            "h":"7", 
            "i":"8", 
            "j":"9",
            }

        def str2int(word):
            result = ""
            for i in word:
                result = result + dic_str2num[i]
            return int(result)
        
        return str2int(firstWord) + str2int(secondWord) == str2int(targetWord)