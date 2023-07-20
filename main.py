import os
import pandas as pd

if __name__ == '__main__':

    dict_path = "dicts"
    export_path = "exports"
    for name in os.listdir(dict_path):
        # print(f"开始处理{name}...")
        df = pd.read_csv(os.path.join(dict_path, name), header=None)
        df.columns = ['name', 'trans']
        # print(df.shape)
        try:
            df['trans'] = df['trans'].apply(lambda x: [x.replace("\n", ",")])
            df.to_json(os.path.join('exports', name.replace("csv", "json")), orient='records', lines=False,
                       force_ascii=False)
        except:
            print(f"处理{name}失败...")
            continue
        # print(f"处理{name}完成...")
