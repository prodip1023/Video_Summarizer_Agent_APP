conda create -n agentapp python=3.11 -y

conda activate agentapp

pip install -r requirements.txt

- 1. Login with your AWS console and launch an EC2 instance
- 2. Run the following commands
   
   - Note: Do the port mapping to this port:- 8501

   ```
   sudo apt update
   
    ```
    ```
    sudo apt-get update
    
    ```
    ```
    sudo apt upgrade -y
    
    ```

    ```
    sudo apt install git curl unzip tar make sudo vim wget -y
    
    ```
    
    ```
    git clone "Your-repository"
    
    ```
    ```
    sudo apt install python3-pip

    ```
    ```
    pip3 install -r requirements.txt or 
    pip3 install -r requirements.txt --break-system-packages
    ```

    ```
    python3 -m streamlit run app.py

    ```
    ```
    nohup python3 -m streamlit run app.py

    ```

    - Note: Streamlit runs on this port: 8501

# Streamlit app Docker Image

- 1. Login with your AWS console and launch an EC2 instance
- 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```
```
git clone "your-project"
```
```
docker build -t entbappy/stapp:latest . 
```
```
docker images -a  
```
```
docker run -d -p 8501:8501 entbappy/stapp 
```
```
docker ps  
```
```
docker stop container_id
```
```
docker rm $(docker ps -a -q)
```
```
docker login 
```
```
docker push entbappy/stapp:latest 
```
```
docker rmi entbappy/stapp:latest
```
```
docker pull entbappy/stapp
```