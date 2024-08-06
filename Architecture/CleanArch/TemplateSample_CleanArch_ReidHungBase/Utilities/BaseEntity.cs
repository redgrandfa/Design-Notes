using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ScriptureMockTest.Models
{
    //主鍵不一定只有一欄，...這兩個都不太好
    public class Entity<TId>
    {
        public TId Id { get; set; }
    }
    public class BaseEntity<TKey>
    {
        /// <summary>
        /// 主鍵
        /// </summary>
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public TKey Id { get; set; }

        // 關聯代號
        //[Key]
        //public Guid RelationId { get; set; }

        /// <summary>
        /// 是否軟刪除
        /// </summary>
        public bool IsDelete { get; set; }

        /// <summary>
        /// 資料建立者
        /// </summary>
        [StringLength(50)]
        public string CreateUser { get; set; }

        /// <summary>
        /// 資料建立時間
        /// </summary>
        public DateTime CreateTime { get; set; }

        /// <summary>
        /// 資料修改者
        /// </summary>
        [StringLength(50)]
        public string ModifyUser { get; set; }

        /// <summary>
        /// 最新資料修改時間 
        /// </summary>
        public DateTime? ModifyTime { get; set; }
    }


    //SQL型別 常數
    public struct Define
    {
        public struct SqlServer
        {
            public const string MONEY_TYPE = "money";
            public const string IMAGE_TYPE = "image";
            public const string MAX_NVARCHAR = "nvarchar(max)";
        }
    }
}
