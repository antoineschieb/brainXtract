  
import nibabel as nib
import numpy as np
from skimage import measure
from acvl_utils.acvl_utils.morphology.morphology_helper import remove_all_but_largest_component

# Charger le volume 3D à partir du fichier .gz
nifti_path = 'filtered_brain.nii.gz'
img = nib.load(nifti_path)
volume = img.get_fdata()

test = remove_all_but_largest_component(volume)
    
    
  