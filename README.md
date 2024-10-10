# Next AI Analyzer Project

The **Next AI** project is a fundamental analysis tool for evaluating projects that utilizes machine learning and natural language processing (NLP) to analyze various data and inputs. This tool examines key factors such as the team, tokenomics, developer activity, and other important criteria to determine the success potential and associated risks of projects.

## Table of Contents

1. [Features](#features)
2. [Installation and Setup](#installation-and-setup)
3. [Usage Instructions](#usage-instructions)
4. [Project Components](#project-components)
5. [Caching Mechanism](#caching-mechanism)
6. [Contributing to Development](#contributing-to-development)
7. [License](#license)

---

## Features

- **Fundamental Analysis**: Evaluates various fundamental factors such as team, tokenomics, developer activity, roadmap, etc.
- **API Integration**: Utilizes OpenAI and Tavily APIs for NLP-based analyses.
- **Caching**: An efficient caching system to prevent redundant processing and improve performance speed.
- **Interactive User Interface**: Built on Streamlit for easy interaction with users.
- **Data Visualization**: Uses Plotly to create interactive charts like spider and gauge charts.

## Installation and Setup

1. **Clone the Project Repository**:
   Start by cloning the project repository:
   ```bash
   https://github.com/saeidsaadatigero/next-ai-analyzer.git
   cd next-ai-analyzer
   ```

2. **Install Required Libraries**:
   Use pip to install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   After installing the dependencies, you can run the application using Streamlit:
   ```bash
   streamlit run main.py
   ```

4. **Set API Keys**:
   To use OpenAI and Tavily APIs, replace the default values with your API keys in the `internet_openai_chat.py` file:
   ```python
   self.client = OpenAI(api_key='your-OpenAI-API-key')
   self.tavily_client = TavilyClient(api_key='your-Tavily-API-key')
   ```

## Usage Instructions

1. **Enter Project Name**: Type the name of the desired project in the text box.
2. **Analyze the Project**: Click on the "Analyze Project" button to start the analysis process. If the project has been previously analyzed, results will be loaded from the cache.
3. **View Analysis Results**: The analysis results will include a final success score for the project (on a scale from 0 to 100) and scores related to different categories like team, tokenomics, etc.
4. **Visualize Results**: The analysis results will be displayed as interactive charts such as spider charts and gauge charts.

## Project Components

1. **`main.py`**:
   - This is the main file of the project that runs the Streamlit user interface and processes user inputs. It interacts with the backend components of the project for analysis and caching results.

2. **`internet_openai_chat.py`**:
   - This file manages the connection to the OpenAI and Tavily APIs. These services are utilized for gathering information and analyzing projects.

3. **`fundamental_analysis.py`**:
   - This file contains the logic for conducting fundamental analysis of projects. Categories such as "Team," "Tokenomics," and other factors are defined here, and projects are analyzed based on scores for each category.

4. **`prompts_text.py`**:
   - This file includes default prompts used to extract information related to projects and perform analyses.

5. **`streamviz.py`**:
   - Responsible for visualizing data, it uses the Plotly library to create interactive charts.

## Caching Mechanism

To prevent reprocessing projects that have been previously analyzed, a caching mechanism has been implemented:

1. **Cache Folder**: A folder named `cache` is created to store the analysis results of projects. This data is stored and loaded using `joblib`.
2. **Loading from Cache**: When a project name is entered, the program first checks if the previous analysis result for that project exists in the cache. If cached data is available, previous results are loaded instead of executing a new analysis.
3. **Storing in Cache**: If no cached data exists for a project, the analysis is performed, and the result is stored in the cache.

### Caching Functions:

- `load_cache(project_name)`: Loads cached results for a specific project.
- `save_cache(project_name, data)`: Stores the analysis results of a project in the cache.

## Contributing to Development

If you wish to contribute to the development of this project, you can fork the repository and submit your change requests. Please observe coding style and testing guidelines when submitting requests.

## License

This project is published under the MIT License. For more details, please refer to the [LICENSE](./LICENSE) file.
```
