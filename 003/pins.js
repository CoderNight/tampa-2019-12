const not = (digit, possibilities) => {
    return possibilities.every(p => p !== digit);
};

const possibilities = (digit) => {
    if (digit === '0') return ['0', '8'];
    if (digit === '8') return ['8', '7', '5', '9', '0'];

    const asNumber = parseInt(digit);
    const numbers = [asNumber];
    if (not(digit, ['1', '2', '3'])) {
        numbers.push(asNumber - 3);
    }
    if (not(digit, ['7', '9'])) {
        numbers.push(asNumber + 3);
    }
    if (not(digit, ['1', '4', '7'])) {
        numbers.push(asNumber - 1);
    }
    if (not(digit, ['3', '6', '9'])) {
        numbers.push(asNumber + 1);
    }
    return numbers.map(n => n.toString());
};

function getPINs(observed) {
    const digits = observed.split('');
    const options = digits.map(d => possibilities(d));
    let entries = options.shift();
    while (options.length > 0) {
        const working = [];
        const next = options.shift();
        for (let entry of entries) {
            for (let nextEntry of next) {
                working.push(entry.concat(nextEntry));
            }
        }
        entries = working;
    }
    return entries;
}
