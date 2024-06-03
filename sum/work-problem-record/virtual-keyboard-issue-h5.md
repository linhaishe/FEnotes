# 软件盘唤起样式错乱

问题一：在安卓机中，软键盘的唤起会影响样式布局，如何处理这样的情况。参考了spotify的解决方案，即，在用户点击手机界面内除了搜索框的位置后，立刻隐藏软件盘。

问题二：安卓手机底部导航固定，但是软件盘唤起后，底部导航被顶起。

```css
@media (min-aspect-ratio: 13/20) {
  .button {
    display: none;
  }
}
```

# refs:

1. https://blog.csdn.net/qq_16122415/article/details/84834633
2. https://blog.csdn.net/yiguoxiaohai/article/details/125872156
3. https://blog.51cto.com/u_16175454/6685183
4. https://cloud.tencent.com/developer/ask/sof/922765
5. https://blog.csdn.net/xialong_927/article/details/92628634
6. https://www.cnblogs.com/520BigBear/p/12395042.html
7. https://blog.csdn.net/weixin_43797908/article/details/123900633?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-123900633-blog-105369392.235%5Ev40%5Epc_relevant_anti_t3_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-123900633-blog-105369392.235%5Ev40%5Epc_relevant_anti_t3_base&utm_relevant_index=5
8. https://cloud.tencent.com/developer/article/2267778
9. https://juejin.cn/post/7090422631521845262
10. https://www.cnblogs.com/xiahj/p/8036419.html
11. https://segmentfault.com/a/1190000021328403
12. https://blog.csdn.net/weixin_44883460/article/details/103062634
13. https://www.cnblogs.com/xiaozhumaopao/p/16348136.html
14. https://juejin.cn/post/7200653914818986043
15. https://juejin.cn/post/6961757804491178014
16. https://segmentfault.com/a/1190000037607005


# keywords:

virtual keyboard body scroll h5，软键盘唤起后样式错乱的问题，安卓软键盘，h5，ios橡皮筋效果