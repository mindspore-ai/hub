# DeepLabv3

---

模型名称：DeepLab_v3_s16

骨干网络：ResNet-101

模块类型：cv-semantic_segmentation

可微调：True

输入形状：[897, 897, 3]

模型版本：1.0

准确率：0.773

作者：MindSpore团队

更新时间：2020-9-4

代码仓链接： <https://gitee.com/mindspore/models/tree/master/official/cv/deeplabv3>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

MindSpore Lite：True

资源：

- 文件格式：.mslite  
  资源链接： <https://download.mindspore.cn/model_zoo/official/lite/deeplabv3_lite/deeplabv3.ms>  
  资源SHA256校验码： 1158a5eadfa6bb729500f7de89c33b1e264f4514a70780055afa1355541b5766

许可证：Apache 2.0

摘要：使用DeepLabv3进行图像语义分割。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的DeepLabv3实现，目录为model_zoo/official/cv/deeplabv3。该训练模型适用于图像分割任务。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
model = "mindspore/ascend/1.0/deeplabv3_v1"
# 根据预训练模型初始化类数
network = mshub.load(model, pretrained=False, num_classes=21)
#...
```

具体用法请参考ModelZoo的README描述： <https://gitee.com/mindspore/models/tree/master/official/cv/deeplabv3>

## Lite推理用法

1. 加载MindSpore Lite模型文件，构建上下文、会话和计算图进行推理。

    - 加载模型文件。导入并配置模型推理上下文。

    ```Java
    // 创建上下文，加载名为'IMAGESEGMENTATIONMODEL'的.ms模型
    model = new Model();
    if (!model.loadModel(Context, IMAGESEGMENTATIONMODEL)) {
      Log.e(TAG, "Load Model failed");
      return;
    }
    ```

    - 创建会话。

    ```Java
    // 创建并初始化配置
    msConfig = new MSConfig();
    if (!msConfig.init(DeviceType.DT_CPU, 2, CpuBindMode.MID_CPU)) {
      Log.e(TAG, "Init context failed");
      return;
    }

    // 创建MindSpore Lite会话
    session = new LiteSession();
    if (!session.init(msConfig)) {
      Log.e(TAG, "Create session failed");
      msConfig.free();
      return;
    }
    msConfig.free();
    ```

    - 编写图进行推理。

    ```Java
    if (!session.compileGraph(model)) {
      Log.e(TAG, "Compile graph failed");
      model.freeBuffer();
      return;
    }
    // 注意：使用model.freeBuffer()时，模型不能重新编译图。
    model.freeBuffer();
    ```

2. 将输入的图片转换为MindSpore模型的Tensor格式。

    ```Java
    List<MSTensor> inputs = session.getInputs();
    if (inputs.size() != 1) {
      Log.e(TAG, "inputs.size() != 1");
      return null;
    }

    // `bitmap`是用于推理的图片。
    float resource_height = bitmap.getHeight();
    float resource_weight = bitmap.getWidth();
    ByteBuffer contentArray = bitmapToByteBuffer(bitmap, imageSize, imageSize, IMAGE_MEAN, IMAGE_STD);

    MSTensor inTensor = inputs.get(0);
    inTensor.setData(contentArray);
    ```

3. 根据模型对输入tensor进行推理，得到输出tensor，并进行后处理。

    - 进行图执行和端侧推理。

    ```Java
    // 模型和图片tensor数据加载完成后，运行推理。
    if (!session.runGraph()) {
      Log.e(TAG, "Run graph failed");
      return null;
    }
    ```

    - 获取输出数据。

    ```Java
    // 获取输出tensor值，模型只输出一个tensor。
    List<String> tensorNames = session.getOutputTensorNames();
    MSTensor output = session.getOutputByTensorName(tensorNames.front());
    if (output == null) {
      Log.e(TAG, "Can not find output " + tensorName);
      return null;
    }
    ```

    - 对输出数据进行后处理。

    ```Java
    // 输出为图片。
    float[] results = output.getFloatData();

    ByteBuffer bytebuffer_results = floatArrayToByteArray(results);

    Bitmap dstBitmap = convertBytebufferMaskToBitmap(bytebuffer_results, imageSize, imageSize, bitmap, dstBitmap, segmentColors);
    dstBitmap = scaleBitmapAndKeepRatio(dstBitmap, (int) resource_height, (int) resource_weight);
    ```

4. 图像和输出数据的处理可以参考下面的方法。

    ```Java
    Bitmap scaleBitmapAndKeepRatio(Bitmap targetBmp, int reqHeightInPixels, int reqWidthInPixels) {
      if (targetBmp.getHeight() == reqHeightInPixels && targetBmp.getWidth() == reqWidthInPixels) {
        return targetBmp;
      }

      Matrix matrix = new Matrix();
      matrix.setRectToRect(new RectF(0f, 0f, targetBmp.getWidth(), targetBmp.getHeight()),
                           new RectF(0f, 0f, reqWidthInPixels, reqHeightInPixels), Matrix.ScaleToFit.FILL;

        return Bitmap.createBitmap(targetBmp, 0, 0, targetBmp.getWidth(), targetBmp.getHeight(), matrix, true);
    }

    ByteBuffer bitmapToByteBuffer(Bitmap bitmapIn, int width, int height, float mean, float std) {
      Bitmap bitmap = scaleBitmapAndKeepRatio(bitmapIn, width, height);
      ByteBuffer inputImage = ByteBuffer.allocateDirect(1 * width * height * 3 * 4);
      inputImage.order(ByteOrder.nativeOrder());
      inputImage.rewind();
      int[] intValues = new int[width * height];
      bitmap.getPixels(intValues, 0, width, 0, 0, width, height);
      int pixel = 0;
      for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
          int value = intValues[pixel++];
          inputImage.putFloat(((float) (value >> 16 & 255) - mean) / std);
          inputImage.putFloat(((float) (value >> 8 & 255) - mean) / std);
          inputImage.putFloat(((float) (value & 255) - mean) / std);
        }
      }
      inputImage.rewind();
      return inputImage;
    }

    ByteBuffer floatArrayToByteArray(float[] floats) {
      ByteBuffer buffer = ByteBuffer.allocate(4 * floats.length);
      FloatBuffer floatBuffer = buffer.asFloatBuffer();
      floatBuffer.put(floats);
      return buffer;
    }

    Bitmap convertBytebufferMaskToBitmap(ByteBuffer inputBuffer, int imageWidth, int imageHeight, Bitmap backgroundImage, int[] colors) {
      Bitmap.Config conf = Bitmap.Config.ARGB_8888;
      Bitmap dstBitmap = Bitmap.createBitmap(imageWidth, imageHeight, conf);
      Bitmap scaledBackgroundImage = scaleBitmapAndKeepRatio(backgroundImage, imageWidth, imageHeight);
      int[][] mSegmentBits = new int[imageWidth][imageHeight];
      inputBuffer.rewind();
      for (int y = 0; y < imageHeight; y++) {
        for (int x = 0; x < imageWidth; x++) {
          float maxVal = 0f;
          mSegmentBits[x][y] = 0;
          // NUM_CLASSSES为标签个数，此处为21。
          for (int i = 0; i < NUM_CLASSES; i++) {
            float value = inputBuffer.getFloat((y * imageWidth * NUM_CLASSES + x * NUM_CLASSES + i) * 4);
            if (i == 0 || value > maxVal) {
              maxVal = value;
              // 判断像素是否属于标签为15的人。
              if (i == 15) {
                mSegmentBits[x][y] = i;
              } else {
                mSegmentBits[x][y] = 0;
              }
            }
          }
          itemsFound.add(mSegmentBits[x][y]);

          int newPixelColor = ColorUtils.compositeColors(
                  colors[mSegmentBits[x][y] == 0 ? 0 : 1],
                  scaledBackgroundImage.getPixel(x, y)
          );
          dstBitmap.setPixel(x, y, mSegmentBits[x][y] == 0 ? colors[0] : scaledBackgroundImage.getPixel(x, y));
        }
      }
      return dstBitmap;
    }
    ```

## 参考论文

1. Chen L C, Papandreou G, Schroff F, et al. Rethinking atrous convolution for semantic image segmentation[J]. arXiv preprint arXiv:1706.05587, 2017.
