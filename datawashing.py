import json

fps = open('E:\\dataset\\annotations_trainval2017\\annotations\\instances_train2017.json', mode='r', encoding='utf-8')
data = json.load(fps)

# 去除无用的info字段和licenses字段
del data['info']
del data['licenses']
'''

'''
# 去除image中不必要的字段
for item in data['images']:
    del item['license']
    del item['coco_url']
    del item['date_captured']
    del item['flickr_url']
'''
'''
# 去除segmentation中不必要的字段
for item in data['annotations']:
    del item['segmentation']
    del item['area']
    del item['bbox']
    del item['iscrowd']



fpl = open('E:\\dataset\\annotations_trainval2017\\annotations\\test.json', mode='w', encoding='utf-8')
json.dump(data, fpl)
print('success!')

if __name__ == '__main__':
    pass