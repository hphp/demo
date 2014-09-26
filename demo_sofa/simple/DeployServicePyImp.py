import sys
import sofa

class DeployServicePyImp:
    MODULE='pyimp.OnlineDeployService.ver_1_0_0'
    IMPLEMENTS=['OnlineDeployService.ver_1_0_0.OpenPlatDeployService']

    def __init__(self, conf):
        sofa.use('OnlineDeployService.ver_1_0_0')

    def Deploy(self, info):
        return "[test] Hello from " + info.prodID;

