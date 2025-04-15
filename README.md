# Audio Skip Tool

A simple Python utility that allows you to skip the first N seconds of any audio file.

## Features

- Skip the first N seconds of any audio file
- Supports multiple audio formats (MP3, WAV, M4A, etc.)
- Preserves audio quality
- Simple command-line interface

## Prerequisites

Before using this tool, you need to install the following:

1. Python 3.x
2. pip (Python package installer)
3. ffmpeg (required for audio processing)

### Installation

1. Install Python dependencies:
```bash
pip3 install -r requirements.txt
```

2. Install ffmpeg (on macOS):
```bash
brew install ffmpeg
```

## Usage

Basic usage:
```bash
python3 skip_audio.py input_file output_file [seconds_to_skip]
```

Parameters:
- `input_file`: Path to your input audio file
- `output_file`: Path where you want to save the processed audio
- `seconds_to_skip`: (Optional) Number of seconds to skip from the beginning. Defaults to 10 seconds.

Examples:

1. Skip first 10 seconds (default):
```bash
python3 skip_audio.py input.mp3 output.mp3
```

2. Skip first 15 seconds:
```bash
python3 skip_audio.py input.mp3 output.mp3 15
```

3. Process M4A file:
```bash
python3 skip_audio.py input.m4a output.m4a
```

## Supported Formats

The tool supports various audio formats including:
- MP3
- WAV
- M4A
- OGG
- And other formats supported by ffmpeg

## Error Handling

The script includes error handling for:
- Missing input/output files
- Invalid file formats
- Processing errors

## License

This project is open source and available under the MIT License. 