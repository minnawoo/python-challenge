import re

def AnalyzeParagraph(filename):
    
    # Fetch paragraph from text file
    input = []
    with open(filename, 'r') as f:
        for line in f:
            if not line.strip(): continue # skip the empty line
            input.append(line.strip())

    # Split into a list of sentences 
    sentence_list = []
    for line in input:
        sentences = re.split("(?<=[^A-Z][.!?]) +", line)
        for sentence in sentences:
            
            # Add each sentence to sentence_list
            sentence_list.append(sentence)
            
            #print(sentence + "\n") # test
    
    num_sentences = len(sentence_list)
        
    # Initialize variables
    words = []
    sum_sentence_len = 0
    sum_word_len = 0
    
    # Loop through each sentence
    for sentence in sentence_list:
        
        # Split the sentence into a list of words
        split_sentence = sentence.split(" ")
        
        # Add the sentence length to a summing variable
        sum_sentence_len += len(split_sentence)
            
        # Split each sentence and compile into the words list
        for word in split_sentence:
            
            # Append each word to the words list
            words.append(word)
            
            # Add the word length to a summing variable
            sum_word_len += len(word)
        
    avg_sentence_length = round(sum_sentence_len/num_sentences, 1)
    num_words = len(words)
    avg_word_length = round(sum_word_len/num_words, 1)
    
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
AnalyzeParagraph('paragraph_1.txt')

