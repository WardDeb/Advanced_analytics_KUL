FROM tensorflow/tensorflow:latest-gpu-jupyter
RUN python3 -m pip install pandas
RUN python3 -m pip install seaborn
RUN python3 -m pip install opencv-python-headless
RUN python3 -m pip install scikit-learn
RUN python3 -m pip install numpy
RUN python3 -m pip install pillow

CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/tf --ip 0.0.0.0 --no-browser --allow-root"]
