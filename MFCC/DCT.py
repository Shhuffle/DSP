'''
In this code first we will create a 2D mel spectrum vector where logarithmic energy form each triangular filter for each frame 
will me stored. Then DCT will be applied on each frame keeping the first 13 coefficients ignore the 0th coefficient.
Finally we will print the MFCCs for certain frames.

'''
import melFilterBank
import numpy as np
from scipy.fft import dct
import matplotlib.pyplot as plt


#2D array of melspecturm with energy values form each triangular mel filter for each frame 
melspectrum =  np.zeros((melFilterBank.FFT.total_frames,melFilterBank.NumberOfFilter), dtype=float)

for i in range(melFilterBank.FFT.total_frames):
    melspectrum[i,:] = melFilterBank.logmelspec(i)


def performdct(melspec):
    num_frames, num_filters = melspec.shape
    cepstrum = np.zeros((num_frames, num_filters), dtype=float)
    for i in range(num_frames):
        cepstrum[i,:] = dct(melspec[i,:], type=2, norm='ortho')
    return cepstrum[:,1:14]  # keep 2nd to 13th coefficients

if __name__ == "__main__":

    #print MFCCS
    starting_frame = 0
    ending_frame = 41
    MFCCS = performdct(melspectrum[starting_frame:ending_frame,:])
    print(f"The MFCCs value for frame {starting_frame} to {ending_frame} is",MFCCS)
    print(f"Total frames {melFilterBank.FFT.total_frames}")


   #plot heat map to visualize       
    MFCCS = performdct(melspectrum)  # shape: (total_frames × 13)

    time_axis = np.arange(MFCCS.shape[0]) * melFilterBank.FFT.hop_length
    coeff_axis = np.arange(1, MFCCS.shape[1]+1)

    plt.figure(figsize=(12,6))
    plt.pcolormesh(time_axis, coeff_axis, MFCCS.T, shading='auto', cmap='viridis')
    plt.xlabel('Time [s]')
    plt.ylabel('MFCC Coefficient')
    plt.title('MFCC Heatmap')
    plt.colorbar(label='Magnitude')
    plt.show()

    starting_frame = 0
    ending_frame = 5  # choose how many frames you want to plot

    for frame_number in range(starting_frame, ending_frame):
        coeffs = MFCCS[frame_number, :]  # 1D array of MFCCs for this frame
        num_coeffs = coeffs.shape[0]

        plt.figure(figsize=(8,4))
        plt.stem(np.arange(1, num_coeffs+1), coeffs, basefmt=" ")
        plt.xlabel("MFCC Coefficient Index")
        plt.ylabel("Magnitude")
        plt.title(f"MFCC Coefficients for Frame {frame_number}")
        plt.grid(True)
        plt.show()



