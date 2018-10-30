import re

# Function for analyzing a paragraph
def AnalyzeParagraph(filename):
    
    # Fetch paragraph from text file and read to text list
    text = []
    with open(filename, 'r') as f:
        for line in f:
            # line.strip() returns false if empty
            if line.strip() == False: continue # skip the empty line
            text.append(line.strip())

    # Split text into a list of sentences 
    sentence_list = []
    for line in text:

        # Look before spaces for punctuation and split on both punctuation and spaces
        #   [^A-Z] ensures that abbreviated names are not split on (Anne V. Coates)
        sentences = re.split("(?<=[^A-Z][.!?]) +", line)
        for sentence in sentences:
            
            # Add each sentence to sentence_list
            sentence_list.append(sentence)
            
            # Debug
            #print(sentence + "\n")
    
    num_sentences = len(sentence_list)
        
    # Initialize variables to enter for-loop (to count number of words)
    words = []
    sum_sentence_len = 0
    sum_word_len = 0
    
    ############################
    # Loop through each sentence
    ############################
    for sentence in sentence_list:
        
        # Split the sentence into a list of words
        word_list = sentence.split(" ")
        
        # Add the sentence length to a sum
        sum_sentence_len += len(word_list)
            
        # Split each sentence into words
        for word in word_list:
            
            # Append each word to the words list
            words.append(word)
            
            # Add the word length to a summing variable
            sum_word_len += len(word)
        
    num_words = len(words)
    avg_word_length = round(sum_word_len/num_words, 1)
    avg_sentence_length = round(sum_sentence_len/num_sentences, 1)
    
    # Print analysis results
    print("Paragraph Analysis")
    print("-----------------")
    print(f"Approximate Word Count: {num_words}")
    print(f"Approximate Sentence Count: {num_sentences}")
    print(f"Average Letter Count: {avg_word_length}")
    print(f"Average Sentence Length: {avg_sentence_length}")

######################################################################
#                      Change the filename below                     #
######################################################################
AnalyzeParagraph('example.txt')
print()
AnalyzeParagraph('paragraph_1.txt')
print()
AnalyzeParagraph('paragraph_2.txt')

