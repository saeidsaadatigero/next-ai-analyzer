#streamlit run main.py # To run the Main.py
import streamlit as st
from stqdm import stqdm
import streamviz
from prompts_text import prompts, initial_prompt, intro_prompt
import plotly.graph_objects as go
import pandas as pd
from internet_openai_chat import Chatbot
from fundamental_analysis import FundamentalAnalyzer
import re
import ast
import joblib
import os

# Cache directory setup
CACHE_DIR = 'cache'
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def get_cache_path(project_name):
    return os.path.join(CACHE_DIR, f'{project_name}.joblib')

def load_cache(project_name):
    cache_path = get_cache_path(project_name)
    if os.path.exists(cache_path):
        return joblib.load(cache_path)
    else:
        return None

def save_cache(project_name, data):
    cache_path = get_cache_path(project_name)
    joblib.dump(data, cache_path)

verbose = False

# Initialize Chatbot and FundamentalAnalyzer
chatbot = Chatbot()
analyzer = FundamentalAnalyzer(verbose=verbose)

# Load streamlit-viz components
st.set_page_config(
    page_title="Next AI",
    page_icon="🤖",
)
st.title('Next AI')
project_name = st.text_input('Project Name', '', placeholder='Enter the project name')

intro_thread = chatbot.create_thread()
questions_thread = chatbot.create_thread()

if st.button('Analyze Project'):
    if not project_name:
        st.error('Project name is required.')
    else:
        cache = load_cache(project_name)
        if cache is not None:
            response, category_scores, predicted_success = cache
        else:
            response = chatbot.chat(intro_prompt.format(project_name), intro_thread)
            st.write("## Project Description:")
            st.write(response)

            response = chatbot.chat(initial_prompt.format(project_name), questions_thread)

            for i in stqdm(range(0, len(prompts), 5), desc='Analyzing project'):
                prompt = ' '.join(prompts[i:i + 5])
                response = chatbot.chat(prompt, questions_thread)

                if verbose:
                    st.write(f"#### responses for question set {i // 5 + 1}:")
                    st.write(response)

                try:
                    response = eval(response.strip())
                except:
                    try:
                        pattern = r"\[.*\]"
                        match = re.search(pattern, response)
                        if match:
                            list_string = match.group(0)
                            response = ast.literal_eval(list_string)
                        if type(response) != list:
                            response = ["I am not sure"] * 5
                    except:
                        if verbose:
                            print(f"Error in response set {i // 5 + 1}")
                            print(response)
                        response = ["I am not sure"] * 5

                for j, r in enumerate(response):
                    current_cat = analyzer.get_current_category(i + j + 1)
                    analyzer.df.loc[analyzer.df['categories'] == current_cat, r] += 1

            predicted_success = analyzer.get_final_score()

            if predicted_success > 100:
                predicted_success = 100 * (predicted_success % 162)

            category_scores = analyzer.get_specific_score()

            save_cache(project_name, (response, category_scores, predicted_success))

        st.write("## Analysis Result:")
        st.write(f"####")
        streamviz.gauge(predicted_success, 'Investment Safety',
                        gSize="MED", arTop=100, grLow=39, grMid=59)

        df = pd.DataFrame({
            "Skill": ["Value Position", "Team", "Developers Activity", "Usecases", "Tokenomics", "Social & Marketing",
                      "Roadmap", "Partners & Investors", "Competitors"],
            "Proficiency": category_scores[:-1],
        })

        labels = list(df[df.columns[0]])
        values = list(df[df.columns[1]])
        labels = (labels + [labels[0]])[::-1]
        values = (values + [values[0]])[::-1]

        data = go.Scatterpolar(
            r=values,
            theta=labels,
            mode="lines+markers",
            opacity=0.9,
            hovertemplate="%{theta}: %{r}<extra></extra>",
            marker_color="#636EFA",
            marker_opacity=1.0,
            marker_size=7,
            marker_symbol="circle",
            line_color="#636EFA",
            line_dash="solid",
            line_shape="linear",
            line_width=2,
            fill="toself",
            fillcolor="RGBA(99, 110,  250, 0.5)",
        )

        layout = go.Layout(
            title=dict(
                text="",
                x=0.5,
                xanchor="center",
            ),
            paper_bgcolor="rgba(100,100,100,0)",
            plot_bgcolor="rgba(100,100,100,0)",
        )

        fig = go.Figure(data=data, layout=layout)
        st.plotly_chart(fig)

        st.write("The data used for the spider chart is randomly generated and does"
                 "not reflect the actual project analysis. The data is only for demonstration purposes.")

