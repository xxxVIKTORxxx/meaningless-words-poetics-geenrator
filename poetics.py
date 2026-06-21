import random
import re
from typing import List, Optional, Dict

# ==========================================
# 1. THE CORE LINGUISTIC MUTATOR
# ==========================================
class PoeticLinguistics:
    """Handles parsing, building base non-existent words, and sound mutations."""
    
    @staticmethod
    def generate_base_word() -> str:
        """Generates a pseudo-word using balanced phonetic weights."""
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'd', 'f', 'g', 'h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v']
        length = max(3, int(random.gauss(5.5, 1.5)))
        word = []
        is_vowel = random.choice([True, False])
        for _ in range(length):
            word.append(random.choice(vowels) if is_vowel else random.choice(consonants))
            is_vowel = not is_vowel
        return "".join(word)

    @staticmethod
    def apply_shift(word: str, shift_type: str) -> str:
        """Applies regular historical sound changes to given words."""
        vowels = "aeiouy"
        # Preserve capitalization style during mutations
        is_caps = word.isupper()
        clean_word = word.lower()
        
        if shift_type == "lenition":
            w_list = list(clean_word)
            shifts = {"p": "b", "t": "d", "k": "g"}
            for i in range(1, len(w_list) - 1):
                if w_list[i-1] in vowels and w_list[i+1] in vowels and w_list[i] in shifts:
                    w_list[i] = shifts[w_list[i]]
            clean_word = "".join(w_list)
            
        elif shift_type == "apocope":
            if len(clean_word) > 2 and clean_word[-1] in vowels:
                clean_word = clean_word[:-1]
                
        elif shift_type == "germanic":
            clean_word = clean_word.replace("t", "s").replace("p", "f")
            
        elif shift_type == "rhotacism":
            w_list = list(clean_word)
            for i in range(1, len(w_list) - 1):
                if w_list[i] == 's' and w_list[i-1] in vowels and w_list[i+1] in vowels:
                    w_list[i] = 'r'
            clean_word = "".join(w_list)
            
        return clean_word.upper() if is_caps else clean_word

