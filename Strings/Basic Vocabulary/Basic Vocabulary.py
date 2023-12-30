"""Functions for creating, transforming, and adding prefixes to strings."""
def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.
 
    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return 'un' + word

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.
 
    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.
 
    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.
 
    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    output = [vocab_words[0]]
    for word in vocab_words[1:]:
        output.append(vocab_words[0] + word)
    return ' :: '.join(output)

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.
 
    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.
 
    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    new_word = ''
    if 'ness' in word:
        if word.replace('ness','').endswith('i'):
           return word.replace('iness','y')
        else:
           return word.replace('ness','')
    elif word.endswith('y'):
        return word.replace('y','iness')
    else:
        return word + 'ness'