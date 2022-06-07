# import regular expression
import re

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from part_of_speech import get_part_of_speech

lemmatizer = WordNetLemmatizer()

oprah_wiki = '<p>Working in local media, she was both the youngest news anchor and the first black female news anchor at Nashville\'s WLAC-TV. </p>'

# for 1 = .sub()
# for 2 = stack_overflow
# for 3 = var.lower()
# for 4 = word_tokenize(string)
# for 5 = list comp. for loop

# line 20, we use regex character sets to strip two html tags

# step 1 and 2
result = re.sub(r'[\<p>\</p>\.]', '', oprah_wiki)
#print(result)

# step 3
result_two = result.lower()
#print(result_two)

# step 4
result_tokenize = word_tokenize(result_two)
print(result_tokenize)

# step 5 - list comp and for loop to lemmatize each word

result_lemmatize = [lemmatizer.lemmatize(word) for word in result_tokenize]
print(result_lemmatize)
