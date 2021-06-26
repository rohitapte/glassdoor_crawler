import os
import json

def aggregate_data_for_word2vec_training(datapath='data'):
    with open('AggregateData.txt','w',encoding='utf-8') as f:
        for fname in os.listdir(datapath):
            for line in open(os.path.join(datapath, fname)):
                data=json.loads(line)
                sTemp=data['pros'].strip().lower()
                if len(sTemp)>0:
                    f.write(sTemp + '\n')
                sTemp = data['cons'].strip().lower()
                if len(sTemp) > 0:
                    f.write(sTemp + '\n')
                sTemp = data['adviceManagement'].strip().lower()
                if len(sTemp) > 0:
                    f.write(sTemp + '\n')



if __name__ == "__main__":
    aggregate_data_for_word2vec_training()