import dlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() #뷰티gan이 tf v1에서 만들어진 거라서
import numpy as np

def align_faces(img, detector, sp) : #이미지 정렬 함수
    dets = detector(img, 1)
    objs = dlib.full_object_detections()
    for detection in dets :
        s = sp(img, detection)
        objs.append(s)
    faces = dlib.get_face_chips(img, objs, size=256, padding=0.35)
    return faces

detector = dlib.get_frontal_face_detector() #얼굴만 찾아줌
sp = dlib.shape_predictor('./models/shape_predictor_5_face_landmarks.dat')

test_img = dlib.load_rgb_image('./imgs/02.jpg')
test_faces = align_faces(test_img, detector, sp)
fig, axes = plt.subplots(1, len(test_faces)+1, figsize=(20,16))
axes[0].imshow(test_img)
for i, face in enumerate(test_faces):
    axes[i+1].imshow(face)

plt.show()


"""
얼굴 인식

img = dlib.load_rgb_image('./imgs/12.jpg')
plt.figure(figsize=(16,10))
plt.imshow(img)
plt.show()

img_result = img.copy()
dets = detector(img) #얼굴의 좌표를 만들어준다
if len(dets) == 0 :
    print('cannot find faces!')
else :
    fig, ax = plt.subplots(1, figsize=(16,10))
    for det in dets :
        x, y, w, h = det.left(), det.top(), det.width(), det.height() #왼쪽, 위, 폭, 높이 좌표가 있음
        rect = patches.Rectangle((x,y),w,h, linewidth=2, edgecolor='r', facecolor='none') # 네모 그렸을 때 선 두께, 색, 내부 채우기 색
        ax.add_patch(rect)
    ax.imshow(img_result)
    plt.show()

fig, ax = plt.subplots(1, figsize=(16,10))
objs = dlib.full_object_detections()
for detection in dets :
    s = sp(img,detection) #학습된 모델
    objs.append(s)
    for point in s.parts() :
        circle = patches.Circle((point.x, point.y),radius=3, edgecolor='r',facecolor='r')
        ax.add_patch(circle)
ax.imshow(img_result)
#plt.show()

faces = dlib.get_face_chips(img, objs, size=256, padding=0.3) #패딩이 얼굴 부분 확대 0이면 얼굴만 보여줌
fig, axes = plt.subplots(1, len(faces)+1, figsize=(20,16))
axes[0].imshow(img)

for i, face in enumerate(faces) :
    axes[i+1].imshow(face)
plt.show()
"""