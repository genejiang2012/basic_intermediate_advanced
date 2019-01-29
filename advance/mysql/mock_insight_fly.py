segmentList=[
    ['SG001', 10000],
    ['SG002', 10001]
]
tagList=[
    {
        'tagId':'FT001',
        'coverage':100000,
        'tagValueList':[
            ['FTV001',200],
            ['FTV002',1200],
            ['FTV003',2200],
            ['FTV004',3200],
            ['FTV005',4200]
        ]
    },
    {
        'tagId':'FT002',
        'coverage':300000,
        'tagValueList':[
            ['FTV006',200],
            ['FTV007',1200],
            ['FTV008',2200],
            ['FTV009',13200],
            ['FTV010',14200]
        ]
    }
]

def createSQL():
    sqlValuesList = []
    for i in range(len(segmentList)):
        for j in range(len(tagList)):
            segId = segmentList[i][0]
            segCoverage = segmentList[i][1]
            tagId = tagList[j]['tagId']
            tagCoverage = tagList[j]['coverage']
            for k in range(len(tagList[j]['tagValueList'])):
                tagOptionId = tagList[j]['tagValueList'][k][0]
                tagOptionCoverage = tagList[j]['tagValueList'][k][1]
                tagOptionCoveragePercent = float(tagList[j]['tagValueList'][k][1])/float(tagList[j]['coverage'])
                featureCoverage = int(segmentList[i][1]*tagOptionCoveragePercent)
                sqlValuesList.append("('"+str(tagId)+"','"+str(segId)+"','"+str(tagOptionId)+"','"+str(segCoverage)+"','"+str(segCoverage)+"','"+str(featureCoverage)+"','2018-03-23 00:00:00','2018-03-23 00:00:00','dmp_user@172.16.6.9')")
    print(','.join(sqlValuesList))


if __name__ == "__main__":
    print(createSQL())
