# Student Guide - Learn Python with Synthesizers

Welcome to **Learn Python with Synthesizers**! This guide will help you make the most of your learning experience.

---

## Your Learning Path

This course consists of **14 modules** (Module 00 through Module 13), progressing from Python basics to advanced synthesizer design. Every concept produces sound—turning abstract programming logic into audible results.

### Module Overview
- **Module 00:** Python Foundations (variables, loops, functions, NumPy)
- **Modules 01-12:** Audio synthesis concepts (waveforms, envelopes, filters, effects, MIDI)
- **Module 13:** Bridge to general programming (data science, game dev, finance)

---

## How to Learn with Antigravity

### The 4-Step Teaching Loop

Every lesson follows this pattern:

1. **The Briefing** - The AI explains what you'll learn and why it matters
2. **Required Reading** - You'll be directed to a lesson file in `curriculum/`
3. **Comprehension Check** - The AI asks questions to verify understanding
4. **Guided Lab** - You build projects with scaffolded hints (not solutions)

### Working with Your AI Tutor

The Synth-Tutor agent uses **scaffolding**, meaning it provides:
- ✅ Hints and guiding questions
- ✅ References to lesson materials
- ✅ Similar (but different) code examples
- ❌ **NOT** complete solutions (you learn by doing!)

**Example Interaction:**
```
You: "I'm stuck on generating a sine wave."
AI: "Take another look at Part B of the lesson file. 
     What NumPy function creates an array of evenly-spaced numbers?"
```

---

## Progress Tracking

### Your Student Portfolio
Your work is saved in: `outputs/[your_name]/`

This folder contains:
- `progress.json` - Tracks which modules you've completed
- Your code files organized by module
- Audio outputs from your projects

### Starting Each Session
Always run this at the beginning of a learning session:
```bash
python start_session.py
```

This script:
- Shows your current progress
- Suggests your next lesson
- Generates a handshake prompt for the AI

---

## Tips for Success

### 🎧 Ear Protection
**CRITICAL:** Keep your volume LOW when first running synthesis scripts. Unexpected loud noises can damage hearing or equipment.

### 🧪 Experiment Fearlessly
- Change variables and listen to results immediately
- Breaking code is part of learning—errors are your friends!
- Save working versions before experimenting

### 🤔 Ask Good Questions
**Good:** "Why does doubling the frequency make the pitch go up an octave?"  
**Good:** "My sine wave sounds clicks at the start—what causes that?"  
**Less helpful:** "It doesn't work. What's wrong?"

### 📝 Document Your Learning
Add notes to your `progress.json`:
```json
"notes": "Learned that exponential decay creates a 'pluck' sound"
```

---

## Common Issues & Solutions

### "I hear clicking/popping in my audio"
- Likely a clipping issue (amplitude > 1.0)
- Check your lesson file for the "amplitude" concept
- Ensure all values stay between -1.0 and +1.0

### "ImportError: No module named 'sounddevice'"
- Run `python start_session.py` to auto-install dependencies
- Or manually: `pip install -r requirements.txt`

### "The AI gave me the full answer instead of a hint"
- This shouldn't happen! Start a fresh chat and paste the handshake again
- Report this in GitHub Issues

### "I completed a lesson but my progress didn't update"
- Edit `outputs/[your_name]/progress.json` manually
- Or tell the AI: "Mark Module 01 as complete"

---

## Getting Help

- **GitHub Issues:** Report bugs or ask technical questions
- **Discussions:** Share projects and connect with other learners
- **AI Tutor:** Ask for clarification on ANY concept

---

## Next Steps

1. Run `python start_session.py`
2. Copy the handshake block into Antigravity chat
3. Start with Module 00 if you're new to Python
4. Start with Module 01 if you know Python basics

**Happy learning!** 🎹🐍
