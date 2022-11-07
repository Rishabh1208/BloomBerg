// sum(1)(2)(3)(4)

// with normal functions
function sum(a) {
  return function (b) {
    return function (c) {
      return function (d) {
        return a + b + c + d;
      };
    };
  };
}

// with arrow functions
const sum = (a) => (b) => (c) => (d) => a + b + c + d;

console.log(sum(1)(2)(3)(4));
