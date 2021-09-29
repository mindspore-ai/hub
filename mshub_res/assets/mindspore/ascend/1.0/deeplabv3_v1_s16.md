# DeepLabv3

---

model-name: DeepLab_v3_s16

backbone-name: Resnet101

module-type: cv-semantic_segmentation

fine-tunable: True

input-shape: [897, 897, 3]

model-version: 1.0

accuracy: 0.773

author: MindSpore team

update-time: 2020-09-04

repo-link: <https://gitee.com/mindspore/models/tree/master/official/cv/deeplabv3>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

mindspore-lite: true

asset:

- file-format: mslite  
  asset-link: <https://download.mindspore.cn/model_zoo/official/lite/deeplabv3_lite/deeplabv3.ms>  
  asset-sha256: 1158a5eadfa6bb729500f7de89c33b1e264f4514a70780055afa1355541b5766  

license: Apache2.0

summary: DeepLabv3 used to image semantic segmentation

---

## Introduction

This MindSpore Hub model uses the implementation of DeepLabv3 from the MindSpore model zoo on Gitee at model_zoo/official/cv/deeplabv3, and is trained to complete image segmentation tasks.

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
model = "mindspore/ascend/1.0/deeplabv3_v1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, pretrained=False, num_classes=21)
#...
```

Refer to the readme description of modelzoo for specific usage: <https://gitee.com/mindspore/models/tree/master/official/cv/deeplabv3>

## Lite Inference  Usage

1. Load the MindSpore Lite model file and build the context, session, and computational graph for inference.

    - Load a model file. Import and configure the context for model inference.

    ```Java
    // Create context and load the .ms model named 'IMAGESEGMENTATIONMODEL'
    model = new Model();
    if (!model.loadModel(Context, IMAGESEGMENTATIONMODEL)) {
      Log.e(TAG, "Load Model failed");
      return;
    }
    ```

    - Create a session.

    ```Java
    // Create and init config.
    msConfig = new MSConfig();
    if (!msConfig.init(DeviceType.DT_CPU, 2, CpuBindMode.MID_CPU)) {
      Log.e(TAG, "Init context failed");
      return;
    }

    // Create the MindSpore lite session.
    session = new LiteSession();
    if (!session.init(msConfig)) {
      Log.e(TAG, "Create session failed");
      msConfig.free();
      return;
    }
    msConfig.free();
    ```

    - Compile graph for inference.

    ```Java
    if (!session.compileGraph(model)) {
      Log.e(TAG, "Compile graph failed");
      model.freeBuffer();
      return;
    }
    // Note: when use model.freeBuffer(), the model can not be compile graph again.
    model.freeBuffer();
    ```

2. Convert the input image into the Tensor format of the MindSpore model.

    ```Java
    List<MSTensor> inputs = session.getInputs();
    if (inputs.size() != 1) {
      Log.e(TAG, "inputs.size() != 1");
      return null;
    }

    // `bitmap` is the picture used to infer.
    float resource_height = bitmap.getHeight();
    float resource_weight = bitmap.getWidth();
    ByteBuffer contentArray = bitmapToByteBuffer(bitmap, imageSize, imageSize, IMAGE_MEAN, IMAGE_STD);

    MSTensor inTensor = inputs.get(0);
    inTensor.setData(contentArray);
    ```

3. Perform inference on the input tensor based on the model, obtain the output tensor, and perform post-processing.

    - Perform graph execution and on-device inference.

    ```Java
    // After the model and image tensor data is loaded, run inference.
    if (!session.runGraph()) {
      Log.e(TAG, "Run graph failed");
      return null;
    }
    ```

    - Obtain the output data.

    ```Java
    // Get output tensor values, the model only outputs one tensor.
    List<String> tensorNames = session.getOutputTensorNames();
    MSTensor output = session.getOutputByTensorName(tensorNames.front());
    if (output == null) {
      Log.e(TAG, "Can not find output " + tensorName);
      return null;
    }
    ```

    - Perform post-processing of the output data.

    ```Java
    // Show output as pictures.
    float[] results = output.getFloatData();

    ByteBuffer bytebuffer_results = floatArrayToByteArray(results);

    Bitmap dstBitmap = convertBytebufferMaskToBitmap(bytebuffer_results, imageSize, imageSize, bitmap, dstBitmap, segmentColors);
    dstBitmap = scaleBitmapAndKeepRatio(dstBitmap, (int) resource_height, (int) resource_weight);
    ```

4. The process of image and output data can refer to methods showing below.

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
          // NUM_CLASSES is the number of labels, the value here is 21.
          for (int i = 0; i < NUM_CLASSES; i++) {
            float value = inputBuffer.getFloat((y * imageWidth * NUM_CLASSES + x * NUM_CLASSES + i) * 4);
            if (i == 0 || value > maxVal) {
              maxVal = value;
              // Check whether a pixel belongs to a person whose label is 15.
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

## Citation

1. Chen L C, Papandreou G, Schroff F, et al. Rethinking atrous convolution for semantic image segmentation[J]. arXiv preprint arXiv:1706.05587, 2017.
