from typing import Optional
from generator import PoeticLinguistics
from poetics import PoeticEngine

class PoeticApplicationPipeline:
    """Central interface managing pipeline execution across all sub-modules."""
    
    def __init__(self):
        self.ling = PoeticLinguistics()
        self.poetics = PoeticEngine(self.ling)

    def run(
        self,
        user_text: Optional[str] = None,
        words_per_line: int = 6,
        lines_count: int = 4,
        poetic_intensity: str = "medium",
        pre_mutation_strategy: str = "none",
        specific_mutation_rule: Optional[str] = None
    ):
        """Coordinates data flow between modules to create the final poetry block."""
        total_required_words = words_per_line * lines_count
        
        # Step 1: Tokenize and handle vocabulary padding
        working_vocabulary = self.poetics.prepare_vocabulary_pool(user_text, total_required_words)
        
        # Step 2: Apply pre-poetic vocabulary shifts
        mutated_vocabulary = []
        for word in working_vocabulary:
            if pre_mutation_strategy == "random":
                mutated_vocabulary.append(self.ling.apply_random_mutation_mix(word))
            elif pre_mutation_strategy == "specific" and specific_mutation_rule:
                mutated_vocabulary.append(self.ling.apply_specific_mutation(word, specific_mutation_rule))
            else:
                mutated_vocabulary.append(word)

        # Step 3: Structural line composition
        print(f"\n" + "="*70)
        print(f" ENGINE RUN: INTENSITY={poetic_intensity.upper()} | PRE-MUTATE={pre_mutation_strategy.upper()}")
        print(f"="*70)
        
        poem_output = self.poetics.compose_verse(
            words_list=mutated_vocabulary,
            intensity=poetic_intensity,
            words_per_line=words_per_line,
            lines_count=lines_count
        )
        print(poem_output)
        print("="*70 + "\n")

# --- EXECUTION DEMONSTRATIONS ---
if __name__ == "__main__":
    app = PoeticApplicationPipeline()
    
    # DEMO 1: Fully Autonomous Mode (No input, entirely filled by generated words)
    app.run(
        user_text=None, 
        words_per_line=4, 
        lines_count=4, 
        poetic_intensity="medium"
    )

    # DEMO 2: Given "Wishable Words" with Automatic Generator Padding & Specific Pre-Mutation
    # Input has 4 words; requires 24 total. It automatically generates 20 pseudowords to fill lines.
    wishable_words = "Cosmos Supernova Eternity Infinity"
    app.run(
        user_text=wishable_words,
        words_per_line=6,
        lines_count=4,
        poetic_intensity="light",
        pre_mutation_strategy="specific",
        specific_mutation_rule="germanic"
    )

    # DEMO 3: Complete Linguistic Decoupling (Heavy Poetics + Random Sound Mutation Mix)
    app.run(
        user_text="Horizon dreaming nebula starlight twilight cascading genesis quantum physics",
        words_per_line=5,
        lines_count=4,
        poetic_intensity="heavy",
        pre_mutation_strategy="random"
    )
