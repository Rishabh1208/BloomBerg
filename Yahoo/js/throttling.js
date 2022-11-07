function throttle(func, wait) {
  let waiting = false;
  let lastArgs = null;
  return function (...args) {
    if (!waiting) {
      func.apply(this, args);
      waiting = true;
      let timeout = () =>
        setTimeout(() => {
          waiting = false;
          if (lastArgs) {
            func.apply(this, lastArgs);
            waiting = true;
            lastArgs = null;
            timeout(); // Once you start the function I need to start the cooldown again.
          }
        }, wait);
      timeout();
    } else lastArgs = args; // we need to store the arguments of the function that are called within the waiting period.
  };
}
