![Penguin Logo](./pictures/logo-no-background.png)

# 🐧 PENGUIN

## 📄 Description

**Penguin** is an AI-powered app created on **29/08/2024** by **Nouh** and **Souad**. It allows users to chat with an engaging AI character named Penguin. The app can be used for casual conversations or as therapy, enabling users to express their thoughts and emotions. Whether for fun or emotional support, **Penguin** is here to chat and connect.

---

## 🛠️ To-Do List

- [~] **Voice-to-text transcription**
- [ ] **Create user interface**
- [ ] **Enhance AI communication abilities** (improve conversational depth)
- [ ] **Integrate mood tracking**
- [ ] **Add reflection prompts**
- [ ] **Implement search bar**
- [ ] **Add audio playback functionality**
- [ ] **Integrate multimedia support** (e.g., images, videos)
- [ ] **Implement in-app purchases**
- [ ] **Choose a logo for the app**
- [ ] **Create `requirements.txt`**

---

## ✅ Done List

- [x] **Set up project structure**
- [x] **Set up version control with Git**
- [x] **Implement continuous integration** with GitHub Actions
- [x] **Basic documentation and README**
- [x] **Model implementation**
- [x] **Successful communication with the AI**

---

## 🚀 Installation Guide

Follow these steps to set up Penguin on your local machine:

### 1. Clone the Repository:

```bash
git clone https://github.com/PENGUIN.git
cd PENGUIN

```bash
# Install Transformers
pip install transformers

# Clone and install ParlAI for BlenderBot
git clone https://github.com/facebookresearch/ParlAI.git
cd ParlAI
python setup.py install
cd ..

#Python verification
sudo apt update
sudo apt install python3.8 python3.8-venv python3.8-dev



💬 Interacting with BlenderBot

You can run BlenderBot using the following command:

```bash
parlai interactive --model-file zoo:blenderbot_400Mdistill/model


Fine-tuning: You can fine-tune the model on dialogue datasets related 
to therapy and mental health.
 Adding Emotional Understanding: Integrate emotion detection tools,
or re-train on emotion-specific datasets to make the responses more empathetic.


 



