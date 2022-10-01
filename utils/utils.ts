type ObjectType = 'number' | 'string' | 'null' | 'undefined' | 'object' | 'array' | 'date' | 'error' | 'promise'

function getType(obj: any): ObjectType {
    const type : string = Object.prototype.toString.call(obj).toLocaleLowerCase();
    // @ts-ignore: Object is possibly 'null'.
    return type.match(/\[object\s(\w+)\]/)[1] as ObjectType;
}

/**
 * 深拷贝对象或数组
 * @param src
 * @param dest
 * @returns
 */

function deepCopy<T>(src: T, dest?: T): T {
    if (!src) {
        return src;
    }

    if (!dest) {
        dest = Array.isArray(src) ? [] : {} as any;
    }

    for (const key of Object.keys(src as any)) {
        const type = getType((src as any)[key]);

        if (type === 'object' || type === 'array') {
            if (!(dest as any)[key]) {
                (dest as any)[key] = type === 'array' ? [] : {};
            }

            deepCopy((src as any)[key], (dest as any)[key]);
        } else {
            (dest as any)[key] = (src as any)[key]
        }
    }

    return (dest as any);
}

const e = [1,2,3,4,5];
const f = deepCopy(e);
console.log(f);
console.log(e === f);

const deepClone = (obj: any) => {
  if (obj === null) return null;
  let clone = { ...obj };
  Object.keys(clone).forEach(
    (key) =>
    (clone[key] =
      typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  // @ts-ignore
    return Array.isArray(obj) && obj.length
        // @ts-ignore
    ? (clone.length = obj.length) && Array.from(clone)
    : Array.isArray(obj)
            // @ts-ignore
      ? Array.from(obj)
      : clone;
};

const a: any[] = [1, 2, 3];
const b = [...a];
const x = a
b[0] = 'motify';
console.log('a', a);
console.log('b', b);
console.log('a === b', a === b);
console.log('a === x', a === x);

const c = {
    name: 'hahaha',
    age: 9,
    family: {
        dad: 'jack',
        mom: 'julie'
    }
};
const d = { ...c };
const e = c;
const f = {
    name: 'hahaha',
    age: 9,
}
const g = {...f}
console.log(c);
console.log(d);
console.log(c === d);
console.log(c === e);
d.name = 'dname' // c.name 未修改
d.family.dad = 'patric'; // c.family.dad 被修改
console.log('ccc', c);
console.log('ddd', d);

g.name = 'gogogo';
console.log('ffff', f);
// sum 拓展运算符可深可浅拷贝

const h = {};
const y = {};
console.log('99', h === y);


const deepClone3 = (obj: any) => {
    if (obj === null) return null;
    let clone = { ...obj };
    Object.keys(clone).forEach(
        (key) =>
            (clone[key] =
                typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
    );
    return Array.isArray(obj) && obj.length
        ? (clone.length = obj.length) && Array.from(clone)
        : Array.isArray(obj)
            ? Array.from(obj)
            : clone;
};



