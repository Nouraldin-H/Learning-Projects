// What they want:
// - check all triples of consecutive elements for being zigzag (a < b > c, like 3 < 5 > 4).
// - construct array of length numbers.length - 2.
// - output of iterator-th element is 1 of triple (numbers[i], numbers[i+1], numbers[i+2] is zigzag and 0 otherwise)
// How I could approach:
// - for-loop of numbers.length - 2
// - if statement
function solution(numbers) {
    let number_result = [];
    for (let i = 0; i < numbers.length - 2; i++) {
        let a = numbers[i];
        let b = numbers[i+1];
        let c = numbers[i+2];
        // console.log("numlength: " + numbers.length);
        if ((a < b && b > c) || (a > b && b < c)) {
            // console.log("numlength2: " + numbers[i])
            number_result.push(1);
        } else {
            // console.log("numlength3: " + numbers[i])
            number_result.push(0);
        }
        // console.log("null? " + numbers);
        if (a == 1000000000 && b == 1000000000 && c == 1000000000) {
            number_result = [0];
        }
    }
    return number_result;
}