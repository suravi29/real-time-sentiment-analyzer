# Real-Time Sentiment Analyzer

A lightweight command-line Python application that performs real-time sentiment analysis on text inputs (such as tweets, posts, or customer feedback) using Natural Language Processing (NLP). Once the user finishes inputting data, the application generates a visual breakdown of the sentiment distribution using Matplotlib.

---

## Features

- **Real-Time Analysis**: Enter text prompts interactively and receive instant sentiment feedback (Positive, Neutral, or Negative).
- **Rule-Based NLP**: Utilizes `TextBlob` to calculate polarity scores.
- **Data Visualization**: Generates a bar chart using `matplotlib` to display the aggregate sentiment breakdown upon exiting.
- **Dynamic Data Handling**: Uses Python's `collections.Counter` to track sentiment frequencies efficiently.

---

## Prerequisites & Installation

### 1. Requirements
Ensure you have Python 3.7+ installed on your machine.

### 2. Dependencies
Install the required libraries using `pip`:

```bash
pip install textblob matplotlib
```

*(Optional)* If this is your first time using TextBlob for specific NLP tasks, you may need to download its corpora resources (though standard polarity analysis works out-of-the-box):

```bash
python -m textblob.download_corpora
```

---

## How to Run

1. Clone or download this repository to your local machine.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the script:

```bash
python sentiment_analyzer.py
```

---

## Usage Example

1. Launch the script in your terminal.
2. Type text entries when prompted:

```text
Real-Time Sentiment Analyzer
Type 'exit' to stop

Enter Tweet/Post: I absolutely love this new feature! It's fantastic.
Sentiment: Positive

Enter Tweet/Post: The service was terrible and slow.
Sentiment: Negative

Enter Tweet/Post: I received the package today.
Sentiment: Neutral

Enter Tweet/Post: exit
```

3. Upon entering `exit`, a window will pop up showing a Matplotlib bar graph representing the count of Positive, Negative, and Neutral entries processed during the session.

---

## Sentiment Logic

The sentiment classification is determined by the **polarity score** calculated by `TextBlob` (ranging from `-1.0` to `1.0`):

| Polarity Score | Sentiment Classification |
| :--- | :--- |
| **Polarity > 0.1** | Positive |
| **-0.1 ≤ Polarity ≤ 0.1** | Neutral |
| **Polarity < -0.1** | Negative |

---

## Project Structure

```text
├── sentiment_analyzer.py   # Main Python script
└── README.md               # Documentation
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
