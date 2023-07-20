# 导入 os
import os
# 导入 pandas 用于处理表格内容
import pandas as pd

if __name__ == '__main__':

    # 原词库地址
    dict_path = "dicts"
    # 导出地址
    export_path = "exports"
    # 遍历词库内容，拿到每一个词库的名字
    for name in os.listdir(dict_path):
        # print(f"开始处理{name}...")
        # 读取csv 文件
        df = pd.read_csv(os.path.join(dict_path, name), header=None)
        # 修改列名为原项目需要格式
        df.columns = ['name', 'trans']
        # print(df.shape)
        try:
            # 删除\n替换为,
            df['trans'] = df['trans'].apply(lambda x: [x.replace("\n", ",")])
            # 导出到新的文件中
            df.to_json(os.path.join('exports', name.replace("csv", "json")), orient='records', lines=False,
                       force_ascii=False)
        except:
            print(f"处理{name}失败...")
            continue
        # print(f"处理{name}完成...")
