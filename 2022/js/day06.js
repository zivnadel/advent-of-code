const fs = require("fs");

const sol = (len) => {
  const seq = fs.readFileSync("input.txt").toString().trim();
  for (let i = 0; i < seq.length; i++) {
    if (new Set(seq.substring(i, i + len)).size === len) return i + len;
  }
};

console.log(sol(4), sol(14));
