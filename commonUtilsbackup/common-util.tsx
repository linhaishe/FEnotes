function getValue(obj: { [key: string]: any }, key: string | string[]): any {
  if (!Array.isArray(key)) {
    // 如果不是数字，是字符串，则分离，拿到字符串
    key = String(key).split('.');
  }

  if (key.length === 0 || !obj) {
    // 如果是数组，但长度为0，或不是对象
    return undefined;
  }

  // 如果是数组且有长度，那么就拿到第一个元素，为'',则删除第一个元素
  const cunrrentKey = key.shift();

  if (key.length === 0) {
    return obj[cunrrentKey];
  }

  return getValue(obj[cunrrentKey], key);
}

/**
 * 是否仅为字母和数字的组合
 * @param value
 */

function isNumOrLetter(value: string): boolean {
  return new RegExp('^[0-9a-zA-Z]+$|^\\*{6}$|^$').test(value);
}

/**
 * 是否为字母、数字和特殊字符的组合
 */

function isNumOrLetterOrSpecialChar(value: string): boolean {
  return new RegExp(
    '^[0-9a-zA-Z`~!@#$%^&*()_=+|;:;<.>\\[\\]\'"?/{}\\\\-]+$|^\\*{6}$|^$'
  ).test(value);
}

/**
 * 安全解析JSON字符串
 * @param text 待解析字符串
 * @param defaultValue 解析失败时的默认值，默认为null
 */
function safeJsonParse<T = any>(text: string, defaultValue: T = null): T {
  try {
    if (
      text === null ||
      text === undefined ||
      typeof text !== 'string' ||
      text === ''
    ) {
      return defaultValue;
    }
    return JSON.parse(text) || defaultValue;
  } catch (e) {
    console.error('JSON.parse failed:', e);
    return defaultValue;
  }
}

/**
 * 复制内容到剪贴板
 * @param content 复制的内容
 */

async function copyContent(content: string) {
  try {
    await navigator.clipboard.writeText(content);
    console.log('复制成功');
  } catch {
    console.log('复制失败');
  }
}

/**
 * promise 节流
 */
function throttlePromise<T>(fn: T): T {
  let promise = null;
  return (async (...args) => {
    try {
      if (promise === null) {
        promise = (fn as any)(...args);
      }
      return await promise;
    } finally {
      promise = null;
    }
  }) as any;
}
