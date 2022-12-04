const fs = require("fs");

const sol = () => {
  let res1 = 0,
    res2 = 0;
  const lines = fs.readFileSync("input.txt").toString().split("\n");
  for (const line of lines) {
    const [start1, end1, start2, end2] = line.replace(",", "-").split("-");
    if (
      (+start1 >= +start2 && +end1 <= +end2) ||
      (+start2 >= +start1 && +end2 <= +end1)
    )
      res1++;
    if (
      (+start1 >= +start2 && +start1 <= +end2) ||
      (+start2 >= +start1 && +start2 <= +end1)
    )
      res2++;
  }
  return [res1, res2];
};

console.log(sol());
