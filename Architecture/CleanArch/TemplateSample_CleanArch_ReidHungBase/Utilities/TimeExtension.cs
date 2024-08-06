using Core.Enums;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Core.Extensions
{
    public static class TimeExtension
    {
        //今年 三月的第三個週三 => 浮動，麻煩

        //15日 UTC 00:00 發息 => 較簡單、好記
        // 台灣時間08:00發 ~隔天07:59 可申請 (國際標準時間) 或開一週?

        // ~21:00 查收/執行 ~ 換季?

        /// <summary>
        /// 申請單 需記錄季節，(交易明細 只須根據申請單 )
        /// </summary>
        public static Season GetSeason(this DateTime d)
        {
            int date = int.Parse(d.ToString("Mdd"));

            if ( date < 316)
                return Season.Spring;
            else if(date < 616)
                return Season.Summer;
            else if(date < 916)
                return Season.Autumn;
            else if(date < 1216)
                return Season.Winter;
            else // 12/16~12/31
                return Season.Spring;
        }
    }

    public static class DateTimeHelper
    {
        public static IEnumerable<DateTime> GetDateRange(DateTime start, DateTime end)
        {
            var dateRange = new List<DateTime>();
            for (var dt = start; dt < end; dt = dt.AddDays(1)) dateRange.Add(dt);

            return dateRange;
        }
    }
}
