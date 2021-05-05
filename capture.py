import cv2 
import dropbox 
import time 
import random 
start_time=time.time()
def takesnap():
    number=random.randint(0,20)
    vedio_obj=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vedio_obj.read()
        print(ret)
        print(frame)
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshot taken")
    vedio_obj.release()
    cv2.destroyAllWindows()


def upload_files(img_name):
    access_token="sl.AwLDrBi0wxzaqqQatIuEK0X6Tyg5ZAFSHJydZswtRcPLPtsWKhc-DG_zXDTrj7z8C6LqBCSOo7jjPF9Y1YElHwLtIkInvaNbiTNl2OJld14sqeeusjmbLtL-NIlXmZd0mFNYezU"
    file=img_name
    file_from=file
    file_to="/images/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode('overwrite'))
        print("file uploaded")



def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=takesnap()
            upload_files(name)
main()
