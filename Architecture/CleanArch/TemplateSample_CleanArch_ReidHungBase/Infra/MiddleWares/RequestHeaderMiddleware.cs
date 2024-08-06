using Microsoft.AspNetCore.Http;
using System.Threading.Tasks;

namespace ScriptureMockTest.Middlewares
{
    public class RequestHeaderMiddleware
    {
        private readonly RequestDelegate _next;
        public RequestHeaderMiddleware(RequestDelegate next)
        {
            _next = next;
        }

        public async Task InvokeAsync(HttpContext context)
        {
            const string JWT_COOKIE_KEY = "jwt";
            if (context.Request.Cookies.ContainsKey(JWT_COOKIE_KEY))
            {
                context.Request.Headers.Add("Authorization", 
                    JwtBearerDefaults.AuthenticationScheme + " " 
                    + context.Request.Cookies[JWT_COOKIE_KEY]);
            }

            await _next(context);
        }

    }
}
