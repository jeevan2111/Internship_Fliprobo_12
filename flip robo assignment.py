#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
import re


# 
# Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Expected Output: Python:Exercises::PHP:exercises:
# 

# In[2]:


def replace_to_colon(text):
    pattern = r'[ ,.]'

    result = re.sub(pattern, ':', text)
    return result

text = 'Python Exercises, PHP exercises.'

print(replace_with_colon(text))


# Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# Expected output-
# 0      hello world
# 1             test
# 2    four five six
# 

# In[4]:


data = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}

df = pd.DataFrame(data)

def clean_text(text):
    return re.sub(r'[^a-zA-Z\s]', '', text).strip()

df['SUMMARY'] = df['SUMMARY'].apply(clean_text)

print(df)


# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[7]:


def find_long_words_method1(text):
    pattern = re.compile(r'\b\w{4,}\b')
    
    matches = pattern.findall(text)
    
    return matches

sample_text = "Kalki is the tenth avatar of Lord Vishnu"
print(find_long_words_method1(sample_text))


# Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

# In[9]:


def find_long_words_method1(text):
    pattern = re.compile(r'\b\w{2,}\b')
    
    matches = pattern.findall(text)
    
    return matches

sample_text = "Kalki is the tenth avatar of Lord Vishnu"
print(find_long_words_method1(sample_text))


# Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output:
# example.com
# hr@fliprobo.com
# github.com
# Hello Data Science World
# Data Scientist

# In[11]:


def remove_parentheses(strings):
    pattern = re.compile(r'\s*\(.*?\)\s*')
    
    return [pattern.sub('', s).strip() for s in strings]

sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
print(remove_parentheses(sample_text))


# In[12]:


def remove_parentheses_method1(strings):
    # Compile the pattern to match parentheses and their contents
    pattern = re.compile(r'\s*\(.*?\)\s*')
    
    # Replace matched parentheses and contents with an empty string
    return [pattern.sub('', s).strip() for s in strings]

# Sample text
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
print(remove_parentheses_method1(sample_text))


# In[13]:


import re

def remove_parentheses(strings):
    # Compile a regular expression pattern to match parentheses and their contents
    pattern = re.compile(r'\s*\(.*?\)\s*')
    
    # Process each string in the list
    cleaned_strings = [pattern.sub('', s).strip() for s in strings]
    
    return cleaned_strings

# Sample text
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

# Call the function and print the result
print(remove_parentheses(sample_text))


# In[14]:


def remove_parentheses_method2(strings):
    # Compile the pattern to match parentheses and their contents
    pattern = re.compile(r'\s*\(.*?\)\s*')
    
    # Process each string in the list
    cleaned_strings = []
    for s in strings:
        # Use re.finditer to find all matches
        for match in pattern.finditer(s):
            s = s.replace(match.group(), '')
        cleaned_strings.append(s.strip())
    
    return cleaned_strings

# Sample text
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
print(remove_parentheses_method2(sample_text))


# In[15]:


def remove_parentheses_method1(strings):

    pattern = re.compile(r'\s*\(.*?\)\s*')
    
    return [pattern.sub('', s).strip() for s in strings]

sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
print(remove_parentheses_method1(sample_text))


# In[44]:


# i tried many methods but output was not same
def remove_parentheses(strings):

    pattern = re.compile(r'\s*\(.*?\)\s*')
    
    return [pattern.sub('', s).strip() for s in strings]

sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

for i in remove_parentheses(sample_text):
    print(i)


# Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
# Note- Store given sample text in the text file and then to remove the parenthesis area from the text.
# 

# In[23]:


def remove_parentheses(strings):
    # Compile a regular expression pattern to match parentheses and their contents
    pattern = re.compile(r'\s*\(.*?\)\s*')
    
    # Process each string in the list
    cleaned_strings = [pattern.sub('', s).strip() for s in strings]
    
    return cleaned_strings

# Sample text
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

# Call the function and print the result
print(remove_parentheses(sample_text))


# In[46]:


def remove_parentheses1(strings):

    pattern = re.compile(r'\s*\(.*?\)\s*')
    
    return [pattern.sub('', s).strip() for s in strings]

sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
print(remove_parentheses1(sample_text))


# Question 7- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[56]:


def split_to_uppercase(text):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    
    para = pattern.split(text)
    
    return para

sample_text = "ImportanceOfRegularExpressionsInPython"
print(split_to_uppercase(sample_text))


