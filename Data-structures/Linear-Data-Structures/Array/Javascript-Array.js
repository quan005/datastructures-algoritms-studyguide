// intializing an Array
let array = [1,2,3,4,5];

// ---- Array Operations ---- //

// Traverse
for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}



// Insert
array.push(6)
console.log(array);


// ---- Delete ----
// Delete the last item
array.pop()
console.log(array);

// Delete the first item
array.shift()
console.log(array);

// Delete an element by index
array.splice(0,1)
console.log(array);



// Search
let array1 = [3,7,42,33]
let found = array1.find(function(element) {
    return element > 33;
});

console.log(found);

// Update
array[1] = 'B';
console.log(array)

// ---- Language Specific Operations ---- //