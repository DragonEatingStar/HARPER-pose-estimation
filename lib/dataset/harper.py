HARPER_KEYPOINTS = [
    "hip",
    "abdomen",
    "chest",
    "neck",
    "head",
    "left_shoulder",
    "left_upper_arm",
    "left_lower_arm",
    "left_hand",
    "right_shoulder",
    "right_upper_arm",
    "right_lower_arm",
    "right_hand",
    "left_shin",
    "left_thigh",
    "left_foot",
    "left_toe",
    "right_shin",
    "right_thigh",
    "right_foot",
    "right_toe",
]

HARPER_SKELETON = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (3, 5), (5, 6), (6, 7), (7, 8),
    (3, 9), (9, 10), (10, 11), (11, 12),
    (0, 13), (13, 14), (14, 15), (15, 16),
    (0, 17), (17, 18), (18, 19), (19, 20),
    (6, 13), (10, 17),
]

DEPTH_FOVS = {
    "frontleft_fisheye_image": [(0, 0), (640, 0), (640, 512), (0, 512)],
    "frontright_fisheye_image": [(0, 0), (640, 0), (640, 512), (0, 512)],
}
