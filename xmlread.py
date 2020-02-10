import xml.etree.ElementTree as ET

xml_file = "C:/Users/p746309/Desktop/Complete_Workspace.xml"

tree = ET.parse(xml_file)
root = tree.getroot()

for job in root.findall("./FOLDER/JOB"):
    jobname = job.get('JOBNAME')
    for subjob in job.iter('SHOUT'):
        message = subjob.get('MESSAGE')
    if not 'ORDERID' in message:
        print(jobname+', None')
    else:
        print(jobname+','+message)