using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.DBModels
{
    //能否改良 ， 不需要一直把泛型填進去
    abstract public class BaseRedisEntity<TPK,TValue> //where TValue : CommonFields
    {
        public TPK PK { get; set; }
        public TValue Value { get; set; }

        abstract public string GetRedisKeyString();
    }

    /// <summary>
    /// 共通欄位
    /// </summary>
    public class CommonFields
    {
        public bool IsDeleted { get; set; }

        public DateTimeOffset CreateTime { get; set; }
        public DateTimeOffset UpdateTime { get; set; }
        //public string CreateMemberId { get; set; }
        //public string UpdateMemberId { get; set; }
    }
    public class EntityCounter
    {
        public int MemberCount { get; set; }

    }

    //實驗 子類別裡的類別 繼承或覆蓋 父類別裡的類別

    //public abstract class A
    //{
    //    public TK PK_T { get; set; }
    //    abstract public class TK { }
    //}


    //public class B: A
    //{
    //    override public class TK //只能new關鍵字 
    //    {
    //        public int Int { get; set; }
    //    }

    //    public void X()
    //    {
    //        this.PK_T.Int;
    //    }
    //}
}
