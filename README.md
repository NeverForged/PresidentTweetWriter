# PresidentTweetWriter
As a simple NLP experiment, I decided to cook up a Jupyter Notebook tweet writer, based on a recent episode of the Daily Show.

## Concept & Explanation
* First, we all know which President I am referring to, but I refuse to use his name since he lives on that.
* A recent episode of the *Daily Show* showed what happens when they compared one of the President's Tweets to allowing the iPhone to auto-select the next words used.  It made about as much sense as his own tweets.

So, my idea is simple: using n-grams and cosine similarity, I will cook up a tweet generator that will make tweets that make as much (or possible more) sense as the 45th President's.

## Challenges
* **Character Limits** - I plan to set this to allow 140 or 280 character limit tweets (likely having a hard stop after the character total hits 135 or 275... he tends to use small words, so).
* **Keeping on Topic** - This is where cosine similarity comes in.  It may do a better job than he does.
* **Time** - It's 11 AM PST on November 17th, 2017 at the time of this inital readme write up.  I plan on finishing quickly.
* **Evaluation** - How does one measure success at something like this?

## Data
I used the [**Kaggle** Tweets](https://www.kaggle.com/austinvernsonger/donaldtrumptweets) data.
* Converted to a txt file with line separations between tweets.

## Finished?
After 1hr, 45mins, I do have a randomized tweet maker.  It makes very little sense, but then again, neither does the source material.  The Kaggle tweets (and other, larger sets) are very election-focused... which is only mildly outdated.
