using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
//using Common.Repositories;

namespace ScriptureExercise.Controllers.WebAPI
{
    [Route("[controller]/[action]")]
    [ApiController]
    public abstract class AppApiControllerBase : ControllerBase
    {
        //private readonly IMemoryCacheRepository repo;
        //public AppApiControllerBase(
        //    IMemoryCacheRepository repo
        //)
        //{
        //    this.repo = repo;
        //}
    }
}
