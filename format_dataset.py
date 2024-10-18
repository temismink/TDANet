import os
import argparse
import stempeg
import soundfile as sf

def create_directory_structure(out_dir):
    """Create the required LRS2-like directory structure."""
    for data_type in ["tr", "tt"]:
        for track_type in ["bass", "drums", "vocals", "other", "mix"]:
            path = os.path.join(out_dir, data_type, track_type)
            os.makedirs(path, exist_ok=True)

def extract_stems(song_path):
    """Extract the stems from the mp4 file using stempeg."""
    stems, _ = stempeg.read_stems(song_path)
    return stems

def save_stems(stems, song_name, out_dir, data_type, samplerate=44100):
    """Save the extracted stems (mixture, drums, bass, other, vocals) to the new structure."""
    # Assign the extracted stems to their respective categories
    mixture, drums, bass, other, vocals = stems[0], stems[1], stems[2], stems[3], stems[4]

    # Save each stem to its respective folder using soundfile
    stem_mapping = {
        "mix": mixture,
        "drums": drums,
        "bass": bass,
        "other": other,
        "vocals": vocals
    }

    for track_type, audio in stem_mapping.items():
        out_path = os.path.join(out_dir, data_type, track_type, f"{song_name}_{track_type}.wav")
        # Save the audio file using soundfile (assuming audio is stereo)
        sf.write(out_path, audio, samplerate)

def process_dataset(in_dir, out_dir, data_type):
    """Process all songs in the dataset (train or test)."""
    for song_file in os.listdir(in_dir):
        if song_file.endswith(".mp4"):
            song_path = os.path.join(in_dir, song_file)
            song_name = os.path.splitext(song_file)[0]
            
            # Extract stems
            stems = extract_stems(song_path)
            
            # Save extracted stems to the appropriate directory
            save_stems(stems, song_name, out_dir, data_type)

def reorganize_musdb18(train_dir, test_dir, output_dir):
    """Reorganize the MUSDB18 dataset into the LRS2-like structure."""
    # Create directory structure
    create_directory_structure(output_dir)
    
    # Process train dataset and move to "tr"
    process_dataset(train_dir, output_dir, "tr")
    
    # Process test dataset and move to "tt"
    process_dataset(test_dir, output_dir, "tt")
    
    print("Reorganization complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reorganize MUSDB18 dataset")
    parser.add_argument(
        "--train_dir",
        type=str,
        required=True,
        help="Path to the MUSDB18 training dataset (e.g., '/home/ubuntu/TDANet/musdb18/train').",
    )
    parser.add_argument(
        "--test_dir",
        type=str,
        required=True,
        help="Path to the MUSDB18 testing dataset (e.g., '/home/ubuntu/TDANet/musdb18/test').",
    )
    parser.add_argument(
        "--out_dir",
        type=str,
        required=True,
        help="Path to save the reorganized dataset (e.g., '/home/ubuntu/restructured_musdb18').",
    )
    args = parser.parse_args()

    reorganize_musdb18(args.train_dir, args.test_dir, args.out_dir)
