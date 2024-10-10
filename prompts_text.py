#prompts_text.py
# This file contains prompts for generating a paragraph describing a cryptocurrency project.
intro_prompt = """
Please provide a paragraph that describes the following cryptocurrency project. The paragraph should be concise and informative, providing a brief overview of the project's purpose, goals, and key features. Avoid using technical jargon and focus on explaining the project in simple terms that can be easily understood by a general audience.
Do not include any source links or references and write it like a human.
The project you will be describing is the {} project.
"""

initial_prompt = """
I would like you to evaluate the following cryptocurrency project based on a set of specific questions that I will give after this prompt. The questions are divided into two categories: Yes/No questions and rating questions. I am going to ask questions about the {} project.

For each given batch of questions, you must just write the answers in a python list format. For example, if I ask 5 questions, you should write the answers in the following format:
['Yes', 'No', 'I am not sure', 'Excellent', 'Decent']
Do not include any additional information or explanations in the response. Just provide the answers in the correct order.

For Yes/No Questions:
Please provide an answer of "Yes" or "No."
If you do not have the necessary data to answer a question, explicitly state "I am not sure."
Ensure that your responses are specific to the named project and avoid giving general explanations and trends.

For Rating Questions:
Please provide an answer in one of the following modes: Excellent, Decent, Average, Bad, Awful.
If specific data is not available to categorize the answer, please respond with "I am not sure."

Field of Activity Categories:
Layer 1 Blockchains, Layer 2 Solutions, DeFi Platforms, NFT and Gaming, Oracles, Privacy Coins, Etc.

Important: Your reviews should be specific to the named project and compare it within its field of activity. Avoid giving general explanations and trends; focus on the data and details specific to the project being evaluated. Just write a python list of answers as the output.
"""

prompts = [
    # Add your prompts here...
]
