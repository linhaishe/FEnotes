// tabs is an array of titles of each site open within the window
var Window = function(tabs) {
  this.tabs = tabs; 
  // we keep a record of the array inside the object
  //意思是将array放在一个对象里，this.tabs是object？，tabs是array?哪个是object?哪个是array?
  //为什么不直接写 this.tabs = [];?
};
console.log(Window)

// When you join two windows into one window
Window.prototype.join = function (otherWindow) {
  this.tabs = this.tabs.concat(otherWindow.tabs);
  return this;
  //这里的this.tabs 指的是构造函数function(tabs){}里的this.tabs吗？
  //return this 的 this 返回的是什么？ 
};

// When you open a new tab at the end
Window.prototype.tabOpen = function (tab) {
  this.tabs.push('new tab'); // let's open a new tab for now
  return this;
};

// When you close a tab
Window.prototype.tabClose = function (index) {

  // Only change code below this line

  var tabsBeforeIndex = this.tabs.splice(0, index); // get the tabs before the tab
  var tabsAfterIndex = this.tabs.splice(1); // get the tabs after the tab

  this.tabs = tabsBeforeIndex.concat(tabsAfterIndex); // join them together

  // Only change code above this line

  return this;
 };

// Let's create three browser windows
var workWindow = new Window(['GMail', 'Inbox', 'Work mail', 'Docs', 'freeCodeCamp']); 
// Your mailbox, drive, and other work sites
var socialWindow = new Window(['FB', 'Gitter', 'Reddit', 'Twitter', 'Medium']); 
// Social sites
var videoWindow = new Window(['Netflix', 'YouTube', 'Vimeo', 'Vine']); 
//  Entertainment sites

// Now perform the tab opening, closing, and other operations
var finalTabs = socialWindow
                    .tabOpen() // Open a new tab for cat memes
                    .join(videoWindow.tabClose(2)) // Close third tab in video window, and join
                    .join(workWindow.tabClose(1).tabOpen());
console.log(finalTabs.tabs);
