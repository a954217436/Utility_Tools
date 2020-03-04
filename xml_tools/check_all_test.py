import os
names=os.listdir('/home/dell/data/BZYB_selected_25/test/xml_all')
det_labels=['bj_bpps','jyz_lw',
'jyz_pl','sly_bjbmyw','sly_dmyw','jsxs','hxq_gjtps',
'xmbhyc','yw_gkxfw','yw_nc','mcqdmsh','gbps','gjptwss',
'bmwh','yxcr','wcaqm','wcgz','xy','bjdsyc','ywzt_yfyc','hxq_gjbs','ybh','ybf','bj_wkps','bj_bpmh']
dict={}
for name in names:
    name=name.split('|')
    name=name[1:-1]
    jiaoji=set(det_labels).intersection(set(name))
    print(jiaoji)
    for label_name in jiaoji:
        if (not label_name in dict) and (label_name in det_labels) :
            dict[label_name]=0
        if label_name in dict:
            dict[label_name]+=1

dict0=sorted(dict.items(),key=lambda x:x[1])
#print(dict)
for i,a in enumerate(dict0):
    print(i+1,a)

