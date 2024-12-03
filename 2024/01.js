const fs = require("node:fs");

fs.readFile("./inputs/input_01.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const leftList = [];
  const rightList = [];

  const lines = data.split("\r").map((l) => l.replace("\n", ""));

  lines.forEach((line) => {
    const [leftEntry, rightEntry] = line.split("   ");
    leftList.push(parseInt(leftEntry));
    rightList.push(parseInt(rightEntry));
  });

  leftList.sort();
  rightList.sort();

  let distance = 0;

  leftList.forEach((number, i) => {
    distance += Math.abs(rightList[i] - number);
  });
});
