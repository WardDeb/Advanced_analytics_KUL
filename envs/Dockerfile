FROM tensorflow/tensorflow:2.15.0.post1-gpu-jupyter
RUN python3 -m pip install pandas ==  2.2.2
RUN python3 -m pip install seaborn == 0.13.2
RUN python3 -m pip install opencv-python-headless == 4.9.0.80
RUN python3 -m pip install scikit-learn == 1.4.2
RUN python3 -m pip install numpy == 1.26.2
RUN python3 -m pip install pillow == 9.5.0
RUN python3 -m pip install visualkeras == 0.0.2
RUN python3 -m pip install scikit-image == 0.23.2
RUN apt-get update
RUN apt-get install -y vim

CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/tf --ip 0.0.0.0 --no-browser --allow-root"]
