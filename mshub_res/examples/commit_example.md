# [model-name]

---

model-name: [] <required>

backbone-name: [] <required>

module-type: [cv/nlp/audio/recommend/RL/3D/video] e.g. cv-classification <required>

> CV: classification, object_detection, object_tracking, image_generation, image_denoise, super_resolution, image_enhancement, instance_segmentation, semantic_segmentation, panoptic_segmentation, keypoint_detection, face_recognition, OCR, pose_estimation, medical_imaging, anomaly_detection, metric_learning, others
>
> NLP: representation_learning, machine_translation, question_answering, language_modelling, text_classification, sentiment_analysis, text_augmentation, text_generation, named_entity_recognition, text_summarization, reading_comprehension, relation_extraction, image_captioning, dependency_parsing, dialogue, semantic_textual_similarity, others
>
> Audio: music_generation, generation, classification, environmental_sound_classification, acoustic_scene_classification, sound_event_detection, tagging, super_resolution, speech_analysis, speech_recognition, emotion_recognition, speech_enhancement, speaker_verification, voice_conversion, speech_separation, spoken_language_understanding, keyword_spotting, speaker_recognition, TTS, others
>
> Recommend: click_through_rate_prediction, session_based, next_basket, content_understanding, recall, rank, multi_task, match, re_rank, others
>
> Reinforcement Learning: curriculum_learning, self_paced_learning, temporal_difference_update, monte_carlo_update, offline, online, model_free, model_based, others
>
> 3D: reconstruction, pose_estimation, shape_reconstruction, shape_representation, object_classification, shape_classification, shape_generation, point_cloud_matching, depth_estimation, object_detection, instance_segmentation, semantic_instance_segmentation, object_recognition, others
>
> video: super_resolution, object_segmentation, prediction, classification, action_classification, object_tracking, understanding, generation, retrieval, recognition, frame_interpolation, multiple_object_tracking, compression, motion_compensation, others
>
> Others: others

fine-tunable: [True/False] <required>

input-shape: [224, 224, 3] <required>

model-version: [1.0] <required>

train-dataset: [cifar10/mnist/...] <optional>

accuracy: []<optional>

author: [] <required>

update-time: [date-time] <required>

repo-link: [link] <required>

user-id: [] <required>

used-for: [inference/extract-feature/transfer-learning] <required>
featured-image: [path_to_image] <optional>

train-backend: [cpu/gpu/ascend] <required>

infer-backend: [cpu/gpu/ascend] <optional>

mindspore-version: [0.6] <required>

allow-cache-ckpt: [True/False] # will try to optimize the model to run in mobile devices, default False

## assets

  -
    file-format: [mindir/ckpt/onnx/air/mslite] <optional>
    asset-link: []  <optional>
    asset_sha256: [] <optional>
  -
    file-format: [mindir/ckpt/onnx/air/mslite] <optional>
    asset-link: []  <optional>
    asset_sha256: [] <optional>
  -
    ...

asset-link: [] <optional>

asset_sha256: <optional>

license: [Apache2.0] <required>

summary: [Description of the model， one line description] <required>

---

## Introduction

[Detailed Description of the model]

## Usage

## Citation

## Change Log
