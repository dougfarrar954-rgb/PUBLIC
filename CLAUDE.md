# CLAUDE.md - AI Assistant Guide for PUBLIC Repository

## Project Overview

This repository is the **AI Community Shared Resources** hub, maintained by Doug Farrar. It serves as a central location for sharing AI knowledge, educational content, and development tools.

**Primary Projects:**
1. **Learn Python with Synthesizers** - Python curriculum teaching programming through audio synthesis
2. **POML-TOON-Starter-Kit** - Toolkit for POML (Prompt Orchestration Markup Language) and Pickaxe AI assistants
3. **Prompts** - Community-contributed prompt collection
4. **Tools** - Workspace automation utilities
5. **AI-Settings** - AI model configuration files

## Repository Structure

```
PUBLIC/
├── Learn_Python_With_Synthesizers/    # Flagship Python curriculum
│   ├── curriculum/                    # Lesson files by module (14 modules)
│   ├── examples/                      # Working Python scripts
│   ├── prompts/                       # AI tutor system prompts
│   ├── tools/                         # Audio helpers and utilities
│   ├── tests/                         # pytest test suite
│   ├── docs/                          # Additional documentation
│   ├── outputs/                       # Student portfolios (gitignored)
│   ├── start_session.py               # Session entry point
│   ├── requirements.txt               # Python dependencies
│   └── GETTING_STARTED.md             # Setup guide
├── POML-TOON-Starter-Kit/             # POML prompt engineering
│   ├── template.poml                  # Production POML template
│   ├── poml_to_toon_converter.py      # Format converter
│   ├── POML-Reference-Guide.md        # Syntax documentation
│   └── Pickaxe-Manual.md              # Platform guide
├── Prompts/                           # Community prompts
├── Tools/                             # Workspace automation
│   └── Launch_My_Workspace.bat        # Windows launcher
├── AI-Settings/                       # AI configuration files
├── README.md                          # Main hub documentation
└── CLAUDE.md                          # This file
```

## Technology Stack

### Languages
- **Python 3.8+** - Primary language for curriculum and utilities
- **Batch/PowerShell** - Windows workspace automation
- **Markdown** - All documentation
- **XML** - POML prompt definitions
- **JSON** - Progress tracking

### Python Dependencies
```
numpy>=1.24.0,<2.0.0      # Array operations for audio
sounddevice>=0.4.6,<1.0.0 # Audio playback
scipy>=1.10.0,<2.0.0      # Signal processing, WAV I/O
matplotlib>=3.7.0,<4.0.0  # Visualization
pytest>=7.4.0,<8.0.0      # Testing framework
pytest-cov>=4.1.0,<5.0.0  # Test coverage
```

### External Tools
- **VS Code** with Antigravity extension - AI tutor integration
- **Pickaxe** - AI assistant platform
- **Google Gemini** - AI tutoring backend

## Development Workflows

### Working with the Python Curriculum