# Question 8- Create a function in python to insert spaces between words starting with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
# 

# In[60]:


def insert_space(text):
    result = []
    i = 0
    while i < len(text):
        result.append(text[i])
        if text[i].isdigit() and i + 1 < len(text) and text[i + 1].isupper():
            result.append(' ')
        i += 1
    return ''.join(result)

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
print(insert_space(sample_text))


# Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython
# 

# In[109]:


def insert_spaces_regex(text):
    # This pattern matches a capital letter or number that follows a lowercase letter or number
    pattern = re.compile(r'(?<=[a-z0-9])(?=[A-Z0-9])')
    
    # Use re.sub to replace the matched pattern with a space
    result = pattern.sub(' ', text)
    
    return result

# Sample text
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
print(insert_spaces_regex(sample_text))


# In[65]:


def insert_space(text):
    pattern = re.compile(r'(?<=[a-z0-9])(?=[A-Z0-9])')
    
    result = pattern.sub(' ', text)
    
    return result

sample_text = "RegularExpression1isAn2importantTopic3inPython"
print(insert_spaces_regex(sample_text))


# Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# In[67]:


import pandas as pd

# Step 1: Read the data from the GitHub link into a DataFrame
url = 'https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
df = pd.read_csv(url)

# Display the first few rows of the DataFrame to understand its structure
print("Initial DataFrame:")
print(df.head())

# Step 2: Extract the first 6 letters of each country and store in a new column
df['first_five_letters'] = df['Country'].str[:6]

# Display the updated DataFrame
print("\nDataFrame with 'first_five_letters' column:")
print(df.head())


# In[72]:


def first_five_letters():
    url = 'https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
    df = pd.read_csv(url)
    
    df['first_five_letters'] = [country[:5] for country in df['Country']]
    
    return df
df_method = first_five_letters()
print(df_method.head())


# Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# Question 12- Write a Python program where a string will start with a specific number. 

# In[87]:


def starts_with_number_match(n, number):
    pattern = re.compile(rf'^{number}')
    
    return bool(pattern.match(n))

num = ["123abc"]

for string in num:
    result = starts_with_number_match(string, number)
    print(f"'{string}' starts with {number}: {result}")


# Question 13- Write a Python program to remove leading zeros from an IP address

# In[94]:


def remove_zero(ip):
    pattern = re.compile(r'\b0+(\d)')

    cleaned_ip = pattern.sub(r'\1', ip)
    
    cleaned_ip = re.sub(r'\b0+', '0', cleaned_ip)
    
    return cleaned_ip

ips = ["192.168.01.001"]

for ip in ips:
    cleaned_ip = remove_zero(ip)
    print(f"Old IP: {ip} -> New IP: {cleaned_ip}")


# Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# Expected Output- August 15th 1947
# Note- Store given sample text in the text file and then extract the date string asked format.
# 

# ans14- didnt understand question 14

# Question 15- Write a Python program to search some literals strings in a string. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 

# In[97]:


def search_word(text, words):
    pattern = re.compile('|'.join(re.escape(word) for word in words))
    
    match = pattern.findall(text)
    
    return match

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_words = ['fox', 'dog', 'cat']

found_words = search_word(sample_text, searched_words)
print("Found words:", found_words)


# Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 

# In[99]:


def search_and_locate(text, word):
    pattern = re.compile(re.escape(word))
    
    matches = pattern.finditer(text)
    
    positions = [(match.start(), match.end()) for match in matches]
    
    return positions

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_word = 'fox'

positions = search_and_locate(sample_text, searched_word)

print(f"Occurrences of '{searched_word}':")
for start, end in positions:
    print(f"Found at position {start} to {end}: {sample_text[start:end]}")


# Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.
# 

# In[102]:


def find_substrings(text, word):
    regex = re.compile(re.escape(word))
    
    matches = regex.finditer(text)
    
    positions = [(match.start(), match.end()) for match in matches]
    
    return positions

sample_text = 'Python exercises, PHP exercises, C# exercises'

word = 'exercises'

positions = find_substrings(sample_text, pattern)

print(f"Occurrences of '{word}':")
for start, end in positions:
    print(f"Found at position {start} to {end}: {sample_text[start:end]}")


# Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[105]:


def find_substrings_with_positions(text, word):
    regex = re.compile(re.escape(word))
    
    matches = regex.finditer(text)
    
    positions = [(match.start(), match.end(), match.group()) for match in matches]
    
    return positions

