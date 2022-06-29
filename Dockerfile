FROM python:3.8.10
RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY main.py .
RUN apt-get update
RUN curl -LJO https://github.com/ayoolaolafenwa/PixelLib/releases/download/0.2.0/pointrend_resnet50.pkl
COPY pointrend_resnet50.pkl ./pointrend_resnet50.pkl
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install torch==1.9.0+cpu torchvision==0.10.0+cpu torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt
EXPOSE 8081
CMD ["python", "main.py"]