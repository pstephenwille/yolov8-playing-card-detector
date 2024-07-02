# card detection/predcition with Yolov8 model

### develop
1. run the flask app cli: `flask run`
2. confirm:` curl localhost:6000/test-image-dir` 

### deploy
1. install nvidia-container-toolkit https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

1. build docker file base
   >docker build -f Dockerfile-base -t detect-cards-base .
1. build docker file app
   >docker build -f Dockerfile-app -t detect-cards-app .
2. run the app
   >docker run \'tf_keras', 'sng4onnx>=1.0.1', 'onnx_graphsurgeon>=0.3.26', 'onnx>=1.12.0', 'onnx2tf>1.17.5,<=1.22.3', 'onnxslim>=0.1.31', 'tflite_support', 'onnxruntime'
   -p 5000:5000 \
   --rm \
   --runtime=nvidia \
   --gpus all \
   --ipc=host \
   detect-cards-app:latest

1. call api: 


