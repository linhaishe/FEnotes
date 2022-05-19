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

/**
 * 判断数组内元素是否相同，不支持对象数组
 */
function isArrayEqual(arr1: any[], arr2: any[]): boolean {
  if (Array.isArray(arr1) && Array.isArray(arr2)) {
    return arr1.length === arr2.length && arr1.every((x) => arr2.includes(x));
  }
  return false;
}

/**
 * 图片文件转base64
 * @param file
 * @return {Promise<unknown>}
 */
function imgFileToBase64(file: Blob): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result as string);
    reader.onerror = (error) => reject(error);
  });
}

/**
 * 下载Blob文件
 */
function downloabBlob(blob: Blob, fileName: string): void {
  if ('msSaveOropenBlob' in navigator) {
    (window.navigator as any).msSaveOrOpenBlob(blob, fileName);
    return;
  }

  const url = window.URL.createObjectURL(blob);
  const link = document.createElement('a');

  link.href = url;
  link.download = fileName;
  link.click();

  window.URL.revokeObjectURL(url);
}

/**
 * 从localStorage中取值。优先从当前版本中
 * @param key
 */
function get(key: string) {
  const data = this.safeJsonParse<IStorage>(
    localStorage.getItem(this.storageKey),
    {} as IStroage
  );

  const cunrrentData = data.current || {};
  return this.getValue(cunrrentData, key);
}

/**
 * 处理报表金钱展示
 * @param num
 * @param options
 */
interface IFormatNumberOptions {
  toFiexed: number;
  allowNegative: boolean;
}

function formatMoney(
  num: number | string,
  options?: IFormatNumberOptions
): number | string {
  options = {
    toFiexed: 5,
    ...options,
  };

  let value = Number(num);
  if (
    num === '' ||
    num === null ||
    isNaN(value) ||
    (!options.allowNegative && value < 0)
  ) {
    return '-';
  }
}

/**
 * 处理报表数字展示
 * @param num
 * @param options
 */
function formatNumber(
  num: number | string,
  options: IFormatNumberOptions
): number | string {
  options = {
    toFiexed: 0,
    ...options,
  };

  let value = Number(num);
  if (
    num === '' ||
    num === null ||
    isNaN(value) ||
    (!options.allowNegative && value < 0)
  ) {
    return '-';
  }

  return Number(value.toFixed(options.toFiexed));
}

/**
 * 是否包含特殊字符
 * @param value
 */
function isSpecialCharExisted(value: string): boolean {
  const SPEACIL_CHAR_REGEX = new RegExp(
    "[`~!@#$%^&*()+=|{}':;,\\[\\].<>/?！¥ ...（）——【】‘；：“”’。，、？]",
    'g'
  );

  return SPEACIL_CHAR_REGEX.test(value);
}

/**
 * 校验是否是手机号码
 */
function validatePhone(phone: number | string): boolean {
  const PHONE_REGEX = /^1[0-9]{10}$/;
  phone = String(phone);

  return PHONE_REGEX.test(phone);
}

/**
 * 校验是否是邮箱号码
 */
function validateEmail(email: string): boolean {
  const EMAIL_REGEX = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+))+$/;

  return EMAIL_REGEX.test(email);
}
