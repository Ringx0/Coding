# The given text that you want to analyze
text = """ It's Time For A Complete DevOps Solution That Does It All. Start Your Free Trial Today. Learn about Auto DevOps. From Project Planning and Source Code Management to CI/CD, Monitoring, and Security. Get Your GitLab Demo. """

# Create an empty dictionary to store word frequencies.
word_count = {}

# Split the text into individual words, convert them to lowercase, and loop through them.
for word in text.lower().split():
    # Check if the word is already in the word_count dictionary.
    if word in word_count:
        # If the word is already in the dictionary, increment its count by 1.
        word_count[word] += 1
    else:
        # If the word is not in the dictionary, add it with a count of 1.
        word_count[word] = 1

# Print the final word count dictionary, which contains each word and its frequency.
print(word_count)
