
# Phantom Developer

Phantom Developer is an AI-powered tool that scans your code, explains it line by line, and reads the explanation aloud with a natural-sounding voice. It's designed to make code explanation and tutorial creation effortless and engaging.

## Inspiration

The project was born out of a need to create code explanation videos without the hassle of self-recording. It's perfect for developers who prefer to let their code speak for itself, quite literally!

## What it does

- Scans your code automatically
- Provides brief, insightful explanations for each line of code
- Reads the explanations aloud with a beautiful, natural-sounding voice

### Use Cases

1. **Explaining Complex Code**: 
   Ideal for breaking down large, complex functions (even those 700-line monsters!) into digestible explanations.

2. **Creating Coding Tutorials**: 
   Record Phantom Developer's explanations to create engaging coding tutorials effortlessly.

## How we built it

- Core AI models deployed on Theta Edge Cloud for code analysis and explanation generation
- Voice synthesis powered by Eleven Labs for natural-sounding speech
- Python for core functionality and integration

## Features

- Screen capture of code snippets
- AI-powered code explanation
- Text-to-speech output of explanations
- Compatible with any IDE

## Prerequisites

- Python 3.7+
- Required Python packages (install using `pip install -r requirements.txt`):
  - dotenv
  - requests
  - openai
  - pyautogui
  - opencv-python
  - numpy
  - pyperclip
  - elevenlabs
  - playsound
  - pyttsx3

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/AaravAtGit/phantom-dev.git
   ```

2. Navigate to the project directory:
   ```
   cd phantom-developer
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following content:
   ```
   theta_endpoint=your_theta_endpoint
   theta_key=your_theta_api_key
   elevenlabs_key=your_elevenlabs_api_key
   ```

## Usage

Run the main script:

```python
python main.py
```

This will:
1. Capture code from your screen
2. Generate an AI explanation of the code
3. Read the explanation aloud

## Challenges we ran into

Initially, we attempted to use open-source text-to-speech models deployed on Theta Edge Cloud. However, these models were either too slow or produced overly robotic voices. We ultimately decided to use Eleven Labs models for their superior voice quality.

## Accomplishments that we're proud of

- Phantom Developer works seamlessly with any IDE
- Smooth, natural-sounding voice output
- Genius-level code explanation abilities

## What we learned

This project provided valuable insights into the capabilities and applications of the Theta chain.

## What's next for Phantom Developer

We're working on expanding Phantom Developer's capabilities to include:
- Automatic code compilation and execution
- Deployment of smart contracts

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/AaravAtGit/phantom-dev/issues) if you want to contribute.


