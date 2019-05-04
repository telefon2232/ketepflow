import subprocess
def get_v():
    text=r'(cd /opt/openfoam-dev/src/transportModels/ && grep -Ril -E "public viscosityModel" | grep -v "lnInclude")'
    child = subprocess.Popen(text, stdout=subprocess.PIPE, shell=True)
    text = child.communicate()[0].decode('utf-8')
    return text