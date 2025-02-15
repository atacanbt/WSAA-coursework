# reads xml from a file and prints it
# Author: atacan buyuktalas

from xml.dom.minidom import parse

filename = 'data/employee.xml'

# read file in two ways
doc = parse(filename)
# or
# with open(filename) as fp:
#     doc = parse(fp)

employeeNodeList = doc.getElementsByTagName('Employee')
print(len(employeeNodeList), 'employees found')
for employeeNode in employeeNodeList:
    firstNameNode = employeeNode.getElementsByTagName('FirstName').item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print(firstName)
