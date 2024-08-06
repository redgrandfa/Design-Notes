using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using ScriptureMockTest.Models;

namespace ScriptureMockTest.Repositories
{
    public interface IGenericRepository<in TId, TEntity> where TEntity : Entity<TId>
    {
        /// <summary>
        ///     取得Entity全部筆數的IQueryable。
        /// </summary>
        /// <returns>Entity全部筆數的IQueryable。</returns>
        IQueryable<TEntity> GetAll();

        /// <summary>
        ///     透過指定條件選取第一個符合的Entity
        /// </summary>
        /// <param name="id"></param>
        /// <returns>符合條件的第一個Entity，若無則回傳default</returns>
        Task<TEntity> GetAsync(Expression<Func<TEntity, bool>> exp);

        /// <summary>
        ///     建立一個Entity
        /// </summary>
        /// <param name="item"></param>
        /// <returns></returns>
        Task CreateAsync(TEntity item);

        /// <summary>
        ///     更新Entity
        /// </summary>
        /// <param name="item"></param>
        /// <returns></returns>
        Task UpdateAsync(TEntity item);

        /// <summary>
        ///     刪除Entity
        /// </summary>
        /// <param name="item"></param>
        /// <returns></returns>
        Task DeleteAsync(TEntity item);

        /// <summary>
        ///     儲存變更
        /// </summary>
        /// <returns></returns>
        Task SaveChangesAsync();

        public class EFGenericRepository<TId, TEntity> : IGenericRepository<TId, TEntity> where TEntity : Entity<TId>
    {
        private readonly AirelaxContext _context;

        public EFGenericRepository(AirelaxContext context)
        {
            _context = context;
        }

        public IQueryable<TEntity> GetAll()
        {
            return _context.Set<TEntity>();
        }

        public async Task<TEntity> GetAsync(Expression<Func<TEntity, bool>> exp)
        {
            return await _context.Set<TEntity>().FirstOrDefaultAsync(exp);
        }

        public async Task CreateAsync(TEntity item)
        {
            await _context.Set<TEntity>().AddAsync(item);
        }

        public async Task UpdateAsync(TEntity item)
        {
            _context.Set<TEntity>().Update(item);
            await Task.CompletedTask;
        }

        public async Task DeleteAsync(TEntity item)
        {
            _context.Set<TEntity>().Remove(item);
            await Task.CompletedTask;
        }

        public async Task SaveChangesAsync()
        {
            await _context.SaveChangesAsync();
        }
    }
}
