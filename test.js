function Dog(name, breed, color) {
  this.name = name;
  this.breed = breed;
  this.color = color;
}

Dog.prototype.bark = function () {
  console.log("wohhoo!!!");
};
