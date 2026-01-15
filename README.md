# FSPSlideDecks - Automated Slide Deck Engineering Platform

## 🎯 Global Vision
FSPSlideDecks ([github.com/FatStinkyPanda/FSPSlideDecks](https://github.com/FatStinkyPanda/FSPSlideDecks)) is a powerful Python-based backend designed for the automated, intelligent creation of professional slide decks of **any size or complexity**. It provides AI agents with a robust suite of tools for generating, validating, and ensuring the quality of presentations across diverse domains.

## 🛠 Project Lifecycle Requirements
This project enforces strict development standards to ensure stability and compatibility.

### 🐍 Python Environment
- **Mandatory Version:** Python 3.11.x
- **Environment:** A dedicated Virtual Environment (`.venv`) MUST be automatically activated and used for the project's **entire lifecycle**, from development to production.
- **Strict Rule:** Direct use of system Python or bypassing the virtual environment is strictly prohibited.

### 🛡 MCP-Global Integration
- This project fully utilizes the **mcp-global** system included in the project root.
- **Enforcement:** MCP-global hooks are strictly enforced and **must never be bypassed**. All development must adhere to the MCP-enforced workflows.
- **Key Commands:**
  - `python mcp.py autocontext` (Run before starting any task)
  - `python mcp.py review <path>` (Run for continuous quality checks)
  - `python mcp.py security <path>` (Run for security audits)

## 🏗 Backend Architecture

### Modular Toolset
The backend is built on a modular "Tool & Function" architecture, enabling AI agents to:
- **Initialization:** Create isolated project folders for each unique slide deck.
- **Generation:** Construct slides using advanced templates with `python-pptx` (and other future libraries).
- **Validation:** Execute automated tools for quality checks (formatting, spelling, structural integrity).
- **Quality Assurance:** Intelligent validation to ensure professional standards for decks of any complexity.

### Slide Deck Management
**Requirement:** Each slide deck project MUST exist in its own dedicated workspace within the `decks/` directory. This ensures complete isolation of content, assets, and specific configurations for every project.

## 🚀 Getting Started

1. **Activate Environment:**
   ```powershell
   # Activation (Windows)
   . .venv/Scripts/Activate.ps1
   ```

2. **Full Installation:**
   ```bash
   # Initialize and install the mcp-global system fully
   python mcp.py setup --all
   ```

3. **Development Cycle:**
   Always follow the MCP-enforced workflow:
   1. `python mcp.py autocontext`
   2. Implement changes
   3. `python mcp.py review <path>`
   4. `python mcp.py security <path>`
   5. Commit progress

## 📈 Roadmap

### Phase 1: Foundation (Completed)
- [x] Modular Backend Core and architecture design.
- [x] Per-project slide deck isolation logic.
- [x] Python 3.11.x lifecycle and venv enforcement.
- [x] `mcp-global` root integration and proxy setup.

### Phase 2: Tooling & Functions (Next)
- [ ] AI Agent MCP Tool integration for automated creation.
- [ ] Support for complex layouts and data-driven slides.
- [ ] Integration of additional asset management tools.

### Phase 3: Validation & QA
- [ ] Structural validation engine for complex decks.
- [ ] Visual consistency QA automation.
- [ ] Export and secure distribution pipelines.
