# Mental health triage LLM agent

A lightweight CLI tool powered by LLMs to analyze user-generated messages for **sentiment**, **response necessity**, and **crisis detection** — with a focus on grief and mental health support.

## What It Does

Given a user message, this tool uses an open source large language model to return a structured JSON analysis of:

- **Sentiment**: Did the user like, dislike, or show no reaction (neutral) to a received message?
- **Response Necessity**: Does the user need a reply?
- **Crisis Detection**: Is the user in immediate distress or crisis?

This is particularly useful for applications involving:

- Mental health chatbots
- Support triage systems
- Social/emotional understanding modules

---

## Usage

### Prerequisites

- Python 3.1+
- GPU minimum requirement: 1 x 24GB GPU (e.g. NVIDIA RTX A6000, 3090, 4090, or better)

### Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/stbedoya/Mental-help-triage-agent/
cd Mental-help-triage-agent
pip install -r requirements.txt
```

### Run from command line
```bash
python -m src.app.app "I can’t stop crying. Everything reminds me of them."
```

### Example output 
```bash
{
  "sentiment": "neutral",
  "response_necessity": "yes",
  "crisis": "yes"
}
```

### License
This project is private and proprietary. All rights reserved.  
Do not copy, modify, or distribute without explicit permission.

