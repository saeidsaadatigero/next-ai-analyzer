#fundamental_analysis.py
import pandas as pd
import random
# Define the weights for each score category
SCORES_WEIGHTS = {
    'Excellent': 4,
    'Decent': 2,
    'Average': 0,
    'Bad': -2,
    'Awful': -4,
    'Yes': 1,
    'No': -1,
    'I am not sure': 0,
}
# Define the categories for which scores will be calculated
CATEGORIES = [
    "Value Position",
    "Team",
    "Developers_Activity",
    "Usecases",
    "Tokenomics",
    "Social & Marketing",
    "Roadmap",
    "Partners & Investors",
    "Competitors",
    "Risks & Weaknesses",
]

# Class to analyze the fundamental aspects of a project based on user responses and predefined prompts
class FundamentalAnalyzer:
    def __init__(self, verbose=False):
        self.df = pd.DataFrame(index=CATEGORIES)
        self.verbose = verbose

# Initialize all scores to 0
        for score_name in SCORES_WEIGHTS:
            self.df[score_name] = 0
        # Reset the index to have 'score_name' as a column
        self.df.reset_index(inplace=True)
        self.df.rename(columns={'index': 'categories'}, inplace=True)

# Add scores to the data frame
    def get_final_score(self):
        self.df['Total'] = self.df.apply(
            lambda row: sum([row[score_name] * SCORES_WEIGHTS[score_name] for score_name in SCORES_WEIGHTS]),
            axis=1
        )

        if self.verbose:
            print(self.df)
# Calculate the final score by summing up the rescaled scores and then rescaling it to 0-100
        final_score = ((self.df['Total'].sum() / len(self.df)) + 1) * 50
        return final_score


# Rescale the scores to 0-100 using the formula: (x - min_val) / (max_val - min_val) * 100
    def rescale_to_0_100(self, scores):
        min_val = min(scores)
        max_val = max(scores)

        if max_val == min_val:
# All scores are the same, return a list of 50s
            return [50] * len(scores)  # return a list of 50s
# Rescale the scores to 0-100 using the formula: (x - min_val) / (max_val - min_val) * 100
        rescaled_numbers = [(x - min_val) / (max_val - min_val) * 75 for x in scores]
        return rescaled_numbers


# Get the final score rescaled to 0-100
    def get_specific_score(self):
        scores = self.df['Total'].tolist()
        rescaled_scores = self.rescale_to_0_100(scores)
        return rescaled_scores


# Add scores to the dataframe
    def get_current_category(self, i):
        if i < 8:
            return CATEGORIES[0]
        elif i < 13:
            return CATEGORIES[1]
        elif i < 18:
            return CATEGORIES[2]
        elif i < 24:
            return CATEGORIES[3]
        elif i < 37:
            return CATEGORIES[4]
        elif i < 44:
            return CATEGORIES[5]
        elif i < 48:
            return CATEGORIES[6]
        elif i < 51:
            return CATEGORIES[7]
        elif i < 54:
            return CATEGORIES[8]
        else:
            return CATEGORIES[9]