1. **Setup Environment:**
   ```bash
   cd Learn_Python_With_Synthesizers
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. **Validate Environment:**
   ```bash
   python tools/validate_environment.py
   ```

3. **Run Tests:**
   ```bash
   pytest tests/ -v
   ```

4. **Start a Learning Session:**
   ```bash
   python start_session.py
   ```

### Working with POML

1. **Edit POML files** using XML syntax with strict mode enabled
2. **Convert to TOON format:**
   ```bash
   python poml_to_toon_converter.py input.poml output.txt
   ```
3. **Validate** against POML Reference Guide standards

## Code Conventions

### Python Standards
- Follow **PEP 8** style guidelines
- Include **docstrings** for functions and classes
- Python version: **3.8+**
- Use only libraries in `requirements.txt`
- All example scripts should be **self-contained** and runnable

### Documentation Standards
- Use **Markdown** for all documentation
- Update relevant README files when adding features
- Keep lessons in the format: `X_Y_Lesson_Title.md`

### File Naming
- Modules: `MODULE_XX_Name/`
- Lessons: `X_Y_Lesson_Title.md`
- Python examples: `descriptive_name.py` (lowercase, underscores)
- POML files: `*.poml`

### What NOT to Commit
- Audio files (`.wav`, `.mp3`, `.flac`, `.aiff`, `.ogg`)
- Python cache (`__pycache__/`, `*.pyc`)
- Virtual environments (`venv/`, `.venv/`)
- IDE settings (`.vscode/`, `.idea/`)
- Student portfolios (`outputs/student_portfolio/`)
- Antigravity cache (`.gemini/`)

## Key Files Reference

### Learn Python with Synthesizers

| File | Purpose |
|------|---------|
| `start_session.py` | Entry point - environment checks, progress loading, AI context generation |
| `tools/audio_helpers.py` | Core audio functions: `play_audio()`, `save_wav()`, `generate_sine()`, `apply_envelope()`, `normalize()` |
| `tools/validate_environment.py` | Checks Python version, packages, audio output |
| `curriculum/CURRICULUM_MASTER.md` | Complete curriculum outline |
| `curriculum/PROGRESS_TRACKER.json` | Student progress template |
| `prompts/synth_tutor_system.md` | AI tutor persona and teaching methodology |
| `tests/test_examples.py` | Parametrized pytest tests for all examples |

### POML Starter Kit

| File | Purpose |
|------|---------|
| `template.poml` | Production-ready POML template (v3.0) |
| `POML-Reference-Guide.md` | Official POML syntax documentation |
| `poml_to_toon_converter.py` | POML to TOON format converter |
| `Pickaxe-Manual.md` | Pickaxe platform documentation |

## Curriculum Module Structure

The Python curriculum has 14 progressive modules:

| Module | Topic | Focus |
|--------|-------|-------|
| 00 | Python Foundations | Variables, loops, functions, lists |
| 01 | Digital Foundations | NumPy arrays, sampling, bit depth |
| 02 | Waveforms | Sine, square, sawtooth, triangle waves |
| 03+ | Progressive modules | Increasingly complex synthesis concepts |
| 13 | Bridge to General Python | Data science, game dev patterns |

Each module follows the structure:
```
curriculum/MODULE_XX_Name/
├── MODULE_XX_OVERVIEW.md      # Module goals and outcomes
├── X_Y_Lesson_Title.md        # Individual lessons
└── (checkpoint exercises)
```

## Testing

### Running Tests
```bash
cd Learn_Python_With_Synthesizers
pytest tests/ -v              # Verbose output
pytest tests/ --cov=tools     # With coverage
```

### Test Coverage
- All example scripts in `examples/` are tested for execution without errors
- Environment validation is covered
- Tests are parametrized across module examples

### Test Requirements
- Test on Python 3.8, 3.9, 3.10, 3.11
- Verify audio output sounds correct
- All examples must be self-contained

## Git Workflow

### Branch Naming
- Feature branches: `feature/your-feature-name`
- AI assistant branches: `claude/session-id-xxx`

### Commit Messages
- Use prefixes: `Add:`, `Fix:`, `Update:`, `feat:`, `fix:`
- Be descriptive about changes
- Reference modules/lessons affected

### Pull Request Process
1. Fork the repository
2. Create feature branch
3. Make and test changes locally
4. Run `pytest` to ensure all tests pass
5. Commit with clear message
6. Push to fork
7. Open Pull Request

## AI Assistant Guidelines

### When Working with Python Code
- Always validate that code follows PEP 8
- Ensure examples are self-contained and runnable
- Test audio output when modifying synthesis code
- Keep dependencies within `requirements.txt`

### When Working with Curriculum Content
- Maintain the 4-step teaching loop: Briefing, Reading, Comprehension Check, Guided Lab
- Use scaffolding (hints, not answers)
- Connect all concepts to audio outcomes
- Keep explanations technical, not "cute"

### When Working with POML
- Use strict mode (`strict_mode="true"`)
- Include Input Constraints for user selections
- Follow Hybrid Architect reasoning protocol
- Test conversions with the converter script

### Common Tasks

**Add a new lesson:**
1. Create `X_Y_Lesson_Title.md` in appropriate module
2. Add corresponding example to `examples/module_XX/`
3. Update `MODULE_XX_OVERVIEW.md`
4. Add tests for new examples

**Add a new prompt:**
1. Create markdown file in `Prompts/`
2. Follow POML structure if applicable
3. Update `Prompts/README.md`

**Fix a bug in audio code:**
1. Read the affected file in `tools/` or `examples/`
2. Make targeted fix
3. Run `pytest` to verify
4. Test audio output manually

## Important Considerations

- **Audio files are gitignored** - use external links for audio examples
- **Student portfolios are local** - `outputs/` directory is not committed
- **Antigravity integration** requires VS Code extension setup
- **POML syntax** follows Microsoft v0.0.8 specification
- **Progress tracking** uses JSON files per student

## Quick Commands Reference

```bash
# Setup
cd Learn_Python_With_Synthesizers
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Validate
python tools/validate_environment.py

# Test
pytest tests/ -v

# Start session
python start_session.py

# Convert POML
python POML-TOON-Starter-Kit/poml_to_toon_converter.py input.poml output.txt
```
