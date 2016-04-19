import cv2
import numpy as np

def read(imagePath):
    """
    type: string => array[array[float]]
    Read image data as grayscale.
    """
    return cv2.imread(imagePath, 0)
    
def resize(img, mat=(-1, -1)):
    """
    type: (array[array[float]], (int, int)) => array[array[(float)]]
    img: Matrix of original image.
    mat: Size of new matrix.
    If mat is default((-1, -1)), resize is not done.
    """
    if mat == (-1, -1):
        return img
    
    return cv2.resize(img, (mat[0], mat[1]))

def write(img, imagePath):
    """
    type: (array[array[float]], string) => Boolean
    """
    return cv2.imwrite(imagePath, img)
    
def writeList(img, path):
    """
    type: (array[array[float]], string) => Boolean
    """
    strOut = ""
    img_l = img.tolist()
    for line in img_l:
        strOut += str(line)
        if not line == len(img)-1:
            strOut += "\n"
    try:
        f = open(path, "w")
        f.write(strOut)
        f.close()
        return True
    except:
        return False

def threshold(image, t=-1):
    """
    type: array[array[float]] => array[array[float]]
    Do threshold using Otsu's algorism.
    If t is None, through input image.
    If t is -1, use Otsu's algorism.
    In other case, do threshold using t as threshold number.
    """

    if t==None:
        return image

    # make histogram(intensity-number)
    maxIntensity = 255
    hist = [0 for i in range(maxIntensity + 1)]
    for y in range(len(image)):
        for x in range(len(image[y])):
            hist[image[y][x]] += 1
    
    # find best threshold
    if t==-1:
        maxScore = [0, 0]
        for t in range(1,len(hist)):
            c1 = hist[0:t]
            c2 = hist[t:len(hist)]
            w1 = len(c1)
            w2 = len(c2)
            m1 = np.mean(np.array(c1)).tolist()
            m2 = np.mean(np.array(c2)).tolist()
            sigma = w1 * w2 * pow(m1 - m2, 2)
            #print("w1:" + str(w1) + ", w2:" + str(w2) + ", m1:" + str(m1) + ", m2:" + str(m2))
            if sigma > maxScore[0]:
                maxScore[0] = sigma
                maxScore[1] = t
                #print("sigma:" + str(sigma) + ", t:" + str(t))
        threshold = maxScore[1]
        #print("threshold:" + str(threshold))
    else:
        threshold = t

    # execute threshold
    res = [[0 for x in range(len(image[y]))] for y in range(len(image))]
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] >= threshold: res[y][x] = 255
            else: res[y][x] = 0

    return np.array(res)

def divideRect(img, rowNum, colNum):
    """
    Divide rect image to rowNum * colNum new image.
    """
    res = []
    rowDiv = len(img)/rowNum
    colDiv = len(img[0])/colNum
    for rn in range(rowNum):
        mat = []
        for cn in range(colNum):
            matRow = []
            for row in range(rowDiv):
                matCol = []
                for col in range(colDiv):
                    matCol.append(img[rn*rowDiv+row][cn*colDiv+col])
                    #print img[rn*rowDiv+row][cn*colDiv+col]
                matRow.append(matCol)
            mat.append(matRow)
        res.append(mat)
    return res

if __name__ == "__main__":
    h = threshold(read("input/face_car_butterfly/test/test0.jpg"), t=-1)
    write(h, "buf.jpg")
    writeList(h, "buf.txt")
    """
    h = threshold(read("img/numbers.jpg"), t=10)
    print np.array(h)
    d = divideRect(h, 7, 10)
    for i in range(7):
        for j in range(10):
            writeList(d[i][j], "img/numbers/numbers_" + str(j) + str(i) + ".txt")
    print("finish.")
    """

