# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:29:30 2020

@author: jpan2
"""
import numpy as np

def vgp4_downsample(im, factor):
    #fft image
    freq_im = np.fft.fft2(im)
    #?? a+bj --> magnitude
    #mag_freq_im = np.abs(freq_im)
    
    #use fft shift (center on 0)
    shifted_freq_im = np.fft.fftshift(freq_im)
    
    #use fft freq combiniation to do freq in 2D
    FreqCompRows = np.fft.fftfreq(shifted_freq_im.shape[0])
    FreqCompCols = np.fft.fftfreq(shifted_freq_im.shape[1])
    
    #use fft shift again
    shifted_FreqCompRows = np.fft.fftshift(FreqCompRows)
    shifted_FreqCompCols = np.fft.fftshift(FreqCompCols)
    
    #build filter based on factor
    #exclue (multiply by 0) on things at freqs > 2x factor [Nyquist]
    #(same dimensions of filter and FT of im)
    my_filter = np.ones((len(shifted_FreqCompRows),len(shifted_FreqCompCols)))
    #Nested for loop still yield a rectangular filter (box)?
    nyquist = np.absolute(2*factor)
    for i in range(len(shifted_FreqCompRows)):
        if(np.abs(shifted_FreqCompRows[i])>=(1.0/nyquist)):
            my_filter[i,:] = 0
    for j in range(len(shifted_FreqCompCols)):
        if(np.abs(shifted_FreqCompCols[j])>=(1.0/nyquist)):
            my_filter[:,j] = 0
#multiply freq_im and filter (in frequency domain)    
    filtered_im = my_filter*shifted_freq_im
    #filtered_im = shifted_freq_im
    
    
    #SHIFT?! back
    reshifted_downsampled_im = np.fft.ifftshift(filtered_im)
    
    #use ifft to convert from freq domain
    space_downsampled_im=np.fft.ifft2(reshifted_downsampled_im)
    mag_space_downsampled_im=np.abs(space_downsampled_im)
    
    #sample (take ever x factor point)
    downsampled_im = mag_space_downsampled_im[::factor, ::factor]
    
    #return ifft 
    return downsampled_im

#1 fft image
#2 get omega values
#3 design filter based on 2x factor (nyquist freq)
#4 multipy filter
#5 downsample
#6 inverse fft