let vue_login = new Vue({
    el: "#vue_login",
    data: {
        fields:{
            cellPhone:{
                text:'手機號碼',
                value:'0912345678',
            },
            password:{
                text:'密碼',
                value:'12345678',
                visible:false,
            },
        },
        errMsgs:{
            cellPhone:'',
            password:'',
        },
        disabled:true,
    },
    //beforeCreate > 【data初始化】 > watch > created > beforeMount > mounted
    mounted(){ },
    methods: {
        changeVisible(fieldkey){
            let t = this.fields[fieldkey]
            t.visible = !t.visible
        },
        check_cellPhone(){
            let fieldkey = 'cellPhone'
            let t = this.fields[fieldkey];
            if(!/^09\d{8}$/.test(t.value)
            ){
                this.errMsgs[fieldkey] = "須為手機號碼格式";
            }
            else{
                this.errMsgs[fieldkey] = "";
            }
        },
        check_password(){
            let fieldkey = 'password'
            let t = this.fields[fieldkey];
            if(!/^[a-zA-Z0-9]+$/.test(t.value)
            ){
                this.errMsgs[fieldkey] = "須為英文、數字的組合";
            }
            else if(t.value.length<8 || t.value.length>16){
                this.errMsgs[fieldkey] = "長度須為8~16碼";
            }
            else{
                this.errMsgs[fieldkey] = "";
            }
        },
        async post_login(){
            let data = {};
            for (let key in this.fields){
                data[key] = this.fields[key].value
            }

            let resp = await fetchPostJson(
                '/ApiAccount/Login',
                data
            )
            
            if(resp.ok){
                let jwt = await resp.text()
                console.log(jwt)
            }
            else if(resp.status == 1404){
                swal.fire( "此手機號碼未註冊會員" )
            }
            else if(resp.status == 1409){
                swal.fire( "密碼錯誤" )
            }
            else{
                swal.fire( '異常，請協助回報' )
            }
        },
    },
    watch: {
        'fields.cellPhone.value':{
            immediate:true,
            handler:function(){
                this.check_cellPhone()
            }
        },
        'fields.password.value':{
            immediate:true,
            handler:function(){
                this.check_password()
            }
        },
        errMsgs:{
            deep:true,
            immediate:true,
            handler:function(){
                //有一個沒過 就沒過
                this.disabled = Object.values(this.errMsgs)
                    .some( errMsg => errMsg != "" );
            }
        }
    },
    computed: {
        fieldPasswordType(){
            return this.fields.password.visible?'text':'password'
        }
    },
    components: {},
});

let vue_register = new Vue({
    el: "#vue_register",
    data: {
        fields:{
            cellPhone:{
                text:'手機號碼',
                value:'0912345678',
            },
            password:{
                text:'密碼',
                value:'12345678',
                visible:false,
            },
            name:{
                text:'姓名',
                value:'花枝魷魚麵',
            },
            lineUserId:{
                text:'Line用戶ID',
                value:'去line的「設定」裡看',
            },
        },
        errMsgs:{
            cellPhone:'',
            password:'',
            // recitePassword:'',
            name:'',
            lineUserId:'',
        },
        disabled:true,
    },
    mounted(){ },
    methods: {
        changeVisible(fieldkey){
            let t = this.fields[fieldkey]
            t.visible = !t.visible
        },
        check_cellPhone(){
            let fieldkey = 'cellPhone'
            let t = this.fields[fieldkey];
            if(!/^09\d{8}$/.test(t.value)
            ){
                this.errMsgs[fieldkey] = "須為手機號碼格式";
            }
            else{
                this.errMsgs[fieldkey] = "";
            }
        },
        check_password(){
            let fieldkey = 'password'
            let t = this.fields[fieldkey];
            if(!/^\w+$/.test(t.value)
            ){
                this.errMsgs[fieldkey] = "須為英文、數字的組合";
            }
            else if(t.value.length<8 || t.value.length>16){
                this.errMsgs[fieldkey] = "長度須為8~16碼";
            }
            else{
                this.errMsgs[fieldkey] = "";
            }
        },
        check_name(){
            let fieldkey = 'name'
            let t = this.fields[fieldkey];
            if(t.value==''){
                this.errMsgs[fieldkey] = "必填";
            }
            else{
                this.errMsgs[fieldkey] = "";
            }
        },
        check_lineUserId(){
            let fieldkey = 'lineUserId'
            let t = this.fields[fieldkey];
            if(t.value==''){
                this.errMsgs[fieldkey] = "必填";
            }
            else{
                this.errMsgs[fieldkey] = "";
            }

        },
        async post_register(){
            let data = {};
            for (let key in this.fields){
                data[key] = this.fields[key].value
            }

            let resp = await fetchPostJson(
                '/ApiAccount/Register',
                data
            )
            
            if(resp.ok){
                swal.fire( "發送成功\n請等營運方手機連絡您" )                
            }
            else if(resp.status == 1409){
                swal.fire( "手機號碼已被註冊" )
            }
            else{
                swal.fire( '異常，請協助回報' )
                // console.log()
            }
        },
    },
    watch: {
        'fields.cellPhone.value':{
            immediate:true,
            handler:function(){
                this.check_cellPhone('cellPhone')
            }
        },
        'fields.password.value':{
            immediate:true,
            handler:function(){
                this.check_password('password')
            }
        },
        errMsgs:{
            deep:true,
            immediate:true,
            handler:function(){
                //有一個沒過 就沒過
                this.disabled = Object.values(this.errMsgs)
                    .some( errMsg => errMsg != "" );
            }
        }
    },
    computed: {
        fieldPasswordType(){
            return this.fields.password.visible?'text':'password'
        }
    },
    components: {},
});



