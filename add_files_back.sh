#!/bin/bash

# List of files to add back
files=(
    ".github/workflows/auto-close.yml"
    ".gitignore"
    "DataPreProcess/Libri2Mix/cv/bass.json"
    "DataPreProcess/Libri2Mix/cv/drums.json"
    "DataPreProcess/Libri2Mix/cv/mix_clean.json"
    "DataPreProcess/Libri2Mix/cv/other.json"
    "DataPreProcess/Libri2Mix/cv/vocals.json"
    "DataPreProcess/Libri2Mix/tr/bass.json"
    "DataPreProcess/Libri2Mix/tr/drums.json"
    "DataPreProcess/Libri2Mix/tr/mix.json"
    "DataPreProcess/Libri2Mix/tr/mix_clean.json"
    "DataPreProcess/Libri2Mix/tr/other.json"
    "DataPreProcess/Libri2Mix/tr/vocals.json"
    "DataPreProcess/Libri2Mix/tt/bass.json"
    "DataPreProcess/Libri2Mix/tt/drums.json"
    "DataPreProcess/Libri2Mix/tt/mix.json"
    "DataPreProcess/Libri2Mix/tt/mix_clean.json"
    "DataPreProcess/Libri2Mix/tt/other.json"
    "DataPreProcess/Libri2Mix/tt/vocals.json"
    "DataPreProcess/process_librimix.py"
    "DataPreProcess/process_lrs2.py"
    "DataPreProcess/process_wham.py"
    "LICENSE"
    "README.md"
    "audio_mix.wav"
    "audio_test.py"
    "audio_train.py"
    "configs/tdanet.yml"
    "format_dataset.py"
    "inference.py"
)

# Add each file back to the index
for file in "${files[@]}"; do
    git add "$file"
done

# Commit the changes
git commit -m "Add files back to the repository"

# Push the changes to the remote repository
git push origin your-branch-name
