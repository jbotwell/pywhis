# PyWhis

This is a CLI application to do TTS conversion using OpenAI's Whisper model,
intended for personal use, with an emphasis on capturing thoughts for
development as written pieces

## TODOS
- [x] Usable script for transcription
- [x] Edit setup so it can be installed
- [ ] Use threading
- [ ] Better validation
- [ ] Idempotency
- [ ] Split logic out of main

## To Run
```bash
source ./venv/bin/activate
export OPENAI_API_KEY=$(pass openai)
pip install dist/pywhis-<...>
```
You'll probably want to convert wav files to mp3. There's a size limit, so that
reduces the chance that you overshoot it
