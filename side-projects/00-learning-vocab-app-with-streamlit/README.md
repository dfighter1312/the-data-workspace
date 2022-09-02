# Side Project: Week 0 - Building Learning new vocabulary app with Streamlit

## What this repository do?

This is an application built on Python using Streamlit as a library to learn new English vocabulary.

Featuring:
- Watch the entire vocabulary.
- Add new words to the vocabulary.
- Do quiz to get score.
- Get more score and add new words to level up and get higher ranking.
- (and more updated in later weeks)

## How to run this repository?

**Step 1:** Go to the directory
```bash
cd side-projects/00-learning-vocab-app-with-streamlit
```

**Step 2:** Install requirements
```bash
pip install -r requirements.txt
```

**Step 3:** Run the app by the following script
```bash
streamlit run app.py
```

## About Streamlit

Streamlit is an open-source app framework for Machine Learning and Data Science teams.

Pros:
- Fast to build.
- Beginner-friendly.

Cons:
- Slow to run.
- Lots of functionalities relating to app state have not been updated.

## Struggle and Derived Tips during implementation

**1. Creating quiz**

There exists several inconvenience in doing the quiz, such as you have to click on the Start/Next button to be able to click on the Submit button. This is the nearly final solution for me to create the quiz tab in this app using Streamlit, since it rerun the script everytime we click on the button, and the answered choice was not saved.

Look at the `app.py` file to see how I have solved this although I am not happy with this solution/output.