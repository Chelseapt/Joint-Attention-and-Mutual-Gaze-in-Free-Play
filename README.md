# Automated-Detection-of-Joint-Attention-and-Mutual-Gaze-in-Free-Play-Parent-Child-Interactions

This repository focuses on detecting joint attention and mutual gaze in parent-child interactions during free play. We leverage advanced computer vision techniques to achieve this.

## Head Tracking
### Head Detection
- **Method**: We utilize the head detection module from [LAEO-Net++](https://github.com/AVAuco/laeonetplus).

### Head Tracking
- **Method**: Head tracking is accomplished using the DeepSORT method, available in the [DeepSORT repository](https://github.com/AVAuco/laeonetplus).

### Interpolation
To handle missing detections and smoothen the tracking results, run the interpolation script:
\```bash
headtracking/interpolate.py
\```

## Object Detection
For detecting objects in the scene, [add details or methods used if any].

## Classification
### Gaze Attention Heatmap
- **Method**: Gaze attention heatmaps are generated using the method proposed in [Detecting Attended Visual Targets in Video](https://github.com/ejcgt/attention-target-detection).

### Visual Focus of Attention (VFOA)
We integrate the gaze attention heatmap with the detected regions to determine if an object is being attended to by either the parent or child. A threshold of 80 is used to make this determination.

### Mutual/Joint Attention
By combining the views from both the parent and child, we derive mutual or joint attention insights.

## Evaluation
For evaluating the results and obtaining performance metrics, run the Cohen's Kappa evaluation script:
\```bash
evaluate/cohen-kappa.py
\```

---

Thank you for exploring this repository. Contributions and suggestions are welcome! Feel free to open issues or submit pull requests.

