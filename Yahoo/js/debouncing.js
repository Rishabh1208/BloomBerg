function debounce(func, wait) {
  let timerId = null; // allocating a scope for the timerid variable
  return function (...args) {
    clearTimeout(timerId); // reseting the timer means it is cancelling the previous timer.
    timerId = setTimeout(() => func.apply(this, args), wait); // it will call the function after some time
  };
}
// But let's say that the visitor keeps writing, so each key release triggers the debounce again.
// Every invocation needs to reset the timer, or, in other words, cancel the previous plans with saveInput(),
// and reschedule it for a new time—300 ms in the future. This goes on as long as the visitor keeps hitting
// the keys under 300 ms.

// The last schedule won’t get cleared, so the saveInput() will finally be called.

// Each scroll or each release will trigger the debounce again and again.\
// Every invocation needs to reset the timer and reschedule it for a new time let'say say 300 ms in the fture.
// This goes on and on as long as user keeps scrolling or hitting the keys under 300ms
// and the last scheduled won't get cleared and finally the fn() will get called.

// The debounce is a special function that handles two tasks:

// Allocating a scope for the timer variable
// Scheduling your function to be triggered at a specific time

function sayHello() {
  console.log("My name is", this.name);
}

const amy = {
  name: "amy",
  speak: debounce(sayHello),
};

amy.speak();
