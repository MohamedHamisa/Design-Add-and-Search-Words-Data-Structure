class WordDictionary:

    def __init__(self):
        self.words = set()
        self.matches = {}

    def addWord(self, word):
        self.words.add(word)
        self.matches.clear()

    def search(self, word):
        if word in self.matches:
            return self.matches[word]
        
        regex = re.compile(f'^{word}$')
        has = any(w for w in self.words if regex.match(w))
        
        self.matches[word] = has
        return has


       
