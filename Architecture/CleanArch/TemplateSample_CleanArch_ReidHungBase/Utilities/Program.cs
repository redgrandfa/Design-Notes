namespace Utilities
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Add services to the container.
            var services = builder.Services;
            services.AddControllersWithViews();


            services.AddDbContext<AirelaxContext>(opt =>
                opt.UseSqlServer(Configuration.GetConnectionString(connectString),
                    x =>
                    {
                        x.MigrationsAssembly(Define.Database.ENTITY_FRAMEWORK);
                        x.UseQuerySplittingBehavior(QuerySplittingBehavior.SplitQuery);
                    })
            );
            services.AddCors(opt =>
            {
                opt.AddPolicy("dev", builder =>
                    builder.WithOrigins("http://airelax.azurewebsites.net")
                        .AllowAnyMethod()
                        .AllowAnyHeader()
                        .AllowCredentials());
            });
            services.AddSwaggerGen(c => { c.SwaggerDoc("v1", new OpenApiInfo { Title = "Airelax", Version = "v1" }); });
            //services.AddAutoMapper(typeof(AutoMapperProfile));
            //services.AddGoogleGeoService(Configuration);
            //services.AddECPayService(Configuration);
            services.Configure<PhotoUploadSetting>(Configuration.GetSection(nameof(PhotoUploadSetting)));

            //services.AddSignalR();





            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (!app.Environment.IsDevelopment())
            {
                app.UseExceptionHandler("/Home/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
                //app.UseCors("dev");
            }



            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            //app.UseMiddleware<RequestHeaderMiddleware>();
            //app.UseWebSockets();

            //app.UseAuthentication();
            app.UseAuthorization();

            app.MapControllerRoute(
                name: "default",
                pattern: "{controller=Home}/{action=Index}/{id?}"
            );
            //app.UseEndpoints(endpoints =>
            //{
            //    endpoints.MapControllerRoute(
            //        name: "default",
            //        pattern: "{controller=Home}/{action=Index}/{id?}");

            //    // SignalR
            //    //endpoints.MapHub<ChatHub>("/chathub");
            //});

            app.Run();
        }
    }
}