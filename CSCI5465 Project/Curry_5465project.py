# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:28:18 2023

@author: cjinr
"""
###################    PART 1    ####################################
# Import needed modules
from pyopenms import MSExperiment, MzMLFile
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks, savgol_filter
import pandas as pd
# Define path to file
mzml_path = r"C:\Users\cjinr\OneDrive\Documents\Grad School Documents\Xcalibur stuff from Evan\SIL Compound Extract\MS1\13C_MS_1.mzML"

# Create empty MSExperiment object
experiment = MSExperiment()

# Load data from file into experiment object
MzMLFile().load(mzml_path, experiment)

# Visualize and check data
first_spectrum = experiment.getSpectrum(0)
print(f"Number of spectra: {len(experiment.getSpectra())}")
print(f"Number of peaks: {first_spectrum.size()}")
print(f"Retention time: {first_spectrum.getRT()} seconds")


###################    PART 2    ####################################
# Initialize variables
all_intensities = []
all_mz = []

# Loop through spectra in experiment and populate intensity & mz lists
for spectrum in experiment.getSpectra():
    mz, intensity = spectrum.get_peaks()
    all_intensities.extend(intensity)
    all_mz.extend(mz)

# Log transform intensities for plotting
log_intensities = np.log10(all_intensities)

# Plotting Log-transformed Intensity Distribution
plt.figure(figsize=(10, 6))
plt.hist(log_intensities, bins=100, color='green')
plt.title('Log-transformed Intensity Distribution')
plt.xlabel('Log10(Intensity)')
plt.ylabel('Number of Peaks')
plt.show()

# Plotting initial m/z Distribution
plt.figure(figsize=(10, 6))
plt.hist(all_mz, bins=100, color='blue')
plt.title('Aggregated m/z Distribution')
plt.xlabel('m/z')
plt.ylabel('Number of Peaks')
plt.show()


###################    PART 3    ####################################
# Set intensity threshhold to filter out noise
mean_intensity = np.mean(all_intensities)
std_intensity = np.std(all_intensities)
threshold = mean_intensity + std_intensity

# initialize filtered lists
filtered_intensities = []
filtered_mz = []

# loop thru original data, if intensity over threshold append to filtered list
for mz, intensity in zip(all_mz, all_intensities):
    if intensity > threshold:
        filtered_intensities.append(intensity)
        filtered_mz.append(mz)

# plot filtered intensity distribution
plt.figure(figsize=(10, 6))
plt.hist(filtered_intensities, bins=100, color='green')
plt.title('Filtered Intensity Distribution')
plt.xlabel('Intensity')
plt.ylabel('Number of Peaks')
plt.show()

# plot filtered m/z distribution
plt.figure(figsize=(10, 6))
plt.hist(filtered_mz, bins=100, color='blue')
plt.title('Filtered m/z distribution')
plt.xlabel('m/z')
plt.ylabel('Number of Peaks')
plt.show()

# turn filtered lists in to numpy arrays for peak detection
filtered_intensities_np = np.array(filtered_intensities)
filtered_mz_np = np.array(filtered_mz)

# Find peaks
peaks, _ = find_peaks(filtered_intensities_np)


plt.figure(figsize=(10, 6))
plt.plot(filtered_mz_np, filtered_intensities_np)
plt.plot(filtered_mz_np[peaks], filtered_intensities_np[peaks], "x")
plt.title('Detected Peaks in Filtered Data')
plt.xlabel('m/z')
plt.ylabel('Intensity')
plt.show()

# Apply new Savitzky-Golay filter method
smoothed_intensity = savgol_filter(all_intensities, window_length=5, polyorder=3)

# Set new threshold at a high percentile of the intensity values
threshold_value = np.percentile(smoothed_intensity, 95)

# Use tuple-unpacking and find_peaks function to find the peaks
smooth_peaks, _ = find_peaks(smoothed_intensity, height=threshold_value)

# Plotting the savgol filter smoothed intensity distribution
plt.figure(figsize=(10, 6))
plt.plot(all_mz, smoothed_intensity, label='Smoothed Intensity')

# Plot each peak individually
for peak_idx in smooth_peaks:
    plt.plot(all_mz[peak_idx], smoothed_intensity[peak_idx], 'x')
plt.xlabel('m/z ratio')
plt.ylabel('Intensity')
plt.title('Mass Spectrometry Data with Detected Peaks')
plt.legend()
plt.show()


###################    PART 4    ####################################
# List indicating peak info
is_peak = [i in smooth_peaks for i in range(len(smoothed_intensity))]

# Pandas dataframe with m/z, smoothed intensity, and peak information
data = pd.DataFrame({
    'mz': all_mz,
    'smoothed_intensity': smoothed_intensity,
    'is_peak': is_peak
})

# Export to CSV for use with R
csv_file = "C:/Users/cjinr/OneDrive/Documents/Grad School Documents/BICB/CSCI5465/Project/projectoutput.csv"
data.to_csv(csv_file, index=False)
