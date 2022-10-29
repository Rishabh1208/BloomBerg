# NodeJS Internals, libuv, event loop, process.nextTick and setImmediate.
# Callbacks, Promise Chaining, Multiple API calls in parallel, Async Await.
# SQL, NoSQL, Query Optimizations, types of Indexes in MongoDB, Replicaset, Sharding, Cache invalidation, In memory DBs, ELK
# How will you improve query performance ?
# Basic to intermediate Javascript questions like Closures, this keyword, callbacks.
# what is javascript object freeze ?

#callback

# A callback function is a function passed into another function as an argument, which is then invoked inside the outer 
# function to complete some kind of routine or action.

#callback hell -  complex nested callbacks
# promise chaining - you want to execute two or more related asynchronous operations, 
# where the next operation starts with the result from the previous step

# let p = new Promise((resolve, reject) => {
#     setTimeout(() => {
#         resolve(10);
#     }, 3 * 100);
# });

# p.then((result) => {
#     console.log(result); // 10
#     return result * 2;
# }).then((result) => {
#     console.log(result); // 20
#     return result * 3;
# }).then((result) => {
#     console.log(result); // 60
#     return result * 4;
# });

# Multiple API calls in parallel - Promise.all() , Promise.allSettled()

#Object.freeze() - The Object.freeze() method freezes an object. 
# Freezing an object prevents extensions and makes existing properties non-writable and non-configurable.
