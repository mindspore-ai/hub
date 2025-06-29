# VideoComposer

---

model-name: VideoComposer

backbone-name: diffusion

module-type: mm

fine-tunable: True

model-version: 2.5

train-dataset: N/A

author: MindSpore team

update-time: 2025-04-22

repo-link: <https://github.com/mindspore-lab/mindone/tree/v0.3.0/examples/videocomposer>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

license: Apache2.0

summary: VideoComposer is a compositional video synthesis model with motion controllability

---

# VideoComposer based on MindSpore

MindSpore implementation & optimization of [VideoComposer: Compositional Video Synthesis with Motion Controllability](https://arxiv.org/pdf/2306.02018.pdf).

## Gallery

### Different conditions to videos

<p align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/9409b63e-c9fb-40c4-8ca6-7e8291a7c983" width="720" />
<br />
<em> Condition: image depth <br /> Text input: "A black swan swam in the water" </em>
</p>

<br />
<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/03af962b-3c56-4bdd-a16b-c6038bfd6389" width="720" />
</div>
<p align="center">
<em> Condition: local image <br /> Text input: "A black swan swam in the water" </em>
</p>

<br />
<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/35c8ea4e-b59e-4dab-a2d9-31eb29ddd098" width="720" />
</div>
<p align="center">
<em> Condition: mask <br /> Text input: "A black swan swam in the water" </em>
</p>

<br />
<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/5bddeb4f-9e6c-42a8-bfed-f74e27a2e490" width="720" />
</div>
<p align="center">
<em> Condition: motion <br /> Text input: "A black swan swam in the water" </em>
</p>

<br />
<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/89cdfceb-e070-446e-9dcb-a983bea8c9d9" width="720" />
</div>
<p align="center">
<em> Condition: sketch <br /> Text input: "A black swan swam in the water" </em>
</p>

### Motion transfer to videos

<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/0617e0de-5eb8-4820-8cac-1847b32b2a90" width="720" />
</div>
<p align="center">
<em> Text input: "Beneath Van Gogh's Starry Sky" </em>
</p>

<br />
<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/1ba8cab5-d646-4574-b62a-a63c0bdd3d25" width="720" />
</div>
<p align="center">
<em> Text input: "A beautiful big silver moon on the water" </em>
</p>

<br />
<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/0f989cc9-24b9-4925-b07b-2d44dc100f24" width="720" />
</div>
<p align="center">
<em> Text input: "A sunflower in a field of flowers" </em>
</p>

### Single sketch to videos with style

<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/b8a2ed38-d209-4ca2-b60c-6cca1114a21b" width="30%" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/d6967daf-7b3d-48bd-8382-ba65724077c0" width="60%" />
</div>
<p align="center">
<em> Style image </em>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<em> Text input: "Red-backed Shrike lanius collurio" </em>
</p>

### Single sketch to videos without style

<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/32d67667-e5ea-4b2e-afbc-be8781f22e04" width="720" />
</div>
<p align="center">
<em> Text input: "A little bird is standing on a branch" </em>
</p>

### Image depth to videos without style

<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/03a71a01-0b66-499d-bfe0-3fd9a8fbf34f" width="720" />
</div>
<p align="center">
<em> Text input: "Ironman is fighting against the enemy, big fire in the background, photorealistic" </em>
</p>

### Image depth to videos with style

<div align="center">
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/124e927b-8291-41ea-b6ab-58279f9ceb1d" width="25%" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://github.com/HaoyangLee/mindone/assets/20376974/7c8a1a1e-4034-4c17-a1f7-1eaac1839fc5" width="60%" />
</div>
<p align="center">
<em> Style image </em>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<em> Text input: "Van Gogh played tennis under the stars" </em>
</p>

<br />

> Inference scripts and configuration referring to [`scripts/run_infer.sh`](scripts/run_infer.sh).

## Main Features

- ✔ Conditional Video Generation including the following tasks:
    - ✔ Motion transfer from a video to a single image (exp02)
    - ✔ Single sketch to videos with or without style guidance (exp03 and exp04)
    - ✔ Depth to video with or without style guidance (exp5 and exp6)
    - ✔ Generate videos based on multiple conditions: depth maps, local image, masks, motion, and sketch
- ✔ Model Training (vanilla finetuning) supporting both Ascend 910 and Atlas 800T A2 machines
- ✔ Acceleration and Memory Reduction
    - ✔ Mixed Precision
    - ✔ Graph Mode for Training
    - ✔ Recompute

<div align="center">
<img src="https://github.com/SamitHuang/mindone/assets/8156835/eb8a19d3-9ce2-4a31-9696-d6a13857e986" width="720" />
</div>
<p align="center">
<em> VideoComposer Architecture </em>
</p>

## Requirements

| mindspore | ascend driver |  firmware   | cann toolkit/kernel |
| :-------: | :-----------: | :---------: | :-----------------: |
|    2.5    |   24.1.RC2    | 7.3.0.1.231 |    8.0.RC3.beta1    |

Python: 3.7 or higher.

Then run `pip install -r requirements.txt` to install the necessary packages.

For `ffmpeg`, install by

```shell
conda install ffmpeg
```

If case you fail to install `motion-vector-extractor` via pip, please manually install it referring to the [official](https://github.com/LukasBommes/mv-extractor) repo.

## Prepare Pretrained Weights

The root path of downloading must be `${PROJECT_ROOT}\model_weights`, where `${PROJECT_ROOT}` means the root path of project.

Download the checkpoints shown in model_weights/README.md from https://download.mindspore.cn/toolkits/mindone/videocomposer/model_weights/ and https://download.mindspore.cn/toolkits/mindone/stable_diffusion/depth_estimator/midas_v3_dpt_large-c8fd1049.ckpt

## Prepare Training Data

The training videos and their captions (.txt) should be placed in the following folder structure.

```text
 ├── {DATA_DIR}
 │   ├── video_name1.mp4
 │   ├── video_name1.txt
 │   ├── video_name2.mp4
 │   ├── video_name2.txt
 │   ├── ...
```

Run `examples/videocomposer/tools/data_converter.py` to generate `video_caption.csv` in `{DATA_DIR}`.

```shell
python data_converter.py {DATA_DIR}
```

Format of `video_caption.csv`:

```text
video,caption
video_name1.mp4,"an airliner is taxiing on the tarmac at Dubai Airport"
video_name2.mp4,"a pigeon sitting on the street near the house"
...
```

## Inference

### Online Inference

To run all video generation tasks on Ascend 910 or Atlas 800T A2 machines, please run

```shell
bash scripts/run_infer.sh
```

On Ascend 910, to run a single task, you can pick the corresponding snippet of code in `scripts/run_infer.sh`, such as

```shell
python infer.py \
    --cfg configs/exp02_motion_transfer_vs_style.yaml \
    --seed 9999 \
    --input_video "demo_video/motion_transfer.mp4" \
    --image_path "demo_video/moon_on_water.jpg" \
    --style_image "demo_video/moon_on_water.jpg" \
    --input_text_desc "A beautiful big silver moon on the water"
```

It takes additional time for graph compilation to execute the first step inference (around 5~8 minutes).

### Key arguments for inference

You can adjust the arguments in `vc/config/base.py` (lower-priority) or `configs/exp{task_name}.yaml` (higher-priority, will overwrite base.py if overlap). Below are the key arguments influencing inference speed and memory usage.

- use_fp16: whether enable mixed precision inference

### Offline (Mindspore Lite) Inference

#### Install Mindspore Lite

You need to have a Mindspore Lite Environment first for offline inference.

To install Mindspore Lite, please refer to [Lite install](https://mindspore.cn/lite/docs/zh-CN/r2.1/use/downloads.html)

1. Download the supporting tar.gz and whl packages according to the environment.
2. Unzip the tar.gz package and install the corresponding version of the WHL package.

   ```shell
   tar -zxvf mindspore-lite-2.1.0-*.tar.gz
   pip install mindspore_lite-2.1.0-*.whl
   ```

3. Configure Lite's environment variables

   `LITE_HOME` is the folder path extracted from tar.gz, and it is recommended to use an absolute path.

   ```shell
   export LITE_HOME=/path/to/mindspore-lite-{version}-{os}-{platform}
   export LD_LIBRARY_PATH=$LITE_HOME/runtime/lib:$LITE_HOME/tools/converter/lib:$LD_LIBRARY_PATH
   export PATH=$LITE_HOME/tools/converter/converter:$LITE_HOME/tools/benchmark:$PATH
   ```

#### Export Mindspore Lite Model

For different tasks, you can use the corresponding snippet of the code in `scripts/run_infer.sh`, and change `infer.py` to `export.py` to save the MindIR model.

```shell
python export.py\
    --cfg configs/exp02_motion_transfer_vs_style.yaml \
    --input_video "demo_video/motion_transfer.mp4" \
    --image_path "demo_video/moon_on_water.jpg" \
    --style_image "demo_video/moon_on_water.jpg" \
    --input_text_desc "A beautiful big silver moon on the water"
```

The exported MindIR models will be saved at `models/mindir` directory. Once the exporting is finished, you need to convert the MindIR model to Mindspore Lite MindIR model. We have provided a script `convert_lite.py` to convert all MindIR models in `models/mindir` directory.

```shell
python convert_lite.py
```

#### Inference using the exported Lite models

Then you can run the offline inference using the `infer_lite.py` for the given task, e.g,

```shell
python lite_infer.py\
    --cfg configs/exp02_motion_transfer_vs_style.yaml \
    --seed 9999 \
    --input_video "demo_video/motion_transfer.mp4" \
    --image_path "demo_video/moon_on_water.jpg" \
    --style_image "demo_video/moon_on_water.jpg" \
    --input_text_desc "A beautiful big silver moon on the water"
```

The compiling time is much shorter compared with the online inference mode.

## Training

### Standalone Training

To run training on a specific task, please refer to `scripts/run_train.sh`.

After changing the `task_name` and `yaml_file` in the script for your task, run:

```shell
bash scripts/run_train.sh $DEVICE_ID $OUTPUT_DIR
```

e.g. `bash scripts/run_train.sh 0 out_train` to launch the training task using NPU card 0 and output folder is out_train.

Under `configs/`, we provide several tasks' yaml files:

```bash
configs/
├── train_exp02_motion_transfer_vs_style.yaml
├── train_exp02_motion_transfer.yaml
├── train_exp03_sketch2video_style.yaml
├── train_exp04_sketch2video_wo_style.yaml
├── train_exp05_text_depths_wo_style.yaml
└── train_exp06_text_depths_vs_style.yaml
```

Taking `configs/train_exp02_motion_transfer.yaml` as an example, there is one critical argument:

```yaml
video_compositions:
  [
    "text",
    "mask",
    "depthmap",
    "sketch",
    "single_sketch",
    "motion",
    "image",
    "local_image",
  ]
```

`video_compositions` defines all available conditions:

- `text`: the text embedding.
- `mask`: the masked video frames.
- `depthmap`: the depth images extracted from visual frames.
- `sketch`: the sketch images extracted from visual frames.
- `single_sketch`: the first sketch image from `sketch`.
- `motion`: the motion vectors extracted from the training video.
- `image`: the image embedding used as an image style vector.
- `local_image`: the first frame extracted from the training video.

However, not all conditions are included in the training process in each of the tasks above. As defined in `configs/train_exp02_motion_transfer.yaml`,

```yaml
conditions_for_train: ["text", "local_image", "motion"]
```

`conditions_for_train` defines the three conditions used for training which are `['text', 'local_image', 'motion']`.

### Distributed Training

Please generate the HCCL config file on your running server at first referring to [this tutorial](https://github.com/mindspore-lab/mindocr/blob/v0.4.0/docs/cn/tutorials/distribute_train.md). Then update `scripts/run_train_distribute.sh` by setting

```shell
rank_table_file=path/to/hccl_8p_01234567_xxx.json
```

After that, please set `task_name` according to your target task. The default training task is `train_exp02_motion_transfer`.

Then execute,

```shell
bash scripts/run_train_distribute.sh
```

#### Training in Step Mode

By default, training is done in epoch mode, i.e. checkpoint will be saved in every `ckpt_save_interval` epoch.
To change to step mode, in train_xxx.yaml, please modify as:

```yaml
dataset_sink_mode: False
step_mode: True
ckpt_save_interval: 1000
```

e.g., it will save checkpoints every 1000 training steps.

Currently, it's not compatible with dataset_sink_mode=True. It can be solved by setting `sink_size=ckpt_save_intervel` and `epochs=num_epochs*(num_steps_per_epoch//ckpt_save_intervel)` in `model.train(...)`, which is under testing.

#### Supporting Annotation File Format

Both json and csv file are supported. JSON has a higher priority.

### Key arguments for training

You can adjust the arguments in `configs/train_base.py` (lower-priority) or `configs/train_exp{task_name}.yaml` (higher-priority, will overwrite train_base.py if overlap). Below are the key arguments.

- max_frames: number of frames to generate for each sample. Without memory reduction tricks, it can be set up to 8 for 910, and 16 for Ascend Atlas 800T A2 machines for task-2 finetuning.
- optim: optimizer name, `adamw` or `momentum`. Recommend `momentum` for Ascend 910 to avoid OOM and `adamw` for Ascend Atlas 800T A2 machines for better loss convergence.
- use_recompute: by enabling it, you can reduce memory usage with a small increase in time cost. For example, on Ascend 910, the max number of trainable frames per batch increases from 8 to 14 after recomputing is enabled.
- `root_dir`: dataset root dir which should contain a csv annotation file. default is `demo_video`, which contains an example annotation file `demo_video/video_caption.csv` for demo traning.
- `num_parallel_workers`: default is 2. Increasing it can help reduce video processing time cost if CPU cores are enough (i.e. num_workers\*num_cards<num_cpu_cores) and Memory is enough (i.e. approximately, prefetch_size\*max_row_size\*num_workers < mem size)

## Results

### Training

The training performance for exp02-motion transfer on Ascend Atlas 800T A2 machines with different modes is as follows:

|  model name   | cards | batch size | resolution | recompute | sink | graph compile |   mode   | jit level | s/step | video/s |
| :-----------: | :---: | :--------: | :--------: | :-------: | :--: | :-----------: | :------: | :-------: | :----: | :-----: |
| videocomposer |   1   |     1      | 16x256x256 |    ON     |  ON  |      N/A      | pynative |    N/A    |   18   |  0.06   |
| videocomposer |   1   |     1      | 16x256x256 |    ON     |  ON  | 13 ~ 16 mins  |  graph   |    O2     |  0.7   |  1.42   |
| videocomposer |   1   |     1      | 16x256x256 |    ON     |  ON  | 21 ~ 24 mins  |  graph   |    O1     |   10   |   0.1   |
| videocomposer |   1   |     1      | 16x256x256 |    ON     |  ON  | 25 ~ 28 mins  |  graph   |    O0     |   16   |  0.06   |

### Inference

The video generation speed is as follows.

|  model name   | cards | batch size | resolution | s/step | video/s |
| :-----------: | :---: | :--------: | :--------: | :----: | :-----: |
| videocomposer |   1   |     1      | 16x256x256 |  0.22  |  0.09   |
