import sys
import os
from openai import OpenAI
from typing import Callable, BinaryIO


def main():
    validate_arguments()
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    do_to_files_in_dir(source_dir, lambda file: transcribe_audio(file, destination_dir))


def validate_arguments():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <source_dir> <destination_dir>")
        sys.exit(1)


def do_to_files_in_dir(directory: str, f: Callable[[BinaryIO], None]):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            with open(os.path.join(directory, filename), "rb") as file:
                f(file)


def transcribe_audio(audio_file, destination_dir):
    file_name = os.path.basename(audio_file.name)
    client = OpenAI()
    transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

    with open(os.path.join(destination_dir, file_name + ".md"), "w") as text_file:
        text_file.write(transcript.text)


if __name__ == "__main__":
    """This runs when you execute '$ python3 mypackage/mymodule.py'"""
    main()
