var projects = [
  
  {
    id: 2,
    name: "The LOTRY App",
    isActive: false,
  },
  {
    id: 3,
    name: "Time Tracker",
    isActive: true,
  },
  {
    id: 4,
    name: "Payroll Runner",
    isActive: true,
  },
  {
    id: 5,
    name: "Kodiak",
    isActive: false,
  },
  {
    id: 6,
    name: "Project Blue Book",
    isActive: false,
  },
  {
    id: 7,
    name: "X Lab",
    isActive: true,
  },
  {
    id: 8,
    name: "Manhattan Project",
    isActive: true,
  },
  {
    id: 1,
    name: "Refactor Main Web App",
    isActive: false,
  },
];

const arr = projects.filter((obj) => obj.isActive == true);
arr.sort((a, b) => a.id - b.id);
res.send(arr)
console.log("arr", arr);
