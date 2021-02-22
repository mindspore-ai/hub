# [模型名称]

---

模型名称：[] <required>

骨干网络：[] <required>

模块类型：[CV、NLP、音频、推荐、强化学习、3D、视频]，如cv-classification。 <required>

> CV：classification, object_detection, object_tracking, image_generation, image_denoise, super_resolution, image_enhancement, instance_segmentation, semantic_segmentation, panoptic_segmentation, keypoint_detection, face_recognition, OCR, pose_estimation, medical_imaging, anomaly_detection, metric_learning, others
>
> NLP：representation_learning, machine_translation, question_answering, language_modelling, text_classification, sentiment_analysis, text_augmentation, text_generation, named_entity_recognition, text_summarization, reading_comprehension, relation_extraction, image_captioning, dependency_parsing, dialogue, semantic_textual_similarity, others
>
> 音频：music_generation, generation, classification, environmental_sound_classification, acoustic_scene_classification, sound_event_detection, tagging, super_resolution, speech_analysis, speech_recognition, emotion_recognition, speech_enhancement, speaker_verification, voice_conversion, speech_separation, spoken_language_understanding, keyword_spotting, speaker_recognition, TTS, others
>
> 推荐：click_through_rate_prediction, session_based, next_basket, content_understanding, recall, rank, multi_task, match, re_rank, others
>
> 强化学习：curriculum_learning, self_paced_learning, temporal_difference_update, monte_carlo_update, offline, online, model_free, model_based, others
>
> 3D：reconstruction, pose_estimation, shape_reconstruction, shape_representation, object_classification, shape_classification, shape_generation, point_cloud_matching, depth_estimation, object_detection, instance_segmentation, semantic_instance_segmentation, object_recognition, others
>
> 视频：super_resolution, object_segmentation, prediction, classification, action_classification, object_tracking, understanding, generation, retrieval, recognition, frame_interpolation, multiple_object_tracking, compression, motion_compensation, others
>
> 其他：其他

可微调：[True、False] <required>

输入形状：[224, 224, 3] <required>

模型版本：[1.0] <required>

训练数据集：[CIFAR-10、MNIST......]<optional>

准确率：[] <optional>

作者：[] <required>

更新时间：[日期时间] <required>

代码仓链接：[链接] <required>

用户ID：[] <required>

用途：[推理、特征抽取、传递学习] <required>
特征图片：[图像路径] <optional>

训练后端：[CPU、GPU、Ascend] <required>

推理后端：[CPU、GPU、Ascend] <optional>

MindSpore版本：[0.6] <required>

可缓存检查点：[True、False] # 将尝试优化模型，使其能够在移动设备上运行，默认False。

## 资源

  -
    文件格式：[.mindir、.ckpt、.onnx、.air、.mslite] <optional>
    资源链接：[] <optional>
    资源SHA256校验码：[] <optional>
  -
    文件格式：[.mindir、.ckpt、.onnx、.air、.mslite] <optional>
    资源链接：[] <optional>
    资源SHA256校验码：[] <optional>
  -
    ...

资源链接：[] <optional>

资源SHA256校验码：<optional>

许可证：[Apache 2.0] <required>

摘要：[一句话描述模型] <required>

---

## 简介

[模型详细介绍]

## 用法

## 参考论文

## 变更日志
