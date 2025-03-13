import json
file_path = r"C:\Users\erbat\OneDrive\Desktop\GitHub\PP2\Labs\Lab4\json\sample-data.json"
with open(file_path, "r") as jfile:
    x = json.load(jfile)

print("Interface Status")
print("="*81)
print(f'{"DN":<50} {"Description":<20} {"Speed":<8} {"MTU":<6}')
print("-"*50+" "+"-"*20+" "+"-"*8+" "+"-"*6)

for i in x["imdata"]:
    attributes = i['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '9150')
    print(f'{attributes["dn"]:<50} {attributes["descr"]:<20} {attributes["speed"]:<8} {attributes["mtu"]:<6}')