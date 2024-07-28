import cv2
import json

annotations = []

def find_closest_annotation(x, y, max_distance=10):
    closest_distance = float('inf')
    closest_index = -1
    for i, annotation in enumerate(annotations):
        ax, ay = annotation['point']
        distance = (ax - x) ** 2 + (ay - y) ** 2
        if distance < closest_distance:
            closest_distance = distance
            closest_index = i
            
    if closest_distance <= max_distance ** 2:
        return closest_index
    return -1

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            closest_index = find_closest_annotation(x, y)
            if closest_index != -1:
                current_label = annotations[closest_index]['label']
                print(f"Current label: {current_label}")
                new_label = input(f"Enter new label for point ({annotations[closest_index]['point']}): ")
                annotations[closest_index]['label'] = new_label

                refresh_image()
        else:
            label = input(f"Enter label for point ({x}, {y}): ")
            b, g, r = img[y, x]
            annotations.append({'point': (x, y), 'label': label, 'rgb': (int(r), int(g), int(b))})

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, label, (x, y), font, 0.5, (0, 255, 0), 1)
            cv2.imshow('image', img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        b, g, r = img[y, x]
        print(f"Color at ({x}, {y}): B={b}, G={g}, R={r}")

def refresh_image():
    global img
    img = cv2.imread('man.jpg', 1)
    for annotation in annotations:
        x, y = annotation['point']
        label = annotation['label']
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, label, (x, y), font, 0.5, (0, 255, 0), 1)
    cv2.imshow('image', img)

def save_annotations(filename):
    with open(filename, 'w') as file:
        json.dump(annotations, file)
    print(f"Annotations saved to {filename}")

def save_image(filename):
    cv2.imwrite(filename, img)
    print(f"Annotated image saved to {filename}")

if __name__ == "__main__":

    img = cv2.imread('man.jpg', 1)

    cv2.imshow('image', img)

    cv2.setMouseCallback('image', click_event)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

    save_annotations('annotations.json')
    save_image('annotated_image.jpg')
