import pyperclip
import math
transZCount = 0
baseleafLayers = 12
base2leafLayers = 6
stack1Layers = 100
stack2Layers = 0
base2layerStart = 150
base2layerEnd = 85
header = """
body {
  margin: 0;
	padding: 0;
	box-sizing: border-box;
	display: flex;
	justify-content: center;
	align-items: center;
	min-height: 100vh;
	background: #f6d7b0;
	perspective: 3200px;
}

.burj_container {
	position: relative;
	width: 400px;
	height: 100px;
	transform-style: preserve-3d;
	animation: animate 30s linear infinite;
}

@keyframes animate {
	0% {
		transform: rotateX(10deg) rotateY(0deg);
	}
	50% {
		transform: rotateX(-80deg) rotateY(180deg);
	}
  100% {
		transform: rotateX(10deg) rotateY(360deg);
	}
}

@keyframes top {
	0% {
		transform: rotateX(-90deg) rotateY(0deg);
	}
  100% {
		transform: rotateX(-90deg) rotateY(360deg);
	}
}

.leaf {
  position: absolute;
  width: 300px;
  height: 150px;
  border-radius: 0 90% 90% 00% / 0 50% 50% 0;
}

.leafB2 {
  position: absolute;
  width: 300px;
  height: 150px;
  border-radius: 0 90% 90% 00% / 0 50% 50% 0;
}
"""
output = header
total_leaf_layers = baseleafLayers * 3 + base2leafLayers * 3 + stack1Layers * 3 + stack2Layers * 3
for i in range(0, baseleafLayers * 3):
    output += "#L" + str(i) + " {\n"
    if i%3 == 0:
        output += f"  transform: rotateX(90deg) translateX(150px) translateZ({5 * transZCount}px);\n"
    elif i%3 == 1:
        output += f"  transform: rotateX(90deg) rotateZ(120deg) translateX(150px) translateZ({5 * transZCount}px);\n"
    else:
        output += f"  transform: rotateX(90deg) rotateZ(240deg) translateX(150px) translateZ({5 * transZCount}px);\n"
        transZCount += 1
    output += f"  background-color: rgb({int(255 - (255 * (i / total_leaf_layers)))}, {int(255 - (255 * (i / total_leaf_layers)))}, {int(255 - (255 * (i / total_leaf_layers)))});\n"
    output += "}\n"
    
moveInAmount = 0
for i in range(0, base2leafLayers * 3):
    output += "#LB2" + str(i) + " {\n"
    if i%3 == 0:
        output += f"  transform: rotateX(90deg) translateX({int(base2layerStart)}px) translateZ({5 * transZCount}px);\n"
        output += f"  width: {int((base2layerStart - moveInAmount) * 2)}px;\n"
        output += f"  height: {int(base2layerStart - moveInAmount)}px;\n"
    elif i%3 == 1:
        output += f"  transform: rotateX(90deg) rotateZ(120deg) translateX({base2layerStart * (((base2layerStart - moveInAmount)) / 150)}px) translateY({math.cos(math.degrees(60)) * int(base2layerStart) * (((base2layerStart - moveInAmount)) / 150) - (base2layerStart * math.cos(math.degrees(60)))}px) translateZ({5 * transZCount}px);\n"
        output += f"  width: {int((base2layerStart - moveInAmount) * 2)}px;\n"
        output += f"  height: {int(base2layerStart - moveInAmount)}px;\n"
    else:
        output += f"  transform: rotateX(90deg) rotateZ(240deg) translateX({base2layerStart * (((base2layerStart - moveInAmount)) / 150)}px) translateY({(base2layerStart * math.cos(math.degrees(60))) - math.cos(math.degrees(60)) * int(base2layerStart) * (((base2layerStart - moveInAmount)) / 150)}px) translateZ({5 * transZCount}px);\n"
        output += f"  width: {int((base2layerStart - moveInAmount) * 2)}px;\n"
        output += f"  height: {int(base2layerStart - moveInAmount)}px;\n"
        transZCount += 1
        moveInAmount += (base2layerStart - base2layerEnd) / base2leafLayers
    output += f"  background-color: rgb({int(255 - (255 * ((i + baseleafLayers * 3) / total_leaf_layers)))}, {int(255 - (255 * ((i + baseleafLayers * 3) / total_leaf_layers)))}, {int(255 - (255 * ((i + baseleafLayers * 3) / total_leaf_layers)))});\n"
    output += "}\n"
    
