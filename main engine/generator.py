import random

class PoeticLinguistics:
    """Core linguistic engine for creating pseudowords and historical shifts."""
    
    def __init__(self):
        # Weighted letter distribution for pronounceable, non-existent words
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.v_weights = [12.5, 13.0, 7.0, 8.0, 3.0]
        self.consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w']
        self.c_weights = [1.5, 2.8, 4.3, 2.2, 2.0, 6.1, 4.0, 2.4, 6.7, 1.9, 6.0, 6.3, 9.1, 1.0, 2.4]

    def generate_meaningless_word(self) -> str:
        """Generates a believable pseudoword using Gaussian length tracking."""
        length = max(3, int(random.gauss(5.4, 1.8)))
        word = []
        is_vowel = random.choice([True, False])
        
        for _ in range(length):
            if is_vowel:
                word.append(random.choices(self.vowels, weights=self.v_weights)[0])
            else:
                word.append(random.choices(self.consonants, weights=self.c_weights)[0])
            is_vowel = not is_vowel
        return "".join(word)

    def apply_specific_mutation(self, word: str, shift_type: str) -> str:
        """Applies a distinct linguistic sound mutation rule."""
        vowels = "aeiouy"
        is_caps = word.isupper()
        clean = word.lower()
        
        if shift_type == "lenition":          # p,t,k -> b,d,g between vowels
            w_list = list(clean)
            shifts = {"p": "b", "t": "d", "k": "g"}
            for i in range(1, len(w_list) - 1):
                if w_list[i-1] in vowels and w_list[i+1] in vowels and w_list[i] in shifts:
                    w_list[i] = shifts[w_list[i]]
            clean = "".join(w_list)
            
        elif shift_type == "apocope":         # Drops the final trailing vowel
            if len(clean) > 2 and clean[-1] in vowels:
                clean = clean[:-1]
                
        elif shift_type == "germanic":        # t -> s, p -> f shift
            clean = clean.replace("t", "s").replace("p", "f")
            
        elif shift_type == "rhotacism":       # Intervocalic s -> r
            w_list = list(clean)
            for i in range(1, len(w_list) - 1):
                if w_list[i] == 's' and w_list[i-1] in vowels and w_list[i+1] in vowels:
                    w_list[i] = 'r'
            clean = "".join(w_list)
            
        elif shift_type == "reverse":         # The chaotic structural text bug
            if len(clean) > 3:
                clean = clean[::-1]
                
        return clean.upper() if is_caps else clean

    def apply_random_mutation_mix(self, word: str) -> str:
        """Pipes a single string through a randomized compound chain of 2-3 historical rules."""
        available_shifts = ["lenition", "apocope", "germanic", "rhotacism", "reverse"]
        num_shifts = random.randint(2, 3)
        chosen_shifts = random.sample(available_shifts, num_shifts)
        
        mutated_word = word
        for shift in chosen_shifts:
            mutated_word = self.apply_specific_mutation(mutated_word, shift)
        return mutated_word
