import spacy
import re

# load spacy model
nlp = spacy.load("en_core_web_sm")

# POS categories
pos_categories = {
    "verb": set(),
    "aux_verb": set(),
    "noun": set(),
    "proper_noun": set(),
    "adjective": set(),
    "adverb": set(),
    "pronoun": set(),
    "determiner": set(),
    "preposition": set(),
    "conjunction": set(),
    "number": set(),
    "interjection": set()
}

# semantic categories
semantic_categories = {
    "question_word": set(),
    "time": set()
}

question_candidates = {"who","what","where","when","why","how","which"}

time_pattern = re.compile(r"\d{1,2}:\d{2}(?:AM|PM)?", re.IGNORECASE)

# read common word list
with open("mostcommon.txt") as f:
    words = [line.strip().lower() for line in f if line.strip()]

print("Total words:", len(words))

# process words
for word in words:

    doc = nlp(word)

    for token in doc:

        pos = token.pos_

        if pos == "VERB":
            pos_categories["verb"].add(word)

        elif pos == "AUX":
            pos_categories["aux_verb"].add(word)

        elif pos == "NOUN":
            pos_categories["noun"].add(word)

        elif pos == "PROPN":
            pos_categories["proper_noun"].add(word)

        elif pos == "ADJ":
            pos_categories["adjective"].add(word)

        elif pos == "ADV":
            pos_categories["adverb"].add(word)

        elif pos == "PRON":
            pos_categories["pronoun"].add(word)

        elif pos == "DET":
            pos_categories["determiner"].add(word)

        elif pos == "ADP":
            pos_categories["preposition"].add(word)

        elif pos in ["CCONJ", "SCONJ"]:
            pos_categories["conjunction"].add(word)

        elif pos == "NUM":
            pos_categories["number"].add(word)

        elif pos == "INTJ":
            pos_categories["interjection"].add(word)

    # semantic categories
    if word in question_candidates:
        semantic_categories["question_word"].add(word)

    if time_pattern.fullmatch(word):
        semantic_categories["time"].add(word)

# verification
all_pos_words = set().union(*pos_categories.values())
all_semantic_words = set().union(*semantic_categories.values())

categorized = all_pos_words | all_semantic_words
missing = set(words) - categorized

print("\nVerification")
print("Total words:", len(words))
print("Categorized:", len(categorized))
print("Missing:", len(missing))

if missing:
    print("Missing words:", missing)

# helper printer
def print_set(name, s):

    print(f"\n{name} = {{")
    for w in sorted(s):
        print(f'    "{w}",')
    print("}")

# print POS categories
print("\n# POS Categories")
for name, s in pos_categories.items():
    print_set(name, s)

# print semantic categories
print("\n# Semantic Categories")
for name, s in semantic_categories.items():
    print_set(name, s)