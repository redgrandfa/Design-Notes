function fetchPostJson( url, body){
    let prefix = 'https://localhost:7054'
    // let prefix = ''
    return fetch(prefix+ url,{
        method:'post',
        headers:{
            'Content-type':'application/json;charset=utf-8',//
        },
        body:JSON.stringify(body),
    })

    // let respBody = await resp.json()

    // if(resp.ok){
    //     alert( respBody.msg)
    //      respBody.data
    // }
    // else{
    //     alert( respBody.msg)
    // }

}

function fetchGet( url ){
    let prefix = 'https://localhost:7054'
    return fetch( prefix + url)
}

// let jwtNameInCookie = "JWT"
// let jwtOptionInCookie = { expires: 14 };

// function fetch_Get_WithJWT(url){
//     return fetch(url ,{
//         headers: {
//             Authorization: `Bearer ${Cookies.get(jwtNameInCookie)}`,
//         },
//     })
//     //.then(response => response.json()) 需要判斷成敗，故不用
// }

// function fetch_Post_WithJWT(url , data){
//     return fetch(url ,{
//         headers: {
//             Authorization: `Bearer ${Cookies.get(jwtNameInCookie)}`,
//             'Content-type': 'application/json',
//         },
//         method: 'POST',
//         body: JSON.stringify(data),
//     })
// }
