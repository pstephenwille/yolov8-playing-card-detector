# card detection/predcition with Yolov8 model

### setup
1. install nvidia-container-toolkit https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

1. build docker file base
   >docker build -f Dockerfile-base -t detect-cards-base .
1. build docker file app
   >docker build -f Dockerfile-app -t detect-cards-app .
2. run the app
   >docker run \
   -p 5000:5000 \
   --rm \
   --runtime=nvidia \
   --gpus all \
   --ipc=host \
   detect-cards-app:latest

1. call api: 



