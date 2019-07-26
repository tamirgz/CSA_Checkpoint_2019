import pandas as pd
from IPy import IP

def match(src_ip, dst_ip, ip):
    ips = IP("%s-%s" % (src_ip, dst_ip))
    if ip in ips:
        # import pdb; pdb.set_trace()
        return True
    return False

data = pd.read_csv('fw_small.log', delimiter='\t', skiprows=1, names = ['time_stamp', 'src_ip', 'dst_ip'])
data['time_stamp'] = pd.to_datetime(data['time_stamp'])

bolivia_ips = pd.read_csv('bo.csv', delimiter=',', names = ['From IP', 'To IP', 'Total IPs', 'Assign Date'])

src_reduced = []
dst_reduced = []
src_unique = []
dst_unique = []
num_src = 0
num_dst = 0
total_rows = data.shape[0]
idx = 0

for row in data.iterrows():
    print("analyzing %d/%d" % (idx, total_rows))
    idx += 1
    hour = row[1]["time_stamp"].time().hour
    if hour >= 6 and hour <= 18: # check the hours
        src_ip_tocheck = row[1]["src_ip"]
        dst_ip_tocheck = row[1]["dst_ip"]
        src_found = False
        dst_found = False
        for ip in src_unique:
            if src_ip_tocheck == ip:
                # import pdb; pdb.set_trace()
                src_found = True
                src_reduced.append(row)
                num_src += 1
        for ip in dst_unique:
            if dst_ip_tocheck == ip:
                # import pdb; pdb.set_trace()
                dst_found = True
                dst_reduced.append(row)
                num_dst += 1

        if dst_found or src_found:
            continue

        if src_found == False:
            src_unique.append(src_ip_tocheck)
            # import pdb; pdb.set_trace()
        if dst_found == False:
            dst_unique.append(dst_ip_tocheck)
            # import pdb; pdb.set_trace()

        for ip_range in bolivia_ips.iterrows():
            from_ip = ip_range[0]
            to_ip = ip_range[1]["From IP"]

            if match(from_ip, to_ip, src_ip_tocheck):
                src_reduced.append(row)
                num_src += 1
            if match(from_ip, to_ip, dst_ip_tocheck):
                dst_reduced.append(row)
                num_dst += 1

# print(src_reduced)
print("num_src: %d" % num_src)
with open("src.txt", "w+") as f:
    for ele in src_reduced:
        f.write(str(ele) + "\n")

# print(dst_reduced)
print("num_dst: %d" % num_dst)
with open("dst.txt", "w+") as f:
    for ele in dst_reduced:
        f.write(str(ele) + "\n")