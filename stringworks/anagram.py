source_word="heart"

target_word="earth"

count_source_word=len(source_word)

count_target_word=len(target_word)


for ch in source_word:

    if ch in target_word and count_source_word==count_target_word:

        is_anagram=True

    else:

        is_anagram=False

print(is_anagram)