# ==========================================
# 2. THE CUSTOMIZABLE POETIC ORCHESTRATOR
# ==========================================
class PoeticEngine:
    def __init__(self):
        self.ling = PoeticLinguistics()
        # Fallback Demonstration Vocabulary if no text/phrases are supplied
        self.fallback_vocabulary = [
            "starlight", "fades", "nebulae", "breathe", "planets", "turn", 
            "galaxies", "dream", "comets", "write", "ancient", "scripts", 
            "silence", "reigns", "echoes", "linger", "moonlight", "dances", 
            "black", "holes", "weep", "solar", "winds", "hum", "dust", "drifts"
        ]

    def _count_syllables(self, phrase: str) -> int:
        """Counts vowel intersections to track metric line constraints."""
        return len(re.findall(r'[aeiouy]+', phrase.lower()))

    def _force_rhyme(self, word: str, target_rhyme_vowel: str) -> str:
        """Mutates the final vocalic target of a word to establish rhyme structures."""
        vowels = "aeiouy"
        w_list = list(word)
        for i in range(len(w_list) - 1, -1, -1):
            if w_list[i].lower() in vowels:
                # Maintain capitalization signature if present
                w_list[i] = target_rhyme_vowel.upper() if w_list[i].isupper() else target_rhyme_vowel
                break
        return "".join(w_list)

    def _parse_input_to_vocabulary(self, raw_input: Optional[str]) -> List[str]:
        """Sanitizes raw text blocks or string fragments into usable tokenized arrays."""
        if not raw_input or not raw_input.strip():
            return self.fallback_vocabulary
        
        # Clean text from punctuation marks to get pure base roots
        words = re.findall(r'\b[a-zA-Z]+\b', raw_input)
        if len(words) < 5:  # Safety fallback check if text input is too short
            return self.fallback_vocabulary + words
        return words

    def generate_poem(
        self, 
        raw_text_input: Optional[str] = None, 
        intensity: str = "medium", 
        words_per_line: int = 6, 
        lines_count: int = 4
    ) -> str:
        """
        Dynamically designs and mutates poetry from raw string feeds.
        
        Parameters:
        - raw_text_input: Pass any raw paragraph/book text here. Left empty, uses default.
        - intensity: 'light', 'medium', or 'heavy' modifications.
        - words_per_line: Dynamic rhythmic meter control (e.g., 4, 6, 8, 12 words per line).
        - lines_count: Total physical row lines to generate.
        """
        vocab_pool = self._parse_input_to_vocabulary(raw_text_input)
        final_poem_lines = []
        
        # Basic alternating AABB/CCDD rhyme matrix setup
        rhyme_vowel_matrix = ["a", "a", "e", "e", "o", "o", "u", "u", "i", "i"]
        
        print(f"--- COMPOSE: {intensity.upper()} MODE | METER: {words_per_line} WORDS/LINE ---")
        
        for line_idx in range(lines_count):
            # Assemble a raw line to the exact user-defined word length configuration
            line_words = [random.choice(vocab_pool) for _ in range(words_per_line)]
            mutated_line_words = []
            
            # Select target vowel code for line-ending rhymes
            target_rhyme_vowel = rhyme_vowel_matrix[line_idx % len(rhyme_vowel_matrix)]
            
            for word_idx, word in enumerate(line_words):
                is_line_end = (word_idx == len(line_words) - 1)
                
                # --- LIGHT MODE ---
                if intensity == "light":
                    if is_line_end:
                        word = self._force_rhyme(word, target_rhyme_vowel)
                    mutated_line_words.append(word)
                
                # --- MEDIUM MODE ---
                elif intensity == "medium":
                    # 15% chance to structurally insert an entirely newly invented root
                    if random.random() < 0.15:
                        word = self.ling.generate_base_word()
                    # Apply classic phonetic rules sequentially
                    word = self.ling.apply_shift(word, random.choice(["lenition", "rhotacism"]))
                    if is_line_end:
                        word = self._force_rhyme(word, target_rhyme_vowel)
                    mutated_line_words.append(word)
                
                # --- HEAVY MODE ---
                elif intensity == "heavy":
                    # Severe compounding mutations
                    word = self.ling.apply_shift(word, "germanic")
                    word = self.ling.apply_shift(word, "apocope")
                    
                    # Intentional word-inversion chaos bug from your heavy_poetry script
                    if len(word) > 3 and random.random() < 0.4:
                        word = word[::-1]
                        
                    if is_line_end:
                        word = self._force_rhyme(word, target_rhyme_vowel)
                    mutated_line_words.append(word.upper())
            
            # Formatting line output string with metrics
            processed_line = " ".join(mutated_line_words)
            syllable_count = self._count_syllables(processed_line)
            final_poem_lines.append(f"{processed_line:<50} (Syllables: {syllable_count})")
            
        return "\n".join(final_poem_lines)

# ==========================================
# 3. VERIFICATION TESTS
# ==========================================
engine = PoeticEngine()

# Test 1: Fallback Default Mode (No input passed, short meter)
print(engine.generate_poem(intensity="light", words_per_line=3, lines_count=4))
print("\n" + "="*60 + "\n")

# Test 2: Custom External Text Input with Extended Meter (Long 8-word line rhythm)
user_custom_text = """
Computational linguistics is an interdisciplinary field concerned with the computational 
modelling of natural language. From historical sound shifts to structural poetry, numbers 
and rules redefine the beauty of mechanical art.
"""

print(engine.generate_poem(
    raw_text_input=user_custom_text, 
    intensity="medium", 
    words_per_line=8, 
    lines_count=4
))
print("\n" + "="*60 + "\n")

# Test 3: Custom Input on Heavy Mutation Mode
print(engine.generate_poem(
    raw_text_input=user_custom_text, 
    intensity="heavy", 
    words_per_line=6, 
    lines_count=4
))
