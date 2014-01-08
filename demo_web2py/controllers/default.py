
def index():
    import os
    case_dir = os.path.join(request.folder,"static/case")
    case_list = os.listdir(case_dir)
    #return len(case_list)
    url_list=[]
    for t in case_list:
        if t=='test_images':
            continue
        url_list.append((t,'default/casepage/'+t))
    return dict(url_list=url_list)


def casepage():
    import os
    #case_dir = os.path.join(request.folder,"static/case")
    orig_img_url= 'http://'+request.env.http_host+'/'+request.application+"/static/case/"+request.args[0]+"/0001.nrm.png"
    bin_img_url= 'http://'+request.env.http_host+'/'+request.application+"/static/case/"+request.args[0]+"/0001.bin.png"
    seg_img_url= 'http://'+request.env.http_host+'/'+request.application+"/static/case/"+request.args[0]+"/0001.showseg.png"
    return dict(orig_img_url= orig_img_url,bin_img_url=bin_img_url,seg_img_url=seg_img_url)


