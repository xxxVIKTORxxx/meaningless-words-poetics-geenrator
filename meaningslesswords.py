import random
import math

# --- STATISTICAL PARAMETERS FOR DIFFERENT LANGUAGES ---
LANG_CONFIGS = {
    "english": {
        "mu": 5.1,
        "sigma": 2.1,
        # Character weights gathered from standard language corpus distributions
        "vowels": {"a": 8.2, "e": 13.0, "i": 7.0, "o": 7.5, "u": 2.8, "y": 2.0},
        "consonants": {
            "b": 1.5, "c": 2.8, "d": 4.3, "f": 2.2, "g": 2.0, "h": 6.1, 
            "j": 0.2, "k": 0.8, "l": 4.0, "m": 2.4, "n": 6.7, "p": 1.9, 
            "q": 0.1, "r": 6.0, "s": 6.3, "t": 9.1, "v": 1.0, "w": 2.4, 
            "x": 0.2, "z": 0.1
        },
        "vowel_prob": 0.40  # Overall text probability of running into a vowel
    },
    "spanish": {
        "mu": 4.7,
        "sigma": 1.9,
        "vowels": {"a": 12.5, "e": 13.7, "i": 6.3, "o": 8.7, "u": 2.9},
        "consonants": {
            "b": 1.4, "c": 4.7, "d": 5.9, "f": 0.7, "g": 1.0, "h": 0.7, 
            "j": 0.4, "k": 0.1, "l": 5.0, "m": 3.1, "n": 6.7, "p": 2.5, 
            "q": 0.9, "r": 6.9, "s": 8.0, "t": 4.6, "v": 1.1, "w": 0.01, 
            "x": 0.2, "y": 0.9, "z": 0.5
        },
        "vowel_prob": 0.45
    }
}

class LinguisticWordGenerator:
    def __init__(self, language_config):
        self.mu = language_config["mu"]
        self.sigma = language_config["sigma"]
        self.vowel_prob = language_config["vowel_prob"]
        
        # Unpack dictionaries into separate lists of characters and weights for random.choices()
        self.vowels = list(language_config["vowels"].keys())
        self.vowel_weights = list(language_config["vowels"].values())
        
        self.consonants = list(language_config["consonants"].keys())
        self.consonant_weights = list(language_config["consonants"].values())

    def _get_random_length(self):
        """Generates length using Gaussian distribution, strictly enforcing a minimum of 1."""
        length = int(random.gauss(self.mu, self.sigma))
        return max(1, length)

    def generate_word(self):
        word_length = self._get_random_length()
        word = []
        
        # Determine initial structural state randomly based on baseline vowel probability
        is_vowel = random.random() < self.vowel_prob
        
        consecutive_count = 0
        
        for _ in range(word_length):
            if is_vowel:
                char = random.choices(self.vowels, weights=self.vowel_weights)[0]
                word.append(char)
                consecutive_count += 1
                # Linguistic Rule: Hard limit phonotactics to prevent unpronounceable strings (e.g., "eee")
                if consecutive_count >= 2 or random.random() > 0.3:
                    is_vowel = False
                    consecutive_count = 0
            else:
                char = random.choices(self.consonants, weights=self.consonant_weights)[0]
                word.append(char)
                consecutive_count += 1
                # Linguistic Rule: Alternate back to vowels after a maximum of 2 consonants
                if consecutive_count >= 2 or random.random() > 0.4:
                    is_vowel = True
                    consecutive_count = 0
                    
        return "".join(word)

# --- EXECUTION ---
# Instantiate the generator using English statistics
generator = LinguisticWordGenerator(LANG_CONFIGS["english"])

print("Generated Meaningless Pseudowords:")
for _ in range(10):
    print(f"- {generator.generate_word()}")
