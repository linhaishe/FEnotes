npm notes 201027

### package.json file

This file lists the package dependencies for your project. Since npm packages are regularly updated, the `package.json` file allows you to set specific version numbers for each dependency. This ensures that updates to a package don't break your project.

储存关于你项目的信息。用single JSON的格式，键值对形式。只有两个必要的内容，是name 和 version.其余的值看情况添加。

Remember that you’re writing JSON, so all field names must use double-quotes (") and be separated with a comma (,).

name , verison , author , description , keywords , filed

<mark>author</mark> field , 记录项目作者，可以由string或object组成(object with contact or other details. An object is recommended for bigger projects,but simple string for small projects.

<mark>keywords</mark> filed : where you can describe your project using related keywords.

<mark>license</mark> filed : is where you inform users of what they are allowed to do with your project. Some common licenses for open source projects include MIT and BSD. License information is not required, and copyright laws in most countries will give you ownership of what you create by default. However, it’s always a good practice to explicitly state what users can and can’t do.

<mark>version</mark> filed : one of the required fields of your package.json file. This field describes the current version of your project.

<mark>dependencies</mark> filed(dependencies section): npm know exactly what your project needs from dependencies filed and automatically installs everything for you.

<mark>Versions</mark>

<mark>"package": "MAJOR.MINOR.PATCH"</mark>

example: "moment":"2.14.0"

- MAJOR version: should increment when you make incompatible API changes. 

- MINOR version: should 
- increment when you add functionality in a backwards-compatible manner. 

- PATCH version: should increment when you make backwards-compatible bug fixes. 

This means that PATCHes are bug fixes and MINORs add new features but neither of them break what worked before. Finally, MAJORs add changes that won’t work with earlier versions.

<mark>Tilde-Character ~</mark>:to Always Use the Latest Patch Version of a Dependency

**Note:** The version numbers themselves should not be changed.

```json
//how to allow updates to any 1.3.x version
"package": "~1.3.8"
//allow the latest 2.10.x version.
"moment":"~2.14.0"
```

<mark>Caret-Character ^ </mark>:allows npm to install future updates as well.The difference is that the caret will allow both MINOR updates and PATCHes.

```json
//allows npm to install to the latest 2.14.x version
"moment":"~2.14.0"
//allowed to update to any 2.x.x version.
"moment":"^2.14.0"
```

```json
{
	"name": "fcc-learn-npm-package-json",
	"author": "Heather",
	"description": "A project that does something awesome",
	"keywords": [ "test", "packagejason", "freecodecamp" ],
	"license": "MIT",
    "version": "1.2.0",
	"dependencies": {
		"express": "^4.14.0",
		"moment":"2.14.0"
	},
	"main": "server.js",
	"scripts": {
		"start": "node server.js"
	},
	"engines": {
		"node": "8.11.2"
	},
	"repository": {
		"type": "git",
		"url": "https://idontknow/todo.git"
	}
}
```

### package-lock.json file

保存小依赖的版本。package.json中保存主依赖的主版本。防止别人安装依赖的时候因为版本号的问题而不能运行文件。

### node_modules

These packages can be installed in two ways:

1. globally in a root node_modules folder, accessible by all projects.
2. locally within a project's own node_modules folder, accessible only to that project.

### Remove a Package from Your Dependencies

 just remove the corresponding key-value pair for that package from your dependencies.