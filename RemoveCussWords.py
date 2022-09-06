# Remove Cuss Words 
# By Busyman.Inc

# pip install better_profanity

from better_profanity import profanity
text = input("Enter your sentence to check:")
censored = profanity.censor(text)
print(censored) 
