System.register(["./index-legacy.b48dc4a7.js","./ArticleCreation-legacy.12992df6.js","./axios-legacy.268bd2b7.js"],(function(e,t){"use strict";var a,i,n=document.createElement("style");return n.textContent="*[data-v-c3661b5a]{margin:5px;padding:10px}.main[data-v-c3661b5a]{width:100%;height:600px;display:flex;justify-content:space-around}.main-container[data-v-c3661b5a]{width:50%;height:70%;background-color:#fff;border-radius:10px}.main-container h2[data-v-c3661b5a]{border-top:solid 1px black;border-bottom:solid 1px black}.main-container[data-v-c3661b5a],.cover-image[data-v-c3661b5a]{height:80%}.cover-image img[data-v-c3661b5a]{display:block;margin:auto;justify-content:center;height:600px;width:auto;background-color:#000}.main-container-btn[data-v-c3661b5a]{display:flex;justify-content:space-between}.side-container[data-v-c3661b5a]{border-radius:10px;width:20%;height:70%;background-color:#c1e2f4}*[data-v-fdeb8d63]{margin:5px;padding:10px}.main[data-v-fdeb8d63]{width:100%;height:600px;display:flex;justify-content:space-around}.main-container[data-v-fdeb8d63]{width:50%;height:70%;background-color:#fff;border-radius:10px}.main-container h2[data-v-fdeb8d63]{border-top:solid 1px black;border-bottom:solid 1px black}.main-container[data-v-fdeb8d63],.cover-image[data-v-fdeb8d63]{height:80%}.cover-image img[data-v-fdeb8d63]{display:block;margin:auto;justify-content:center;height:600px;width:auto;background-color:#000}.main-container-btn[data-v-fdeb8d63]{display:flex;justify-content:space-between}.side-container[data-v-fdeb8d63]{border-radius:10px;width:20%;height:70%;background-color:#c1e2f4}*[data-v-e6b428e8]{margin:5px;padding:10px}.main[data-v-e6b428e8]{width:100%;height:600px;display:flex;justify-content:space-around}.main-container[data-v-e6b428e8]{width:50%;height:70%;background-color:#fff;border-radius:10px}.main-container h2[data-v-e6b428e8]{border-top:solid 1px black;border-bottom:solid 1px black}.main-container[data-v-e6b428e8],.cover-image[data-v-e6b428e8]{height:80%}.cover-image img[data-v-e6b428e8]{display:block;margin:auto;justify-content:center;height:600px;width:auto;background-color:#000}.main-container-btn[data-v-e6b428e8]{display:flex;justify-content:space-between}.side-container[data-v-e6b428e8]{border-radius:10px;width:20%;height:70%;background-color:#c1e2f4}*[data-v-a61fbebc]{margin:5px;padding:10px}.main[data-v-a61fbebc]{width:100%;height:600px;display:flex;justify-content:space-around}.main-container[data-v-a61fbebc]{width:50%;height:70%;background-color:#fff;border-radius:10px}.main-container h2[data-v-a61fbebc]{border-top:solid 1px black;border-bottom:solid 1px black}.main-container[data-v-a61fbebc],.cover-image[data-v-a61fbebc]{height:80%}.cover-image img[data-v-a61fbebc]{display:block;margin:auto;justify-content:center;height:600px;width:auto;background-color:#000}.main-container-btn[data-v-a61fbebc]{display:flex;justify-content:space-between}.side-container[data-v-a61fbebc]{border-radius:10px;width:20%;height:70%;background-color:#c1e2f4}.scheduling-form[data-v-df78152a],.scheduling-form[data-v-7739c199]{max-width:600px;margin:auto}\n",document.head.appendChild(n),{setters:[function(e){a=e.n},function(e){i=e.default},function(){}],execute:function(){var t=a({name:"ArticleApproved",data:function(){return{}}},(function(){return this._self._c,this._m(0)}),[function(){var e=this._self._c;return e("main",{staticClass:"home"},[e("h1",[this._v("List of Approved Articles")]),e("div",{staticClass:"main"})])}],!1,null,"c3661b5a",null,null).exports,n=a({name:"ArticleApproved",data:function(){return{}}},(function(){return this._self._c,this._m(0)}),[function(){var e=this._self._c;return e("main",{staticClass:"home"},[e("h1",[this._v("List of Rejected Articles")]),e("div",{staticClass:"main"})])}],!1,null,"fdeb8d63",null,null).exports,l=a({data:function(){return{valid:!0,name:"",nameRules:[function(e){return!!e||"Name is required"},function(e){return e&&e.length<=10||"Name must be less than 10 characters"}],email:"",emailRules:[function(e){return!!e||"E-mail is required"},function(e){return/.+@.+\..+/.test(e)||"E-mail must be valid"}],select:null,items:["Item 1","Item 2","Item 3","Item 4"],checkbox:!1}},methods:{validate:function(){this.$refs.form.validate()},reset:function(){this.$refs.form.reset()},resetValidation:function(){this.$refs.form.resetValidation()}}},(function(){var e=this,t=e._self._c;return t("main",{staticClass:"editing"},[t("v-container",[t("h2",[e._v("Create a Magazine")]),t("div",{staticClass:"article-form"},[t("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:e.valid,callback:function(t){e.valid=t},expression:"valid"}},[t("v-text-field",{attrs:{label:"Magazine ID"},model:{value:e.mag_id,callback:function(t){e.mag_id=t},expression:"mag_id"}}),t("v-text-field",{attrs:{label:"Magazine title"},model:{value:e.mag_title,callback:function(t){e.mag_title=t},expression:"mag_title"}}),t("v-select",{attrs:{article_num:e.article_num,label:"Number of articles"}}),t("v-file-input",{attrs:{"show-size":"",label:"Article cover image"}}),t("v-btn",{staticClass:"primary"},[e._v("submit")])],1)],1)])],1)}),[],!1,null,null,null,null).exports,c=a({name:"ArticleApproved",data:function(){return{}}},(function(){return this._self._c,this._m(0)}),[function(){var e=this._self._c;return e("main",{staticClass:"home"},[e("h1",[this._v("List of All Articles")]),e("div",{staticClass:"main"})])}],!1,null,"e6b428e8",null,null).exports,s=a({name:"ArticleApproved",data:function(){return{}}},(function(){return this._self._c,this._m(0)}),[function(){var e=this._self._c;return e("main",{staticClass:"home"},[e("h1",[this._v("List of Articles to Check")]),e("div",{staticClass:"main"})])}],!1,null,"a61fbebc",null,null).exports,r=a({data:function(){return{valid:!0,mag_id:"",mag_title:"",selectedDay:null,selectedMonth:null,selectedYear:null,selectedHour:null,selectedMinutes:null,selectedSeconds:null,items_d:["1","2","3","4","5","6","7","8","9","10"],items_m:["January","February","March","April","May","June","July","August","September","October","November","December"],items_y:["2022","2023","2024"],items_h:Array.from({length:24},(function(e,t){return"".concat(t)})),items_ms:Array.from({length:60},(function(e,t){return"".concat(t)})),items_s:Array.from({length:60},(function(e,t){return"".concat(t)})),dayPicker:!1}},methods:{validate:function(){this.$refs.form.validate()},reset:function(){this.$refs.form.reset()},resetValidation:function(){this.$refs.form.resetValidation()}}},(function(){var e=this,t=e._self._c;return t("main",{staticClass:"editing"},[t("v-container",[t("h2",[e._v("Create a Schedule")]),t("div",{staticClass:"scheduling-form"},[t("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:e.valid,callback:function(t){e.valid=t},expression:"valid"}},[t("v-text-field",{attrs:{label:"Magazine ID"},model:{value:e.mag_id,callback:function(t){e.mag_id=t},expression:"mag_id"}}),t("v-text-field",{attrs:{label:"Magazine Title"},model:{value:e.mag_title,callback:function(t){e.mag_title=t},expression:"mag_title"}}),t("v-row",[t("v-col",{attrs:{cols:"4"}},[t("v-menu",{attrs:{"close-on-content-click":!1,transition:"scale-transition","offset-y":""},scopedSlots:e._u([{key:"activator",fn:function(a){var i=a.on;return[t("v-text-field",e._g({attrs:{label:"Day",readonly:""},model:{value:e.selectedDay,callback:function(t){e.selectedDay=t},expression:"selectedDay"}},i))]}}]),model:{value:e.dayPicker,callback:function(t){e.dayPicker=t},expression:"dayPicker"}},[t("v-date-picker",{model:{value:e.selectedDay,callback:function(t){e.selectedDay=t},expression:"selectedDay"}})],1)],1),t("v-col",{attrs:{cols:"4"}},[t("v-select",{attrs:{items:e.items_m,label:"Month"},model:{value:e.selectedMonth,callback:function(t){e.selectedMonth=t},expression:"selectedMonth"}})],1),t("v-col",{attrs:{cols:"4"}},[t("v-select",{attrs:{items:e.items_y,label:"Year"},model:{value:e.selectedYear,callback:function(t){e.selectedYear=t},expression:"selectedYear"}})],1)],1),t("v-row",[t("v-col",{attrs:{cols:"4"}},[t("v-select",{attrs:{items:e.items_h,label:"Hour"},model:{value:e.selectedHour,callback:function(t){e.selectedHour=t},expression:"selectedHour"}})],1),t("v-col",{attrs:{cols:"4"}},[t("v-select",{attrs:{items:e.items_ms,label:"Minutes"},model:{value:e.selectedMinutes,callback:function(t){e.selectedMinutes=t},expression:"selectedMinutes"}})],1),t("v-col",{attrs:{cols:"4"}},[t("v-select",{attrs:{items:e.items_s,label:"Seconds"},model:{value:e.selectedSeconds,callback:function(t){e.selectedSeconds=t},expression:"selectedSeconds"}})],1)],1)],1)],1)])],1)}),[],!1,null,"df78152a",null,null).exports,o=a({data:function(){return{valid:!0,mag_id:"",mag_title:"",selectedMagazine:null,selectedDate:null,selectedTime:null,magazines:["Magazine A","Magazine B","Magazine C","Magazine D"],timeOptions:["08:00 AM","09:00 AM","10:00 AM","11:00 AM","12:00 PM","01:00 PM","02:00 PM","03:00 PM"],datePicker:!1}},methods:{validate:function(){this.$refs.form.validate()},reset:function(){this.$refs.form.reset()},resetValidation:function(){this.$refs.form.resetValidation()}}},(function(){var e=this,t=e._self._c;return t("main",{staticClass:"editing"},[t("v-container",[t("h2",[e._v("Reschedule a Magazine")]),t("div",{staticClass:"scheduling-form"},[t("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:e.valid,callback:function(t){e.valid=t},expression:"valid"}},[t("v-select",{attrs:{items:e.magazines,label:"Scheduled Magazine(s)"},model:{value:e.selectedMagazine,callback:function(t){e.selectedMagazine=t},expression:"selectedMagazine"}}),t("v-text-field",{attrs:{label:"Magazine ID"},model:{value:e.mag_id,callback:function(t){e.mag_id=t},expression:"mag_id"}}),t("v-text-field",{attrs:{label:"Magazine Title"},model:{value:e.mag_title,callback:function(t){e.mag_title=t},expression:"mag_title"}}),t("v-row",[t("v-col",{attrs:{cols:"12",sm:"6"}},[t("v-menu",{attrs:{"close-on-content-click":!1,"nudge-right":40,transition:"scale-transition","offset-y":""},scopedSlots:e._u([{key:"activator",fn:function(a){var i=a.on;return[t("v-text-field",e._g({attrs:{label:"Date",readonly:""},model:{value:e.selectedDate,callback:function(t){e.selectedDate=t},expression:"selectedDate"}},i))]}}]),model:{value:e.datePicker,callback:function(t){e.datePicker=t},expression:"datePicker"}},[t("v-date-picker",{attrs:{"no-title":"",scrollable:""},model:{value:e.selectedDate,callback:function(t){e.selectedDate=t},expression:"selectedDate"}})],1)],1),t("v-col",{attrs:{cols:"12",sm:"6"}},[t("v-select",{attrs:{items:e.timeOptions,label:"Time"},model:{value:e.selectedTime,callback:function(t){e.selectedTime=t},expression:"selectedTime"}})],1)],1)],1)],1)])],1)}),[],!1,null,"7739c199",null,null).exports,d=a({},(function(){var e=this,t=e._self._c;return t("main",[t("v-container",[t("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:e.valid,callback:function(t){e.valid=t},expression:"valid"}},[t("v-textarea",{attrs:{width:"350px",label:"Feedback comment"},model:{value:e.feedback_comment,callback:function(t){e.feedback_comment=t},expression:"feedback_comment"}}),t("v-row",{attrs:{align:"center",justify:"space-between"}},[t("v-btn",{staticClass:"success",attrs:{depressed:""}},[e._v("accept")]),t("v-btn",{staticClass:"error",attrs:{depressed:""}},[e._v("reject")])],1)],1)],1)],1)}),[],!1,null,null,null,null).exports;e("default",a({components:{ArticleApprove:t,ArticleReject:n,ArticleCreation:i,MagazineCreation:l,ArticleList:c,ArticleWait:s,ScheduleSet:r,RescheduleSet:o,FeedbackApp:d},data:function(){return{tab:null,links:[{text:"Create Article",component:"ArticleCreation"},{text:"Create Magazine",component:"MagazineCreation"},{text:"View Article(s)",component:"ArticleList"},{text:"Add Categories",component:""},{text:"Create a Feedback",component:"FeedbackApp"},{text:"New Article to Check",component:"ArticleWait"},{text:"Approved Article",component:"ArticleApprove"},{text:"Rejected Articles",component:"ArticleReject"},{text:"Schedule Magazine",component:"ScheduleSet"},{text:"Reschedule Magazine",component:"RescheduleSet"}]}}},(function(){var e=this,t=e._self._c;return t("div",{staticClass:"side-drawer"},[t("v-card",[t("v-navigation-drawer",{attrs:{app:"",permanent:"",color:"#c1e2f4",width:325}},[t("v-tabs",{attrs:{vertical:"","background-color":"#c1e2f4"},model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},[e._l(e.links,(function(a,i){return t("v-tab",{key:i},[e._v(" "+e._s(a.text)+" ")])})),t("v-spacer"),t("v-tab",[e._v("Home")])],2)],1),t("v-container",[t("v-tabs-items",{model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},e._l(e.links,(function(e,a){return t("v-tab-item",{key:a},[t(e.component,{tag:"component"})],1)})),1)],1)],1)],1)}),[],!1,null,"6aaf0430",null,null).exports)}}}));