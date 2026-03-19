#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

add(firstInt, secondInt);
