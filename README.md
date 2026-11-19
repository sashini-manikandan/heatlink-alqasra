# HEATLINK — Streamlit deployment

## Files
- `app.py` — Streamlit wrapper that displays the existing HEATLINK HTML prototype.
- `heatlink_al_qasra.html` — the original self-contained website.
- `requirements.txt` — Python dependency for Streamlit.

## Deploy
1. Create a GitHub repository, for example `heatlink-al-qasra`.
2. Upload all three files to the repository's root.
3. Open https://share.streamlit.io/ and sign in with GitHub.
4. Choose **Create app** / **Deploy an app**.
5. Select the repository, branch (usually `main`), and main file path `app.py`.
6. Click **Deploy**. Streamlit will build the app and provide a public `*.streamlit.app` URL.

## Important prototype limitations
This deployment only hosts the existing front end. The forms generate demonstration reference IDs in the browser; they do not send requests to emergency services or real response teams. Directory entries are placeholders that must be verified. There is no database or secure case-management backend.
