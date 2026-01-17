# Antigravity Setup Guide - Learn Python with Synthesizers

## Requirements
- Python 3.8+
- Visual Studio Code (recommended)
- Antigravity extension installed

## Quick Start

### Step 1: Clone and Navigate
```bash
git clone https://github.com/AI-Community-Shared/Learn_Synth_Python_Curriculum.git
cd Learn_Synth_Python_Curriculum
```

### Step 2: Run the Session Initializer
The session initializer will automatically:
- Check your environment for required packages
- Offer to install missing dependencies
- Create your student profile
- Generate a "handshake" prompt for the AI tutor

```bash
python start_session.py
```

### Step 3: Initialize the AI Tutor
1. **Copy the "ACTION REQUIRED" block** from the terminal output
2. Open a **new Antigravity chat** (click the + icon in the chat header)
3. **Paste the handshake prompt** into the chat
4. The AI will adopt the **Synth-Tutor** persona and begin guiding you

### Step 4: Start Learning
The AI tutor will:
- Reference your current module and progress
- Use scaffolding (hints, not solutions)
- Guide you through lessons step-by-step
- Update your progress as you complete modules

## How the Handshake Works

The `start_session.py` script generates a personalized prompt that tells the AI:
- Your name
- Your current module
- Where to find your progress file
- Which teaching persona to adopt

This ensures every session starts with full context, even if the AI loses memory between conversations.

## Troubleshooting

### "I don't see the ACTION REQUIRED block"
- Make sure you ran `python start_session.py` in the terminal
- Check that the script completed without errors

### "The AI isn't using scaffolding"
- Verify you pasted the full handshake block (including the line about "no full solutions")
- Start a fresh chat and paste the handshake again

### "My progress isn't being tracked"
- Check that `outputs/[your_name]/progress.json` exists
- Run `start_session.py` again to reinitialize your profile
