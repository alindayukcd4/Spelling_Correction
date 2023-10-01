from textblob import TextBlob

def correct_words(words):
    corrected_words = []
    for word in words:
        corrected_word = TextBlob(word).correct()
        corrected_words.append(str(corrected_word))
    return corrected_words

if __name__ == "__main__":
    input_text = input("Enter a list of words separated by spaces: ")
    words = input_text.split()
    
    corrected_words = correct_words(words)
    
    print("Original words:", words)
    print("Corrected words:")
    for word in corrected_words:
        print(word, end=" ")
