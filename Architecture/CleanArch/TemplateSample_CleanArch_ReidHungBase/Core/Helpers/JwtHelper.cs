using Core.Models.Entities.Accounts;
using System.Security.Claims;
using System.Text;
using System.IdentityModel.Tokens.Jwt;
using Microsoft.IdentityModel.Tokens;

namespace API.Helpers
{
    public class JwtHelper
    {
        public ClaimsIdentity GenerateClaimsIdentity(Member member)
        {
            var claims = new List<Claim>();
            claims.Add(new Claim(ClaimTypes.Name, member.PK.MemberId.ToString()));

            //RFC 7519 規格書 第四章 定義了七個Registered Claim Names
            //Iss   Issuer  發行者
            //Sub   Subject         
            //Aud   Audience        
            //Exp   Expiration Time 過期時間
            //Nbf   Not Before      起效時間
            //Iat   Issued At       發行時間
            //Jti   JWT ID          unique identifier


            // 筆者對七個Registered Claim的測試：
            //claims.Add(new Claim(JwtRegisteredClaimNames.Iss, "在claim設定的")); //有效，但會被後面描述子裡的設定蓋過
            //claims.Add(new Claim(JwtRegisteredClaimNames.Sub, "在claim設定的")); //有效
            //claims.Add(new Claim(JwtRegisteredClaimNames.Aud, "在claim設定的")); //有效，但與後面描述子裡的 會組成陣列
            //claims.Add(new Claim(JwtRegisteredClaimNames.Exp, "1656666663")); //測試沒作用
            //claims.Add(new Claim(JwtRegisteredClaimNames.Nbf, "1656666662")); //測試沒作用
            //claims.Add(new Claim(JwtRegisteredClaimNames.Iat, "1656666661")); //測試沒作用
            //claims.Add(new Claim(JwtRegisteredClaimNames.Jti, "在claim設定的"));  //有效

            //結論：cliam這邊只需設定 Sub 和 Jti 這兩個
            claims.Add(new Claim(JwtRegisteredClaimNames.Sub, member.Value.Name));
            claims.Add(new Claim(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString()));
            //註：有兩種命名空間可選，根據參考文章是選using System.IdentityModel.Tokens.Jwt;
            //    (這個命名空間含在 Nuget套件Authentication.JwtBearer 之中的)

            // 集合所有聲明描述的身分識別。這些聲明，將記在token的payload中
            return new ClaimsIdentity(claims);
        }

        public ClaimsIdentity GenerateClaimsIdentity(Member.PK_T MemberPK)
        {
            var claims = new List<Claim>();
            claims.Add(new Claim(ClaimTypes.Name, MemberPK.MemberId.ToString()));

            //RFC 7519 規格書 第四章 定義了七個Registered Claim Names
            //Iss   Issuer  發行者
            //Sub   Subject         
            //Aud   Audience        
            //Exp   Expiration Time 過期時間
            //Nbf   Not Before      起效時間
            //Iat   Issued At       發行時間
            //Jti   JWT ID          unique identifier


            // 筆者對七個Registered Claim的測試：
            //claims.Add(new Claim(JwtRegisteredClaimNames.Iss, "在claim設定的")); //有效，但會被後面描述子裡的設定蓋過
            //claims.Add(new Claim(JwtRegisteredClaimNames.Sub, "在claim設定的")); //有效
            //claims.Add(new Claim(JwtRegisteredClaimNames.Aud, "在claim設定的")); //有效，但與後面描述子裡的 會組成陣列
            //claims.Add(new Claim(JwtRegisteredClaimNames.Exp, "1656666663")); //測試沒作用
            //claims.Add(new Claim(JwtRegisteredClaimNames.Nbf, "1656666662")); //測試沒作用
            //claims.Add(new Claim(JwtRegisteredClaimNames.Iat, "1656666661")); //測試沒作用
            //claims.Add(new Claim(JwtRegisteredClaimNames.Jti, "在claim設定的"));  //有效

            //結論：cliam這邊只需設定 Sub 和 Jti 這兩個
            //claims.Add(new Claim(JwtRegisteredClaimNames.Sub, member.Value.Name));
            claims.Add(new Claim(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString()));
            //註：有兩種命名空間可選，根據參考文章是選using System.IdentityModel.Tokens.Jwt;
            //    (這個命名空間含在 Nuget套件Authentication.JwtBearer 之中的)

            // 集合所有聲明描述的身分識別。這些聲明，將記在token的payload中
            return new ClaimsIdentity(claims);
        }

        //public ClaimsIdentity GenerateClaimsIdentity(Manager manager)
        //{
        //    var claims = new List<Claim>();

        //    claims.Add(new Claim(ClaimTypes.Name, manager.PK.ManagerId.ToString()));
        //    claims.Add(new Claim(ClaimTypes.Role, "manager"));

        //    claims.Add(new Claim(JwtRegisteredClaimNames.Sub, "manager"));
        //    claims.Add(new Claim(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString()));

        //    return new ClaimsIdentity(claims);
        //}

        private readonly IConfiguration configuration;
        public JwtHelper(IConfiguration configuration)
        {
            this.configuration = configuration;
        }
        public string ToJWT(ClaimsIdentity claimsIdentity)
        {
            #region (二)準備token的descriptor(譯：描述子)
            var issuer = configuration["JwtSettings:Issuer"];
            var signKey = configuration["JwtSettings:SignKey"]; //私鑰不可外流

            // 先將 金鑰 以 byte陣列 表示，做成個物件
            //  HmacSha256加密演算法 => 用來產生 JWT的signature(簽章)
            var secretKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(signKey));
            var signingCredentials = new SigningCredentials(secretKey, SecurityAlgorithms.HmacSha256Signature);
            // 註：有要求必須要大於 128 bits，所以signKey 至少要 16 字元以上


            // 描述token的相關設定的物件
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                // 七個Registered Claim中，claim區有四個設定有效，這四個在此的測試：
                //Issuer = "在Descriptor設定的",  //會覆蓋claim 設定的Iss
                //Subject 是ClaimsIdentity型別
                //Audience = "在Descriptor設定的",  //會與claim的設定併存組成陣列
                //沒有Jti 屬性可以設定

                //結論：cliam區設定兩個，在此設定五個：
                Issuer = issuer,
                Subject = claimsIdentity, //這些聲明，將記在token的payload中
                Expires = DateTime.UtcNow.AddDays(333),
                //NotBefore = DateTime.UtcNow,
                //IssuedAt = DateTime.UtcNow,
                //註：三個時間都有預設值：Nbf與Iat是UtcNow，Exp是UtcNow再加3600(秒)


                //此屬性負責JWT的signature(JWT第三段)
                SigningCredentials = signingCredentials,
            };
            #endregion

            #region (三) 造出JWT回傳
            var tokenHandler = new JwtSecurityTokenHandler();

            //若signKey < 16 字元，這句會拋例外
            var securityToken = tokenHandler.CreateToken(tokenDescriptor);
            //可加中斷點觀察：header、payload => 加密後的兩者  + RawSignature => RawData  用.隔開

            var serializeToken = tokenHandler.WriteToken(securityToken);
            //可加中斷點觀察：此字串值會是 RawData
            #endregion

            return serializeToken;
        }
    }
}
