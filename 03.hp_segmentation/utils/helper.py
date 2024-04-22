# import lib
import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from pathlib import Path
import nrrd
import shutil

#image convert to nifti from nrrd. 
def convert_nrrd_to_nifti(nrrd_file_path, nifti_file_path):
    # Read the NRRD file
    nrrd_data, nrrd_options = nrrd.read(nrrd_file_path)
    
    # Convert NRRD data to NIfTI
    nifti_img = nib.Nifti1Image(nrrd_data.astype(np.float32), affine=np.eye(4))
    
    # Save the NIfTI image
    nib.save(nifti_img, nifti_file_path)

# create directory
def create_folder(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)

# Function to plot all slices of a 3D image
def plot_all_slices(data):
    # Determine the number of slices to display
    slices = data.shape[-1]
    # Calculate the number of subplots needed (square root of number of slices, rounded up)
    subplot_dim = int(np.ceil(np.sqrt(slices)))
    fig, ax = plt.subplots(subplot_dim, subplot_dim, figsize=(15, 15))
    ax = ax.flatten()
    for i in range(slices):
        ax[i].imshow(data[:, :, i], cmap='gray')
        ax[i].axis('off')
    # Hide any unused subplots
    for i in range(slices, len(ax)):
        ax[i].axis('off')
    plt.show()

# Function to plot histogram of voxel intensities
def plot_histogram(data):
    fig, ax = plt.subplots()
    ax.hist(data.ravel(), bins=256, color='c', alpha=0.75)
    ax.set_xlabel('Intensity Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Voxel Intensities')
    plt.show()

# Function to generate a binary image based on a threshold
def generate_binary_image(data, threshold):
    binary_data = np.where(data > threshold, 0, 1)
    return binary_data

# Function to adjust voxel spacing and set the origin to 0
def adjust_affine_for_spacing_and_origin(affine):
    # Create a new affine matrix with 1mm spacing if not already set
    new_affine = affine.copy()
    np.fill_diagonal(new_affine[:3, :3], 1)
    # Set the origin to 0
    new_affine[:3, 3] = 0
    return new_affine

# Function to save binary data as a new NIfTI image with 1mm³ voxel spacing and origin set to 0
def save_binary_image_with_adjusted_origin(binary_data, original_nii, output_filename):
    # Adjust affine for 1mm³ voxel spacing and set the origin to 0
    adjusted_affine = adjust_affine_for_spacing_and_origin(original_nii.affine)
    
    # Ensure the header is copied and modified for the new image dimensions
    new_header = original_nii.header.copy()
    new_header.set_zooms((1, 1, 1))  # Set voxel sizes to 1mm³
    
    # Create a NIfTI image from the binary data with adjusted affine
    binary_img = nib.Nifti1Image(binary_data.astype(np.int16), adjusted_affine, new_header)
    
    # Save the binary image to disk with the specified filename
    nib.save(binary_img, output_filename + '.nii.gz')

def make_if_dont_exist(folder_path,overwrite=False):

    if os.path.exists(folder_path):
        
        if not overwrite:
            print(f'{folder_path} exists.')
        else:
            print(f"{folder_path} overwritten")
            shutil.rmtree(folder_path)
            os.makedirs(folder_path)

    else:
      os.makedirs(folder_path)
      print(f"{folder_path} created!")