########## Wrote by Mehrshad! ##########
import json

defaultFilePath = ''


def read_from(fileName: str, get_keys=False):
    global defaultFilePath

    if len(fileName) > 5:
        if fileName[-5:] != '.json':
            fileName += '.json'
    else:
        fileName += '.json'

    if defaultFilePath != '':
        if defaultFilePath[-1] != '/':
            defaultFilePath += '/'
        fileName = defaultFilePath+fileName

    try:
        with open(fileName) as json_file:
            data = json.load(json_file)

        if get_keys:
            return data, list(data.keys())
        return data
    except:
        return


def write_to(fileName: str, data: dict, indent=4, sort_keys=True):
    global defaultFilePath

    if len(fileName) > 5:
        if fileName[-5:] != '.json':
            fileName += '.json'
    else:
        fileName += '.json'

    if defaultFilePath != '':
        if defaultFilePath[-1] != '/':
            defaultFilePath += '/'
        fileName = defaultFilePath+fileName

    try:
        with open(fileName, 'w') as json_file:
            json.dump(data, json_file, indent=indent, sort_keys=sort_keys)
        return 'done!'
    except:
        return
