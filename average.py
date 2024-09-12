import text_utils
# Defines average
def average():
    # Creates a variable named file to open filename in read mode
    file = with open(sample.txt, 'r'):
        # Creates a variable named lines to read the lines in the file
        lines = file.readlines()
        # Sets line_count and word_count to zero for possible array and list
        line_count = 0
        word_count = 0
        #Creates a for loop for line in lines
        for line in lines:
            # Creates an array to go up every line
            line_count = line_count + 1
            # Makes word_count into a variable and adds word_count into the text_utils to count all the words in each line
            word_count = word_count + text_utils.count_words(lines)
            # Closes the file
        file.close()
        # Before average constant equation(divides word count by line count to find the average words per line)
        b4avg = word_count // line_count
        #Returns variable
        return(b4avg)
    #Prints line for averages words per line
    print(f"Average words per line: {average()}")