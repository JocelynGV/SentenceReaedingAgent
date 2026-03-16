import spacy
import re

# load spacy model
nlp = spacy.load("en_core_web_sm")

# categories we want
verbs = set()
aux_verbs = set()
nouns = set()
proper_nouns = set()
adjectives = set()
adverbs = set()
pronouns = set()
determiners = set()
prepositions = set()
conjunctions = set()
numbers = set()
interjections = set()

# semantic categories
question_words = set()
times = set()

# question words list
question_candidates = {"who","what","where","when","why","how","which"}

# time pattern
time_pattern = re.compile(r"\d{1,2}:\d{2}")

# read the word list
with open("mostcommon.txt") as f:
    words = [line.strip().lower() for line in f if line.strip()]

print("Total words:", len(words))

# process each word
for word in words:

    doc = nlp(word)

    for token in doc:

        pos = token.pos_

        if pos == "VERB":
            verbs.add(word)

        elif pos == "AUX":
            aux_verbs.add(word)

        elif pos == "NOUN":
            nouns.add(word)

        elif pos == "PROPN":
            proper_nouns.add(word)

        elif pos == "ADJ":
            adjectives.add(word)

        elif pos == "ADV":
            adverbs.add(word)

        elif pos == "PRON":
            pronouns.add(word)

        elif pos == "DET":
            determiners.add(word)

        elif pos == "ADP":
            prepositions.add(word)

        elif pos == "CCONJ" or pos == "SCONJ":
            conjunctions.add(word)

        elif pos == "NUM":
            numbers.add(word)

        elif pos == "INTJ":
            interjections.add(word)

    # detect question words
    if word in question_candidates:
        question_words.add(word)

    # detect times
    if time_pattern.fullmatch(word):
        times.add(word)

# verification
categorized = (
    verbs | aux_verbs | nouns | proper_nouns |
    adjectives | adverbs | pronouns |
    determiners | prepositions | conjunctions |
    numbers | interjections | question_words | times
)

missing = set(words) - categorized

print("\nVerification")
print("Total words:", len(words))
print("Categorized:", len(categorized))
print("Missing:", len(missing))

if missing:
    print("Missing words:", missing)

# helper to print python sets
def print_set(name, s):
    print(f"\n{name} = {{")
    for w in sorted(s):
        print(f'    "{w}",')
    print("}")

# print everything for copy/paste
print_set("verbs", verbs)
print_set("aux_verbs", aux_verbs)
print_set("nouns", nouns)
print_set("proper_nouns", proper_nouns)
print_set("adjectives", adjectives)
print_set("adverbs", adverbs)
print_set("pronouns", pronouns)
print_set("determiners", determiners)
print_set("prepositions", prepositions)
print_set("conjunctions", conjunctions)
print_set("numbers", numbers)
print_set("interjections", interjections)
print_set("question_words", question_words)
print_set("times", times)