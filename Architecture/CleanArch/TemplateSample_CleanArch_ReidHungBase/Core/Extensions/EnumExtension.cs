using Common.Attributes;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Extensions
{
    public static class EnumExtension
    {
        /// <summary>
        /// 取得特定Attribute的值，可以寫個Enum擴充方法
        /// </summary>
        public static object GetEnumMessage(this Enum value)
        {
            var field = value.GetType().GetField(value.ToString());
            if (field != null)
            {
                if (field.GetCustomAttributes(typeof(EnumMessageAttribute), true)
                    .SingleOrDefault() is EnumMessageAttribute attr)
                {
                    return attr.Value;
                }
            }

            //失敗 就傳原本整數值
            return Convert.ToInt32(value);
        }
    }
}
