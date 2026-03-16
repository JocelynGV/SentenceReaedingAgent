class SentenceReadingAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, sentence, question):
        
      thematic_role = {
        "verb": None,
        "agent": None,
        "action": None,
        "object": None,
        "recipient": None,
        "location": None,
        "time": None,
        "distance": None,
        "descriptor": None,
        "beneficiary": None,
        "duration": None,
        "source": None,
        "coagent": None,
        "instrument": None,
        "conveyance": None
      }
      # words = sentence.split()
      # print(words)

      # for word in words:
      #     if word in verb:
      #         pos_categories["verb"].add(word)      

      sentence = sentence.lower().replace(".", "")
      words = sentence.split()
      info = self.categorize_words(words)

      for w in info:
        print(w)

      verb_index = None

      for token in info:
          if token["pos"] == "verb":
              verb_index = token["index"]
              action = token["word"]
              thematic_role["verb"] = action
              break


      # rules for thematic role 
      agents = []

      # get agent
      for token in info:
          if token["index"] < verb_index and token["type"] == "animate":
              agents.append(token["word"])
      thematic_role["agent"] = agents

      # get object
      for t in info:
        if t["index"] > verb_index:

            if t["pos"] == "preposition":
                break

            if t["pos"] == "noun":
                thematic_role["object"] = t["word"]
                break

      # analyze prepositions
      for token in info:
          if token["pos"] == "preposition":
              preposition = token["word"]

              if preposition in ["by"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["type"] == "animate":
                            thematic_role["agent"] = t["word"]
                            break
                          if t["type"] == "inanimate":
                            thematic_role["conveyance"] = t["word"]
                            thematic_role["location"] = t["word"]
                            break

              elif preposition in ["for"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["type"] == "animate":
                            thematic_role["beneficiary"] = t["word"]
                            break
                          if t["type"] == "time":
                            thematic_role["duration"] = t["word"]
                            break
                      
              elif preposition in ["from"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["pos"] == "noun":
                            thematic_role["source"] = t["word"]
                            break

              elif preposition in ["to"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["pos"] == "noun":
                            thematic_role["destination"] = t["word"]
                            break
                          if t["type"] == "animate":
                            thematic_role["recipient"] = t["word"]
                            break
              
              elif preposition in ["at"]:
                for t in info:
                    if t["index"] > token["index"]:
                        if t["pos"] == "preposition":
                            break
                        if t["type"] == "time":
                            thematic_role["time"] = t["word"]
                            break
                        if t["pos"] == "noun":
                            thematic_role["location"] = t["word"]
                            break


              elif preposition in ["in", "on", "under", "near"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["pos"] == "noun":
                              thematic_role["location"] = t["word"]
                              break


              elif preposition in ["before", "after", "during", "until"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["type"] == "time":
                              thematic_role["time"] = t["word"]
                              break
                          if t["pos"] == "noun":
                              thematic_role["time"] = t["word"]
                              break
              
              elif preposition in ["with"]:
                  # likely recipient
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["type"] == "animate":
                            thematic_role["coagent"] = t["word"]
                            break
                          if t["pos"] == "noun":
                            thematic_role["instrument"] = t["word"]
                            break

              elif preposition in ["after", "before"]:
                  # likely time
                  for t in info:
                      if t["index"] > token["index"] and t["type"] == "inanimate":
                          thematic_role["time"] = t["word"]
                          break
                      
              elif preposition in ["toward", "through"]:
                for t in info:
                    if t["index"] > token["index"]:
                        if t["pos"] == "preposition":
                            break
                        if t["pos"] == "noun":
                            thematic_role["path"] = t["word"]
                            break


              elif preposition in ["between", "among"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["type"] == "animate":
                              thematic_role["coagent"] = t["word"]
                              break


              elif preposition in ["against"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["pos"] == "noun":
                              thematic_role["object"] = t["word"]
                              break


              elif preposition in ["of"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["pos"] == "noun":
                              thematic_role["possessor"] = t["word"]
                              break


              elif preposition in ["off"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["pos"] == "noun":
                              thematic_role["source"] = t["word"]
                              break


              elif preposition in ["than"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["pos"] == "noun":
                              thematic_role["comparison"] = t["word"]
                              break


              elif preposition in ["as"]:
                  for t in info:
                      if t["index"] > token["index"]:
                          if t["pos"] == "preposition":
                              break
                          if t["pos"] == "noun":
                              thematic_role["role"] = t["word"]
                              break

      print("Thematic Role:" + str(thematic_role))



      '''
      You can use a library like spacy (https://spacy.io/usage/linguistic-features) to preprocess the
      mostcommon.txt file. There are others that could be used but you must use them in preprocessing only.
      You CANNOT import the library into Gradescope.

      You must include whatever preprocessing you've done into your SentenceReadingAgent.py.

      DO NOT use another file .txt or .csv. Hard code your DICTS | LISTS into this .py file

      While the supplied mostcommon.txt contains most of the common words you will need
      you can (and SHOULD) expand the file as you find cases that the agent has problems
      processing. 

      Also not all words will be processed using the correct lexing for every possible problem the 
      agent might encounter and you are ENCOURAGED to expand these in your agents knowledge representation.
      '''

      #Add your code here! Your solve method should receive
      #two strings as input: sentence and question. It should
      #return a string representing the answer to the question.
      pass

    def is_time(word):
      word = word.strip()

      # Check AM/PM
      period = None
      if word.endswith("AM") or word.endswith("PM"):
          period = word[-2:]
          word = word[:-2]

      # Must contain :
      if ":" not in word:
          return False

      parts = word.split(":")
      if len(parts) != 2:
          return False

      hour, minute = parts

      # Check numeric
      if not hour.isdigit() or not minute.isdigit():
          return False

      hour = int(hour)
      minute = int(minute)

      # Validate minutes
      if minute < 0 or minute > 59:
          return False

      if period:  # 12-hour clock
          return 1 <= hour <= 12
      else:       # 24-hour clock
          return 0 <= hour <= 23
      

      
    def categorize_words(self, words):
      # POS dictionary
      pos_categories = {
          "verb": verb,
          "aux_verb": aux_verb,
          "noun": noun,
          "proper_noun": proper_noun,
          "pronoun": pronoun,
          "adjective": adjective,
          "adverb": adverb,
          "determiner": determiner,
          "preposition": preposition,
          "conjunction": conjunction,
          "number": number,
          "interjection": interjection
      }

      word_info = []

      for i, word in enumerate(words):

          word_lower = word.lower()

          pos = "unknown"
          semantic_type = None

          # Detect part of speech
          for category, word_set in pos_categories.items():
              if word_lower in word_set:
                  pos = category
                  break

          # Detect semantic type
          if word in proper_noun or word in animate:
              semantic_type = "animate"
          elif word in noun:
              semantic_type = "inanimate"

          if self.is_time(word):
              semantic_type = "time"

          # Store structured information
          word_info.append({
              "word": word,
              "pos": pos,
              "type": semantic_type,
              "index": i
          })

      return word_info
    
    def is_time(self, word):
      word = word.upper()

      # check AM/PM
      if word.endswith("AM") or word.endswith("PM"):
          time_part = word[:-2]
      else:
          time_part = word

      if ":" not in time_part:
          return False

      parts = time_part.split(":")
      if len(parts) != 2:
          return False

      hour, minute = parts

      if not hour.isdigit() or not minute.isdigit():
          return False

      hour = int(hour)
      minute = int(minute)

      if hour < 0 or hour > 12:
          return False

      if minute < 0 or minute > 59:
          return False

      return True


verb = {
"add","answer","appear","ask","began","begin","bring","brought","build","call","came","care",
"carry","cause","change","check","come","contain","cover","cross","cry","cut","decide","develop",
"did","differ","do","does","don't","done","draw","drive","eat","face","feel","fill","find","fly",
"follow","found","gave","get","give","go","got","govern","grow","had","happen","has","have",
"hear","heard","help","hold","keep","knew","know","laugh","lay","lead","learn","leave","left",
"let","listen","look","made","make","mean","mind","miss","move","need","note","notice","object",
"pass","play","pose","produce","pull","put","ran","reach","read","remember","rest","run","said",
"saw","say","see","seem","serve","set","show","sing","sings","sit","sound","spell","stand",
"start","stay","step","stood","stop","take","talk","teach","tell","think","thought","told",
"took","try","turn","wait","walk","want","watch","went","work","write","wrote","yeeling"
}

aux_verb = {
"am","are","be","been","can","could","is","may","might","must","should","was","were","will","would"
}

noun = {
"act","adult","adults","age","air","animal","area","base","beauty","bed","bird","boat","body",
"boy","car","children","city","class","color","country","course","day","dog","dogs","door",
"earth","ease","end","example","eye","fact","fall","family","farm","feet","field","figure",
"fire","fish","food","foot","force","form","friend","front","game","girl","gold","ground",
"group","hand","head","heat","home","horse","hour","idea","inch","interest","island","king",
"land","language","laura","letter","life","light","line","list","lot","love","machine","man",
"map","measure","men","mile","minute","money","moon","morning","mother","mountain","music",
"name","night","north","number","order","page","paper","part","pattern","people","person",
"picture","piece","place","plan","plane","plant","point","port","pound","power","press",
"problem","product","question","rain","river","road","rock","room","rule","school","science",
"sea","self","sentence","serena","shape","ship","side","size","sleep","snow","song","state",
"story","street","study","surface","table","tail","test","thing","time","town","travel","tree",
"unit","use","voice","vowel","war","water","way","week","weight","wheel","wind","wonder",
"wood","word","world","year","book","box","center","east","father","green","house","record",
"star","sun","west","note"
}

proper_noun = {
"ada","andrew","bobbie","cason","david","farzana","frank","hannah",
"ida","irene","jim","jose","keith","lucy","mark","meredith","nick","yan"
}

adjective = {
"able","big","black","blue","busy","certain","cold","common","complete","cool","correct",
"dark","deep","direct","dry","fast","few","final","fine","free","full","good","great","half",
"hard","high","hot","large","last","little","live","low","main","many","much","new","next",
"numeral","old","open","other","own","possible","quick","ready","real","red","round","same",
"second","several","short","simple","slow","small","south","special","strong","such","sure",
"top","true","usual","warm","white","whole","young"
}

adverb = {
"about","above","again","ago","also","always","back","behind","best","better","clear","close",
"down","early","enough","even","ever","far","first","here","just","kind","late","less","long",
"more","most","never","now","often","once","only","out","over","perhaps","plain","so","soon",
"still","then","together","too","up","very","well","yet"
}

pronoun = {
"he","her","him","his","i","it","me","my","nothing","our","she","their","them","there",
"they","us","we","you","your"
}

determiner = {
"a","an","the","this","that","these","those","each","every","some","any","both"
}

preposition = {
"to","after","against","among","as","at","before","between","by","during","for",
"from","in","near","of","off","on","than","through","toward","under","until","with"
}

conjunction = {
"and","but","if","or","since","that","though","while"
}

number = {
"one","two","three","four","five","six","ten","hundred","thousand"
}

interjection = {
"like","no","oh","right","yes"
}

question_word = {
"how","what","when","where","which","who","why"
}

animate = {
"ada","andrew","bobbie","cason","david","farzana","frank","hannah",
"ida","irene","jim","jose","keith","lucy","mark","meredith","nick","yan",
"adult","adults","boy","children","dog","dogs","family","friend",
"girl","king","man","men","mother","people","person"
}



'''
verb = {"add","answer","appear","ask","began","begin","bring","brought","build","call","came","care","carry","cause","change","check","come","contain","cover","cross","cry","cut","decide","develop","did","differ","do","does","don't","done","draw","drive","eat","face","feel","fill","find","fly","follow","found","gave","get","give","go","got","govern","grow","had","happen","has","have","hear","heard","help","hold","keep","knew","know","laugh","lay","lead","learn","leave","left","let","listen","look","made","make","mean","mind","miss","move","need","note","notice","object","pass","play","pose","produce","pull","put","ran","reach","read","remember","rest","run","said","saw","say","see","seem","serve","set","show","sing","sings","sit","sound","spell","stand","start","stay","step","stood","stop","take","talk","teach","tell","think","thought","told","took","try","turn","wait","walk","want","watch","went","work","write","wrote","yeeling"}

aux_verb = {"am","are","be","been","can","could","is","may","might","must","should","was","were","will","would"}

noun = {"act","adult","adults","age","air","animal","area","base","beauty","bed","bird","boat","body","boy","car","children","city","class","color","country","course","day","dog","dogs","door","earth","ease","end","example","eye","fact","fall","family","farm","feet","field","figure","fire","fish","food","foot","force","form","friend","front","game","girl","gold","ground","group","hand","head","heat","home","horse","hour","idea","inch","interest","island","king","land","language","laura","letter","life","light","line","list","lot","love","machine","man","map","measure","men","mile","minute","money","moon","morning","mother","mountain","music","name","night","north","number","order","page","paper","part","pattern","people","person","picture","piece","place","plan","plane","plant","point","port","pound","power","press","problem","product","question","rain","river","road","rock","room","rule","school","science","sea","self","sentence","serena","shape","ship","side","size","sleep","snow","song","state","story","street","study","surface","table","tail","test","thing","time","town","travel","tree","unit","use","voice","vowel","war","water","way","week","weight","wheel","wind","wonder","wood","word","world","year"}

proper_noun = {"ada","andrew","bobbie","book","box","cason","center","david","dog's","east","farzana","father","frank","green","hannah","house","ida","irene","jim","jose","keith","lucy","mark","meredith","nick","noun","record","star","sun","west","yan"}

adjective = {"able","big","black","blue","busy","certain","cold","common","complete","cool","correct","dark","deep","direct","dry","fast","few","final","fine","free","full","good","great","half","hard","high","hot","large","last","little","live","low","main","many","much","new","next","numeral","old","open","other","own","possible","quick","ready","real","red","round","same","second","several","short","simple","slow","small","south","special","strong","such","sure","top","true","usual","warm","white","whole","young"}

adverb = {"about","above","again","ago","also","always","back","behind","best","better","clear","close","down","early","enough","even","ever","far","first","here","just","kind","late","less","long","more","most","never","now","often","once","only","out","over","perhaps","plain","so","soon","still","then","together","too","up","very","well","yet"}

pronoun = {"a","all","an","any","both","each","every","he","her","him","his","i","it","me","my","nothing","our","she","some","the","their","them","there","these","they","this","those","us","we","what","which","who","you","your"}

determiner = {}

preposition = {"to","after","against","among","as","at","before","between","by","during","for","from","in","near","of","off","on","than","through","toward","under","until","with"}

conjunction = {"and","but","how","if","or","since","that","though","when","where","while","why"}

number = {"five","four","hundred","one","six","ten","thousand","three","two"}

interjection = {"like","no","oh","right","yes"}

question_word = {"how","what","when","where","which","who","why"}
'''

'''
verbs = {"add","answer","appear","ask","began","begin","bring","brought","build","call","came","care","carry","cause","change","check","come","contain","cover","cross","cry","cut","decide","develop","did","differ","do","does","don't","done","draw","drive","eat","face","feel","fill","find","fly","follow","found","gave","get","give","go","got","govern","grow","had","happen","has","have","hear","heard","help","hold","keep","knew","know","laugh","lay","lead","learn","leave","left","let","listen","look","made","make","mean","mind","miss","move","need","note","notice","object","pass","play","pose","produce","pull","put","ran","reach","read","remember","rest","run","said","saw","say","see","seem","serve","set","show","sing","sings","sit","sound","spell","stand","start","stay","step","stood","stop","take","talk","teach","tell","think","thought","told","took","try","turn","wait","walk","want","watch","went","work","write","wrote","yeeling"}

aux_verbs = {"am","are","be","been","can","could","is","may","might","must","should","was","were","will","would"}

nouns = {"act","adult","adults","age","air","animal","area","base","beauty","bed","bird","boat","body","boy","car","children","city","class","color","country","course","day","dog","dogs","door","earth","ease","end","example","eye","fact","fall","family","farm","feet","field","figure","fire","fish","food","foot","force","form","friend","front","game","girl","gold","ground","group","hand","head","heat","home","horse","hour","idea","inch","interest","island","king","land","language","laura","letter","life","light","line","list","lot","love","machine","man","map","measure","men","mile","minute","money","moon","morning","mother","mountain","music","name","night","north","number","order","page","paper","part","pattern","people","person","picture","piece","place","plan","plane","plant","point","port","pound","power","press","problem","product","question","rain","river","road","rock","room","rule","school","science","sea","self","sentence","serena","shape","ship","side","size","sleep","snow","song","state","story","street","study","surface","table","tail","test","thing","time","town","travel","tree","unit","use","voice","vowel","war","water","way","week","weight","wheel","wind","wonder","wood","word","world","year"}

proper_nouns = {"ada","andrew","bobbie","book","box","cason","center","david","dog's","east","farzana","father","frank","green","hannah","house","ida","irene","jim","jose","keith","lucy","mark","meredith","nick","noun","record","star","sun","west","yan"}

adjectives = {"able","big","black","blue","busy","certain","cold","common","complete","cool","correct","dark","deep","direct","dry","fast","few","final","fine","free","full","good","great","half","hard","high","hot","large","last","little","live","low","main","many","much","new","next","numeral","old","open","other","own","possible","quick","ready","real","red","round","same","second","several","short","simple","slow","small","south","special","strong","such","sure","top","true","usual","warm","white","whole","young"}

adverbs = {"about","above","again","ago","also","always","back","behind","best","better","clear","close","down","early","enough","even","ever","far","first","here","just","kind","late","less","long","more","most","never","now","often","once","only","out","over","perhaps","plain","so","soon","still","then","together","too","up","very","well","yet"}

pronouns = {"a","all","an","any","both","each","every","he","her","him","his","i","it","me","my","nothing","our","she","some","the","their","them","there","these","they","this","those","us","we","what","which","who","you","your"}

determiners = {}

prepositions = {"after","against","among","as","at","before","between","by","during","for","from","in","near","of","off","on","than","through","toward","under","until","with","to"}

conjunctions = {"and","but","how","if","or","since","that","though","when","where","while","why"}

numbers = {"five","four","hundred","one","six","ten","thousand","three","two"}

interjections = {"like","no","oh","right","yes"}

question_words = {"how","what","when","where","which","who","why"}
'''