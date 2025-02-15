# read the Irish Rail API and print train information

import requests
import csv
from xml.dom.minidom import parseString

url = 'https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML'
page = requests.get(url)
doc = parseString(page.content)

# make an array for tags
retriveTags = ['TrainStatus',
               'TrainLatitude',
               'TrainLongitude',
               'TrainCode',
               'TrainDate',
               'PublicMessage',
               'Direction']

# sanity check
# print(doc.toprettyxml())

# write to a file
# with open("data/train.xml", "w") as xmlfp:
#     doc.writexml(xmlfp)

# open a csv file
with open("data/train_nodes_with_D.csv", mode="w", newline="") as train_file:
    train_writer = csv.writer(train_file, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName('objTrainPositions')
    for objPositionsNode in objTrainPositionsNodes:
    # TrainLatitudeNode = objPositionsNode.getElementsByTagName('TrainLatitude').item(0)
    # TrainLatitude = TrainLatitudeNode.firstChild.nodeValue.strip()
        trainCodeNode = objPositionsNode.getElementsByTagName('TrainCode').item(0)
        trainCode = trainCodeNode.firstChild.nodeValue.strip()
        # trainCode check
        if trainCode.startswith('D'):
            dataList = []
            for retriveTag in retriveTags:
                retriveNode = objPositionsNode.getElementsByTagName(retriveTag).item(0)
                dataList.append(retriveNode.firstChild.nodeValue.strip())
            train_writer.writerow(dataList)

        