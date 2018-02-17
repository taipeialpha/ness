# NESS - An open source finance platform

The goal of this project is going to provides a modularize framework, that user can customize platform with their own modules.

## Platform Architecture

The following figure describes the platform architecture of Ness:

![Platform Architecture of Ness](https://i.imgur.com/PVMCvtg.png)

The web framework is the core technology of this architecture. To serve end user, we provide front-end build with [Vue.js](https://vuejs.org/) which is a powerful javascript framework focus on the view of web.

The front-end is split from this project to a new project: [ness-ui](https://github.com/maple52046/ness-ui). So, in this document, we will focus on the backend part.

The backend server is RESTful server developed with [Node.js](https://nodejs.org/en/), provides API for front-end to fetch stock data, analysis stock, ... etc.

Currently, the backend server is generated by [Express](http://expressjs.com/) generator.
The code sturcture is look like the following figure:

![Code Structure of Ness](https://i.imgur.com/A8wxXaF.png)

In the root of source code, there are two important folder:

- **routes**
- **external_module**

The **"routes"** folder contains several js files, and these files contains **"routers"** those are used to handle user request.

The **"external_modules"** folder contains serval program, help backend to process stock data, like data analyzer and data loader.


## Developer

- [Ku Chen-Hao](https://maple52046.github.io) <[maple52046@gmail.com](mailto:maple52046@gmail.com)>
