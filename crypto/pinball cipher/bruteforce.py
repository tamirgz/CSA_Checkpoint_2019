import os

for py in range(10):
	for px in range(7):
		for vy in ["+", "-"]:
			for vx in ["+", "-"]:
				print("running: ./pinball.elf transform msg.enc msg.dec %s %s %s %s" % (str(py), str(px), vy, vx))
				os.system("./pinball.elf transform msg.enc msg.dec %s %s %s %s" % (str(py), str(px), vy, vx))
				with open("msg.dec", "rb") as f:
					file_content = f.read()
					# import pdb; pdb.set_trace()
					print(file_content)
					if b'{' in file_content and b'}' in file_content and b'flag' in file_content:
						print("!!! WIN !!! ./pinball.elf transform test.enc msg.dec %s %s %s %s" % (str(py), str(px), vy, vx))
						exit()
