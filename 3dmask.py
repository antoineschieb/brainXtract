# Obtain a 3D mask by:
# 0. using one U-Net model for each dimension
# 1. performing the intersection of the 3D masks resulting from the predictions of each model
# 2. keeping the largest components of the intersection
# Input: nifti image
# Output: nifti image in wich the 3D mask is saved


from acvl_utils.morphology.morphology_helper import (
    remove_all_but_largest_component,
)
import nibabel as nib
import numpy as np
import torch


nifti_path = ""
xy_model_path = ""
xz_model_path = ""
yz_model_path = ""
output_path = ""


# Slice the nifti 3D data along one axis.
# Returns a list of slices which are 2D arrays.
def slicing(input_vol: nib.nifti1.Nifti1Image, axis_number: int) -> list:
    data = input_vol.get_fdata()
    slice_list = []
    for i in input_vol.shape[axis_number]:
        if axis_number == 0:
            slice = data[i, :, :].astype(np.bool_)
        elif axis_number == 1:
            slice = data[:, i, :].astype(np.bool_)
        else:
            slice = data[:, :, i].astype(np.bool_)
        slice_list.append(slice)
    return slice_list


# Run a U-Net model on a list of 2D arrays which are slices of nifti 3D data.
# The U-Net model is chosen based on the axis the 3D data has been sliced along:
# ij_model U-Net for ij_slices
# Return a list of predicted 2D mask
def unetpredict(slice_list: list, axis_number: int) -> list:
    if axis_number == 0:
        model = yz_model_path
    elif axis_number == 1:
        model = xz_model_path
    else:
        model = xy_model_path
    model = torch.load(model)
    mask2d_list = []
    for slice in slice_list:
        slice_pred = model.predict(slice)
        mask2d_list.append(slice_pred)
    return mask2d_list


# Stack 2D arrays from a list onto one 3D array
# Return a 3D array
def make3d(arrays_list: list, axis_number: int) -> np.ndarray:
    array3d = np.stack(arrays_list, axis_number)
    return array3d


# Intersection of 3d masks from the list of three masks.
def vote(mask3d_list: list) -> np.ndarray:
    best_mask3d = mask3d_list[0] & mask3d_list[1] & mask3d_list[2]
    return best_mask3d


# For each spatial axis:
# 0. The 3D data of the nifti image is sliced along the axis
# 1. A U-Net model is chosen based on the axis, then it predicts 2D masks for each slice of the data
# 2. The 2D masks are stacked to produce one 3D mask
# By repeating this approach for the three axes, three 3D masks are produced.
# The final 3D mask is obtained by performing:
# 0. The intersection of the three 3D masks
# 1. Keeping the largest components of the intersection
def pipeline(input_vol: nib.nifti1.Nifti1Image) -> np.ndarray:
    mask3d_list = []
    for axis_number in range(0, 3):
        slice_list = slicing(input_vol, axis_number)
        mask2d_list = unetpredict(slice_list, axis_number)
        mask3d = make3d(mask2d_list, axis_number)
        mask3d_list.append(mask3d)
    best_mask3d = vote(mask3d_list)
    final_mask3d = remove_all_but_largest_component(best_mask3d)
    return final_mask3d


# Load the nifti image, apply the pipeline processes, then save the 3D mask as a nifti image.
input_vol = nib.load(nifti_path)
final_mask3d = pipeline(input_vol)
nib.save(nib.Nifti1Image(final_mask3d, np.eye(4)), output_path)
