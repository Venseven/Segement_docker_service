# Segment_docker_service

### Input
- Place the input images inside `data/input`  

### To run the docker segmentation service
`sudo docker-compose up --build`

### To trigger the inference
`curl http://127.0.0.1:8081/home?type=trigger`

### Predictions and object counts
- Output segmentation images will be stored inside `data/output`
- Object counts for each images will be returned as a JSON