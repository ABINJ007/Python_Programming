import json
with open("014_file_handling/Serialization/serialize.txt","a+") as f:
    l=["Akash","Bhoomi","Agni","vaayu","Neera"]

    jstr=json.dumps(l)
    f.write(jstr)
