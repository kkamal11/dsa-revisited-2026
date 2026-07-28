/*
If you add a custom method to an array, JavaScript gives that 
method access to the array it was called on through 'this'.
*/

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
    if (!Array.isArray(this)) {
        return
    }
    const obj = {}
    for (const elem of this) {
        const key = fn(elem)
        if (obj[key] != undefined) {
            obj[key].push(elem)
        }
        else {
            obj[key] = [elem]
        }
    }
    return obj
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */