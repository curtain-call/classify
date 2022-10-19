import torch.cuda
from flask_cors import cross_origin
import os
from flask import Flask,request
from werkzeug.datastructures import FileStorage
from main import test
import transjson

base = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
# 随服务器ip地址变化，前端需要修改请求发送的dest
@cross_origin()
def get_data():
    for i in range(20):
        file = request.file.get(str(i)+".jpg")
        if file:
            FileStorage(file).save(base + "/images/" +str(i) + ".jpg")

    torch.cuda.empty_cache()
    print(test(test_data_root=base + "/images/"))
    json_data = transjson.transjson(("./submission.csv"))
    return json_data


if __name__ == "__main__":
    app.run()