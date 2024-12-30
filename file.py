def count_words_in_file(file_path):
    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            text = file.read()
        
        # Split the text into words and normalize (lowercase)
        words = text.lower().split()
        
        # Remove punctuation from words
        import string
        words = [word.strip(string.punctuation) for word in words]
        
        # Count word occurrences
        word_count = {}
        for word in words:
            if word:
                word_count[word] = word_count.get(word, 0) + 1
        
        # Sort by alphabetical order
        sorted_word_count = dict(sorted(word_count.items()))
        
        # Display the results
        print("Word occurrences in alphabetical order:")
        for word, count in sorted_word_count.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the text file
file_path = input("Enter the path to the text file: ")

# Call the function
count_words_in_file(file_path)

