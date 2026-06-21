import random

# --- 12 DIVERSE LINGUISTIC RULES ---

def lenition(word: str) -> str:
    """Intervocalic voicing (Romance): p, t, k become b, d, g between vowels."""
    vowels = "aeiouy"
    w_list = list(word)
    shifts = {"p": "b", "t": "d", "k": "g"}
    for i in range(1, len(w_list) - 1):
        if w_list[i-1] in vowels and w_list[i+1] in vowels:
            if w_list[i] in shifts:
                w_list[i] = shifts[w_list[i]]
    return "".join(w_list)

def palatalization(word: str) -> str:
    """Slavic Palatalization: k/g shift to ch/j before i, e."""
    return word.replace("ki", "chi").replace("ke", "che").replace("gi", "ji").replace("ge", "je")

def final_vowel_loss(word: str) -> str:
    """Apocope (Germanic): Dropping the very last vowel of a word."""
    vowels = "aeiouy"
    if len(word) > 2 and word[-1] in vowels:
        return word[:-1]
    return word

def nasal_assimilation(word: str) -> str:
    """Nasal Assimilation: 'n' changes to 'm' before labials 'p' or 'b'."""
    return word.replace("np", "mp").replace("nb", "mb")

def high_german_consonant_shift(word: str) -> str:
    """Grimm's Law: Voiceless stops turn into fricatives (t -> s, p -> f)."""
    return word.replace("t", "s").replace("p", "f")

# --- NEW WEIRD, INTERESTING, AND FUNNY RULES ---

def metathesis(word: str) -> str:
    """Metathesis (Psycholinguistics/Spoonerism): Swaps 'a' and 'e' if they are separated 
    by exactly one consonant (e.g., 'kated' becomes 'ketad')."""
    w_list = list(word)
    for i in range(len(w_list) - 2):
        if w_list[i] == 'a' and w_list[i+2] == 'e':
            w_list[i], w_list[i+2] = 'e', 'a'
        elif w_list[i] == 'e' and w_list[i+2] == 'a':
            w_list[i], w_list[i+2] = 'a', 'e'
    return "".join(w_list)

def hawaiian_reduction(word: str) -> str:
    """Polynesian Minimalization: Hawaiian has no 't', 'b', or 'g'. 
    All 't's become 'k', 'b's become 'p', and 'g's become 'k'."""
    return word.replace("t", "k").replace("b", "p").replace("g", "k")

def dramatic_epenthesis(word: str) -> str:
    """Epenthesis (Exaggerated Phonology): Breaking up heavy consonant clusters 
    by aggressively sticking an 'o' or an 'h' between them so they can be shouted."""
    w_list = list(word)
    vowels = "aeiouy"
    result = []
    for i in range(len(w_list) - 1):
        result.append(w_list[i])
        # If two consonants are touching, separate them dramatically
        if w_list[i] not in vowels and w_list[i+1] not in vowels:
            result.append(random.choice(["o", "ha"]))
    result.append(w_list[-1])
    return "".join(result)

def celtic_initial_mutation(word: str) -> str:
    """Gaelic Initial Mutation: The first letter of the word undergoes a grammatical shift. 
    A starting 'm' or 'b' gets an 'h' stuck to it, turning it into a 'v' sound."""
    if word.startswith(('b', 'm', 'p', 't')):
        return word[0] + "h" + word[1:]
    return word

def total_reduplication(word: str) -> str:
    """Austronesian Reduplication (Plural/Intensifier): If a word is very short (3 letters or less), 
    the language panics and just repeats the whole word twice (e.g., 'kat' -> 'katkat')."""
    if len(word) <= 3:
        return word + word
    return word

def arabic_pharyngealization(word: str) -> str:
    """Semitic Hardening: Replacing standard soft vowels following 'd', 't', or 's' 
    with a harsh, deep 'kh' sound to make it sound incredibly intense."""
    return word.replace("da", "dkha").replace("ta", "tkha").replace("sa", "skha")

def rhotacism(word: str) -> str:
    """Latin Rhotacism: S between vowels turns into a vibrant, rolling 'r'."""
    vowels = "aeiouy"
    w_list = list(word)
    for i in range(1, len(w_list) - 1):
        if w_list[i] == 's' and w_list[i-1] in vowels and w_list[i+1] in vowels:
            w_list[i] = 'r'
    return "".join(w_list)


# --- DICTIONARY MAPPING ALL 12 RULES ---
ALL_RULES = {
    "Intervocalic Lenition (Romance: p,t,k -> b,d,g)": lenition,
    "Palatalization (Slavic: k,g -> ch,j before i,e)": palatalization,
    "Apocope (Germanic: Drop final vowel)": final_vowel_loss,
    "Nasal Assimilation (np/nb -> mp/mb)": nasal_assimilation,
    "High German Consonant Shift (Grimm: t -> s, p -> f)": high_german_consonant_shift,
    "Metathesis (Bizarre: Swap 'a' and 'e' across consonants)": metathesis,
    "Hawaiian Minimalization (No t/g/b -> k/k/p)": hawaiian_reduction,
    "Dramatic Epenthesis (Conlang: Break up clusters with 'o'/'ha')": dramatic_epenthesis,
    "Initial Celtic Mutation (Gaelic: Add 'h' to start letter)": celtic_initial_mutation,
    "Total Reduplication (Austronesian: Repeat tiny words)": total_reduplication,
    "Pharyngealization (Semitic: Toughen syllables into 'kh')": arabic_pharyngealization,
    "Rhotacism (Latin: Intervocalic s -> r)": rhotacism,
}

def transform_word(input_word: str):
    print(f"==================================================")
    print(f"ORIGINAL PROTOLANGUAGE WORD: '{input_word}'")
    print(f"==================================================\n")

    # STEP 1: Isolated rules
    print("--- 1. SINGLE RULE SEPARATION ---")
    for rule_name, rule_func in ALL_RULES.items():
        transformed = rule_func(input_word)
        print(f" Rule: {rule_name:<65} -> '{transformed}'")
    print()

    # STEP 2: Random Mixes
    print("--- 2. RANDOM COMPLEMENTARY MIXES ---")
    for mix_round in range(1, 3):
        num_to_pick = random.randint(3, 4)
        chosen_rules = random.sample(list(ALL_RULES.items()), num_to_pick)
        
        current_word = input_word
        print(f" Round #{mix_round} Pipeline:")
        for rule_name, rule_func in chosen_rules:
            current_word = rule_func(current_word)
            print(f"   -> Applied: {rule_name:<55} -> '{current_word}'")
        print(f" Final Round #{mix_round} Result: '{current_word}'\n")

    # STEP 3: The Ultimate Mega-Pipeline
    print("--- 3. COMPLETE EVOLUTIONARY PIPELINE (ALL 12 RULES) ---")
    all_rules_word = input_word
    for rule_name, rule_func in ALL_RULES.items():
        all_rules_word = rule_func(all_rules_word)
    print(f" Final Catastrophic Combined Result: '{all_rules_word}'\n")


# --- RUNNING THE TEST ---
transform_word("arcanist")