# Start of stack:
for i in range(0, stack1Layers * 3):
    output += "#S1" + str(i) + " {\n"
    if i%3 == 0:
        output += f"  transform: rotateX(90deg) translateX({int(base2layerStart)}px) translateZ({5 * transZCount}px);\n"
        output += f"  width: {int((base2layerStart - moveInAmount) * 2)}px;\n"
        output += f"  height: {int(base2layerStart - moveInAmount)}px;\n"
    elif i%3 == 1:
        output += f"  transform: rotateX(90deg) rotateZ(120deg) translateX({base2layerStart * (((base2layerStart - moveInAmount)) / 150)}px) translateY({math.cos(math.degrees(60)) * int(base2layerStart) * (((base2layerStart - moveInAmount)) / 150) - (base2layerStart * math.cos(math.degrees(60)))}px) translateZ({5 * transZCount}px);\n"
        output += f"  width: {int((base2layerStart - moveInAmount) * 2)}px;\n"
        output += f"  height: {int(base2layerStart - moveInAmount)}px;\n"
    else:
        output += f"  transform: rotateX(90deg) rotateZ(240deg) translateX({base2layerStart * (((base2layerStart - moveInAmount)) / 150)}px) translateY({(base2layerStart * math.cos(math.degrees(60))) - math.cos(math.degrees(60)) * int(base2layerStart) * (((base2layerStart - moveInAmount)) / 150)}px) translateZ({5 * transZCount}px);\n"
        output += f"  width: {int((base2layerStart - moveInAmount) * 2)}px;\n"
        output += f"  height: {int(base2layerStart - moveInAmount)}px;\n"
        transZCount += 1
    output += f"  background-color: rgb({int(255 - (255 * ((i + baseleafLayers * 3 + base2leafLayers * 3) / total_leaf_layers)))}, {int(255 - (255 * ((i + baseleafLayers * 3 + base2leafLayers * 3) / total_leaf_layers)))}, {int(255 - (255 * ((i + baseleafLayers * 3 + base2leafLayers * 3) / total_leaf_layers)))});\n"
    output += "}\n"
    
# Move stack in:
moveInAmount = 0

base3LayerStart = base2layerEnd
base3LayerEnd = base3LayerStart - 20
print(base2layerStart, base2layerEnd, base3LayerStart, base3LayerEnd)
for i in range(0, stack2Layers * 3):
    output += "#S2" + str(i) + " {\n"
    if i%3 == 0:
        output += f"  transform: rotateX(90deg) translateX({int(base3LayerStart)}px) translateZ({5 * transZCount}px);\n"
        output += f"  width: {int((base3LayerStart - moveInAmount) * 2)}px;\n"
        output += f"  height: {int(base3LayerStart - moveInAmount)}px;\n"
    elif i%3 == 1:
        output += f"  transform: rotateX(90deg) rotateZ(120deg) translateX({base3LayerStart * (((base3LayerStart - moveInAmount)) / 150)}px) translateY({math.cos(math.degrees(60)) * int(base3LayerStart) * (((base3LayerStart - moveInAmount)) / 150) - (base3LayerStart * math.cos(math.degrees(60)))}px) translateZ({5 * transZCount}px);\n"
        output += f"  width: {int((base3LayerStart - moveInAmount) * 2)}px;\n"
        output += f"  height: {int(base3LayerStart - moveInAmount)}px;\n"
    else:
        output += f"  transform: rotateX(90deg) rotateZ(240deg) translateX({base3LayerStart * (((base3LayerStart - moveInAmount)) / 150)}px) translateY({(base3LayerStart * math.cos(math.degrees(60))) - math.cos(math.degrees(60)) * int(base3LayerStart) * (((base3LayerStart - moveInAmount)) / 150)}px) translateZ({5 * transZCount}px);\n"
        output += f"  width: {int((base3LayerStart - moveInAmount) * 2)}px;\n"
        output += f"  height: {int(base3LayerStart - moveInAmount)}px;\n"
        transZCount += 1
        moveInAmount += (base3LayerStart - base2layerEnd) / stack2Layers
    output += f"  background-color: rgb({int(255 - (255 * ((i + baseleafLayers * 3 + base2leafLayers * 3 + stack1Layers * 3) / total_leaf_layers)))}, {int(255 - (255 * ((i + baseleafLayers * 3 + base2leafLayers * 3 + stack1Layers * 3) / total_leaf_layers)))}, {int(255 - (255 * ((i + baseleafLayers * 3 + base2leafLayers * 3 + stack1Layers * 3) / total_leaf_layers)))});\n"
    output += "}\n"

# copy the output to the clipboard

pyperclip.copy(output)

input("Ready for HTML?")
output2 = """<body>
    <div class="burj_container">
"""
for i in range(0, baseleafLayers * 3):
    output2 += f'        <div id="L{i}" class="leaf"></div>\n'
    
for i in range(0, base2leafLayers * 3):
    output2 += f'        <div id="LB2{i}" class="leafB2"></div>\n'
for i in range(0, stack1Layers * 3):
    output2 += f'        <div id="S1{i}" class="leafB2"></div>\n'
for i in range(0, stack2Layers * 3):
    output2 += f'        <div id="S2{i}" class="leafB2"></div>\n'

output2 += """    </div>
</body>
"""
pyperclip.copy(output2)
