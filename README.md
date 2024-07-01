# PyWhis

This is a CLI application to do TTS conversion using OpenAI's Whisper model,
intended for personal use, with an emphasis on capturing thoughts for
development as written pieces

If you're not me, you're more than welcome to use it, but I'm sure there are 
more polished projects that do the same thing. If you have nix, you can just

```bash
export OPENAI_API_KEY=$(pass openai)
nix run github:jbotwell/pywhis <source_dir> <destination_dir>
```

You'll probably want to convert wav files to mp3. There's a size limit, so that
reduces the chance that you overshoot it. I use ogg opus, and I've never overshot
it.
