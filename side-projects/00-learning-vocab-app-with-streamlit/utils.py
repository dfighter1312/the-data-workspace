import os
import random
from select import select
import pandas as pd
import numpy as np

from datetime import datetime

vocab_path = 'vocab_list/vocab.csv'

def read_vocab():
    if os.path.exists(vocab_path):
        return pd.read_csv('vocab_list/vocab.csv')
    else:
        df = pd.DataFrame(
            columns=['word', 'type', 'meaning', 'category', 'last_updated', 'test_passed', 'test_failed', 'score']
        )
        df.to_csv(vocab_path, index=False)
        return df

def add_new_words(**kwargs):
    new_word_object = kwargs
    new_word_object['last_updated'] = datetime.now()
    new_word_df = pd.DataFrame(
        new_word_object,
        columns=['word', 'type', 'meaning', 'category', 'last_updated', 'test_passed', 'test_failed', 'score']
    ).fillna(0)
    new_word_df.to_csv(vocab_path, mode='a', header=False, index=False)

def update_dict(df, ans_obj):
    """
    Example answer obj:
    {
        "word": word_lst['word'].values[0],
        "expected": {
            "type": word_lst['type'].values[0],
            "meaning": word_lst['meaning'].values[0]
        },
        "answered": {
            "type": type,
            "meaning": meaning
        }
    }
    """
    correct = ans_obj["expected"] == ans_obj["answered"]
    idx = df[df['word'] == ans_obj['word']].index
    if correct:
        df.loc[idx, 'test_passed'] += 1
        cummulative_passed =  df.loc[idx, 'test_passed']
        score_obtained = 100 / np.sqrt(cummulative_passed / 2) + (200 - 100 * np.sqrt(2)) / cummulative_passed + (cummulative_passed) / 5 + len(df) / 10
        score_obtained = int(score_obtained)
        df.loc[idx, 'score'] += score_obtained
        df.to_csv(vocab_path, index=False)
        return score_obtained
    else:
        df.loc[idx, 'test_failed'] += 1
        cummulative_passed = df.loc[idx, 'test_passed']
        score_deducted = 5 * (cummulative_passed + 1)
        score_deducted = int(score_deducted)
        df.loc[idx, 'score'] -= score_deducted
        df.to_csv(vocab_path, index=False)
        return score_deducted

def generate_words(df, category):
    if category == "All Topics":
        selected_df = df
    else:
        selected_df = df[df["category"] == category]
    word = selected_df.sample(weights=1 / (selected_df["score"] - selected_df["score"].min() + 1))
    return {
        "word": word['word'].values[0],
        "options": set(list(df.sample(4, replace=True)['meaning']) + [word['meaning'].values[0]]),
        "expected": {
            "type": word['type'].values[0],
            "meaning": word['meaning'].values[0]
        }
    }

def generate_fake_ranking():
    if os.path.exists('vocab_list/ranking.csv'):
        return pd.read_csv('vocab_list/ranking.csv')
    else:
        import names
        lst_users = []
        score = 100
        multiplier = np.random.random(2000)
        print(multiplier)
        for i in range(2000):
            score = int(score * (1 + multiplier[i] / 50))
            user = {
                "Name": names.get_full_name(),
                "Score": score
            }
            print(user)
            lst_users.append(user)
        df_ranking = pd.DataFrame(lst_users)
        df_ranking.to_csv('vocab_list/ranking.csv', index=False)

def find_ranking(score):
    df_ranking = pd.read_csv('vocab_list/ranking.csv')
    df_you = pd.DataFrame({
        "Name": ["You"],
        "Score": [score]
    })
    df_ranking = pd.concat([df_ranking, df_you]).sort_values("Score", ignore_index=True, ascending=False)
    rank = df_ranking[df_ranking["Name"] == "You"].index.values[0]
    return df_ranking[rank-10:rank+10], rank