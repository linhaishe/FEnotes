Quality Assurance with Chai notes

```js
 browser
          .fill('surname', 'Colombo')
          .pressButton('submit', function(){
            browser.assert.success();
            browser.assert.text('span#name', 'Cristoforo');
            browser.assert.text('span#surname', 'Colombo');
            browser.assert.element('span#dates', 1);
            done();   
          });
```

