docker stop mongo_py_sdk
docker rm mongo_py_sdk
docker run --name mongo_py_sdk -v /home/core/python_sdk:/work -it mongo_py_sdk

