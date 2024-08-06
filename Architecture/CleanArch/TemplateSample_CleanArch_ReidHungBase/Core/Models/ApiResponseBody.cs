using Common.Enums;
using System;

namespace ScriptureExercise.Models
{
    //public class ResultBase
    //{
    //}

    //public class ActionOperationResult : ResultBase { }

    //擴張到 Action操作結果? 讓普通action和API都可以用? => 先否決 因應只有API 需要打包一個物件 船完整資訊給前端。普通action只需要自己搞邏輯流程

    /// <summary> 
    /// API內部的操作結果(網路斷線 找不到等等溝通失敗因素...成功與API溝通後就統一回httpCode200)
    /// </summary>

    public class ApiResponseBody //: ResultBase
    {
        public ApiOperationStatus Status { get; set; } //可能需要用這個 在前端做條件判斷
        public string StatusMeaning => Status.ToString();
        //public int StatusCode => (int)ApiOperationStatus; 
        //public string Code => Convert.ToInt32(Status).ToString().PadLeft(3, '0'); //好像沒必要補0

        //一個API Action內部，希望要保有【型別彈性】，因為前端才不管型別。也可善用【匿名類型】組裝
        public object Payload { get; set; } //考慮名稱：Body 
        public string Message { get; set; } //訊息：失敗直接拿service的失敗訊息、成功另寫?在action/js設定? => action設定的畫，前端可便於封裝
    }

    
}
