let name = {
  firstName: "Rishabh",
  lastName: "Singhal",
};

let printName = function (hometown, state, country) {
  console.log(
    this.firstName + " " + this.lastName + " ," + hometown,
    state,
    country
  );
};

let printMyName = printName.bind(name, "Kota", "Rajashthan");
printMyName("India");

// Polyfill for Bind()
Function.prototype.myBind = function (...args) {
  let func = this; // Function
  params = args.splice(1);
  console.log("splice", params);
  return function (...args1) {
    func.apply(args[0], [...params, ...args1]);
  };
};

let printMyName2 = printName.myBind(name, "Kota", "Rajasthan");
printMyName2("India");
