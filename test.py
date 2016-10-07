import subprocess

# def libin(a,b):
# 	add = a+b
# 	return (add)
# print libin(1,2)

def execute():
 	output=subprocess.check_output(['du'])
 	#"root a.txt 45\nmanju b.txt 2000\nDe v.txt 200"
 	#o = subprocess.check_output(cmd)
 	#return output.split('\n')
 	return (output)
print execute()

def split(output):
	fileinfo = []
	for line in output:
		column = line.split(' ')
		file = {'name': column[1], 'size':int(column[0])}
		fileinfo.append(file)
	return fileinfo
print split(execute)