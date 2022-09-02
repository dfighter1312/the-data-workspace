from copy import deepcopy
from re import M
import streamlit as st

from streamlit_option_menu import option_menu

from utils import *

# Configurations
st.set_page_config(
    page_title="Learning New Words",
    layout="wide"
)
st.markdown(
    """
<style>
.streamlit-expanderHeader {
    font-size: x-large;
}
</style>
""",
    unsafe_allow_html=True,
)
reduce_header_height_style = """
    <style>
        div.block-container {padding-top:1rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title='Learning New Words',
        options=["Quick Review", "Check Vocab", "Add More Words", "Your Stats"],
        default_index=0,
    )

# Read vocab
df = read_vocab()
generate_fake_ranking()

if selected == "Quick Review":
    st.title('List of all words')
    st.table(df[['word', 'type', 'meaning', 'category']])

elif selected == "Check Vocab":
    st.title("Checking your vocabulary")
    category = st.selectbox(label="Select category", options=["All Topics"] + df["category"].unique().tolist())
    
    if 'word' not in st.session_state:
        st.session_state['word'] = generate_words(df, category)
    word = st.session_state['word']
    # with st.form(f"Question"):
    st.markdown(f"### Define: {word['word']}")
    type = st.radio(
        "Word type",
        ["noun", "verb", "adjective", "adverb", "other"],
        horizontal=True,
        key=f"type:ans"
    )

    meaning = st.radio(
        "Meaning",
        word['options'],
        key=f"check:ans"
    )
    cols = st.columns([1, 10])
    next = cols[0].button("Start/Next", help="Click to enable the Submit button")
    submitted = cols[1].button("Submit", disabled=not next)
    if submitted:
        if 'answered' in st.session_state['word']:
            st.write("You have answered this question, please click next")
        else:
            st.session_state['word']['answered'] = {
                'type': type,
                'meaning': meaning
            }
            ans_obj = st.session_state['word']
            correct = ans_obj["expected"] == ans_obj["answered"]
            score = update_dict(df, ans_obj)
            if correct:
                st.success(f"Correct answer, you obtained {score} points.")
            else:
                st.warning(f"Incorrect answer, you lost {score} points.")
            
            st.write(st.session_state['word'])
            st.session_state['word'] = generate_words(df)


elif selected == "Add More Words":
    st.title("Add More Words To Your Vocabulary")
    with st.form("insert", clear_on_submit=True):
        word = st.text_input("Word")
        type = st.multiselect(
            label="type",
            options=["noun", "verb", "adjective", "adverb", "other"],
            default=st.session_state.get("type_set", "noun")
        )
        meaning = st.text_input("Meaning")
        st.write("You can pick the category on the multi-selection or by text input")
        category = st.text_input("Category")
        category_alt = st.selectbox(
            label="",
            options=df["category"].unique()
        )
        submitted = st.form_submit_button("Submit")
        if submitted:
            add_new_words(
                word=word,
                type=type,
                meaning=meaning,
                category=category if len(category) > 0 else category_alt
            )
            st.session_state["type_set"] = type
            st.success("Add word successfully")

elif selected == "Your Stats":
    
    st.header("Your stats:")
    st.write(f"Cummulative score: {df['score'].sum()}")
    st.write(f"Correct rate: {(df['test_passed'].sum() + 1) / (df[['test_passed', 'test_failed']].values.sum() + 1) * 100}%")
    tabs = st.tabs(["Level", "Ranking"])

    rank_table, rank = find_ranking(df['score'].sum())
    tabs[1].markdown(f"Current ranking is **{rank}**/2001")
    tabs[1].table(rank_table)

    level_description = pd.DataFrame(
            {
                "Level": np.arange(1, 100),
                "Score": 50 * np.arange(1, 100) ^ 2,
                "Minimum words": 5 * np.arange(1, 100)
            }
        )
    score_level = np.floor(np.sqrt(df['score'].sum() / 50))
    vocab_level = np.floor(len(df) / 5)
    tabs[0].markdown(f"Current level is **{int(min(score_level, vocab_level))}**")
    tabs[0].table(level_description)


# elif selected == "Combat":
#     pass

# Remove footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# df = pd.read_csv('elect_dịch pha.csv', index_col='time')
# st.line_chart(df)