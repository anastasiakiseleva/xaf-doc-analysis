---
uid: DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1.#ctor(DevExpress.ExpressApp.Security.ISelectDataSecurityProvider,Microsoft.Extensions.DependencyInjection.ServiceCollection,Microsoft.EntityFrameworkCore.DbContextOptions{`0},DevExpress.ExpressApp.DC.ITypesInfo,System.String)
name: SecuredEFCoreObjectSpaceProvider(ISelectDataSecurityProvider, ServiceCollection, DbContextOptions<TDbContext>, ITypesInfo, String)
type: Constructor
summary: Initializes a new instance of the @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 class with specified settings.
syntax:
  content: public SecuredEFCoreObjectSpaceProvider(ISelectDataSecurityProvider selectDataSecurityProvider, ServiceCollection services, DbContextOptions<TDbContext> dbContextOptions, ITypesInfo typesInfo, string connectionString)
  parameters:
  - id: selectDataSecurityProvider
    type: DevExpress.ExpressApp.Security.ISelectDataSecurityProvider
    description: An object that implements the **ISelectDataSecurityProvider** interface (for example, a @DevExpress.ExpressApp.Security.SecurityStrategyComplex instance).
  - id: services
    type: Microsoft.Extensions.DependencyInjection.ServiceCollection
    description: A collection of services registered in your application (see [Dependency injection](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection)).
  - id: dbContextOptions
    type: Microsoft.EntityFrameworkCore.DbContextOptions{{TDbContext}}
    description: An object that allows you to configure @Microsoft.EntityFrameworkCore.DbContext your application uses.
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypesInfo) object that provides access to XAF-related information on business classes.
  - id: connectionString
    type: System.String
    description: An application's connection string.
seealso: []
---
