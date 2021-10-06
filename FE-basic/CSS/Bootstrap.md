Bootstrap will figure out how wide your screen is and respond by resizing your HTML elements - hence the name responsive design.

With responsive design, there is no need to design a mobile version of your website. It will look good on devices with screens of any width.

You can add Bootstrap to any app by adding the following code to the top of your HTML:

```html
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"/> 

<link href="https://fonts.googleapis.com/css?family=Lobster" rel="stylesheet" type="text/css">
```

### Bootstrap Grid

Bootstrap uses a responsive 12-column grid system, which makes it easy to put elements into rows and specify each element's relative width. Most of Bootstrap's classes can be applied to a `div` element. 

Bootstrap's `col-md-*` class. Here, `md` means medium, and `*` is a number specifying how many columns wide the element should be. In this case, the column width of an element on a medium-sized screen, such as a laptop, is being specified.

In the Cat Photo App that we're building, we'll use `col-xs-*`, where `xs` means extra small (like an extra-small mobile phone screen), and `*` is the number of columns specifying how many columns wide the element should be.

```html
/***
*每行/列以12为单位进行分割，每个都要有div
*加起来等于12
*
*/
<div class="row">
    <div class="col-xs-4">
      <button class="btn btn-block btn-primary">Like</button>
    </div>
    <div class="col-xs-4">
      <button class="btn btn-block btn-info">Info</button>
    </div>
    <div class="col-xs-4">
      <button class="btn btn-block btn-danger">Delete</button>
    </div>
  </div>
```

```html
<div class="row">
  <div class="col-xs-8">
  <h2 class="text-primary text-center">CatPhotoApp</h2>
  </div>
<div class="col-xs-4">
  <a href="#"><img class="img-responsive thick-green-border" src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>
  </div>
</div>
```

###  Font Awesome

Font Awesome is a convenient library of icons. These icons can be webfonts or vector graphics. These icons are treated just like fonts. You can specify their size using pixels, and they will assume the font size of their parent HTML elements. 

```html
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
```

 Font Awesome classes to the `i` element to turn it into an icon 

` <i class="fas fa-info-circle"></i> `

```html
 <div class="row">
    <div class="col-xs-4">
      <button class="btn btn-block btn-primary"><i class="fas fa-thumbs-up"></i> Like</button>
    </div>
    <div class="col-xs-4">
      <button class="btn btn-block btn-info"><i class="fas fa-info-circle"></i>Info</button>
    </div>
    <div class="col-xs-4">
      <button class="btn btn-block btn-danger"><i class="fas fa-trash"></i>Delete</button>
    </div>
  </div>
```

## Radio Buttons, form

```html
<div class="row">
      <div class="col-xs-6">
        <label><input type="radio" name="indoor-outdoor"> Indoor</label>
      </div>
      <div class="col-xs-6">
        <label><input type="radio" name="indoor-outdoor"> Outdoor</label>
      </div>
</div>
```



