sample_text = 'Python exercises, PHP exercises, C# exercises'

substring = 'exercises'

positions = find_substrings_with_positions(sample_text, substring)

print(f"Occurrences of '{substring}':")
for start, end, match in positions:
    print(f"Found '{match}' at position {start} to {end}")


# Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[106]:


from datetime import datetime

def convert_date_format(date_str):
    input_format = "%Y-%m-%d"
    date_obj = datetime.strptime(date_str, input_format)
    
    output_format = "%d-%m-%Y"
    formatted_date = date_obj.strftime(output_format)
    
    return formatted_date

date_string = "2002-11-21"

converted_date = convert_date_format(date_string)
print(f"Original date: {date_string}")
print(f"Converted date: {converted_date}")


# Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']
# 

# In[107]:


def find_decimal_num(text):
    pattern = re.compile(r'\b\d*\.\d{1,2}\b')
    
    matches = pattern.findall(text)
    
    return matches

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

result = find_decimal_num(sample_text)

print("Decimal numbers with precision of 1 or 2 decimal places:", result)


# Question 21- Write a Python program to separate and print the numbers and their position of a given string.

# ans - 21- i tried but didnt understand

# Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# Expected Output: 950
# 

# In[108]:


def find_max_value(text):
    pattern = re.compile(r'\d+')
    
    matches = pattern.findall(text)

    numbers = [int(match) for match in matches]

    max_value = max(numbers) if numbers else None
    
    return max_value

sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

max_numeric_value = find_max_value(sample_text)

print(f"The maximum numeric value is: {max_numeric_value}")


# Question 23- Create a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# Expected Output: Regular Expression Is An Important Topic In Python
# 

# In[114]:


def insert_spaces_regex(text):
    pattern = re.compile(r'(?=[A-Z])')
    
    result = pattern.sub(' ', text)
    
    return result

sample_text = "RegularExpressionIsAnImportantTopicInPython"
print(insert_spaces_regex(sample_text))


# Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[118]:


def find_upper_by_lower(text):
    pattern = re.compile(r'[A-Z][a-z]+')
    
    matches = pattern.findall(text)
    
    return matches

sample_text = 'RegularExpressionIsAnImportantTopicInPython.'

sequences = find_upper_followed_by_lower(sample_text)

print("Sequences of one uppercase letter followed by lowercase letters:")
print(sequences)


# Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# Expected Output: Hello hello world
# 

# In[119]:


def remove_continuous_duplicates(sentence):
    # Compile the regex pattern to match continuous duplicate words
    pattern = re.compile(r'\b(\w+)\s+\1\b', re.IGNORECASE)
    
    # Substitute the duplicates with a single occurrence of the word
    cleaned_sentence = pattern.sub(r'\1', sentence)
    
    return cleaned_sentence

# Sample text
sample_text = "Hello hello world world"

# Remove continuous duplicate words
result = remove_continuous_duplicates(sample_text)

# Print the result
print("Original Sentence:", sample_text)
print("Cleaned Sentence:", result)


# Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[122]:


def alphanumeric(text):
    pattern = re.compile(r'\w$')
    
    if pattern.search(text):
        return True
    else:
        return False

test_strings = [
    "Hello1",
    "Python program",
    "click123",
    "Just a test.",
    "Valid_"
]

# Check each string
for text in test_strings:
    result = alphanumeric(text)
    print(f"'{text}' ends with an alphanumeric character: {result}")


# Question 27-Write a python program using RegEx to extract the hashtags.
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
# 

# In[125]:


def extract_hashtags(text):
    # Compile the regex pattern to match hashtags
    pattern = re.compile(r'#\w+')
    
    # Find all hashtags in the text
    hashtags = pattern.findall(text)
    
    return hashtags

# Sample text
sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered #USELESS """

# Extract hashtags
hashtags = extract_hashtags(sample_text)

# Print the result
print("Extracted hashtags:", hashtags)


# Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders
# 

# ans-28 - didnt understand

# Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
# The use of the re.compile() method is mandatory.
# Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.
# 

# In[126]:


def remove_short_words(text):
    pattern = re.compile(r'\b\w{2,4}\b')

    cleaned_text = pattern.sub('', text).strip()

    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    return cleaned_text

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

result = remove_short_words(sample_text)

print("Cleaned Text:", result)

