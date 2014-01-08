def index():

    import os
    case_dir = os.path.join(request.folder,"static/case")
    case_list = os.listdir(case_dir)
    #TODO filter the test image dir
    #return len(case_list)
    for d in case_list:
        url_list=[ 'default/casepage/'+c for c in case_list]
    return dict(url_list=url_list)

def casepage():
    return 'the case:', request.args[0]

def showimg():
    import os
    img_dir = os.path.join("../static/case/case0/0001.bin.png")
    return dict(img_dir = img_dir)
