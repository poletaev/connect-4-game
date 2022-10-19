FROM  continuumio/miniconda3

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . $APP_HOME

#---------------- Prepare the envirennment
RUN conda update conda && \
    conda create --name app --file requirements.txt python=3.9 -c conda-forge 
RUN echo 'conda activate app \n' >> /root/.bashrc
ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
CMD ["python game_src/connect4_game.py"]
