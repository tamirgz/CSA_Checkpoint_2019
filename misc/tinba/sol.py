import pandas as pd
from IPy import IP

def match(src_ip, dst_ip, ip):
    ips = IP("%s-%s" % (src_ip, dst_ip))
    if ip in ips:
        # import pdb; pdb.set_trace()
        return True
    return False

data = pd.read_csv('fw.log', delimiter='\t', skiprows=1, names = ['time_stamp', 'src_ip', 'dst_ip'])
data['time_stamp'] = pd.to_datetime(data['time_stamp'])

bolivia_ips = pd.read_csv('bo.csv', delimiter=',', names = ['From IP', 'To IP', 'Total IPs', 'Assign Date'])

src_reduced = []
dst_reduced = []
src_unique = []
dst_unique = []
total_rows = data.shape[0]
idx = 0

for row in data.iterrows():
    print("analyzing %d/%d" % (idx, total_rows))
    idx += 1
    hour = row[1]["time_stamp"].time().hour
    if hour >= 6 and hour <= 18: # check the hours
        # src_ip_tocheck = row[1]["src_ip"]
        dst_ip_tocheck = row[1]["dst_ip"]
        src_found = False
        dst_found = False
        # for ip in src_unique:
        #     if src_ip_tocheck == ip:
        #         src_found = True
        #         src_reduced.append(row)
        for ip in dst_unique:
            if dst_ip_tocheck == ip:
                dst_found = True
                dst_reduced.append(row)

        if dst_found or src_found:
            continue

        # if src_found == False:
        #     src_unique.append(src_ip_tocheck)
        if dst_found == False:
            dst_unique.append(dst_ip_tocheck)

        for ip_range in bolivia_ips.iterrows():
            from_ip = ip_range[0]
            to_ip = ip_range[1]["From IP"]

            # if match(from_ip, to_ip, src_ip_tocheck):
            #     src_reduced.append(row)
            if match(from_ip, to_ip, dst_ip_tocheck):
                dst_reduced.append(row)

print(src_reduced)
print(dst_reduced)