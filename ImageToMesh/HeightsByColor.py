# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:24:16 2020
Matrix of Image
Creates a matrix with the color info of each pixel of a picture
@author: Juan G. Diosa
Improved with chatGPT on Sat Mar 18 2023
"""

def HeightsByColor(height, columns, rows, Image):
    """
    
    
    Input:
    
    height: a float representing the maximum height value of the terrain
    columns: an integer representing the number of columns in the image
    rows: an integer representing the number of rows in the image
    Image: a 3D numpy array representing the color image
    Output:
    
    height_array: a 2D numpy array representing the height values for each color in 
    the input image, where the dimensions of the array are (rows, columns)

    """
    import numpy as np
      # Reshape the 3D image array into a 2D array with 3 columns
    Image_2d = Image.reshape(columns * rows, 3)

    # Find the unique colors in the image and assign them a height value
    unique_colors, color_indices = np.unique(Image_2d, axis=0, return_inverse=True)
    height_values = np.linspace(0, height, num=len(unique_colors), endpoint=True)
    height_array = height_values[color_indices].reshape(rows, columns)
    
    return height_array

# Let's go through what each line does:

# Import the numpy module.
# Define the HeightsByColor function
# Reshape the Image array into a 2D array with 3 columns, using the reshape method.
# Find the unique colors in the image and assign them a height value. The np.unique function returns a tuple containing the unique colors and their indices in the original array. We pass the axis=0 parameter to only consider the colors in each pixel (i.e. not the individual RGB values). We also pass the return_inverse=True parameter to get an array of indices that can be used to map the colors to their height values. We then use the linspace function to create an array of height_values that spans from 0 to height, with one value for each unique color in the image. Finally, we use NumPy's advanced indexing to map the color indices to their corresponding height values, and reshape the resulting array back into a 2D array with rows rows and columns columns.
# Return the height_array.
# I hope this helps! Let me know if you have any questions.