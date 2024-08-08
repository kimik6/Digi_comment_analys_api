### Sentiment Analysis of Digikala Comments


---

## Table of Contents
1. [Introduction](#introduction)
2. [Part One: Data Scraping](#part-one-data-scraping)
3. [Part Two: Fine Tuning](#part-two-fine-tuning)
4. [Part Three: Final Product](#part-three-final-product)
5. [How to Run](#how-to-run)
6. [Conclusion](#conclusion)

---

## Introduction

This project focuses on sentiment analysis of user comments from Digikala, a popular online marketplace. The goal is to classify comments into three sentiment categories: positive, neutral, and negative.

---

## Part One: Data Scraping

In the first step, we inspect the Digikala website to identify the relevant labels for our task. I decided to use the "recommendation" section because it provides three ready-to-use labels that match our task requirements. Digikala allows users to write custom text in this section, but I chose to discard these data and retain only the three predefined labels: "I recommend," "Not sure," and "I don't recommend." These labels correspond to positive, neutral, and negative sentiments, respectively.

For this part of the project, we used Selenium to scrape data from the Digikala website for the specified product. The process of retrieving and reading comments is as follows:

1. We start by using the `stopScrolling` command, scrolling down the page at a speed appropriate to the internet connection until we reach the comments section.
2. We look for the "More Comments" button and click on it.
3. After that, we access the next page by clicking the "Next" button and continue saving the comments.

By reviewing 100 pages of comments, we created and saved the dataset named `digi_comments_scraped.csv`.

Here’s the breakdown of the sentiment distribution:

- **I recommend**: 1695 comments
- **Not sure**: 109 comments
- **I don’t recommend**: 92 comments

There is a concern about data imbalance among the classes, which will likely affect the model’s performance. This issue should be addressed using appropriate metrics for imbalanced data or data augmentation methods, but this is beyond the scope of this project. To eliminate data inconsistency in terms of sentence length, we removed single-word comments and converted the labels to 0, 1, and 2, making them suitable for the classification task. After preprocessing, we split the data using the `train_test_split` command, preparing the dataset for training and testing.

---

## Part Two: Fine Tuning

For sentiment analysis, we used the pre-trained `ParsBERT` model and its corresponding tokenizer. After defining the required `trainer`, we fine-tuned the model on the defined dataset and uploaded the trained weights to Hugging Face.

Here are the results of the fine-tuning process:

| Epoch | Step | Validation Loss | Accuracy |
|-------|------|-----------------|----------|
| 1.0   | 138  | 0.3028          | 0.8696   |
| 2.0   | 276  | 0.3404          | 0.8732   |
| 3.0   | 414  | 0.4432          | 0.8804   |

As we can see, the accuracy improved slightly after training.

---

## Part Three: Final Product

In this section, after training the model, it's time for testing and deployment. Using Streamlit, we designed a simple interface that allows users to input a new comment and receive sentiment analysis in one of the three predefined labels.

To run this section, execute the following command:

```bash
streamlit run app.py
```

Once executed, the following page will open, functioning as shown in the example:

[Insert example interface image here]

---

## How to Run

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app with the following command:

   ```bash
   streamlit run app.py
   ```

---
![image](https://github.com/user-attachments/assets/10a84e67-ec70-494e-9c07-c640caa47c51)

## Conclusion

It’s important to note that all code was developed within a limited time frame and is subject to improvement. 😊

Thank you for your attention!

---

Feel free to use this code for any other product and share the output 😉

