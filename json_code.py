import json
json_list=[]
with open("s3.json", "r") as json_file:
    in_data = json.load(json_file)
    for i in in_data["Records"]:
    	json_list.append(i["s3"]["bucket"]["arn"])
print(json_list)

'''
Output
['arn:aws:s3:::mybucket']
'''