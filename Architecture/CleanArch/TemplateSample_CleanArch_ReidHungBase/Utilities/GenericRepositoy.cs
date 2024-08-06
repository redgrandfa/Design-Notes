using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ScriptureExercise.Repositories
{
    public class GenericRepositoy<TId,T> //where T:Entity<TId>
    {
        // //private readonly AirelaxContext _context;

        // //public EFGenericRepository(AirelaxContext context)
        // //{
        // //    _context = context;
        // //}
        // public IQueryable<T> GetAll<T>()
        // {
        //     return null;
        //     //return _context.Set<TEntity>();
        // }
        // public async Task<T> GetAsync<T>(Func<T,bool> lambda)//Expression
        // {
        //     return null;
        //     //return await _context.Set<TEntity>().FirstOrDefaultAsync(exp);

        // }
        // public async Task CreateAsync<T>(T entity)
        // {
        //     //await _context.Set<TEntity>().AddAsync(item);
        // }
        // public async Task UpdateAsync<T>(T entity)
        // {
        //     //_context.Set<TEntity>().Update(item);
        //     //await Task.CompletedTask;
        // }
        // public async Task DeleteAsync<T>(T entity)
        // {
        //     //_context.Set<TEntity>().Remove(item);
        //     //await Task.CompletedTask;
        // }
        // public async Task SaveChangeAsync()
        // {
        //     //await _context.SaveChangesAsync();
        // }
    }
}
