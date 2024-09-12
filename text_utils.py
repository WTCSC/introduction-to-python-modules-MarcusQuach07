# Define count_chars as a function to put text into as a list to count the amount of characters
def count_chars(text):
    # Returns the length of the text
    return len(text)

# Define count_words as a function to put text into a list to count the amount of words
def count_words(text):
    # splits the text up into individual words as a variable named word_count
    word_count = text.split()
    # return the length of word_count
    return len(word_count)

# Define count_sentences as a function to put punctuation into as a list to count the amount of sentences
def count_sentences(text):
    # Counts the amount of periods
    period_count = text.count('.')
    # Counts the amount of exclamation marks
    exclamation_count = text.count('!')
    # Counts the amount of question marks
    question_mark_count = text.count('?')
    # Adds all the counts up to a total amount of sentences
    total_sentence = (period_count + exclamation_count + question_mark_count)
    # Returns the total sentence
    return(total_sentence)