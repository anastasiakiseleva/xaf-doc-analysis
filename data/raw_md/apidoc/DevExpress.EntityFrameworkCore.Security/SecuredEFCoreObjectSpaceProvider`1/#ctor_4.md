---
uid: DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1.#ctor(DevExpress.ExpressApp.Security.ISelectDataSecurityProvider,DevExpress.ExpressApp.EFCore.EFCoreDatabaseProviderHandler{`0})
name: SecuredEFCoreObjectSpaceProvider(ISelectDataSecurityProvider, EFCoreDatabaseProviderHandler<TDbContext>)
type: Constructor
summary: Initializes a new instance of the @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 class with specified settings.
syntax:
  content: public SecuredEFCoreObjectSpaceProvider(ISelectDataSecurityProvider selectDataSecurityProvider, EFCoreDatabaseProviderHandler<TDbContext> databaseProviderHandler)
  parameters:
  - id: selectDataSecurityProvider
    type: DevExpress.ExpressApp.Security.ISelectDataSecurityProvider
    description: An object that implements the **ISelectDataSecurityProvider** interface (for example, a @DevExpress.ExpressApp.Security.SecurityStrategyComplex instance).
  - id: databaseProviderHandler
    type: DevExpress.ExpressApp.EFCore.EFCoreDatabaseProviderHandler{{TDbContext}}
    description: A delegate with @Microsoft.EntityFrameworkCore.DbContextOptionsBuilder and **string** parameters where you can specify the [database provider](https://learn.microsoft.com/en-us/ef/core/providers/) your application uses.
seealso: []
---
