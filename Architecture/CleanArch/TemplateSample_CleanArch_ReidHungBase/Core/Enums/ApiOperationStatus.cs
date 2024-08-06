using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Enums
{
    public enum ApiOperationStatus
    {
        Success = 0,

        Fail = 1,
        //失敗 = 某正整數

        //UnAuthorized = 1,

        LoginFail = 101,

        //NewPasswordIsNotMatch = 102,

        //OldPasswordIsNotMatch = 103,

        //MemberIsNotEnable = 104,

        DataNotFound = 401, //R U D

        DataRequireUnique = 402, //C

        MissingRequiredInformation = 403, //C U

        Exception = 999,
    }
}
