function a() {
  let b = 10;
  function c() {
    console.log(b);
  }
  return c;
}

let test = a();
test();
