import{n as a,_ as o}from"./index.973f68ef.js";import{a as r}from"./axios.8446186b.js";const i={components:{SideBar:()=>o(()=>import("./SideBar.2c755222.js"),["assets/SideBar.2c755222.js","assets/index.973f68ef.js","assets/index.bd4a1d26.css","assets/ArticleCreation.74d07ca5.js","assets/axios.8446186b.js","assets/ArticleCreation.6a9131dd.css","assets/SideBar.18c159be.css"])},name:"axios-category",mounted(){const t={Accept:"application/json"};r.get("http://localhost:8083/getAllCategories",{headers:t}).then(e=>{this.responseData=e.data,console.log(this.responseData),console.log("CCCCC")}).catch(e=>{console.error("Error fetching data:",e)})},methods:{validate(){this.$refs.form.validate()},reset(){this.$refs.form.reset()},resetValidation(){this.$refs.form.resetValidation()}}};var n=function(){var e=this,s=e._self._c;return s("main",{staticClass:"editing"},[s("side-bar"),s("div",{staticClass:"main-container"}),s("div",{staticClass:"side-container"},[s("h2",[e._v("Categories")]),s("div",[e.responseData?s("div",[e._v(" "+e._s(e.responseData)+" ")]):s("div",[e._v("Loading...")])])])],1)},_=[],d=a(i,n,_,!1,null,"048175d9",null,null);const m=d.exports;export{m as default};
