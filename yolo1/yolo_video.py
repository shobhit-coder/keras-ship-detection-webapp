import sys
import argparse
from yolo1.yolo import YOLO, detect_video
from PIL import Image
from argparse import Namespace
import cv2

def detect_img(yolo,filename,filepath):
   
    #img = input('Input image filename:')
    imgname = filename
    img = "static/uploads/"+imgname 
    try:
        print(img)
        image = Image.open(img)
    except Exception as e:
        print(e)
        print('Open Error! Try again!')
        #continue
    else:
        r_image = yolo.detect_image(image)
        #cv2.imwrite("static/uploads/predicted/predicted_"+imgname,r_image)
        r_image.save("static/predicted/predictedyolo_"+imgname)
        #r_image.show()
        
    yolo.close_session()

FLAGS = None

def runmodel(filename,filepath=""):
    # class YOLO defines the default value, so suppress any default here
    #parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    # parser.add_argument(
    #     '--model', type=str,
    #     help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    # )

    # parser.add_argument(
    #     '--anchors', type=str,
    #     help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    # )

    # parser.add_argument(
    #     '--classes', type=str,
    #     help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    # )

    # parser.add_argument(
    #     '--gpu_num', type=int,
    #     help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    # )

    # parser.add_argument(
    #     '--image', default=False, action="store_true",
    #     help='Image detection mode, will ignore all positional arguments'
    # )
    # '''
    # Command line positional arguments -- for video detection mode
    # '''
    # parser.add_argument(
    #     "--input", nargs='?', type=str,required=False,default='./path2your_video',
    #     help = "Video input path"
    # )

    # parser.add_argument(
    #     "--output", nargs='?', type=str, default="",
    #     help = "[Optional] Video output path"
    # )

    #FLAGS = parser.parse_args()

    FLAGS = Namespace(image = "True")

    #print(FLAGS)

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)),filename,filepath)
    elif "input" in FLAGS:
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
