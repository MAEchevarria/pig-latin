def translate(word_or_phrase):
  word_list = word_or_phrase.split()
  pig_latin = []

  for word in word_list:
    for x, letter in enumerate(word):
      if word[0] in "aeiou":
        pig_latin.append(f"{word}ay")
        break
      else:
          if letter in "aeiou":
            if (word[0] == word[0].upper()):
              pig_latin.append(f"{word[x].upper()}{word[x + 1:]}{word[:x].lower()}ay")
              break
            elif (word[0:3] == "squ"):
              pig_latin.append(f"{word[3:]}{word[0:3]}ay")
              break
            elif (word[0:2] == "qu"):
              pig_latin.append(f"{word[2:]}{word[0:2]}ay")
              break
            else:
              pig_latin.append(f"{word[x:]}{word[:x]}ay")
              break
  return " ".join(pig_latin)

print(f"translates a word beginning with a vowel: {translate('apple') == 'appleay'}")
print(f"translates a word beginning with a consonant: {translate('banana') == 'ananabay'}")
print(f"translates a word beginning with two consonants: {translate('cherry') == 'errychay'}")
print(f"translates two word_list: {translate('eat pie') == 'eatay iepay'}")
print(f"translates a word beginning with three consonants: {translate('three') == 'eethray'}")
print(f"counts 'sch' as a single phoneme: {translate('school') == 'oolschay'}")
print(f"counts 'qu' as a single phoneme: {translate('quiet') == 'ietquay'}")
print(f"counts 'qu' as a consonant even when it's preceded by a consonant: {translate('square') == 'aresquay'}")
print(f"translates many word_list: {translate('the quick brown fox') == 'ethay ickquay ownbray oxfay'}")
