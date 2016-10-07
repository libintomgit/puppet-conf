import subprocess

def execute(c):
	output="root a.txt 45\nmanju b.txt 2000\nDe v.txt 200"
 #o = subprocess.check_output(cmd)
	return output.split('\n')

def loaddata(o):
	fileinfo = []
	for line in o:
		column = line.split(' ')
		file = {'name': column[1], 'size':int(column[2])} 
		fileinfo.append(file)
	return fileinfo

def totalsize(f):
	total=0
	for line in f:
		total = total + line['size']
	return total

def main():
	outputt = execute(['a'])
	fileinfoo = loaddata(outputt)
	total = totalsize(fileinfoo)
	print fileinfoo

main()

#manjufile = filesby(fileinfo, 'Manju')

# import subprocess

# def execute(cmd):
#  output="root a.txt 45\nmanju b.txt 1000\nDe v.txt 200"
#  o = subprocess.check_output(cmd)
#  return output.split('\n')

# def loaddata(output):
#  fileinfo = []
#  for line in output:
#   column = line.split(' ')
#   file = {'name': column[1], 'size':int(column[2])} 
#   fileinfo.append(file)
#  return fileinfo

# def totalsize(fileinfo):
#   total=0
#   for file in fileinfo:
#     total = total + file['size']
#   return total

# def main():
#  output = execute(['ls', '-l'])
#  fileinfo = loaddata(output)
#  total = totalsize(fileinfo)
#  print total

# main()

#manjufile = filesby(fileinfo, 'Manju')
