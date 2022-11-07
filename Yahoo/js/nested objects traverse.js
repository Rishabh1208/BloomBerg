// let obj = {
//   name: "raj",
//   roll: 892,
//   id: {
//     idName: "raj",
//   },
//   section: {
//     sectionName: "raj",
//     alias: {
//       name: "raj",
//     },
//   },
// };

let obj1 = {
  node: "node1",
  children: [
    {
      node: "node2",
      children: [
        {
          node: "node3",
        },
      ],
    },
  ],
};

function test(obj, node) {
  let flag = false;
  if (obj["node"] == node) {
    return true;
  } else {
    if (obj["children"]) {
      for (let child of obj["children"]) {
        flag = test(child, node);
        if (flag == true) {
          break;
        }
      }
    }
  }
  return flag;
}

console.log(test(obj1, "node0"));

// let changeName = (obj) => {
//   for (let i in obj) {
//     if (obj[i] == "raj") {
//       obj[i] == "abhishek";
//     } else {
//       changeName(obj[i]);
//     }
//   }
// };

// changeName(obj);

// console.log(obj);
