import random
import matplotlib.pyplot as plt
import numpy as np

class PatternRecognitionArt:
    """
    A Python-based art regimen designed to help users improve their pattern recognition skills.
    The regimen involves generating, identifying, and replicating complex patterns using Python's visualization libraries.
    """

    def __init__(self, difficulty_level=1):
        self.difficulty_level = difficulty_level

    def generate_pattern(self):
        """Generates a visual pattern based on the current difficulty level."""
        np.random.seed(random.randint(0, 1000))
        pattern_size = self.difficulty_level * 5 + 5  # Increase size with difficulty

        # Create a random pattern grid
        grid = np.random.choice([0, 1], size=(pattern_size, pattern_size), p=[0.5, 0.5])

        # Apply symmetry rules for complexity
        if self.difficulty_level >= 2:
            grid = (grid + np.flip(grid, axis=1)) % 2
        if self.difficulty_level >= 3:
            grid = (grid + np.flip(grid, axis=0)) % 2
        return grid

    def display_pattern(self, grid):
        """Displays the generated pattern."""
        plt.figure(figsize=(5, 5))
        plt.imshow(grid, cmap='binary', interpolation='nearest')
        plt.axis('off')
        plt.show()

    def replicate_pattern(self, original_grid):
        """Provides a blank grid for the user to replicate the pattern."""
        pattern_size = original_grid.shape[0]
        blank_grid = np.zeros_like(original_grid)

        print("Replicate the pattern by filling the grid with 0s and 1s.")
        print("Tip: Think about symmetry and structure as you replicate.")
        
        return blank_grid

    def check_pattern_match(self, user_grid, original_grid):
        """Checks if the user's replicated pattern matches the original."""
        match = np.array_equal(user_grid, original_grid)
        if match:
            print("Great job! Your pattern matches perfectly.")
        else:
            print("Keep practicing! Patterns don't match this time.")
        return match

    def increase_difficulty(self):
        """Increases the difficulty level for more complex patterns."""
        self.difficulty_level += 1
        print(f"Difficulty increased to {self.difficulty_level}.")


# Example usage
if __name__ == "__main__":
    # Initialize the art regimen
    art_regimen = PatternRecognitionArt(difficulty_level=1)

    print("Welcome to the Pattern Recognition Art Regimen!")

    for i in range(3):
        print(f"\nLevel {art_regimen.difficulty_level}: Generate a pattern")
        pattern = art_regimen.generate_pattern()
        art_regimen.display_pattern(pattern)

        user_attempt = art_regimen.replicate_pattern(pattern)
        # For simplicity, here we simulate the user's input as perfect (you can implement input collection)
        user_attempt = pattern.copy()
        
        art_regimen.check_pattern_match(user_attempt, pattern)

        art_regimen.increase_difficulty()

    print("Congratulations! You've completed the regimen.")
