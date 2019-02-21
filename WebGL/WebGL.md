阅读笔记：从基础理论开始学习WebGL，稳！推荐 [WebGL 理论基础](https://webglfundamentals.org/webgl/lessons/zh_cn/)。

# WebGL 基础概念

- WebGL（Web Graphics Library）只是一个光栅化 API。
- WebGL 有两类着色器数据：顶点在裁剪空间中的坐标值和颜色值。
- GLSL（Graphics Library Shader Language）着色器专用语言。
- 顶点着色器计算顶点的坐标值。裁剪空间的坐标范围永远是 -1 到 1 。
- 片断着色器计算当前绘制图元中每个像素的颜色值。
- WebGL 颜色值范围从 0 到 1 。例如，`vec4(1, 0, 0.5, 1);` 其中1代表红色值，0代表绿色值，0.5代表蓝色值，最后一个1表示阿尔法通道值。
- 着色器数据传递给 GPU（Graphics Processing Unit）运行。
