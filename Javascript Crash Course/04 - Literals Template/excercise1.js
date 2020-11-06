let firstName = "Carlos";
let lastName = "Quintero";

let fullName = `${firstName} ${lastName}`;
// console.log(fullName);

let searchResults = 2;
let output = `${ searchResults > 0 ? `${searchResults} results`: "No search results"}`
console.log(output)

// Separator

fruits = ["Apple", "Orange", "Guava", "Dragonfruit", "Banana"];

console.log("\n\nIteration classic way...\n");
for (let index = 0; index < fruits.length; index++){
    console.log(`a fruit could be...${fruits[index]}`);
}


console.log("\n\nIteration using FOR...\n");
for(let fruit of fruits){
    console.log(fruit);
}

console.log("\n\nIteration using MAP...\n");
var newFruits = fruits.map((fruit) => {
    console.log(fruit);
    return fruit;
})
console.log(newFruits);
console.log("NOTE: MAP can be used for returned a retouched array");

console.log("\n\nIteration using FOREACH...\n");
var newFruitsAgain = fruits.forEach((fruit) =>{
    console.log(fruit);
    return fruit;
})
console.log(newFruitsAgain);

console.log("\n\nReal world usage example...\n");

console.log("\n\nIteration using MAP...\n");
var newFruitsAA = fruits.map((fruit) => {
    console.log(fruit);
    return fruit;
}).filter((value) => {
    if (value == "Banana") {
        return false;
    } else {
        return true;
    }
})
console.log(newFruitsAA);
console.log("NOTE: Banana is NOT longer returned")