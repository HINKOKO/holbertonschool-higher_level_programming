#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
// parseInt function => second argument '10' specifies radix (math base)
add(parseInt(process.argv[2], 10), parseInt(process.argv[3], 10));
