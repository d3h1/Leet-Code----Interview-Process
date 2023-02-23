const nemo = ['Nemo']; // !Very quick, one loop

const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']; // !Still quick, 10 loops

const large = new Array(10000).fill('nemo'); // !This shows that bloat and lots of data needs different approaches in order to make it more efficient and SCALABLE hence big O

function findNemo(array) {
    let t0 = performance.now(); // This will measure performance -- How well the code performs -- The start of the timer

    for (let i = 0; i < array.length; i++) {
        if (array[i] ===  'nemo') {
            console.log('Found NEMO!');
        }
    }

    let t1 = performance.now(); // This will measure performance -- How well the code performs -- The end of the timer
    console.log('Call to find nemo took ' + (t1 - t0) + ' milliseconds')
}

findNemo(everyone);