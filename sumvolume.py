import subprocess
import os
handle = open("inputpdb.txt","r")

volume_dict = {}
group_num = 1

#Read in each group of protein files
for line in handle:
	line = line.strip()
	pdbids = line.split(",")

	#compute volume for each protein in the group
	for id in pdbids:
		id = id.strip()
		pdbid = id + ".pdb"
		val = subprocess.check_call("./3vvolume.sh '%s'" % pdbid, shell=True)

	#compute individual protein volume and its sum
	handle2 = open("3vvolumelog.txt","r")
	
	protein_dict = {}
	volume_sum = 0
	for line in handle2:
		info = line.split()
		#read the pdb id of the information
		if len(info) == 1:
			info= info[0]
			proteinid = info[:4]
		else:
			volume = float(info[2])
			protein_dict[proteinid]=volume
			volume_sum+=volume
	protein_dict["sum"] = volume_sum
	group_id = "group "+str(group_num)
	volume_dict[group_id] = protein_dict

	handle2.close()
	os.remove("3vvolumelog.txt")
	group_num+=1

handle.close()


print(volume_dict)




