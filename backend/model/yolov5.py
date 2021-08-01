import torch

model = torch.hub.load("ultralytics/yolov5", "custom", path="./model/best.pt")


def yolov5(img):
    results = model(img)

    coordinate = {}
    names = results.names
    if results.pred is not None:
        pred = results.pred[0]
        if pred is not None:
            for item in pred:
                item_name = names[int(item[-1])]
                if item_name in coordinate:
                    coordinate[item_name].append(item[:-1].tolist())
                else:
                    coordinate[item_name] = [item[:-1].tolist()]

    return coordinate
