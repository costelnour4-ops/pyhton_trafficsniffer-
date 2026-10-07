import json
def import_to_json(protocol, src_ip,src_port, dst_ip,dst_port):
    with open("data.json", "r") as fout:
        old_data=json.load(fout)
    
    x={
        "protocol":protocol,
        "src_ip":src_ip,
        "src_port":src_port,
        "dst_ip":dst_ip,
        "dst_port":dst_port
    }
    old_data.append(x)
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(old_data, f, indent=2)
        f.write("\n")

