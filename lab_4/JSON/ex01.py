import json
heading =  'Interface Status\n{}\n{:50} {:21} {:8} {:4}\n{} {}  {}  {}'.format('='*80, 'DM' ,'Description', 'Speed', 'MTU', '-'*50, '-'*20, '-'*6, '-'*6)
path = "C:/Users/User/Documents/PPSPRING/py/PP2_2024Spring-main/lab_4/JSON/sample-data.json"
with open(path) as f:
    main_data = json.load(f)
    print(heading)
    for i in main_data["imdata"]:
        mn = i["l1PhysIf"]["attributes"]
        print('{:50} {:20} {:8}  {}'.format(mn["dn"], mn["descr"], mn["speed"], mn["mtu"]))
