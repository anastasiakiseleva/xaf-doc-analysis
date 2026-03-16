---
uid: DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1.#ctor(DevExpress.ExpressApp.Security.ISelectDataSecurityProvider,Microsoft.Extensions.DependencyInjection.ServiceCollection,DevExpress.ExpressApp.DC.ITypesInfo,System.String,DevExpress.ExpressApp.EFCore.EFCoreDatabaseProviderHandler{`0})
name: SecuredEFCoreObjectSpaceProvider(ISelectDataSecurityProvider, ServiceCollection, ITypesInfo, String, EFCoreDatabaseProviderHandler<TDbContext>)
type: Constructor
summary: Initializes a new instance of the @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 class with specified settings.
syntax:
  content: public SecuredEFCoreObjectSpaceProvider(ISelectDataSecurityProvider selectDataSecurityProvider, ServiceCollection services, ITypesInfo typesInfo, string connectionString, EFCoreDatabaseProviderHandler<TDbContext> databaseProviderHandler)
  parameters:
  - id: selectDataSecurityProvider
    type: DevExpress.ExpressApp.Security.ISelectDataSecurityProvider
    description: An object that implements the **ISelectDataSecurityProvider** interface (for example, a @DevExpress.ExpressApp.Security.SecurityStrategyComplex instance).
  - id: services
    type: Microsoft.Extensions.DependencyInjection.ServiceCollection
    description: A collection of services registered in your application (see [Dependency injection](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection)).
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypesInfo) object that provides access to XAF-related information on business classes.
  - id: connectionString
    type: System.String
    description: An application's connection string.
  - id: databaseProviderHandler
    type: DevExpress.ExpressApp.EFCore.EFCoreDatabaseProviderHandler{{TDbContext}}
    description: A delegate with @Microsoft.EntityFrameworkCore.DbContextOptionsBuilder and **string** parameters where you can specify the [database provider](https://learn.microsoft.com/en-us/ef/core/providers/) your application uses.
seealso: []
---
