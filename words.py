def print_upper_words(words, starts):
        """
        Takes a list of words and a dict of letters 
        searches through in order to create the words
        """
        thing = []

        for letter in starts:
            for word in words:
                print(letter, word)
                if letter in word:
                    thing.append(word)

        
        # print(thing)
        for t in thing:
            z = t.capitalize()
            print(z)
        


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])