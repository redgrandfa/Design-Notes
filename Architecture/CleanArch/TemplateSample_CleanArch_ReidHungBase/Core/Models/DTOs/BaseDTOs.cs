
using System;
namespace Common.DTOModels
{
    //規劃：  如何給足action 所需資訊?   service內部也可能有各種錯誤?，因須告知前端是哪一種 ，直接把訊息寫好!!
    //R => 成：回傳obj
    //      敗-key不存在：回傳null

    //C => 成：回傳obj (有可能需要回傳寫入的結果，去更新前端)
    //      敗-key【已】存在：回傳null

    //U => 成：回傳obj (有可能需要回傳寫入的結果，去更新前端)
    //      敗-key不存在：回傳null

    //D => 成：無須回傳東西
    //      敗-key不存在：無須回傳東西

    //任何service方法
    //  會有複雜的打包??...ex. 寫入紀錄 又 更新會員
    //  SystemException => 前端非200，統一告知有異常(actionFilter?)，無須設計

    public class BaseOutput
    {
        public string FailMessage { get; set; }
        public bool IsFail => FailMessage != null;  //where T : Enum 或bool //考慮利用 attribute 製造 enum各項的資訊?
        public bool IsSuccess => FailMessage == null;  
    }

    public class BaseOutput_withPayload<T>: BaseOutput
    {
        public T Payload { get; set; }
    }
}
