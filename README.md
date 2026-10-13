# Image Filtering App

A small Python desktop app for applying convolution-based image filters.

## Overview

This project lets you upload an image, choose a filter, preview the result, and save the filtered output. The filtering logic is implemented using NumPy and Pillow, with an optional optimized convolution path.

## Included filters

- Averaging
- Sharpening
- Gaussian
- Laplacian

## Features

- Upload an image from disk
- Preview original and filtered versions side by side
- Adjust filter parameters such as sigma for Gaussian, strength for sharpening and kernel size for Averaging and Gaussian
- Toggle between optimized and basic convolution implementations
- Save the filtered image as PNG or JPEG

## Project structure

- `gui.py` — Tkinter interface and user controls
- `convolution.py` — convolution logic and filter application
- `filters_config.py` — filter kernel definitions

## Requirements

Install the following dependencies before running the app:

```bash
pip install pillow numpy
```

## Run the app

From the project root:

```bash
python gui.py
```

## Notes

- GenAI tools used - Gemini for:
    - User Interface implementation (desktop window, user controls etc.),
    - helping with the development of the optimized convolution (vectorization for faster image processing),
    - handling image edges,
    - usual debugging.

- Observations after testing with different parameters values:
    - Averaging and Gaussian as smoothing (blurring) filters produce more blur with larger kernel and/or larger sigma values, which means less details and softer edges.
    <img width="895" height="629" alt="averaging example 1" src="https://github.com/user-attachments/assets/38e0f3d0-39ca-4009-9a29-489508b96aa9" />
    <img width="896" height="629" alt="averaging example 2" src="https://github.com/user-attachments/assets/e2ceb62e-02bc-4af2-885b-621e77fd17b0" />

    <img width="893" height="629" alt="gaussian example 1" src="https://github.com/user-attachments/assets/ddcd61a1-c153-4357-85eb-8c2ddefeda73" />
    <img width="894" height="626" alt="gaussian example 2" src="https://github.com/user-attachments/assets/50c5dbbb-9d46-443f-8906-e024857d4cca" />

    - Sharpening is obviously the opposite so the higher the strength, the more emphasized are the edges.
    <img width="898" height="629" alt="sharpening example 1" src="https://github.com/user-attachments/assets/4dd17961-acdd-4e89-8a9c-dd1025baa60d" />
    <img width="896" height="628" alt="sharpening example 2" src="https://github.com/user-attachments/assets/b578231c-07c1-4645-bdbd-5f90d5780e0a" />

    - The optimized version of the convolution runs significantly faster than the basic one. Because of the use of multiple nested loops in the basic version it also slows down a lot with the kernel size increase.
