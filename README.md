# DRIVE: Diffusion Refinement and Instance-level Video Editing

**DRIVE** (Diffusion Refinement and Instance-level Video Editing) is a training-free video editing pipeline designed for precise instance-level control in video editing. Built on the foundations of the RAVE framework, DRIVE introduces several key innovations to improve quality, maintain temporal consistency, and enhance instance-aware editing without the need for additional training.

![Pipeline Overview](https://github.com/leolinpotato/DRIVE/blob/main/assets/examples/main_teaser.png)

## Key Features
- **Mask-Guided Compositional Denoising**: Leverages semantic guidance and spatial masking to apply precise style transformations to target objects while maintaining coherence with the surrounding scene.
- **Foreground-Background Composition**: Discards the generated background and reuses the original unaltered background to ensure natural fidelity and prevent artifacts caused by the denoising process.
- **Harmonization Post-Processing**: Aligns the visual properties of the foreground and background using neural regressor-based white-box filters for seamless blending and stylistic coherence.
- **EasyInv for DDIM Inversion**: Reduces error and preserves distinctive details by integrating exponential moving average (EMA) at key time steps during the inversion process.

## Methodology
DRIVE's pipeline integrates several components for efficient and precise video editing:
1. **Preprocessing**:
   - A zero-shot visual tracking model (e.g., SAMURAI) generates binary masks for tracking objects across frames. These masks ensure spatial and temporal consistency throughout the pipeline.
2. **Denoising**:
   - The **Mask-Guided Compositional Denoising** step generates conditional noise $`(\hat{\epsilon}_\text{cond})`$ and unconditional noise $`(\hat{\epsilon}_\text{uncond})`$, composited using a binary mask:

```math
     \hat{\epsilon} = M \cdot \hat{\epsilon}_\text{cond} + (1 - M) \cdot \hat{\epsilon}_\text{uncond}
```

3. **Composition**:
   - The refined foreground is composited with the original background to discard artifacts from the generated background and retain the natural scene integrity.
4. **Harmonization**:
   - Ensures seamless blending of foreground and background using filter-based adjustments for attributes like brightness, contrast, and color tone.
5. **Detail Refinement**:
   - **EasyInv** enhances detail preservation by periodically blending latent states during DDIM inversion:

```math
     z_{\bar{t}} = \eta z_{\bar{t}} + (1 - \eta) z_{\bar{t}-1}
```

## Installation

### RAVE
1. Set up environments following REAMD.md in RAVE

### Harmonizer

1. Set up environments following REAMDME.md in Harmonizer/demo/video_harmonization

2. Prepare foreground/background/mask videos and put them into Harmonizer/demo/video_harmonization

3. If the foreground video is a GIF file, run the following script under Harmonizer/demo/video_harmonization
```shell
python gif_to_mp4.py --gif your_gif_file
```

4. Create individual folders for foreground/background/mask, put videos into corresponding folder, and rename them to 0.mp4

5. Modify video_harmonization.sh under Harmonizer and run
```shell
bash video_harmonization.sh
```

## Acknowledgments
This project is developed based on the following open-source codebases:
- [RAVE](https://github.com/RehgLab/RAVE)
- [Harmonizer](https://github.com/ZHKKKe/Harmonizer)
- [EasyInv](https://github.com/potato-kitty/EasyInv)
- [SAMURAI](https://github.com/yangchris11/samurai) 