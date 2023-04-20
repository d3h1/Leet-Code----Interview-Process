const nemo = ['Nemo']; // !Very quick, one loop >> O(1)

const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']; // !Still quick, 10 loops >> O(10)

const large = new Array(10000).fill('nemo'); // !A lot slower at 10,000 loops >> O(10000)



function findNemo(array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] ===  'nemo') {
            console.log('Found NEMO!');
        }
    }
}

findNemo(everyone); // !This function is O(n) -- big O of n. LINEAR TIME
// n in O(n) is basically arbitrary as anything can be used in its place but n is used for the usual computer science practice

// With the numbers above: O(1), O(10), O(10000) -- As inputs increase, the number of operations grow // !LINEARLY with it

// *This is linear time -- Number of elements increases while number operations also increases at the same pace, meaning it is O(n).

// ?The big "O" depends on the number "n" of inputs -- Basic explanation

// O(n) is the most common notation -- it is a fair performance compared to others


// ! BIG O DOES NOT MEASURE THINGS IN SECONDS, RATHER, IN HOW QUICKLY RUN TIMES GROW -- size of input and compare to number of operations that increase -- SCALABILITY 







