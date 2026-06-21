import re
import random
from typing import List, Optional
from generator import PoeticLinguistics  # Connecting the generator logic

class PoeticEngine:
    """Manages the alignment of text arrays into balanced structural stanzas."""
    
    def __init__(self, linguistics_module: PoeticLinguistics):
        self.ling = linguistics_module

    def _count_syllables(self, line: str) -> int:
        """Approximates phonetic metrics via local vowel clusters."""
        return len(re.findall(r'[aeiouy]+', line.lower()))

    def _force_rhyme(self, word: str, target_rhyme_vowel: str) -> str:
        """Enforces line-ending rhyme by altering the trailing syllable vowel."""
        vowels = "aeiouy"
        w_list = list(word)
        for i in range(len(w_list) - 1, -1, -1):
            if w_list[i].lower() in vowels:
                w_list[i] = target_rhyme_vowel.upper() if w_list[i].isupper() else target_rhyme_vowel
                break
        return "".join(w_list)

    def prepare_vocabulary_pool(self, raw_input: Optional[str], target_pool_size: int) -> List[str]:
        """Cleans input tokens and automatically pads missing space with generated words."""
        if not raw_input or not raw_input.strip():
            # If input is empty, fill the matrix entirely with unique meaningless words
            return [self.ling.generate_meaningless_word() for _ in range(target_pool_size)]
        
        tokens = re.findall(r'\b[a-zA-Z]+\b', raw_input)
        
        # Padding routine if user wishable words fall short of meter needs
        while len(tokens) < target_pool_size:
            tokens.append(self.ling.generate_meaningless_word())
        return tokens

    def compose_verse(self, words_list: List[str], intensity: str, words_per_line: int, lines_count: int) -> str:
        """Formats text sequences into structured lines using intensity rules."""
        final_poem_lines = []
        rhyme_vowel_matrix = ["a", "a", "e", "e", "o", "o", "u", "u", "i", "i"]
        
        word_index = 0
        for line_idx in range(lines_count):
            line_words = words_list[word_index : word_index + words_per_line]
            word_index += words_per_line
            
            mutated_line_words = []
            target_vowel = rhyme_vowel_matrix[line_idx % len(rhyme_vowel_matrix)]
            
            for w_idx, word in enumerate(line_words):
                is_line_end = (w_idx == len(line_words) - 1)
                
                if intensity == "light":
                    if is_line_end:
                        word = self._force_rhyme(word, target_vowel)
                    mutated_line_words.append(word)
                    
                elif intensity == "medium":
                    if random.random() < 0.15:
                        word = self.ling.generate_meaningless_word()
                    word = self.ling.apply_specific_mutation(word, random.choice(["lenition", "rhotacism"]))
                    if is_line_end:
                        word = self._force_rhyme(word, target_vowel)
                    mutated_line_words.append(word)
                    
                elif intensity == "heavy":
                    word = self.ling.apply_shift=self.ling.apply_specific_mutation(word, "germanic")
                    word = self.ling.apply_specific_mutation(word, "apocope")
                    if random.random() < 0.3:
                        word = self.ling.apply_specific_mutation(word, "reverse")
                    if is_line_end:
                        word = self._force_rhyme(word, target_vowel)
                    mutated_line_words.append(word.upper())
                    
            processed_line = " ".join(mutated_line_words)
            syllables = self._count_syllables(processed_line)
            final_poem_lines.append(f"  {processed_line:<55} (Syllables: {syllables})")
            
        return "\n".join(final_poem_lines)
