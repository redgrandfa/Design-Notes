using Coravel.Invocable;
using Core.Intrfaces;
using Core.Models.Entities;

//--排- 季末：發息 >> 換季 >> 開放季初調整
//使用者前端互動 xx小時申請，申請單標季節 直接標下一季就好啦??
//--排- ： 封閉申請； (App初始化時要設定 季節...或人工寫入就好)
//  選擇權釋出保證金 15:00
//  開始處理次一季初始帳務

namespace API.Schedule
{
    public class CloseApplyInvocable : IInvocable
    {
        //有支援DI，需要的就注進來
        private readonly IMemoryCacheRepository cacheRepo;
        public CloseApplyInvocable(IMemoryCacheRepository cacheRepo)
        {
            this.cacheRepo = cacheRepo;
        }

        public async Task Invoke()
        {
            Console.WriteLine( nameof(CloseApplyInvocable) );

            //TODO：更新singleton 數值
            var globalData = cacheRepo.Get<GlobalData.Value_T>(nameof(GlobalData));
            globalData.AllowApplyForTransaction = false;

            cacheRepo.Set(nameof(GlobalData), globalData);
        }
    }
}
