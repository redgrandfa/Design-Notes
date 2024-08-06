using Microsoft.Extensions.DependencyInjection;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Extensions.Configuration;

namespace Infra.Configuration
{
    public static class ConfigureAuth
    {
        public static IServiceCollection AddCoreServices(this IServiceCollection services, IConfigurationBuilder configuration)
        {

            return services;
        }

    }
}
