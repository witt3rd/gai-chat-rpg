# ChatRPG

_Generative Realms: AI-driven Dungeons & Dragons_

<img src="app/static/hero.jpg" width="704" />

## Setup

### Configuration

Create a copy of `.env.template` named `.env` and fill in the required values (e.g., `OPENAI_API_KEY`).

### Dependencies

Create and activate a fresh Python virtual environment, then run:

```bash
pip install -r requirements.txt
```

### Running

Start the [streamlit](https://streamlit.io/) auto-reload server:

```bash
cd app
streamlit run main.py
```

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
