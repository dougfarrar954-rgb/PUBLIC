# Calculate how many samples we need for a 3-second audio file
sample_rate = 44100    # CD quality
duration = 280       # seconds

total_samples = sample_rate * duration
print(f"We need {total_samples} samples for {duration} seconds of audio")

