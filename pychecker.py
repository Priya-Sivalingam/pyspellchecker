from spellchecker import SpellChecker

# Initialize the spell checker
spell = SpellChecker()

# Split the sentence into words
sentence = 'Thes is a sample paragraf with some incorectly spelt words.'
words = sentence.split()  # Split sentence into words

# Find misspelled words
misspelled = spell.unknown(words)

# Loop through each misspelled word
for word in misspelled:
    # Get the 'most likely' correction
    print(f"Correction for '{word}': {spell.correction(word)}")

    # Get a list of likely candidates
    print(f"Candidates for '{word}': {spell.candidates(word)}")
