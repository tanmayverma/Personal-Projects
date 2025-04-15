from pydub import AudioSegment
import sys
import os

def skip_first_seconds(input_file, output_file, seconds_to_skip=10):
    """
    Skip the first N seconds of an audio file and save the result.
    
    Args:
        input_file (str): Path to the input audio file
        output_file (str): Path where the output audio file will be saved
        seconds_to_skip (int): Number of seconds to skip from the beginning (default: 10)
    """
    try:
        # Load the audio file
        audio = AudioSegment.from_file(input_file)
        
        # Convert seconds to milliseconds
        skip_ms = seconds_to_skip * 1000
        
        # Skip the first N seconds
        skipped_audio = audio[skip_ms:]
        
        # Get the file extension
        file_ext = os.path.splitext(output_file)[1][1:].lower()
        
        # Set format-specific parameters
        export_params = {}
        if file_ext == 'm4a':
            export_params = {
                'format': 'ipod',  # Use ipod format for m4a
                'codec': 'aac'     # Use AAC codec
            }
        else:
            export_params = {'format': file_ext}
        
        # Export the result
        skipped_audio.export(output_file, **export_params)
        print(f"Successfully created {output_file} with first {seconds_to_skip} seconds skipped")
        
    except Exception as e:
        print(f"Error processing audio file: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python skip_audio.py input_file output_file [seconds_to_skip]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    seconds_to_skip = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    
    skip_first_seconds(input_file, output_file, seconds_to_skip) 