const boxes = [0,1,2,3,4,5];

function logFirstTwoBoxes(boxes) {
    console.log(boxes[0]); // O(1)
    console.log(boxes[1]); // O(1)
}

logFirstTwoBoxes(boxes); //O(2) -- Still constant time and the fastest operation that can happen -- We would round this down and explain it as CONSTANT TIME or O(1)